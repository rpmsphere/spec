Name:          libol
Version:       0.3.18
Release:       3.1
Summary:       A nonblocking I/O and OO library used by syslog-ng
Group:         System/Libraries
URL:           http://www.balabit.com/network-security/syslog-ng/
Source:        http://www.balabit.com/downloads/files/libol/0.3/%{name}-%{version}.tar.gz
License:       GPL
BuildRequires: gcc-c++
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

%description
A nonblocking I/O and OO library used by syslog-ng.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description devel
A nonblocking I/O and OO library used by syslog-ng.
This package contains static libraries and header files need for development.

%prep
%setup -q

%build
%configure
make SCSH=/bin/sh

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall SCSH=/bin/sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/libol.so.*
%doc COPYING

%files devel
%defattr(-,root,root)
%{_bindir}/libol-config
%{_bindir}/make_class
%{_libdir}/libol.so
%{_libdir}/libol.a
%{_libdir}/libol.la
%{_includedir}/libol/*.h
%{_includedir}/libol/*.h.x
%doc ChangeLog

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.18
- Rebuild for Fedora

* Wed Sep 03 2008 Tiziana Ferro <tiziana.ferro@email.it> 0.3.18-1mamba
- update to 0.3.18

* Mon Oct 09 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.3.17-2qilnx
- rebuilt

* Thu Dec 01 2005 Silvan Calarco <silvan.calarco@qilinux.it> 0.3.17-1qilnx
- package created by autospec
