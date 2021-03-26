Name:         nana
Summary:      A modern C++ GUI library 
URL:          http://nanapro.org/
Group:        System
License:      BSL-1.0
Version:      1.5.6
Release:      5.1
Source0:      https://github.com/cnjinhao/nana/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: libXft-devel

%description
Nana is a C++ library designed to allow developers to easily create
cross-platform GUI applications with modern C++11 style.

%package devel
Summary: Development files for the modern C++ GUI library %{name}
#Requires: %{name} = %{version}

%description devel
Header files and libraries for Nana.
Nana is a C++ library designed to allow developers to easily create
cross-platform GUI applications with modern C++11 style.

%prep
%setup -q

%build
%cmake -DNANA_CMAKE_SHARED_LIB:BOOL=ON
make %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files devel
%{_includedir}/*
%{_libdir}/lib*.so

%changelog
* Thu Mar 08 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.6
- Rebuild for Fedora
