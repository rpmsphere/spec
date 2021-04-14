%define pyname Tungsteno

Name:           tungsteno
Version:        1.1
Release:        1
Summary:        A free, light-weight alternative to Mathematica
License:        GPL-3.0
Group:          Development/Languages/Python
URL:            https://github.com/tungstenoapp/Tungsteno
Source:         https://github.com/tungstenoapp/Tungsteno/archive/v%{version}.tar.gz#/%{pyname}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-colorama
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sympy
BuildRequires:  python3-numpy
BuildArch:      noarch

%description
Tungsteno is a programming language intended to be 100%% compatible with
Wolfram Language. It is designed to be lightweight, and easily extensible
through modules, and module repositories.

%prep
%setup -q -n %{pyname}-%{version}
sed -i 's|/usr/bin/python$|/usr/bin/python3|' app.py

%build
%py3_build

%install
%py3_install
install -Dm755 app.py %{buildroot}%{_bindir}/%{name}
cp -a tsteno/* %{buildroot}%{python3_sitelib}/tsteno

%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{python3_sitelib}/*

%changelog
* Thu Feb 18 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
