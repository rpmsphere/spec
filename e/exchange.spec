%define	name	exchange
%define version 0.0.0.002
%define release 1
%define major 0
%define libname lib%{name}
%define libnamedev lib%{name}-devel

Summary: 	exchange is a place to share themes
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source: 	%{name}-%{version}.tar.gz
# Common
BuildRequires:	ncurses-devel
BuildRequires: zlib-devel
# Enlightenment BR
BuildRequires:	libeina-devel
BuildRequires: 	eet-devel
BuildRequires:  evas-devel
BuildRequires:	ecore-devel
BuildRequires:	efreet-devel
BuildRequires:	embryo-devel
BuildRequires:	edje-devel
BuildRequires:	emotion-devel
BuildRequires:	e_dbus-devel

%description
exchange is a place to share themes, applications and modules for the enlightenment shell.

This package is part of the Enlightenment DR17 desktop shell.


%package devel
Summary: Headers and development libraries from %{name}
Group: Graphical desktop/Enlightenment
Requires: %name = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{libname}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description devel
%{name} development headers and libraries

%prep
%setup -q

%build
./autogen.sh --disable-static --prefix=/usr
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/lib*.so.%{major}*


%files devel
%{_libdir}/pkgconfig/*
%{_libdir}/libexchange.so
%{_libdir}/libexchange.la
%{_includedir}/exchange-0


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.0.002
- Rebuild for Fedora
* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101225-1pclos2010
- update svn
* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update svn 55246
