%undefine _debugsource_packages

Name: shark
Summary: A modular C++ library for the design and optimization of adaptive systems
Version: 2.3.4
Release: 12.1
License: GPLv2
Group: devel
URL: http://shark-project.sourceforge.net/
Source0: %{name}-%{version}.zip
BuildRequires: cmake

%description
SHARK provides methods for linear and nonlinear optimization, in particular
evolutionary and gradient-based algorithms, kernel-based learning algorithms
and neural networks, and various other machine learning techniques. SHARK
serves as a toolbox to support real world applications as well as research
in different domains of computational intelligence and machine learning.
The sources are compatible with the following platforms: Windows, Solaris,
MacOS X, and Linux.

%package devel
Summary: Development header files and libraries for SHARK
Group: Development/Libraries
Requires: %{name}

%description devel
This package contains the development files required to compile programs that use SHARK.

%prep
%setup -q -n Shark

%build
export CXXFLAGS="-fpermissive -fPIC"
%cmake
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files
%doc *.txt
%{_libdir}/*.so.*
%{_datadir}/%{name}

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.4
- Rebuilt for Fedora
