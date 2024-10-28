Name:          libdjconsole
Version:       0.1.3
Release:       3.1
Summary:       A driver for the DJ Console, built on top of libusb
Group:         System/Libraries
URL:           https://djplay.sourceforge.net/
Source:        https://dfn.dl.sourceforge.net/sourceforge/djplay/libdjconsole-%{version}.tar.gz
License:       GPL
BuildRequires: gcc-c++
BuildRequires: libusb-compat-0.1-devel

%description
A driver for the DJ Console, built on top of libusb.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
A driver for the DJ Console, built on top of libusb.

This package contains static libraries and header files need for development.

%prep
%setup -q
sed -i 's|\(hdev.\) < 0|\1 == NULL|' djconsole.cpp

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%files
%{_libdir}/libdjconsole.so.*
%{_datadir}/libdjconsole/*
%doc AUTHORS COPYING ChangeLog NEWS README

%files devel
%{_sysconfdir}/udev/rules.d/45-hpdjconsole.rules
%{_libdir}/libdjconsole.a
#{_libdir}/libdjconsole.la
%{_libdir}/libdjconsole.so
%{_includedir}/libdjconsole/*.h
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.3
- Rebuilt for Fedora

* Fri Oct 03 2008 gil <puntogil@libero.it> 0.1.3-1mamba
- update to 0.1.3

* Thu May 10 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 0.1.2-1mamba
- package created by autospec
