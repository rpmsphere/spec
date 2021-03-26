%global srcname lazyasd

Name:           python3-lazyasd
Version:        0.1.3
Release:        2.1
Summary:        Lazy & self-destructive tools for speeding up module imports
License:        BSD 3-clause
URL:            http://pypi.python.org/pypi/lazyasd
Source0:        https://pypi.python.org/packages/source/l/lazyasd/%{srcname}-%{version}.tar.gz
BuildRequires:  python3-devel
BuildArch:      noarch

%description
This is useful whenever startup times are critical, such as for command line
interfaces or other user-facing applications.

%prep
%setup -q -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}/usr/LICENSE %{buildroot}/usr/README.rst %{buildroot}%{_docdir}/%{name}

%files
%{_docdir}/%{name}
%{python3_sitelib}/*

%changelog
* Thu Oct 05 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.3
- Rebuild for Fedora
