%global debug_package %{nil}

Name:           dlib
Version:        18.0
Release:        4.1
Summary:        A general purpose cross-platform C++ library
Group:          Development/Libraries/C and C++
License:        Boost Software License
URL:            http://dlib.net/
Source0:        dlib-%{version}.tar.bz2
BuildRequires:  cmake libjpeg-devel libpng-devel gcc-c++ gcc

%description
Dlib is designed using contract programming and modern C++ techniques.

%package        devel
Summary:        Development files for Dlib
Group:          Development/Libraries/C and C++
Requires:      gcc-c++

%description    devel
Dlib is designed using contract programming and modern C++ techniques.

%prep
%setup -q

%build
cd dlib
cmake  -DCMAKE_INSTALL_PREFIX:PATH=/usr \
       -DCMAKE_BUILD_TYPE:STRING="Release"

make VERBOSE=1 %{?_smp_mflags}

%install
mkdir %{buildroot}/usr
mkdir %{buildroot}/usr/%{_lib}
mkdir %{buildroot}/usr/include
mv ./dlib/libdlib.a %{buildroot}/usr/%{_lib}/
rm -rf ./dlib/CMakeFiles
mv dlib %{buildroot}/usr/include/
mv docs %{buildroot}/usr/include/dlib/
mv examples %{buildroot}/usr/include/dlib/
mv documentation.html %{buildroot}/usr/include/dlib/

%clean
rm -rf %{buildroot}

%files devel
%{_libdir}/lib*.a
%{_includedir}/dlib/

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 18.0
- Rebuild for Fedora
