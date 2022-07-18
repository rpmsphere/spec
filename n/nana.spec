Name:         nana
Summary:      A modern C++ GUI library 
URL:          http://nanapro.org/
Group:        System
License:      BSL-1.0
Version:      1.7.4
Release:      1
Source0:      %{name}_%{version}.zip
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
%setup -q -n %{name}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON .
sed -i 's|$<1:-static-libgcc -static-libstdc++> $<0:-static-libgcc -static-libstdc++>|-static-libgcc -static-libstdc++ -static-libgcc -static-libstdc++|' CMakeFiles/nana.dir/link.txt
%make_build

%install
rm -rf $RPM_BUILD_ROOT
install -d %{buildroot}%{_includedir}
cp -a include/nana %{buildroot}%{_includedir}
install -Dm755 libnana.so %{buildroot}%{_libdir}/libnana.so

%files devel
%doc LICENSE *.html ChangeLog.txt
%{_includedir}/*
%{_libdir}/lib*.so

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7.4
- Rebuilt for Fedora
