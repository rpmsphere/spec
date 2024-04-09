Summary:	Multi-platform implementation of OpenCL 1.2 targeting CPUs
Name:		freeocl
Version:	0.3.6.20180107
Release:	1
License:	LGPL
Group:		System/Libraries
URL:		http://code.google.com/p/freeocl/
Source: freeocl-master.zip
BuildRequires:	cmake, gcc-c++, libatomic_ops-devel
Provides:	opencl = 1.2.0

%description
FreeOCL is an implementation of OpenCL 1.2 specifications targeting CPUs.
Instead of using a built-in or dedicated compiler, it relies on an external
C++ compiler. It aims to provide a debugging tool and a reliable platform
which can run everywhere.

%package devel
Summary:	FreeOCL development files
Group:		Development/C
Requires:	opencl = 1.2.0
Requires:	opencl-headers
Provides:	opencl-devel = 1.2.0

%description devel
FreeOCL is an implementation of OpenCL 1.2 specifications targeting CPUs.
Instead of using a built-in or dedicated compiler, it relies on an external
C++ compiler. It aims to provide a debugging tool and a reliable platform
which can run everywhere.

This package provides the files needed to compile software that uses
OpenCL.

%prep
%setup -q -n freeocl-master
sed -i 's|_mm_pause()|__asm__ __volatile__ ("rep; nop")|' src/utils/threadpool.cpp
sed -i '13,15d' CMakeLists.txt

%build
cmake . -DCMAKE_INSTALL_PREFIX=/usr
make

%install
rm -rf %{buildroot}
%make_install
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf %{buildroot}

%files
%doc README COPYING* TODO AUTHORS
%{_libdir}/libOpenCL.so.*
/etc/OpenCL/vendors/freeocl.icd

%files devel
%{_libdir}/libOpenCL.so
%{_libdir}/libFreeOCL.so
%{_includedir}/FreeOCL

%changelog
* Sun Oct 02 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.6.20180107
- Rebuild for Fedora
