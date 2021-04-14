%undefine _debugsource_packages
Name:           python-sqlcc
Version:        0.3.2
Release:        3.1
License:        GPLv2
Summary:        A Python SQL API to make SQL more Python friendly
URL:            https://bitbucket.org/thinker/sqlcc/
Group:          Development/Languages/Python
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: python

%description
sqlcc is an SQL command composer; it provides API for create SQL commands in
Python's syntax. With sqlcc, developers no more compose SQL commands with
string operations.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}

%files
%{python2_sitelib}/*

%changelog
* Sun Jun 09 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2
- Rebuilt for Fedora
