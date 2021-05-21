Summary: Lazy RPC client/server library
Name: azy
Version: 1.0.0
Release: 20101225
License: LGPLv2.1
Group: Graphical desktop/Enlightenment
Source: %{name}-%{version}.tar.gz
URL: http://www.enlightenment.org/
Requires: libeina, ecore
BuildRequires: libeina-devel, ecore-devel

%description
Azy is a full rewrite of libzxr, itself a modification of libxr.  It is meant for
implementing rpc clients and servers in a simple manner.

%package devel
Summary: Azy headers, static libraries, documentation and test programs
Group: Graphical desktop/Enlightenment
Requires: %{name} = %{version}

%description devel
Headers, static libraries, test programs and documentation for Azy

%prep
%setup -q

%build
./autogen.sh
%configure --disable-static
%__make

%install
rm -fr $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_bindir}/azy_parser
%{_mandir}/man1/azy_parser.1.*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Jan 05 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101225-1pclos2010
- update svn
