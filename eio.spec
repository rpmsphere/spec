Summary:	Enlightenment Input Output Library
Name:		eio
Version:	0.1.0.65643
Release:	1%{?dist}
License:	BSD
Group:		Graphical desktop/Enlightenment
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.enlightenment.org/
Source:		http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.bz2
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
This library is intended to provide non blocking IO by using thread for all
operation that may block. It depends only on eina and ecore right now.


%package devel
Summary:  eio headers, static libraries, documentation and test programs
Group:    Graphical desktop/Enlightenment
Requires: %name = %version
Provides: lib%{name}-devel = %version-%release
Provides: %{name}-devel = %version-%release

%description devel
Headers, static libraries, test programs and documentation for eio.

%prep
%setup -q

%build
./autogen.sh --disable-static --prefix=/usr
%__make

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL NEWS README
%_libdir/libeio*.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/eio-0
%{_libdir}/libeio.la
%{_libdir}/libeio.so
%{_libdir}/pkgconfig/eio.pc

%changelog
* Fri Mar 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> 0.1.0
- Update to r65643

* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101225-1pclos2010
- update svn

* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update svn 55246
