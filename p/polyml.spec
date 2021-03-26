Name: polyml
Version: 5.8
Release: 1
Summary: Standard ML implementation
Summary(ru_RU.UTF-8): Реализация Standard ML
License: GPLv2+
Group: Development/ML
URL: http://www.polyml.org
Source0: https://codeload.github.com/polyml/polyml/tar.gz/v%version#/%name-%version.tar.gz
Patch0: %name-5.4.1-gcc8-fix.patch
BuildRequires: gcc-c++ imake libXext-devel gmp-devel

%description
Poly/ML is a full implementation of Standard ML. Poly/ML supports the full
version of the language as given in the "Definition of Standard ML (Revised)",
generally known as ML97. As well as being extremely fast and efficient
implementation of Standard ML Poly/ML provides several additional features.

There is a foreign language interface which allows dynamically linked libraries
to be loaded and functions within them called from ML. An X-Windows interface
using Motif is available. There is also a symbolic debugger for Poly/ML.

%description -l ru_RU.UTF-8
Poly/ML — это быстрая и эффективная реализация языка Standard ML,
поддерживающая все возможности стандарта "Definition of Standard ML (Revised)"
(ML97). Кроме того, Poly/ML предоставляет разработчику интерфейс для вызова
функций, написанных на других языках, библиотеку для создания графических
интерфейсов на основе Motif и отладчик.

%prep
%setup -q
%patch0 -p2

%build
# Quick fix for RPATH bug
autoreconf -ifv
%configure --with-x
%make_build

%install
%make_install

%files
%doc COPYING README.md
%_bindir/*
%_mandir/man1/*
%_libdir/*.so*
%_libdir/pkgconfig/polyml.pc
%_libdir/polyml/modules/IntInfAsInt
%exclude %_libdir/libpoly*.*a

%changelog
* Tue Mar 17 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 5.8
- Rebuild for Fedora
* Wed Feb 13 2019 Pavel Moseev <mars@altlinux.org> 5.4.1-alt4
- no return statement in the non-void function fixed (according g++8)
* Thu Aug 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.4.1-alt3.1
- Rebuilt with gmp 5.0.5
* Sat Jun 02 2012 Yuriy Shirokov <yushi@altlinux.org> 5.4.1-alt3
- wrong russian description fixed
* Wed May 30 2012 Yuriy Shirokov <yushi@altlinux.org> 5.4.1-alt2
- spec bug with %%_libdir/* fixed
* Sun May 27 2012 Yuriy Shirokov <yushi@altlinux.org> 5.4.1-alt1
- initial build
