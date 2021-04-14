%undefine _debugsource_packages
Name:         codeville
License:      BSD
Group:        Development/Libraries/Python
Version:      0.8.0
Release:      3.1
Summary:      A high-level Python Web framework
URL:          http://codeville.org/
Source:       http://codeville.org/download/Codeville-%{version}.tar.gz
BuildRequires:  python2-devel python2-setuptools 
BuildArch:    noarch

%description
Codeville is a distributed version control system. It began with a novel idea
for a merge algorithm and has grown from there. It is designed to be easy to
use and scale from small personal projects to very large distributed ones.

%prep
%setup -q -n Codeville-%{version}

%build
export CFLAGS="%{optflags}"
python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{python2_sitelib}/Codeville*
%{_datadir}/doc/Codeville-%{version}

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.0
- Rebuilt for Fedora
