%undefine _debugsource_packages

Summary: Command line libofetion client implemention
Name: cliofetion
Version: 2.2.0
Release: 7.1
Group: Networking/Instant messaging
License: GPLv2+
URL: https://code.google.com/p/ofetion/
Source0: https://ofetion.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires: libofetion-devel >= 2.2.0
BuildRequires: gcc-c++, cmake, sqlite-devel

%description
ClioFetion is a command-line IM client, using CHINA MOBILE's Fetion
Protocol Version 4.

%prep
%setup -q

%build
cmake . -DCMAKE_INSTALL_PREFIX=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc AUTHORS ChangeLog README
%{_bindir}/%name
%{_mandir}/man1/*

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.0
- Rebuilt for Fedora
* Sat May 14 2011 Funda Wang <fwang@mandriva.org> 2.2.0-1mdv2011.0
+ Revision: 674491
- update file list
- new version 2.2.0
* Sun Dec 26 2010 Funda Wang <fwang@mandriva.org> 2.1.0-1mdv2011.0
+ Revision: 625229
- import cliofetion
