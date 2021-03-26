Name:         pegtl
Summary:      Parsing Expression Grammar (PEG) Template Library
URL:          http://code.google.com/p/pegtl/
Group:        Compiler
License:      MIT
Version:      0.32
Release:      2.1
Source0:      http://pegtl.googlecode.com/files/pegtl-%{version}.tgz
BuildArch:    noarch

%description
The Parsing Expression Grammar Template Library (PEGTL) is a C++0x
library for creating parsers according to a Parsing Expression
Grammar (PEG). Grammars are embedded as regular C++ code, and
consist of template hierarchies of classes. These hierarchies
naturally correspond to the inductive definition of PEGs. The
library extends on the subject of PEGs with new expression types,
actions that can be attached to grammar rules, and mechanisms to
ensure helpful diagnostics in case of parsing errors.

%prep
%setup -q

%build

%install
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_includedir}
cp -rp include/* $RPM_BUILD_ROOT%{_includedir}

%files
%{_includedir}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.32
- Rebuild for Fedora
