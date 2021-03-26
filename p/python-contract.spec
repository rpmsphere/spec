%global debug_package %{nil}
%define corename contract

Summary:    Programming by Contract for Python
Name:       python-%{corename}
Version:    1.4
Release:    2.1
Source0:    %{corename}-%{version}.tar.bz2
License:     Artistic; LPGL; Python Software Foundation License
Group:      Development/Libraries/Python
BuildArch:     noarch
URL:        http://www.wayforward.net/pycontract/
BuildRequires:  python-devel
BuildRequires:  python-setuptools >= 0.6

%description
Annotate function docstrings with pre- and post-conditions,
and class/module docstrings with invariants, and this
automatically checks the contracts while debugging.

%prep
%setup -q -n %{corename}-%{version}

%build
python2 setup.py build

%install
python2 setup.py install \
   --prefix=%{_prefix} \
   --root="%{buildroot}" \
   --record=%{name}.files

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%{python2_sitelib}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuild for Fedora
* Tue Sep 14 2010 toms@suse.de
- Initial version 1.4
