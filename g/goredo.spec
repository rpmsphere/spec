%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

Name: goredo
Version: 1.3.0
Release: 1
Summary: Go implementation of djb's redo, Makefile replacement that sucks less
Group: Development/Tools
License: GPLv3
URL: http://www.goredo.cypherpunks.ru/index.html
# Source-url: http://www.goredo.cypherpunks.ru/download/goredo-%version.tar.zst
Source: %name-%version.tar.gz
BuildRequires: golang

%description
Originally it was just a rewrite of redo-c,
but later most features of apenwarr/redo were also implemented.
Why yet another implementation? It is feature full and has better performance
comparing to shell and Python implementation.

%prep
%setup -q

%build
cd src
go build -mod=vendor
./goredo -symlinks

%install
mkdir -p %buildroot%_bindir/
cp -a src/goredo src/redo* %buildroot%_bindir/
mkdir -p %buildroot%_infodir/
install -m644 goredo.info %buildroot%_infodir/

%files
%doc NEWS INSTALL README THANKS
%_bindir/goredo
%_bindir/redo*
%_infodir/*

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.0
- Rebuilt for Fedora
* Sat Jan 23 2021 Vitaly Lipatov <lav at altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus
