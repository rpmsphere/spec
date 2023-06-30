Name: jff-algol
Version: 2.1.1
Release: 6.1
Summary: A simple ALGOL 60 to C translator
License: GPLv2
Group: Development/Languages
URL: https://github.com/JvanKatwijk/algol-60-compiler
Source: https://www.algol60.org/translators/algol-60-compiler.zip

%description
In 2002 and 2003 I wrote, as a hobby project, a simple Algol 60 to C
translator. The rationale being expressing the semantics of (some of
the) Algol 60 constructs into C expressions. 
The resulting compiler compiled Algol 60, using C as intermediate language
and - if the compilation succeeds - generates an executable. For those interested:
it had no problems with "man or boy".

%prep
%setup -q -n algol-60-compiler

%build
export CFLAGS="-Wno-error -fPIC"
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS README.md NEWS COPYING ChangeLog
%{_bindir}/%{name}
%{_bindir}/jff-a2c
%{_includedir}/jff_header.h
%{_libdir}/lib_jff.a
%{_datadir}/jff-a2c

%changelog
* Thu Oct 18 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.1
- Rebuilt for Fedora
