Name: python-pylibnet
Summary: Python module for the libnet packet injection library
Version: 3.0
Release: 24.1
Group: Development/Libraries
License: GPLv3
URL: http://pylibnet.sourceforge.net/
Source0: http://sourceforge.net/projects/pylibnet/files/pylibnet-%{version}/pylibnet-%{version}-beta-rc1.tar.gz
BuildRequires: python2-devel
BuildRequires: libnet-devel

%description
pylibnet is a python module for the libnet packet injection library that
was originally developed by David Margrave at the time of libnet 0.9.8a.
The project has since been revived and is now under active maintenance by
Nadeem Douba. The project now features support for libnet 1.1.x and has
all of the packet building functionality that is provided by libnet.

%prep
%setup -q -n pylibnet-%{version}-beta-rc1
sed -i -e 's|include_dir = None|include_dir = "%{_includedir}"|' -e 's|lib_dir = None|lib_dir = "%{_libdir}"|' -e 's|libnet.a|libnet.so|' setup.py
sed -i 's|n_time|uint32_t|g' src/builders.c

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc README LICENSE COPYING
%{_bindir}/*
%{python_sitearch}/*

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.beta.rc1
- Rebuild for Fedora
