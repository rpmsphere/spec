%undefine _debugsource_packages

Summary: Simple, elegant, Pythonic functional programming
Name: coconut
Version: 2.1.1
Release: 1
License: Apache 2.0
Group: Development/Languages
Source0: https://github.com/evhub/coconut/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: https://coconut-lang.org/
BuildArch: noarch

%description
Coconut is a variant of Python that adds on top of Python syntax new features
for simple, elegant, Pythonic functional programming.

%prep
%setup -q

%build
%py3_build

%install
%py3_install

%files 
%doc LICENSE.txt README.rst *.md
%{_bindir}/*
%{python3_sitelib}/*
%{_datadir}/jupyter/kernels/coconut/kernel.json

%changelog
* Sun Jan 01 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.1
- Rebuilt for Fedora
