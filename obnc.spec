%global debug_package %{nil}

Name: obnc
Summary: Oberon-07 Compiler
Version: 0.16.1
Release: 1
Group: Development/Language
License: GPLv3
URL: https://miasap.se/obnc/
Source0: https://miasap.se/obnc/downloads/%{name}_%{version}.tar.gz
BuildRequires: gc-devel

%description
OBNC is a compiler for Niklaus Wirth’s programming language Oberon.
It implements the latest version of the language from 2016. OBNC translates
source code written in Oberon to the lower-level programming language C.
The translated code is then compiled and linked with the C compiler and linker
of the host operating system. The build command obnc performs all these tasks
and keeps track of which files need to be compiled or recompiled.

%prep
%setup -q

%build
./build --libdir=%{_lib} --prefix=/usr

%install
./install --destdir=%{buildroot}

%files
%{_bindir}/*
%{_includedir}/%{name}
%{_libdir}/%{name}
%{_docdir}/%{name}
%{_mandir}/man1/*
%{_datadir}/obnc/style.css

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.16.1
- Rebuild for Fedora
