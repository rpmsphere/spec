%global _name eldf

Summary:        A Python implementation of ELDF data format
Name:           python3-%{_name}
Version:        2021.2.1
Release:        1
License:        MIT
Group:          Development/Tools
Source0:        %{_name}-%{version}.tar.gz
URL:            https://eldf.org/
BuildArch:      noarch

%description
ELDF is an extra lightweight data format, an alternative to JSON.

%prep
%setup -q -n %{_name}-%{version}

%build
python3 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python3 setup.py install --prefix=/usr --root=%{buildroot} --skip-build

%files
%doc README.md
%{python3_sitelib}/%{_name}*
%{python3_sitelib}/__pycache__/*

%changelog
* Sun Jan 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2021.2.1
- Rebuilt for Fedora
