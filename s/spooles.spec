%global flavor %{nil}

%define pkgname spooles

%if "%{flavor}" == ""
%define my_prefix %_prefix
%define my_bindir %_bindir
%define my_libdir %_libdir
%define my_incdir %_includedir
%define my_datadir %_datadir
%endif

%if "%{flavor}" == "openmpi"
%if 0%{?suse_version} >= 1550
%define my_suffix  -openmpi1
%define mpi_flavor  openmpi1
%else
%define my_suffix  -openmpi
%define mpi_flavor  openmpi
%endif
%define mpiprefix %{_libdir}/mpi/gcc/%{mpi_flavor}
%endif

%if "%{flavor}" == "openmpi2"
%define my_suffix  -openmpi2
%define mpi_flavor  openmpi2
%define mpiprefix %{_libdir}/mpi/gcc/%{mpi_flavor}
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}

%if %{with mpi}
%define my_prefix %{mpiprefix}
%define my_bindir %{my_prefix}/bin
%define my_libdir %{my_prefix}/%{_lib}/
%define my_incdir %{my_prefix}/include/
%define my_datadir %{my_prefix}/share/
%endif


Name:           %{pkgname}%{?my_suffix}
Version:        2.2
Release:        3.56
Summary:        A sparse matrix library
# SPOOLES: Public Domain
# SPOOLES: Utilities/src/iohb.c: BSD 2-Clause style
License:        BSD-2-Clause AND SUSE-Public-Domain
Group:          System/Libraries
URL:            http://www.netlib.org/linalg/spooles/spooles.2.2.html
Source0:        http://netlib.bell-labs.com/netlib/linalg/spooles/spooles.2.2.tar.bz2
Patch0:         patch-spooles-shared
Patch1:         patch-spooles-shared-mpi
Patch2:         patch-spooles-I2Ohash-from-debian
%if %{with mpi}
BuildRequires:  %{mpi_flavor}-devel
%endif

%description
SPOOLES is a library for solving sparse real and complex linear systems
of equations, written in the C language using object oriented design.

%{with mpi:This package has been built with %{mpi_flavor} support.}

%prep
%setup -c -q

%patch0 -p1
%patch1 -p1
%patch2 -p1

%package devel
Summary:        Header files for the SPOOLES library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}

%description devel
spooles-devel provides the header file for the SPOOLES library.

%build
cd ${RPM_BUILD_DIR}/%{name}-%{version}
export CFLAGS="$RPM_OPT_FLAGS -O2 -pthread -Wno-format-security"

%if %{without mpi}
make -f makeRPM all %{?_smp_mflags}

%else
# openmpi
make -f makeRPM-mpi all %{?_smp_mflags} \
   CC=%{my_bindir}/mpicc \
   MPI_INSTALL_DIR=%{my_prefix} \
   MPI_LIB_PATH=-L%{my_libdir}/
%endif

%install
mkdir -p %{buildroot}/%{my_libdir}
cp -P libspooles* %{buildroot}/%{my_libdir}
chmod 755 %{buildroot}/%{my_libdir}/libspooles.so.%{version}

# header files: use same convention as debian spooles package:
# all headers under /usr/include/spooles

mkdir -p %{buildroot}/%{my_incdir}/spooles
for headerfile in `find . -name \*.h -print`; do
	dir="%{buildroot}/%{my_incdir}/spooles/`dirname $headerfile`"
	mkdir -p $dir
	install -m 644 $headerfile $dir
done

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{my_libdir}/libspooles.so.2.2
%doc spooles.2.2.html

%files devel
%defattr(-,root,root)
%{my_incdir}/spooles/
%{my_libdir}/libspooles.so

%changelog
* Thu Nov 28 2019 Stefan Brüns <stefan.bruens@rwth-aachen.de>
- Cleanup spec file
- Convert to multibuild
- Fix openmpi naming on TW
* Tue May  8 2012 scorot@free.fr
- spec file cleanup
- set compiler optimisation to -O2 as -O3 did not result in any
  speedup
