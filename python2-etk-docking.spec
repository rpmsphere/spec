%define package_name etk.docking

Name:           python2-etk-docking
Version:        0.2
Release:        4.1
Summary:        Simple PyGTK Docking Widgets
License:        GPLv2
URL:            http://pypi.python.org/pypi/etk.docking
Source0:        http://pypi.python.org/packages/source/e/%{package_name}/%{package_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2
BuildRequires:  python2-setuptools

%description
etk.docking provides GTK+ docking widgets for use in Python applications.

%prep
%setup -q -n %{package_name}-%{version}

%build
python2 setup.py build

%install
python2 setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}/usr/doc

%files
%doc AUTHORS COPYING COPYING.LESSER README TODO
%{python2_sitelib}/*

%changelog
* Sun Dec 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
* Sat Dec 17 2011 qmp <glang@lavabit.com> - 0.2-1
- Initial packaging
