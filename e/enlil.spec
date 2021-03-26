%define	name enlil
%define version 0.6
%define release 20101225

%define major 1
%define libname lib%{name}
%define libnamedev lib%{name}-devel


Summary:	enil Library for EFL
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source:		%{name}-%version.tar.gz
BuildRequires:  libiptcdata-devel
BuildRequires:	flickcurl-devel
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
BuildRequires:	exchange-devel
BuildRequires:	eeze-devel
BuildRequires:  ethumb-devel

%description
Enlil is a library using the EFL which allows to manage
a list of albums and photos. EET is used to create the
database and ecore to manage events and file.


%package devel
Summary:  enil headers, static libraries, documentation and test programs
Group:    Graphical desktop/Enlightenment
Requires: %name = %version
Provides: lib%{name}-devel = %version-%release
Provides: %{name}-devel = %version-%release

%description devel
Headers, static libraries, test programs and documentation for Enlil.

%prep
%setup -q

%build
./autogen.sh --disable-static --prefix=/usr
%__make

%install
rm -fr $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL NEWS README
%_bindir/enlil_db_load_sync
%_bindir/enlil_db_print
%_bindir/enlil_db_sync
%_bindir/enlil_geocaching_print
%_bindir/enlil_transformations
%_libdir/libenlil.so.*

%files devel
%defattr(-, root, root)
%_includedir/enlil/Enlil.h
%_libdir/libenlil.la
%_libdir/libenlil.so
%_libdir/pkgconfig/enlil.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Wed Jan 05 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101225-1pclos2010
- update svn

* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update svn 55246
