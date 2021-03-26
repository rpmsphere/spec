# https://fedoraproject.org/wiki/Packaging:Haskell

Name:           idris
Version:        1.1.1
Release:        1
Summary:        Functional Programming Language with Dependent Types

License:        BSD
Url:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:         idris-ASTBuilding-ghc78.patch
Patch1:         idris-rts-opt-fprintf.patch

ExcludeArch:    armv7hl
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-haskeline-devel
BuildRequires:  ghc-language-java-devel
BuildRequires:  ghc-libffi-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-vector-binary-instances-devel
BuildRequires:  ghc-vector-devel
# End cabal-rpm deps
BuildRequires:  gc-devel
## idris compiles to C and then uses gcc linking to the static rts library
## to generate executables (so devel files are included in the main package)
Requires:       gcc
Requires:       gmp-devel

%description
Idris is a general purpose language with full dependent types.
It is compiled, with eager evaluation. Dependent types allow types to
be predicated on values, meaning that some aspects of a program's
behavior can be specified precisely in the type. The language is
closely related to Epigram and Agda. There is a tutorial at
<http://www.idris-lang.org/documentation>. Features include:

* Full dependent types with dependent pattern matching
* where clauses, with rule, simple case expressions, pattern matching let and
  lambda bindings
* Type classes, monad comprehensions
* do notation, idiom brackets, syntactic conveniences for lists, tuples,
  dependent pairs
* Totality checking
* Coinductive types
* Indentation significant syntax, extensible syntax
* Tactic based theorem proving (influenced by Coq)
* Cumulative universes
* Simple foreign function interface (to C)
* Hugs style interactive environment.


%prep
%setup -q
%patch0 -p1 -b .orig
%patch1 -p1 -b .orig

cabal-tweak-flag LLVM False


%build
# libidris_rts.a is arch dependent
cabal_configure_extra_options=--datadir=%{_libdir}
%ghc_bin_build


%install
%ghc_bin_install


%files
%doc LICENSE tutorial
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/%{name}-%{version}


%changelog
* Thu Jul 28 2016 Jens Petersen <petersen@redhat.com> - 0.9.9.1-8
- require gmp-devel (#1360168)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr  6 2015 Jens Petersen <petersen@redhat.com> - 0.9.9.1-5
- rebuild

* Wed Jan 28 2015 Jens Petersen <petersen@redhat.com> - 0.9.9.1-4
- cblrpm refresh
- fix build with ghc78
- temporarily exclude armv7hl until RTS issues resolved (#1190261)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct  5 2013 Jens Petersen <petersen@redhat.com> - 0.9.9.1-1
- update to 0.9.9.1
- depends on ansi-terminal and time

* Fri Oct  4 2013 Jens Petersen <petersen@redhat.com> - 0.9.9-1
- update to 0.9.9
  http://www.idris-lang.org/idris-0-9-9-released/
- disable LLVM backend for now
- depends on vector-binary-instances
- buildrequires gc-devel

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul  9 2013 Jens Petersen <petersen@redhat.com> - 0.9.8-3
- use cabal_configure_extra_options to set datadir (#947819)
- add a comment about the devel files in the main package (#947819)

* Mon Jul  8 2013 Jens Petersen <petersen@redhat.com> - 0.9.8-2
- install idris devel data files under libdir (#947819)

* Mon Jul  1 2013 Jens Petersen <petersen@redhat.com> - 0.9.8-1
- update to 0.9.8
- http://idris-lang.org/archives/272

* Sat Apr  6 2013 Jens Petersen <petersen@redhat.com> - 0.9.7-2
- requires gcc

* Wed Apr  3 2013 Jens Petersen <petersen@redhat.com> - 0.9.7-1
- spec file regenerated with cabal-rpm-0.8.0

* Sat Feb 25 2012 Jens Petersen <petersen@redhat.com> - 0.9.1-1
- update to 0.9.1

* Fri Jan 27 2012 Jens Petersen <petersen@redhat.com> - 0.9.0-1
- BSD license

* Fri Jan 27 2012 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.4
