#undefine _missing_build_ids_terminate_build

Summary: The Elena Programming Language
Name: elena
Version: 5.0.23
Release: 1
License: MIT
Group: Development/Language
URL: https://elena-lang.github.io/
Source0: https://github.com/ELENA-LANG/elena-lang/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
ELENA is a general-purpose language with late binding. It is multi-paradigm,
combining features of functional and object-oriented programming. It supports
both strong and weak types, run-time conversions, boxing and unboxing primitive
types, direct usage of external libraries. A rich set of tools is provided to
deal with message dispatching : multi-methods, message qualifying, generic
message handlers. Multiple-inheritance can be simulated using mixins and type
interfaces. The built-in script engine allows incorporating custom-defined
scripts into your applications. Both stand-alone applications and Virtual
machine clients are supported.

%prep
%setup -q -n ELENA-LANG-elena-lang-7c6c0ff

%build
%cmake .
%make_build

%install
#install -Dm755 %{name} %{buildroot}%{_bindir}/%{_name}
%make_install

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE *.md
%{_bindir}/%{name}

%changelog
* Sun Sep 26 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0.23
- Rebuilt for Fedora
