Name:          stlport
Version:       5.2.1
Release:       1
Summary:       Multiplatform C++ Standard Library
Group:         System/Libraries
License:       GPL
URL:           http://www.stlport.org/
Source0:       http://sourceforge.net/projects/stlport/files/STLport/STLport-5.2.1/STLport-5.2.1.tar.gz
BuildRequires: gcc-c++, libstdc++-static, boost-devel

%description
STLport is a multiplatform ANSI C++ Standard Library implementation. It is
free, open-source product, featuring the following:
-  Advanced techniques and optimizations for maximum efficiency
-  Exception safety and thread safety
-  Important extensions - hash tables, singly-linked list, rope

%package devel
Group:         Development/C++
Summary:       Devel package for %{name}
Requires:      %name = %{version}-%{release}

%description devel
STLport is a multiplatform STL implementation based on SGI STL. Complete   
C++ standard library, including <complex> and SGI STL iostreams.

This package contains static libraries and header files need for development.

%prep
%setup -q -n STLport-%{version}
sed -i 's|__USE_BSD|__USE_MISC|' src/time_facets.cpp

%build
./configure \
  --prefix=%_prefix \
  --bindir=%_bindir \
  --libdir=%_libdir \
  --includedir=%_includedir \
  --use-compiler-family=gcc \
  --with-system-boost \
  --with-extra-cxxflags="-std=gnu++11" \
  --without-debug
make

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%_libdir/libstlport*.so.*
%doc README

%files devel
%_includedir/stlport
%_libdir/libstlport*.so
%doc INSTALL* etc/ChangeLog* etc/*.txt etc/*.gif doc/FAQ doc/README.utf8 doc/*.txt

%changelog
* Sun Nov 18 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 5.2.1
- Rebuild for Fedora
* Wed Dec 28 2011 gil <gil> 5.2.1-1.mga2
+ Revision: 188331
- imported package stlport
