Name:          mISDNuser
Version:       2.0.19
Release:       2.1
Summary:       User space tools for the mISDN driver
Group:         System/Kernel and Hardware
URL:           https://www.misdn.org
Source0:       %{name}-%{version}.tar.gz
License:       GPL v2 only ; LGPL v2.1 only

%description
User space tools for the mISDN 2.0 driver.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries    
Requires:      %{name} = %{version}

%description devel
Library for supporting the %{name}.
This package contains static libraries and header files need for development.

%prep
%setup -q
sed -i 's|const const|const|' lib/suppserv/diversion.c
sed -i 's|-Werror | |' */Makefile*

%build
make
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall INSTALL_PREFIX=$RPM_BUILD_ROOT
rm %{buildroot}%{_libdir}/libmisdn.a %{buildroot}%{_libdir}/libmisdn.la

%files
%doc LICENSE NEWS COPYING.LIB README AUTHORS
%{_sysconfdir}/udev/rules.d/45-misdn.rules
%{_bindir}/isdn_text2wireshark
%{_bindir}/l1oipctrl
%{_bindir}/misdn_E1test
%{_bindir}/misdn_bridge
%{_bindir}/misdn_info
%{_bindir}/misdn_log
%{_libdir}/libmisdn.so.1
%{_libdir}/libmisdn.so.1.0.0
%{_sbindir}/misdn_cleanl2
%{_sbindir}/misdn_rename

%files devel
%{_includedir}/mISDN/l3dss1.h
%{_includedir}/mISDN/mISDNcompat.h
%{_includedir}/mISDN/mISDNif.h
%{_includedir}/mISDN/mbuffer.h
%{_includedir}/mISDN/mlayer3.h
%{_includedir}/mISDN/q931.h
%{_includedir}/mISDN/suppserv.h
%{_libdir}/libmisdn.so

%changelog
* Wed Feb 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.19
- Rebuilt for Fedora
* Fri Aug 28 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 1.1.9-1mamba
- update to 1.1.9
* Fri Jun 19 2009 coolo@novell.com
- disable as-needed for this package as it fails to build with it
* Mon Sep  1 2008 kkeil@suse.de
- first version
