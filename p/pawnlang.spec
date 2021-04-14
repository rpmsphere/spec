Summary: A tiny and fast embedded scripting language
Name: pawnlang
Version: 4.0.5749
Release: 1
License: Apache 2.0
Group: Development/Languages
Source: https://www.compuphase.com/pawn/pawn-%{version}.zip
URL: https://www.compuphase.com/pawn/pawn.htm

%description
pawn is a simple, typeless, 32-bit extension language with a C-like syntax.
A pawn "source" program is compiled to a binary file for optimal execution
speed. The pawn compiler outputs P-code (or bytecode) that subsequently runs
on an abstract machine. Execution speed, stability, simplicity and a small
footprint were essential design criteria for both the language and the
abstract machine.

%prep
%setup -q -c

%build
%cmake .
make

%install
install -d %{buildroot}%{_bindir}
install -m755 pawn* stategraph %{buildroot}%{_bindir}

%files 
%doc LICENSE NOTICE history.txt readme.txt
%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Mar 05 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.5749
- Rebuilt for Fedora
