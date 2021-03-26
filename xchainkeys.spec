Name: xchainkeys
Version: 0.11
Release: 3.1
Summary: Create chained key bindings for X11
License: GPLv3
Group: System/Configuration/Other
URL: http://henning-bekel.de/xchainkeys/
Source0: http://henning-bekel.de/download/xchainkeys/%name-%version.tar.gz
BuildRequires: libX11-devel

%description
xchainkeys is a standalone X11 program to create chained key bindings
similar to those found in the ratpoison window manager or the screen
terminal multiplexer.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_mandir/man1/*
%doc ChangeLog AUTHORS README NEWS example.conf

%changelog
* Thu Dec 08 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11
- Rebuild for Fedora
* Mon Apr 16 2012 Terechkov Evgenii <evg@altlinux.org> 0.10-alt1
- Initial build for ALT Linux Sisyphus
