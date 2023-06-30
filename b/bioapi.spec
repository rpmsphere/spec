%global __os_install_post %{nil}

Name:          bioapi
Version:       1.2.3
Release:       10.1
Summary:       A high-level generic biometric authentication model
Group:         Applications/Security
URL:           https://code.google.com/p/bioapi-linux/
Source:        https://bioapi-linux.googlecode.com/files/%{name}_%{version}.tar.gz
Patch0:        %{name}-1.2.2-gcc44.patch
License:       BSD
BuildRequires: libpng-devel
BuildRequires: gcc-c++, qt3-devel, libXmu-devel, libXi-devel

%description
The BioAPI Specification is intended to provide a high-level generic biometric
authentication model, one suited for any form of biometric technology.
It covers the basic functions of Enrollment, Verification, and Identification,
and includes a database interface to allow a biometric service provider (BSP)
to manage the Identification population for optimum performance.
It also provides primitives that allow the application to manage the capture of
samples on a client, and the Enrollment, Verification, and Identification on a server. 

%package -n libbioapi
Summary:       A high-level generic biometric authentication model
Group:         System/Libraries

%description -n libbioapi
The BioAPI Specification is intended to provide a high-level generic biometric
authentication model, one suited for any form of biometric technology.
It covers the basic functions of Enrollment, Verification, and Identification,
and includes a database interface to allow a biometric service provider (BSP)
to manage the Identification population for optimum performance.
It also provides primitives that allow the application to manage the capture of
samples on a client, and the Enrollment, Verification, and Identification on a server. 

%package -n libbioapi-devel
Summary:       Devel package for libbioapi
Group:         Development/Libraries
Requires:      libbioapi = %{?epoch:%epoch:}%{version}-%{release}

%description -n libbioapi-devel
This package contains static libraries and header files need for libbioapi.

%package -n libbioapi-qt
Summary:       A qt implementation of the high-level generic biometric authentication model
Group:         System/Libraries

%description -n libbioapi-qt
A qt implementation of the high-level generic biometric authentication model.

%package -n libbioapi-qt-devel
Summary:       Devel package for libbioapi-qt
Group:         Development/Libraries
Requires:      libbioapi-qt = %{?epoch:%epoch:}%{version}-%{release}

%description -n libbioapi-qt-devel
This package contains static libraries and header files need for libbioapi-qt.

%prep
%setup -q -n %{name}-linux
%patch0 -p1
ln -sf /usr/share/automake-1.1?/config.guess config.guess
ln -sf /usr/share/automake-1.1?/config.sub config.sub
sed -i '26060,26163d' configure

%build
%configure --with-Qt-dir=%{_libdir}/qt-3.3
make

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/BioAPITest
%{_bindir}/MdsEdit
%{_bindir}/QSample
%{_bindir}/Sample
%{_bindir}/mds_install
%{_bindir}/mod_install

%files -n libbioapi
%{_libdir}/libbioapi100.so.*
%{_libdir}/libbioapi_dummy100.so.*
%{_libdir}/libbioapi_mds300.so.*
%{_libdir}/libmds_util.so.*
%{_libdir}/libpwbsp.so.*
%doc README

%files -n libbioapi-devel
%{_includedir}/bioapi.h
%{_includedir}/bioapi_api.h
%{_includedir}/bioapi_err.h
%{_includedir}/bioapi_schema.h
%{_includedir}/bioapi_spi.h
%{_includedir}/bioapi_type.h
%{_includedir}/bioapi_typecast.h
%{_includedir}/bioapi_uuid.h
%{_includedir}/biospi.h
%{_includedir}/biospi_type.h
%{_includedir}/bioapi_installdefs.h
%{_includedir}/bioapi_util.h
%{_includedir}/cssmtype.h
%{_includedir}/bsp_schema.h
%{_libdir}/libbioapi100.a
%{_libdir}/libbioapi_dummy100.a
%{_libdir}/libbioapi_mds300.a
%{_libdir}/libmds_util.a
%{_libdir}/libpwbsp.a
%{_libdir}/libbioapi100.la
%{_libdir}/libbioapi_dummy100.la
%{_libdir}/libbioapi_mds300.la
%{_libdir}/libmds_util.la
%{_libdir}/libpwbsp.la
%{_libdir}/libbioapi100.so
%{_libdir}/libbioapi_dummy100.so
%{_libdir}/libbioapi_mds300.so
%{_libdir}/libmds_util.so
%{_libdir}/libpwbsp.so

%files -n libbioapi-qt
%{_libdir}/libqtpwbsp.so.*

%files -n libbioapi-qt-devel
%{_libdir}/libqtpwbsp.a
%{_libdir}/libqtpwbsp.la
%{_libdir}/libqtpwbsp.so

%changelog
* Wed Jun 15 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.3
- Rebuilt for Fedora

* Thu Dec 16 2010 Automatic Build System <autodist@mambasoft.it> 1.2.2-3mamba
- automatic rebuild by autodist

* Sun May 10 2009 Automatic Build System <autodist@mambasoft.it> 1.2.2-2mamba
- automatic rebuild by autodist

* Fri May 25 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 1.2.2-1mamba
- package created by autospec
