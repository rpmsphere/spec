%undefine _debugsource_packages
Name: pybrainfuck
Summary: A speed-optimized Brainfuck interpreter written in Python
Version: 0.2
Release: 3.1
Group: Development/Languages
License: MIT
URL: https://bitbucket.org/fboender/pybrainfuck
Source0: https://bitbucket.org/fboender/pybrainfuck/downloads/%{name}-%{version}.tar.gz
BuildRequires: python2-devel
BuildArch: noarch

%description
Brainfuck is an esoteric (joke) programming language which is Turing-complete
(given enough memory) with only 8 op-codes (instructions). It was designed to
allow for the smallest possible compiler.

Some other Python interpreters already exists for Brainfuck, but they are
either obfuscated or awfully slow. PyBrainfuck has been optimized for speed by
doing various preprocessing on the code such as pre-caching loop instructions,
removing non-instructions, etc. PyBrainfuck also has configurable memory size,
infinite loop protection and a somewhat spartan debugger.

PyBrainfuck can be used both as a stand-alone Brainfuck interpreter or as a
python library. It can read from standard input or from a string (in library
mode) and write to standard out or to a string buffer (in library mode).

%prep
%setup -q

%build

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{python2_sitelib}/brainfuck
install -m644 brainfuck/* %{buildroot}%{python2_sitelib}/brainfuck

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc README LICENSE
%{_bindir}/%{name}
%{python2_sitelib}/*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
