%undefine _debugsource_packages

Summary: The xwhirl screensaver
Name: xwhirl
Version: 1.1
Release: 9.1
License: GPL
Group: X11/Utilities
Source: xwhirl-%{version}.src.tar.gz
Patch: xwhirl-1.1-bindir-install.patch
URL: https://www.eleves.ens.fr/home/horvai/xwhirl
BuildRequires: imake
BuildRequires: libX11-devel
BuildRequires: libXext-devel

%description
Whirling deformation of screen under X Window,
sort of screensaver. It is optimized for speed, and
is much faster then xscreensaver/hacks/distort.

%prep
%setup -q
%patch -p1

%build
xmkmf
make xwhirl

%install
install -Dm755 xwhirl %{buildroot}%{_bindir}/%{name}
install -Dm644 xwhirl.1 %{buildroot}%{_mandir}/man1/%{name}.1x

%files
%{_bindir}/xwhirl
%{_mandir}/man1/xwhirl.1x.*

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Fri Aug 07 1998 Arkadi E. Shishlov <arkadi@kvin.lv>
- Initial package
