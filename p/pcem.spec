Name:          pcem
Version:       17
Release:       2
License:       GPLv2
Summary:       A PC emulator that specializes in emulating ancient models of PC
Source0:       https://pcem-emulator.co.uk/files/PCemV17Linux.tar.gz
URL:           https://pcem-emulator.co.uk
BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: openal-soft-devel
BuildRequires: SDL2-devel
BuildRequires: wxGTK3-devel

%description
A PC emulator that specializes in emulating ancient models of PC.

%prep
%setup -qc
sed -i 's/\r//' readme.html COPYING

%build
# Create a desktop file
cat >%{name}.desktop <<EOF
[Desktop Entry]
Name=PCem
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;Emulator;
EOF

# Override linking flags as PIE seems to cause pcem to crash on emulating processors >= 486
LDFLAGS="${LDFLAGS:--Wl,-z,relro -Wl,--as-needed  -Wl,-z,now}" ; export LDFLAGS;
%configure  --enable-networking --enable-alsa --enable-release-build CFLAGS="%{optflags} -fcommon" CPPFLAGS="%optflags -fcommon"
make %{?_smp_mflags} CFLAGS="%{optflags} -fcommon" CPPFLAGS="%optflags -fcommon"

%install
mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps,%{name}/roms}
%make_install

# Install the .desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{name}.desktop
install -p -m0644 src/icons/32x32/motherboard.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%doc readme.html
%license COPYING

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 17
- Rebuilt for Fedora
* Mon Dec 28 2020 RPMBuilder - 17-2
- SPEC modernisation and minor cleanups
- Enabled building of debug packages
* Mon Dec 21 2020 RPMBuilder - 17-1
- Upgrade to v17
* Tue May 12 2020 RPMBuilder - 16-2
- Use the correct source this time. Truly upgrade to v16
* Mon May 11 2020 RPMBuilder - 16-1
- Upgrade to v16
- Added -fcommon to C flags. This reverses a GCC 10 default for failing on
  multiple defines. Should really be fixed upstream
  * Wed Aug 07 2019 RPMBuilder - 15-2
- Not ideal but override linking flags for PIE to avoid pcem segfaulting
  when emulating processors >= 486. Forcing -fPIC in previous builds was
  probably the incorrect approach
* Sun May 26 2019 RPMBuilder - 15-1
- Upgrade to v15
* Sun Nov 11 2018 RPMBuilder - 14-2
- Changed BRs due to new F29 buildroot
* Tue May 22 2018 RPMBuilder - 14-1
- Upgrade to v14
- Tweaked the build flags to use -fPIC
- Undefine the debug source package generation
* Mon Mar 05 2018 RPMBuilder - 13.1-1
- Initial RPM release
