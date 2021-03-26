Summary:	Mesa OpenCL implementation
Name:		clover
Version:	0.1.0
Release:	19.1
License:	opensource
Group:		System/Libraries
URL:		http://cgit.freedesktop.org/~steckdenis/clover/
Source:		%{name}-master.tar.gz
BuildRequires:  cmake, gcc-c++, boost-devel, clang-devel, llvm-devel, mesa-libGL-devel, python2
Provides:	opencl = 1.1.0

%description
OpenCL is a royalty-free standard for cross-platform, parallel programming
of modern processors found in personal computers, servers and
handheld/embedded devices.

This package provides an OpenCL 1.1 software and Gallium-based implementation.

%package devel
Summary:	OpenCL development files
Group:		Development/C
Requires:	opencl = 1.1.0
Requires:	opencl-headers
Provides:	opencl-devel = 1.1.0

%description devel
OpenCL is a royalty-free standard for cross-platform, parallel programming
of modern processors found in personal computers, servers and
handheld/embedded devices.

This package provides the files needed to compile software that uses
OpenCL.

%prep
%setup -q -n %{name}
sed -i '/examples/d' CMakeLists.txt
sed -i -e 's| -fno-rtti||' -e 's|/usr/lib|%{_libdir}|' src/CMakeLists.txt
sed -i 's|getNameStr()|getName().str()|' src/core/program.cpp src/core/kernel.cpp src/core/cpu/builtins.cpp
%if %fedora > 17
sed -i -e 's|getHostTriple|getDefaultTargetTriple|' -e 's|std::make_pair(clang::IK_OpenCL, "program.cl")|clang::FrontendInputFile("program.cl", clang::IK_OpenCL)|' src/core/compiler.cpp
%endif

%build
%cmake
make

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%files
%doc README COPYING
%{_libdir}/libOpenCL.so.*

%files devel
%{_libdir}/libOpenCL.so
#{_libdir}/pkgconfig/OpenCL.pc

%changelog
* Sun Dec 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0
- Rebuild for Fedora
