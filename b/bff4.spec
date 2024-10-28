Name:           bff4
Version:        1
Release:        11.1
Summary:        Fast Brainfuck interpreter
License:        SUSE-Public-Domain
Group:          Development/Languages/Other
URL:            https://mazonka.com/brainf/
Source0:        %{name}.c
# bnc#761551
Source1:        license-clarification.txt
# PATCH-FEATURE-OPENSUSE bff4-arg.patch adam@mizerski.pl -- add option to pass input file as command line argument
Patch0:         %{name}-arg.patch

%description
Optimizing brainfuck implementation of dialect based on Daniel's dbfi
(see "A very short self-interpreter"). This interpreter has only one input:
program and input to the program have to be separated with ! e.g. ",.!a"
prints 'a' To use it in interactive mode paste your program as input.

This program is compiled with optimization of linear loops(where '<>' balanced),
e.g. [->+>++<<]. Linear loop is then executed in one step.

%prep
cp %{SOURCE0} %{SOURCE1} .
%patch 0

%build
gcc %{name}.c -o %{name} %{optflags}

%install
install -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc license-clarification.txt

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuilt for Fedora
* Tue Jun 19 2012 adam@mizerski.pl
- added license-clarification.txt (bnc#761551) and updated
  license tag
- updated bff4.c
- renamed arg.patch -> bff4-arg.patch and added patch info
- improved and cleaned-up spec file
* Sat Sep 17 2011 jengelh@medozas.de
- Remove redundant tags/sections from specfile
* Sun Apr 11 2010 adam@mizerski.pl
- new package
