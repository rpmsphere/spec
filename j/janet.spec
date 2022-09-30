%undefine _debugsource_packages

Summary: A dynamic language and bytecode vm
Name: janet
Version: 1.24.1
Release: 1
License: MIT
Group: Development/Languages
Source: https://github.com/janet-lang/janet/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: https://github.com/janet-lang/janet
#BuildRequires: gtkglext-devel

%description
Janet is a functional and imperative programming language and bytecode
interpreter. It is a lisp-like language, but lists are replaced by other
data structures (arrays, tables (hash table), struct (immutable hash table),
tuples). The language also supports bridging to native code written in C,
meta-programming with macros, and bytecode assembly.

%prep
%setup -q
sed -i -e 's|/usr/local|/usr|' -e 's|$(PREFIX)/lib|%{_libdir}|' Makefile

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files 
%doc *.md *.txt
%{_bindir}/*
%{_includedir}/%{name}
%exclude %{_includedir}/%{name}.h
%{_libdir}/lib%{name}.*
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.24.1
- Rebuilt for Fedora
