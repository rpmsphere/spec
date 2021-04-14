Name: grandr
Version: 1.0.2
Release: 5.1
Summary: RandR user interface using GTK+ libraries
License: MIT/X11
Group: System/X11
URL: http://cgit.freedesktop.org/xorg/app/%name/
Source: %name-%version.tar
Patch1: grandr-debian-01-fix-segfault-when-click-monitor.patch
Patch2: grandr-mandriva-synchronize-before-and-after-apply.patch
BuildRequires: GConf2-devel libXrandr-devel gtk2-devel
BuildRequires: xorg-x11-util-macros

%description
RandR user interface using GTK+ libraries.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
autoreconf -ifv
%configure 
make LIBS="-lgthread-2.0 -lX11"

%install
make DESTDIR=%buildroot install

%files
%doc README NEWS AUTHORS
%_bindir/*

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuilt for Fedora
* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 1.0.2-alt3
- DSO list completion
* Tue Apr 10 2012 Fr. Br. George <george@altlinux.ru> 1.0.2-alt2
- Fix build
* Tue May 25 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Initial build
