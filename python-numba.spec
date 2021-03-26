%global debug_package %{nil}
Name: python-numba
Version: 0.26.0
Release: 6.1
Summary: NumPy aware dynamic compiler for Python
License: BSD-like
Group: Development/Python
URL: http://numba.pydata.org/
Source: numba-%version.tar.gz
BuildRequires: atlas-devel
BuildRequires: python2-devel
BuildRequires: numpy
BuildRequires: Cython

%description
numba is a NumPy aware dynamic compiler for Python. It creates LLVM
bit-code from Python syntax and then creates a wrapper around that
bitcode to call from Python.

%prep
%setup -q -n numba-%version

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc AUTHORS CHANGE_LOG LICENSE README.*
%{_bindir}/*
%{python2_sitearch}/*

%changelog
* Sun Jul 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.26.0
- Rebuild for Fedora
* Wed Mar 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20130304
- Initial build for Sisyphus

