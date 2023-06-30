Name:          beebem
Version:       0.0.13
Release:       3
License:       "Distributable"
Summary:       BBC Micro and Master 128 Emulator
Source0:       https://beebem-unix.bbcmicro.com/download/%{name}-%{version}.tar.gz
Source1:       %{name}.png
Patch:         %{name}-0.0.13-cast.patch
Patch1:        %{name}-0.0.13-keys.patch
Patch2:        %{name}-0.0.13-menu-crash.patch
Patch3:        %{name}-0.0.13-rpmlint.patch
Patch4:        %{name}-0.0.13-gccfixes.patch
URL:           https://beebem-unix.bbcmicro.com/
BuildRequires: desktop-file-utils
BuildRequires: SDL-devel
BuildRequires: gtk2-devel
BuildRequires: gcc-c++

%description
BBC Micro and Master 128 emulator.

%prep
%setup -q
%patch
%patch1 -p1
%patch2 -p1
%patch3
%patch4 -p1
sed -i 's/\r//' doc/{CHANGES.txt,Ibos.txt,README.txt,README_Z80.TXT}
rm -f doc/*.zip

%build
# Create a desktop file
cat >%{name}.desktop <<EOF
[Desktop Entry]
Name=BeebEm
Comment=BBC Micro Emulator
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;Emulator;
EOF

%configure --enable-econet
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}

# pkgdatadir works around an installer bug
%make_install pkgdatadir=%{buildroot}/usr/share/%{name}

# Fix up the permissions
find %{buildroot}/usr/share/%{name} -type d -exec chmod 0755 {} \;
find %{buildroot}/usr/share/%{name} -type f -exec chmod 0644 {} \;

# Install the .desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
                     %{name}.desktop
install -p -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps

%files
%doc AUTHORS COPYING ChangeLog NEWS README THANKS doc/[^M]*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.13
- Rebuilt for Fedora
* Mon Dec 28 2020 RPMBuilder - 0.0.13-3
- SPEC modernisation and minor cleanups
* Fri May 17 2019 RPMBuilder - 0.0.13-2
- Update because of stupid bug with rpmbuild or rpmlint which does not like dates
- before 2017 on F30
* Sat Jul 16 2016 RPMBuilder - 0.0.13-1
- Initial RPM release