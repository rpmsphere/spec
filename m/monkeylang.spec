%undefine _missing_build_ids_terminate_build
%global _name monkey

Summary: An interpreted languages written in Go
Name: monkeylang
Version: 0.9.4
Release: 1
License: MIT
Group: Development/Language
URL: https://monkeylang.org/
Source0: https://github.com/skx/monkey/archive/refs/tags/release-%{version}.tar.gz#/%{_name}-release-%{version}.tar.gz

%description
This repository contains an interpreter for the "Monkey" programming language,
as described in Write an Interpreter in Go.

%prep
%setup -q -n %{_name}-release-%{version}

%build
go build

%install
install -Dm755 %{_name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE *.md
%{_bindir}/%{name}

%changelog
* Sun Sep 19 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.4
- Rebuilt for Fedora
