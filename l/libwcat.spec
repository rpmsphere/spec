%global debug_package %{nil}

Summary:	Library for the watchcat software watchdog
Name:		libwcat
Version:	1.1
Release:	11.1
License:	LGPL
Group:		System/Libraries
URL:		http://oss.digirati.com.br/watchcatd/
Source0:	http://oss.digirati.com.br/watchcatd/%{name}-%{version}.tar.gz
Patch0:		libwcat-ldflags.diff
Patch1:		libwcat-socket_location_fix.diff
Requires:   watchcatd

%description
libwcat is an API to watchcatd, a software watchdog that uses an
approach not as drastic as the usual watchdog solutions. It tries
to kill the locked process only.

%package devel
Summary:	Static library and header files for the watchcat library
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
libwcat is an API to watchcatd, a software watchdog that uses an
approach not as drastic as the usual watchdog solutions. It tries
to kill the locked process only.

This package contains the static libwcat library and its header files
needed to compile applications that use libwcat.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build
make 

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}
install -m755 %{name}.so.1.%{version} %{buildroot}%{_libdir}/
install -m644 %{name}.a %{buildroot}%{_libdir}/
install -m644 watchcat.h %{buildroot}%{_includedir}/

ln -s %{name}.so.1.%{version} %{buildroot}%{_libdir}/%{name}.so
ln -s %{name}.so.1.%{version} %{buildroot}%{_libdir}/%{name}.so.1

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a

%changelog
* Wed Sep 21 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuild for Fedora
* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 1.1-4
+ Revision: 14f23a7
- MassBuild#464: Increase release tag
