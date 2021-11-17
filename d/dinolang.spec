%global _name dino

Summary: Interpreter of the language DINO
Name: dinolang
Version: 0.97git
Release: 1
Source0: https://codeload.github.com/dino-lang/dino/zip/refs/heads/master#/%{_name}-master.zip
License: GPL
Group: Development/Tools
URL: https://github.com/dino-lang/dino
BuildRequires: gmp-devel
Requires: gmp
Conflicts: cocom

%description
DINO is oriented on the same domain of applications as famous
scripting languages perl, tcl, python.

%prep
%setup -q -n %{_name}-master

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_includedir}/*
%{_docdir}/*
%{_mandir}/man?/*
%{_libdir}/d_*
%{_libdir}/lib*
%{_libdir}/pkgconfig/*

%changelog
* Sun Oct 3 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.97git
- Rebuilt for Fedora
