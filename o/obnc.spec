%global __arch_install_post %{nil}
%undefine _debugsource_packages

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
export CFLAGS="-g -O2 -fPIC -fPIE"
./build --libdir=%{_lib} --prefix=/usr

%install
sed -i 's|CFLAGS="|CFLAGS="-g -O2 -fPIC -fPIE |' install
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
- Rebuilt for Fedora
