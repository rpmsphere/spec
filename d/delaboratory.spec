%undefine _debugsource_packages

Name:               delaboratory
Version:            0.8
Release:            10.1
Summary:            Color Correction Utility
Source0:            https://delaboratory.googlecode.com/files/delaboratory-%{version}.tar.gz
Source1:            delaboratory.desktop
Source2:            delaboratory.png
URL:                https://code.google.com/p/delaboratory/
Group:              Productivity/Graphics/Other
License:            GPL-3.0
BuildRequires:      libpng-devel
BuildRequires:      wxGTK-devel
BuildRequires:      libxml2-devel
BuildRequires:      libtiff-devel
BuildRequires:      gcc-c++ make glibc-devel pkgconfig
BuildRequires:      autoconf automake libtool

%description
delaboratory is a Free Software color correction utility, it allows you to
modify color/contrast of your photo in a creative way - by performing
non-destructive operations in different colorspaces (RGB/BW, XYZ/LAB/LCH,
CMY/CMYK, HSL/HSV) with floating-point precision per channel.

%prep
%setup -q
sed -i -e 's|-Wno-long-long|-Wno-long-long -fPIC|' -e 's|-DNDEBUG|-DNDEBUG -fPIC|' Makefile

%build
%ifarch x86_64
export ARCH=64
%endif
%ifarch aarch64
sed -i 's|-march=i686||' Makefile
%endif
make

%install
rm -rf "$RPM_BUILD_ROOT"
install -D -m0755 delaboratory $RPM_BUILD_ROOT%{_bindir}/delaboratory
install -D -m0644 "%{SOURCE1}" $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -D -m0644 "%{SOURCE2}" $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%doc COPYING README
%{_bindir}/delaboratory
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Jan 11 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuilt for Fedora
* Sun Sep  4 2011 pascal.bleser@opensuse.org
- initial version (0.4)
