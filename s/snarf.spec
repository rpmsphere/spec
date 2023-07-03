Name:           snarf
URL:            https://www.xach.com/snarf/
License:        GNU GENERAL PUBLIC LICENSE
Group:          Productivity/Networking/Web/Utilities
Version:        7.0
Release:        6.1
Summary:        A command line resource grabber
Source:         https://www.xach.com/snarf/download/source/snarf-7.0.tar.gz
BuildRequires:  make

%description
Snarf is a command line resource grabber.
It can transfer files through the http, gopher, finger, and ftp protocols
without user interaction. It is small and fast.

%prep
%setup -q

%build
./configure --prefix=/usr --mandir=/usr/share/man --bindir=/usr/bin
make 

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING ChangeLog README TODO
%{_bindir}/snarf
%{_mandir}/man1/*

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 7.0
- Rebuilt for Fedora
* Fri Jan 14 2011 Robert Herb <robertherb@arcor.de>
- initial package created
