%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages
%global _name abs

Summary: The ABS Programming Language
Name: abslang
Version: 2.6.0
Release: 1
License: MIT
Group: Development/Language
URL: https://www.abs-lang.org/
Source0: https://github.com/abs-lang/abs/archive/refs/tags/%{version}.tar.gz#/%{_name}-%{version}.tar.gz

%description
ABS is a programming language that works best when you're scripting on your
terminal. It tries to combine the elegance of languages such as Python, or
Ruby with the convenience of Bash.

%prep
%setup -q -n %{_name}-%{version}

%build
go build

%install
install -Dm755 %{_name} %{buildroot}%{_bindir}/%{_name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE *.md
%{_bindir}/%{_name}

%changelog
* Sun Nov 13 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.0
- Rebuilt for Fedora
