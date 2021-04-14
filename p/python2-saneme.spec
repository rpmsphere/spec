Name:           python2-saneme
Summary:        A pythonic interface to the SANE scanning library
Version:        0.1.0
Release:        1
License:        GPL
Group:          Development/Libraries/Python
Source:         python-saneme-%{version}.tar.gz
URL:		http://www.etlafins.com/saneme
BuildArch:      noarch
Requires:       sane-backends-libs, python2-imaging

%description
SaneMe (Scanner Access Now Even More Easy) is a Python wrapper around
the SANE API for Linux. It allows for applications to access SANE
without resorting to command line automation, custom wrapper code,
or a C extension.

SaneMe is, in a sense, a competitor with the python-imaging-sane module
that is packaged with PIL.

%prep
%setup -q -n python-saneme-%{version}

%build
python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%doc COPYING README
%{python2_sitelib}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0
- Rebuilt for Fedora
