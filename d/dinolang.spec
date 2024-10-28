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
Provides: cocom

%description
DINO is oriented on the same domain of applications as famous
scripting languages perl, tcl, python.

%prep
%setup -q -n %{_name}-master
rename .d .dino DINO/*.d DINO/Examples/*.d DINO/MODULES/*.d
sed -i 's|STANDARD_INPUT_FILE_SUFFIX ".d"|STANDARD_INPUT_FILE_SUFFIX ".dino"|' DINO/d_common.h
sed -i -e 's|d_flatten\.d|d_flatten.dino|' -e 's|d_minimize\.d|d_minimize.dino|' -e 's|process_ucodedb\.d|process_ucodedb.dino|' DINO/*.c DINO/Makefile*
sed -i -e 's|mpi\.d|mpi.dino|' -e 's|ieee\.d|ieee.dino|' -e 's|ipcerr\.d|ipcerr.dino|' -e 's|socket\.d|socket.dino|' DINO/Makefile* DINO/MODULES/Makefile*
sed -i 's|command line: %{_name}|command line: %{name}|' DINO/d_dino.c

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mv %{buildroot}%{_bindir}/%{_name} %{buildroot}%{_bindir}/%{name}

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
