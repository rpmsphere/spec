Name: openclcc
Version: 11.8
Release: 9.1
Source0: http://openclcc.googlecode.com/files/%{name}-%{version}.tar.gz
License: GPLv3
Group: Development/Tools
URL: http://code.google.com/p/openclcc/
Summary: OpenCL Compiler Wrapper
BuildRequires: opencl-headers
BuildRequires: ocl-icd-devel
BuildRequires: mesa-libOpenCL-devel llvm-devel

%description
OpenCLcc is a compiler wrapper that performs a static null compilation of
OpenCL kernels. Basically, openclcc is just the code to set up a minimum
OpenCL context, load one or more text files containing OpenCL kernel code,
compile those files and show the OpenCL compiler output to the user.
This simple piece of code eases OpenCL development, because you can compile
your OpenCL kernels in an isolated way, and get descriptive compilation errors.

%prep
%setup -q

%build
%configure
make CFLAGS+=-fPIC

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}*
%{_datadir}/%{name}

%changelog
* Sun Dec 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 11.8
- Rebuilt for Fedora
