Name:           elkulator
Version:        1.1
Release:        7
Summary:        Acorn Electron emulator
License:        GPLv2 (Except ROMs)
URL:            https://github.com/rcook/elkulator
Source0:        %{name}-master.zip
Source1:        %{name}-roms.zip
Patch0:         %{name}-remove-alut-test.patch
Patch1:         %{name}-fix-config.patch
Patch2:         %{name}-fix-roms.patch
BuildRequires:  allegro-devel
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freealut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  openal-devel
BuildRequires:  zlib-devel

%description
An Acorn Electron emulator. This is a fork of the original Elukator emulator.

%prep
%setup -qn %{name}-master
# The alut check fails so patch it out. BuildRequires takes care of that anyway
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1
unzip %{SOURCE1}

%build
# Create a desktop file
cat >%{name}.desktop <<EOF
[Desktop Entry]
Name=Elkulator
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;Emulator;
EOF

# Create the wrapper for /usr/bin
cat >%{name}.wrapper <<EOF
#!/bin/bash
# Wrapper script to launch Elkulator
#
# Improve configuration handling
#
echo "Launching %{name} via wrapper..."

# Check HOME is defined and a directory, otherwise do nothing.
# Try to follow XDG standard
if [ ! -z \${HOME} ] && [ -d \${HOME} ] ; then
    XDG_CONFIG_HOME=\${XDG_CONFIG_HOME:=\$HOME/.config}
    if [ ! -e "\$XDG_CONFIG_HOME/%{name}.cfg" ] ; then
        mkdir -p "\$XDG_CONFIG_HOME"
        cat "/etc/%{name}.cfg" > "\$XDG_CONFIG_HOME/%{name}.cfg"
    fi
fi

%{name}.bin "\$@" --conf "\$XDG_CONFIG_HOME/%{name}.cfg"
EOF

# We need -fcommon for it to compile
export CFLAGS="%{optflags} -fcommon"
%cmake --no-warn-unused-cli -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix}
%cmake_build

%install 
mkdir -p %{buildroot}%{_datadir}/%{name}/roms \
         %{buildroot}%{_datadir}/applications \
         %{buildroot}%{_datadir}/pixmaps/ \
         %{buildroot}%{_sysconfdir}

install -pm 0644 icon/%{name}.png  %{buildroot}%{_datadir}/pixmaps
install -pm 0644 samples/elk.cfg %{buildroot}%{_sysconfdir}/%{name}.cfg
install -pm 0644 %{name}-roms/* %{buildroot}%{_datadir}/%{name}/roms

pushd %{__cmake_builddir}
make install DESTDIR="%{buildroot}"
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}.bin
popd

install -pm 0755 %{name}.wrapper  %{buildroot}%{_bindir}/%{name}
# Install the .desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
                     
%files
%{_bindir}/%{name}.bin
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%license LICENSE.md
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}.cfg

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Mon Dec 28 2020 RPMBuilder - 1.1-7
- Rebased to new GIT. Negligible code changes
- SPEC modernisation and minor cleanups
- Improved use of Macros, particularly for CMAKE
- Enabled building of debug packages
* Mon May 11 2020 RPMBuilder - 1.1-6
- Added -fcommon to C flags. This reverses a GCC 10 default for failing on
  multiple defines but the effort in fixing the code is not worth it when the
  code is no longer actively maintained.
* Sat May 18 2019 RPMBuilder - 1.1-5
- Rebased to new GIT for F30. Almost zero actual changes
* Sun Nov 11 2018 RPMBuilder - 1.1-4
- Updated BRs due to new F29 buildroot
* Mon Jun 11 2018 RPMBuilder - 1.1-3
- Improve config handling via a wrapper script, settings are now saved
* Fri Jun 08 2018 RPMBuilder - 1.1-2
- Fixes to the .desktop file
- Force standard Fedora build flags
* Mon Dec 12 2016 RPM Builder - 1.1-1
- Initial RPM Release
