Name:         peg-c
Summary:      Recursive-Descent parser generators for C
URL:          http://piumarta.com/software/peg/
Group:        Compiler
License:      MIT
Version:      0.1.18
Release:      1
Source0:      http://piumarta.com/software/peg/peg-%{version}.tar.gz

%description
peg(1) and leg(1) are tools for generating recursive-descent
parsers: programs that perform pattern matching on text. They
processes a Parsing Expression Grammar (PEG) to produce a program
that recognises legal sentences of that grammar. peg(1) processes
PEGs written using the original syntax described by Ford while
leg(1) processes PEGs written using slightly different syntax and
conventions that are intended to make it an attractive replacement
for parsers built with lex(1) and yacc(1). Unlike lex(1) and
yacc(1), peg(1) and leg(1) support unlimited backtracking, provide
ordered choice as a means for disambiguation, and can combine
scanning (lexical analysis) and parsing (syntactic analysis) into a
single activity.

%prep
%setup -q -n peg-%{version}

%build
#   bootstrap tools
touch peg.peg-c leg.c
%{__make} %{_smp_mflags} \
    CC="%{__cc}" \
    OFLAGS="%{optflags -O}"

#   re-build from scratch
touch peg.peg leg.leg
rm peg.o leg.o
%{__make} %{_smp_mflags} \
    CC="%{__cc}" \
    OFLAGS="%{optflags -O}"

%install
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_bindir} \
    $RPM_BUILD_ROOT%{_mandir}/man1
install -c -m 755 \
    peg leg $RPM_BUILD_ROOT%{_bindir}
install -c -m 644 \
    src/peg.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install -c -m 644 \
    src/peg.1 $RPM_BUILD_ROOT%{_mandir}/man1/leg.1

%files
%doc ChangeLog README.txt LICENSE.txt
%{_bindir}/peg
%{_bindir}/leg
%{_mandir}/man1/peg.1.*
%{_mandir}/man1/leg.1.*

%changelog
* Sun Apr 4 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.18
- Rebuilt for Fedora
