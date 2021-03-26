Name:           cocoalib
Version:        0.9943
Release:        3.1
Summary:        Computations library in Commutative Algebra
Group:          Development/Libraries
License:        GPL
URL:            http://cocoa.dima.unige.it/cocoalib/
Source0:        http://cocoa.dima.unige.it/cocoalib/tgz/CoCoALib-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gcc-c++, gmp-devel, gsl-devel, atlas-devel

%description
CoCoALib is a GPL C++ library for doing Computations in Commutative Algebra.
CoCoALib will be the mathematical kernel for the completely new system CoCoA-5.

%package        devel
Summary:        Computations library in Commutative Algebra - Development files
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains libraries and header files for CoCoALib.

%prep
%setup -q -n CoCoALib-%{version}

%build
./configure --with-libgmp=%{_libdir}/libgmp.so
make %{?_smp_mflags}
cd src/AlgebraicCore/TmpHilbertDir
g++ -fPIC -shared -o ../../../lib/libcocoa.so *.o

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
cp -a lib/libcocoa.* $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/CoCoA
cp -a include/CoCoA/* $RPM_BUILD_ROOT%{_includedir}/CoCoA

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING-GPLv2 COPYING-GPLv3 README
%{_libdir}/libcocoa.so

%files devel
%defattr(-,root,root,-)
%doc doc examples
%{_includedir}/CoCoA
%{_libdir}/libcocoa.a

%changelog
* Wed May 11 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9943
- Initial package
