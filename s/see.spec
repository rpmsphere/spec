Name:         see
Summary:      Simple ECMAScript Engine
URL:          https://www.adaptive-enterprises.com.au/~d/software/see/
Group:        Language
License:      BSD
Version:      3.1.1424
Release:      18.1
Source0:      https://www.adaptive-enterprises.com.au/~d/software/see/see-%{version}.tar.gz
Patch:        see.patch
BuildRequires: libtool-ltdl-devel

%description
ECMAScript is a standardized language also known variously as
JavaScript, JScript, and LiveScript. SEE is a library that provides
a parser and runtime environment for this language. It conforms to
ECMAScript Edition 3, and to JavaScript 1.5, with some compatibility
switches for earlier versions of JavaScript and Microsoft's JScript.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q
%patch -p0
cp -f /usr/share/automake-*/config.guess .
cp -f /usr/share/automake-*/config.guess libltdl/config/
sed -i 's|defined(__alpha__)|defined(__aarch64__)|' libsee/dtoa_config.h

%build
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --enable-full-unicode \
    --enable-parser-print \
    --enable-parser-visit \
    --enable-bytecode \
    --enable-ast-eval \
    --disable-ssp-example \
    --enable-longjmperror \
    --disable-native-dtoa \
    --with-boehm-gc \
    --with-pcre \
    --with-readline \
    --enable-shared \
    --enable-static
sed -i 's|-lm |-lm -Wl,--allow-multiple-definition |' Makefile */Makefile
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_libdir}/see/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/see/lib*.a
%{_libdir}/see/lib*.la
%{_libdir}/see/lib*.so
%{_libdir}/pkgconfig/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1.1424
- Rebuilt for Fedora
