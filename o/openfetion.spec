Summary: IM client based on GTK+2.0, using CHINA MOBILE's Fetion Protocol
Name: openfetion
Version: 2.2.1
Release: 4.1
Group: Networking/Instant messaging
License: GPLv2+
URL: http://code.google.com/p/ofetion/
Source0: http://ofetion.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires: libpng-devel
Buildrequires: gtk2-devel
BuildRequires: sqlite-devel
#BuildRequires: libnotify-devel
BuildRequires: gstreamer-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libofetion-devel >= %{version}
BuildRequires: gcc-c++
BuildRequires: cmake

%description
OpenFetion is a IM client based on GTK+2.0, using CHINA MOBILE's Fetion
Protocol Version 4.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
mkdir build ; cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DLIB_INSTALL_DIR=%{_libdir} -DCMAKE_BUILD_TYPE=release .. -DWITH_NETWORKMANAGER=OFF
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT -C build install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_datadir}/man/man1/*

%changelog
* Tue Jan 03 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.1
- Rebuilt for Fedora
* Sun Dec 26 2010 Funda Wang <fwang@mandriva.org> 2.1.0-1mdv2011.0
+ Revision: 625216
- new version 2.1.0
* Mon Nov 29 2010 Funda Wang <fwang@mandriva.org> 2.0.7-1mdv2011.0
+ Revision: 602974
- new version 2.0.7
- BR sqlite3
- new version 2.0.1
* Sat Sep 25 2010 Funda Wang <fwang@mandriva.org> 1.9-1mdv2011.0
+ Revision: 580965
- update to new version 1.9
* Thu Aug 19 2010 Funda Wang <fwang@mandriva.org> 1.8-1mdv2011.0
+ Revision: 571352
- new version 1.8
* Mon Aug 09 2010 Funda Wang <fwang@mandriva.org> 1.7-1mdv2011.0
+ Revision: 568148
- New version 1.7
* Fri Jul 09 2010 Funda Wang <fwang@mandriva.org> 1.6.1-1mdv2011.0
+ Revision: 549879
- import openfetion
