Summary:	Python wrapper for OpenCL
Name:		python-pyopencl
Version:	2014.1
Release:	6.1
Source0:	pyopencl-%{version}.tar.gz
License:	MIT
Group:		Development/Python
URL:		http://mathema.tician.de/software/pyopencl
BuildRequires:  opencl-headers
BuildRequires:	ocl-icd-devel
BuildRequires:	python-sphinx
BuildRequires:	python-setuptools
BuildRequires:	python-distribute
BuildRequires:	numpy
BuildRequires:	gcc-c++
BuildRequires:	boost-devel
BuildRequires:	python-mako
BuildRequires:	python-devel
BuildRequires:	atlas-devel

%description
PyOpenCL gives you easy, Pythonic access to the OpenCL parallel
computation API. What makes PyOpenCL special?

* Object cleanup tied to lifetime of objects. This idiom, often called
  RAII in C++, makes it much easier to write correct, leak- and
  crash-free code.
* Completeness. PyOpenCL puts the full power of OpenCL’s API at your
  disposal, if you wish. Every obscure get_info() query and all CL
  calls are accessible.
* Automatic Error Checking. All errors are automatically translated
  into Python exceptions.
* Speed. PyOpenCL's base layer is written in C++, so all the niceties
  above are virtually free.
* Helpful Documentation.

%prep
%setup -q -n pyopencl-%{version}
sed -i 's|BOOST_DISABLE_THREADS|BOOST_HAS_THREADS|' bpl-subset/bpl_subset/boost/config/stdlib/libstdcpp3.hpp
sed -i 's|TIME_UTC|TIME_UTC_|' bpl-subset/bpl_subset/boost/thread/xtime.hpp bpl-subset/bpl_subset/libs/thread/src/pthread/thread.cpp bpl-subset/bpl_subset/libs/thread/src/pthread/timeconv.inl
sed -i '/use_setuptools/d' aksetup_helper.py

%build
%__python ./configure.py --cl-lib-dir=/usr/lib,/usr/lib64 \
--boost-inc-dir=/usr/include/,/usr/include/boost \
--boost-lib-dir=/usr/lib,/usr/lib64 --boost-python-libname=boost_python 
%__python setup.py build

#pushd doc/
#export PYTHONPATH=%{buildroot}%{python_sitearch}
#make PAPER=letter html
#find -name .buildinfo | xargs rm -f
#popd

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%doc examples README*
#_includedir/pyopencl/*
%{python_sitearch}/pyopencl*

%changelog
* Tue Jan 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2014.1
- Rebuild for Fedora
* Tue Dec 06 2011 Lev Givon <lev@mandriva.org> 2011.2-1mdv2012.0
+ Revision: 738066
- Update to 2011.2.
* Fri May 20 2011 Lev Givon <lev@mandriva.org> 2011.1-1.beta3
+ Revision: 676421
- Don't try to download distribute when building for Mandriva < 2011.0
* Fri May 20 2011 Lev Givon <lev@mandriva.org> 2011.1-0.beta3
+ Revision: 676420
- import python-pyopencl
