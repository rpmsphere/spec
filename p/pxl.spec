Name: pxl
Summary: Physics eXtension Library
Version: 4.0.1
Release: 1
Group: Development/Libraries
License: GPL
URL: https://vispa.physik.rwth-aachen.de/pxl
Source0: https://forge.physik.rwth-aachen.de/attachments/download/496/%{name}-v%{version}.tar.gz
BuildRequires: cmake
#BuildRequires: python2-devel python-unversioned-command
BuildRequires: swig

%description
C++ Toolkit for Physics Analysis, Relation Management and
Hypothesis Evolution in High Energy and Astroparticle Physics.

%package devel
Summary: Development files for PXL
Requires: %{name}

%description devel
Header files and Libraries for the package PXL.

%prep
%setup -q -n %{name}-v%{version}
#sed -i 's|-classic||' scripting/CMakeLists.txt

%build
#export CXXFLAGS="-std=c++98 -fPIC"
#cmake -DPYTHON_EXECUTABLE=/usr/bin/python3
%cmake
%cmake_build

%install
%cmake_install
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
mkdir -p %{buildroot}%{_datadir}/cmake/
mv %{buildroot}%{_datadir}/FindPXL.cmake %{buildroot}%{_datadir}/cmake/
rm %{buildroot}/usr/setup.sh

%files
%doc *.md
%{_bindir}/%{name}*
%{_libdir}/lib%{name}*.so.*
#{python2_sitearch}/*

%files devel
%{_includedir}/%{name}*
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}*
%{_datadir}/cmake/*

%changelog
* Fri Sep 11 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.1
- Rebuilt for Fedora
