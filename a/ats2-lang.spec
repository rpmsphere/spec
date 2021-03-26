%global debug_package %{nil}
%global __python %{__python3}

Name: ats2-lang
Summary: ATS version 2 programming language compiler
Version: 0.4.1
Release: 1
Group: Development
License: Free Software
URL: http://www.ats-lang.org/
Source0: https://dl.sourceforge.net/project/ats2-lang/ats2-lang/ats2-postiats-%{version}/ATS2-Postiats-%{version}.tgz
BuildRequires: gmp-devel
BuildRequires: gc-devel

%description
ATS2 a.k.a. ATS/Postiats is a programming language with a highly expressive
type system rooted in the framework Applied Type System. In particular, both
dependent types and linear types are available in ATS. The current
implementation of ATS (ATS/Postiats) is written in ATS (ATS/Anairiats) itself.
It can be as efficient as C/C++ and supports a variety of programming
paradigms.

In addition, ATS contains a component ATS/LF that supports a form of
(interactive) theorem proving, where proofs are constructed as total
functions. With this component, ATS advocates a programming style
that combines programming with theorem proving. Furthermore, this
component may be used as a logical framework to encode various
deduction systems and their (meta-)properties.

%prep
%setup -q -n ATS2-Postiats-%{version}

%build
%configure
make

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/*
/usr/lib/ats2-postiats*

%changelog
* Mon Mar 08 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuild for Fedora
