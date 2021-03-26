%define debug_package %{nil}
%define devname properties-cpp-devel

Name: properties-cpp
Version: 0.0.1
Release: 1
Source0: %{name}-%{version}.tar.xz
Patch0: properties-cpp-system-gmock.patch
Summary: C++11 implementation of properties and signals
URL: http://launchpad.net/properties-cpp
License: LGPLv3
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: gtest-devel
BuildRequires: gmock-devel
BuildRequires: gmock-source
BuildRequires: doxygen

%description
process-cpp is a simple header-only implementation of properties and
signals. It is meant to be used for developing low-level system
services. Its main features include:

 - Thread-safe signal invocation and observer mgmt.
 - The ability to dispatch signal invocations via arbitrary event loops.
 - Typed properties with an in-place update mechanism that avoids unneccessary
   deep copies.
 - Well tested and documented.


%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -qn %{name}
%patch0 -p1

%cmake -G Ninja \
	-DGTEST_LIBRARY=-lgtest

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{devname}
%{_includedir}/*
%{_libdir}/pkgconfig/*
%doc %{_docdir}/properties-cpp
