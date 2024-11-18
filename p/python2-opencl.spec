%undefine _debugsource_packages

Name:           python2-opencl
Version:        0.5.2
Release:        7.1
Summary:        Yet another set of Python bindings for OpenCL
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://srossross.github.com/oclpb/
Source0:        srossross-oclpb-0.5.2-0-g02d70d9.tar.bz2
BuildRequires:  opencl-headers
BuildRequires:  ocl-icd-devel
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  mesa-libOpenCL-devel llvm-devel

%description
This is yet another set of Python bindings for OpenCL.
It has the followon features: 
 * Supports OpenCL 1.1 
 * Discoverable properties and methods
 * Tight integration with ctypes
 * Call kernels like a python function with defaults and keyword arguments
 * Memory objects support indexing and slicing

%prep
%setup -q -n srossross-oclpb-02d70d9

%build
CFLAGS="%{optflags} -fno-strict-aliasing -Wno-incompatible-pointer-types" python2 setup.py build

%install
python2 setup.py install --root %{buildroot} --prefix=%{_prefix}

%files
%doc license.rst README.rst
%{python2_sitearch}/*

%changelog
* Sun Dec 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.2
- Rebuilt for Fedora
* Fri Jun 15 2012 scorot@free.fr
- first package
