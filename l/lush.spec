%undefine _missing_build_ids_terminate_build
%define __arch_install_post %{nil}

Name: lush
Version: 2.0.1
Release: 1
Summary: Object-oriented programming language for large-scale numerical and graphic applications
License: LGPL v2.0+
Group: Development/Lisp
URL: http://lush.sourceforge.net/
Source: %name-%version.tgz
BuildRequires: binutils-devel gcc-c++ gcc-gfortran
BuildRequires: lapack-devel readline-devel atlas
BuildRequires: gsl-devel mesa-libGL-devel mesa-libGLU-devel freeglut-devel
BuildRequires: SDL-devel opencv-devel libv4l-devel alsa-lib-devel
BuildRequires: libXft-devel ncurses-devel fontconfig-devel

%description
Lush is an object-oriented programming language designed for
researchers, experimenters, and engineers interested in large-scale
numerical and graphic applications. Lush is designed to be used in
situations where one would want to combine the flexibility of a
high-level, weakly-typed interpreted language, with the efficiency of a
strongly-typed, natively-compiled language, and with the easy
integration of code written in C, C++, or other languages.

%prep
%setup -q

%build
autoreconf -fiv
#add_optflags -include stddef.h
export CPPFLAGS="%optflags"
%configure \
	--bindir=%_libdir/%name/bin \
	--datadir=%_libdir/%name/share \
	--with-x
%ifarch aarch64
sed -i 's|define HAVE_FPU_CONTROL_H 1|undef HAVE_FPU_CONTROL_H|' include/lushconf.h
%endif
%make_build -i

%install
%make_install -i
install -d %buildroot%_bindir
ln -s %_libdir/%name/bin/lush2 %buildroot%_bindir/lush2
ln -s lush2 %buildroot%_bindir/lush

%files
%doc README COPYRIGHT
%_libdir/%name
%_bindir/*
%_mandir/man1/*

%changelog
* Thu Apr 19 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.1
- Rebuild for Fedora
* Fri Jul 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt3
- Fixed build
* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt2
- Fixed build
* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Version 2.0.1
* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.beta2.1
- Rebuilt for debuginfo
* Thu Dec 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.beta2
- Initial build for Sisyphus
