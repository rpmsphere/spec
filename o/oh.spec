%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build

Summary: A new Unix shell
Name: oh
Version: 0.8.0
Release: 1
License: MIT
Group: Development/Language
URL: https://github.com/michaelmacinnis/oh
Source0: https://github.com/michaelmacinnis/oh/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Oh is a reimagining of the Unix shell as a programming language. Oh provides:
* Lexical scope;
* Exceptions;
* First-class channels, pipes, environments and functions;
* A list type (no word splitting);
* Rich return values that work with standard shell constructs;
* Kernel-style fexprs (allowing the definition of new language constructs);
* Support for modularity;
* A simplified set of evaluation and quoting rules; and
* A syntax that deviates as little as possible from established conventions;

%prep
%setup -q

%build
go build

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc AUTHORS LICENSE *.md doc/*
%{_bindir}/%{name}

%changelog
* Sun Sep 19 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.0
- Rebuilt for Fedora
