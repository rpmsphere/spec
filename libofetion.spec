Summary: Fetion protocol library powered by ofetion project
Name: libofetion
Version: 2.2.2
Release: 5.1
Group: Networking/Instant messaging
License: GPLv2+
URL: http://code.google.com/p/ofetion/
Source0: http://ofetion.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires: openssl-devel
BuildRequires: sqlite-devel
BuildRequires: libxml2-devel
BuildRequires: gcc-c++
BuildRequires: cmake
Conflicts: openfetion < 2.1.0

%description
OpenFetion is a IM client based on GTK+2.0, using CHINA MOBILE's Fetion
Protocol Version 4.

%files
%{_datadir}/libofetion*/resource
%{_libdir}/libofetion.so.*

%package devel
Summary: Fetion protocol library powered by ofetion project
Group: Development/C
Requires: %{name} = %{version}

%description devel
OpenFetion is a IM client based on GTK+2.0, using CHINA MOBILE's Fetion
Protocol Version 4.

%files devel
%{_includedir}/*
%{_libdir}/libofetion.so
%{_libdir}/libofetion.a
%{_libdir}/pkgconfig/*.pc

%prep
%setup -q
sed -i 's|r->n = bnn;\tr->e = bne;\tr->d = NULL;|RSA_set0_key(r,bnn,bne,NULL);|' fetion_login.c

%build
mkdir build ; cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DLIB_INSTALL_DIR=%{_libdir} -DCMAKE_BUILD_TYPE=release ..
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT -C build install

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jan 3 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.2
- Rebuild for Fedora
* Sun Dec 26 2010 Funda Wang <fwang@mandriva.org> 2.1.0-1mdv2011.0
+ Revision: 625215
- import libofetion
