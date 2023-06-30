%undefine _debugsource_packages

Summary: The Compiler Generator Coco/R, C++ version
Name: coco-cpp
Version: 20120102
Release: 13.1
License: GPL
Group:  Development/Tools
Source0: https://www.ssw.uni-linz.ac.at/Coco/CPP/CocoSourcesCPP.zip
URL: https://www.ssw.uni-linz.ac.at/coco/
BuildRequires: gcc-c++, perl

%description
Coco/R is a compiler generator, which takes an attributed grammar of a
source language and generates a scanner and a parser for this
language. The scanner works as a deterministic finite automaton. The
parser uses recursive descent. LL(1) conflicts can be resolved by a
multi-symbol lookahead or by semantic checks. Thus the class of
accepted grammars is LL(k) for an arbitrary k.

%prep
%setup -q -c

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/usr/lib/%{name}
mkdir -p $RPM_BUILD_ROOT/usr/share/%{name}
make DESTDIR=${RPM_BUILD_ROOT} install
%ifarch x86_64 aarch64
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Coco.atg
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 20120102
- Rebuilt for Fedora
* Sat Nov  6 2010 Mark Olesen
- created spec file
