Name:           python2-ordereddict
Version:        1.1
Release:        1
Summary:        OrderedDict that works in Python 2.4-2.6 
URL:            http://pypi.python.org/pypi/ordereddict
License:        MIT
Group:          Development/Libraries/Python
Source:         ordereddict-%{version}.tar.bz2
BuildRequires:  python2-devel
BuildArch:      noarch

%description
Drop-in substitute for Py2.7's new collections.OrderedDict. The recipe has
big-oh performance that matches regular dictionaries (amortized O(1)
insertion/deletion/lookup and O(n) iteration/repr/copy/equality_testing).

Originally based on http://code.activestate.com/recipes/576693/

Authors:
--------
    Raymond Hettinger

%prep
%setup -q -n ordereddict-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%doc PKG-INFO
%{python_sitelib}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuild for Fedora
* Sun Jan  9 2011 hpj@urpla.net
- initial release: 1.1
