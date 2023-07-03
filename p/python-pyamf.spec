%undefine _debugsource_packages
Name: python-pyamf
Summary: Action Message Format support for Python
Version: 0.6.1
Release: 7.1
Group: Development/Libraries
License: MIT
URL: https://www.pyamf.org/
Source0: https://pypi.python.org/packages/source/P/PyAMF/PyAMF-%{version}.tar.gz
BuildRequires: python-devel
BuildRequires: python-setuptools

%description
PyAMF provides Action Message Format (AMF) support for Python
that is compatible with the Flash Player. It includes integration
with Python web frameworks like Django, Pylons, Twisted, and more.

The Adobe Integrated Runtime and Adobe Flash Player use AMF to
communicate between an application and a remote server. AMF encodes
remote procedure calls (RPC) into a compact binary representation
that can be transferred over HTTP/HTTPS or the RTMP/RTMPS protocol.
Objects and data values are serialized into this binary format,
which increases performance, allowing applications to load data up
to 10 times faster than with text-based formats such as XML or SOAP.

%prep
%setup -q -n PyAMF-%{version}
sed -i '/use_setuptools/d' setup.py

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%doc *.txt
%{python2_sitearch}/*

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1
- Rebuilt for Fedora
