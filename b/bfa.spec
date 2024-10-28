%undefine _debugsource_packages

Summary: Brain Fuck Assembler
Name: bfa
Version: 0.2
Release: 1
License: GPL2+
Group: Development/Language
Source0: https://koeln.ccc.de/ablage/brainfuck/%{name}-%{version}.tar.gz
URL: https://koeln.ccc.de/ablage/brainfuck/index.en.xml

%description
bfa is an assembler for the minimalized programming language Brain Fuck.
It translates a better readable BFA source code to native absolutely unreadable
Brain Fuck code. The produced code can be executed with a Brain Fuck Interpreter
like bfi from Urban Mueller, or directly on a system providing a Brain Fuck processor.

%prep
%setup -q
sed -i 's|const iLine|const int iLine|' bfa/bfa.c
sed -i -e '2i #include <stdlib.h>' -e 's|^main|void main|' contrib/bfi.c

%build
%{make_build}

%install
install -Dm755 bfa/bfa %{buildroot}%{_bindir}/bfa
install -Dm644 bfa/bfa.1.gz %{buildroot}%{_mandir}/man1/bfa.1.gz
install -Dm755 contrib/bfi %{buildroot}%{_bindir}/bfi

%files
%doc README readme.html examples
%{_bindir}/*
%{_mandir}/man?/*

%changelog
* Fri Jun 14 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
