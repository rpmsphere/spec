Summary: Embedded InnoDB library
Name: innodb
Version: 1.0.6.6750
Release: 7.1
License: GPL
Group: System Environment/Libraries
BuildRequires: gcc zlib-devel
URL: http://www.innodb.com/products/embedded_innodb/
Source: http://www.innodb.com/download/embedded_%{name}/embedded_%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Made for application developers, device makers and ISVs, Embedded InnoDB
provides all the high-performance, proven and reliable data management features
of InnoDB in an embeddable form, without the overhead, footprint or unneeded
features of the MySQL server.

Embedded InnoDB is used independently of MySQL. It is not a plugin, nor a
storage engine for MySQL. It is designed to be linked directly into application
programs, and provides highly efficient, low-level database management
services, not using SQL.

Embedded InnoDB provides the features, functions and capabilities that embedded
applications require:

  * Embedded InnoDB delivers all the high-performance and reliability
    capabilities of the InnoDB storage engine, including concurrency control,
    sophisticated indexing, crash recovery and more.
  * For application programmers, Embedded InnoDB provides a non-SQL, ISAM-like
    API for creating and querying tables and executing other data management
    functions.
  * Designed for use in environments without a database administrator, Embedded
    InnoDB configuration is fully automatic and has all the operational
    characteristics needed for stand-alone applications and devices.

%package devel
Group: Development/Libraries
Summary: Embedded InnoDB Library - Header files
Requires: innodb zlib-devel

%description devel
Development files for the Embedded InnoDB library.

Made for application developers, device makers and ISVs, Embedded InnoDB
provides all the high-performance, proven and reliable data management features
of InnoDB in an embeddable form, without the overhead, footprint or unneeded
features of the MySQL server.

Embedded InnoDB is used independently of MySQL. It is not a plugin, nor a
storage engine for MySQL. It is designed to be linked directly into application
programs, and provides highly efficient, low-level database management
services, not using SQL.

Embedded InnoDB provides the features, functions and capabilities that embedded
applications require:

  * Embedded InnoDB delivers all the high-performance and reliability
    capabilities of the InnoDB storage engine, including concurrency control,
    sophisticated indexing, crash recovery and more.
  * For application programmers, Embedded InnoDB provides a non-SQL, ISAM-like
    API for creating and querying tables and executing other data management
    functions.
  * Designed for use in environments without a database administrator, Embedded
    InnoDB configuration is fully automatic and has all the operational
    characteristics needed for stand-alone applications and devices.

%prep
%setup -q -n embedded_%{name}-%{version}

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR="$RPM_BUILD_ROOT"
# Remove redundant license file to satisfy rpmlint
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}-1.0/examples/COPYING

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%{_libdir}/libinnodb.so.*

%files devel
%defattr(-, root, root)
%doc ChangeLog COPYING COPYING.Google README
%{_datadir}/embedded_%{name}-1.0
%{_includedir}/embedded_%{name}-1.0
%{_libdir}/libinnodb.a
%{_libdir}/libinnodb.la
%{_libdir}/libinnodb.so

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.6.6750
- Rebuild for Fedora
* Thu Mar 11 2010 lenz@grimmer.com
- Update to version 1.0.6.6750
- Bumped up shared library number
* Mon Jun 29 2009 lenz@grimmer.com
- Fixed Requirements for the devel package
- Added Provides/Obsoletes Tag to the shared library package to
  allow smooth upgrading from version 1.0.0
* Thu Jun 25 2009 lenz@grimmer.com
- Update to version 1.0.3.5325
- Bumped up shared library number
- Bzipped sources
- Fixed name of the library package to satisfy rpmlint
- Added versioned dependency to the devel package
- Adjusted file list, remove redundant COPYING file in the
  examples directory
* Wed Jun 17 2009 lenz@grimmer.com
- Initial package (version 1.0.0)
