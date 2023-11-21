Summary:	OTP token authentication daemon
Name:		libotpdb
Version:	88d5c3b7a826
Release:	22.1
License:	GPL
Group:		System Environment/Daemons
Vendor:		lsexperts
URL:		https://opensource.lsexperts.de/projects/linotp/
Source:		%{name}-%{version}.tar.gz
BuildRequires:	openssl-devel, openldap-devel

%description
Otpd is part of a suite of software for authenticating users with handheld OTP tokens.

%package devel
License:        GPL
Group:          Development/Libraries
Summary:        Libotpdb Development Files
Requires:       %{name} = %{version}

%description devel
This package contains all necessary include files and libraries needed to develop applications using libotpdb

%prep
%setup -q

%build
./autogen.sh
%configure --enable-static=no
make  %{?jobs:-j%jobs}

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig  

%postun -p /sbin/ldconfig

%files
%doc README COPYING
%{_libdir}/*.so*
#{_libdir}/*.la

%files devel
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 88d5c3b7a826
- Rebuilt for Fedora
* Wed Oct 21 2009 joop.boonen@opensuse.org
- Build version 3.1.0 for OBS
