Summary: libpurple plugin powered by libofetion
Name: pidgin-openfetion
Version: 0.3
Release: 8.4
Group: Networking/Instant messaging
License: GPLv2+
URL: http://code.google.com/p/ofetion/
Source0: http://ofetion.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires: libpng-devel
BuildRequires: pidgin-devel
BuildRequires: openssl-devel
BuildRequires: libxml2-devel
BuildRequires: gcc-c++
BuildRequires: cmake

%description
libpurple plugin powered by libofetion.

%prep
%setup -q
sed -i 's|r->n = bnn;\tr->e = bne;\tr->d = NULL;|RSA_set0_key(r,bnn,bne,NULL);|' fx_login.c

%build
mkdir build ; cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DLIB_INSTALL_DIR=%{_libdir} -DCMAKE_BUILD_TYPE=release ..
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT -C build install
%find_lang pidgin-ofetion

%clean
rm -rf $RPM_BUILD_ROOT

%files -f pidgin-ofetion.lang
%{_libdir}/purple-2/libopenfetion.so
%{_datadir}/pixmaps/pidgin/protocols/16/openfetion.png
%{_datadir}/purple/openfetion

%changelog
* Tue Jan 03 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
* Sun Mar 13 2011 Funda Wang <fwang@mandriva.org> 0.1-2mdv2011.0
+ Revision: 644364
- fix typo of xml libs
- import pidgin-openfetion
