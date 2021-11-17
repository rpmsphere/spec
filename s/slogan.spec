%undefine _debugsource_packages

Summary: The Slogan Programming Language
Name: slogan
Version: 0.12.6
Release: 1
License: Apache v2
Group: Development/Language
URL: https://schemer.in/slogan/
Source0: https://github.com/vijaymathew/slogan/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Slogan is a programming language designed for high-performance concurrent,
networked applications. It features first-class functions, lexical scoping and
operations on structured data like strings, lists, arrays, sets and hash tables.
Its powerful control flow and syntactic abstraction capabilities makes Slogan
a highly extensible programming language.

%prep
%setup -q
sed -i 's|lib/libffi.a|lib64/libffi.a|' src/Makefile

%build
./configure
make

%install
install -Dm755 src/%{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE README.md ChangeLog
%{_bindir}/%{name}

%changelog
* Sun Sep 26 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.12.6
- Rebuilt for Fedora
