Name:           sdcc
Version:        3.5.0
Release:        5.1
Summary:        Small Device C Compiler
License:        GPL-2.0+ and GPL-3.0+
Group:          Development/Languages/C and C++
URL:            http://sdcc.sourceforge.net/
Source:         http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.bz2
Patch:          sdcc_add_ppc64le_suse_support.patch
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  lyx
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  gputils
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  python-devel
BuildRequires:  latex2html

%description
SDCC is a C compiler for 8051 class and similar microcontrollers.
The package includes the compiler, assemblers and linkers, a device
simulator and a core library. The processors supported (to a varying
degree) include the 8051, ds390, z80, hc08, and PIC.

%package        doc
Summary:        Documentation for the SDCC C compiler
Group:          Documentation/HTML
BuildArch:      noarch

%description    doc
SDCC is a C compiler for 8051 class and similar microcontrollers.
The package includes the compiler, assemblers and linkers, a device
simulator and a core library. The processors supported (to a varying
degree) include the 8051, ds390, z80, hc08, and PIC.

This package contains documentation for SDCC C compiler.

%package        libc-sources
Summary:        Small Device C Compiler
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description    libc-sources
SDCC is a C compiler for 8051 class and similar microcontrollers.
The package includes the compiler, assemblers and linkers, a device
simulator and a core library. The processors supported (to a varying
degree) include the 8051, ds390, z80, hc08, and PIC.

This package contains sources for the C library and other files for
development.

%prep
%setup -q
rm support/regression/tests/bug3304184.c
%patch -p1

%build
CFLAGS="%{optflags} -fno-strict-aliasing" \
%configure \
    --docdir=%{_docdir}/sdcc \
    --enable-doc

make %{?_smp_mflags}

%install
%make_install

# install documentation
mkdir -p %{buildroot}%{_docdir}/%{name}/sdas
cp sdas/doc/* %{buildroot}%{_docdir}/%{name}/sdas
cp ChangeLog %{buildroot}%{_docdir}/%{name}
cp COPYING %{buildroot}%{_docdir}/%{name}

mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp
mv %{buildroot}%{_bindir}/*.el %{buildroot}%{_datadir}/emacs/site-lisp

#remove useless file
rm %{buildroot}%{_docdir}/%{name}/INSTALL.txt

cp ChangeLog %{buildroot}%{_docdir}/%{name}
cp COPYING %{buildroot}%{_docdir}/%{name}

#remove strange suff (installed by mistake?)
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}

# remove non-free libraries, see doc/README.txt: Licenses
rm -rf %{buildroot}%{_datadir}/%{name}/non-free/

%if 0%{?suse_version} <= 1210
find %{buildroot}%{_datadir}/%{name} -name '*.Po' -exec rm {} \;
rm -rf %{buildroot}%{_datadir}/%{name}/lib/src/pic16/*/.deps
rm -rf %{buildroot}%{_datadir}/%{name}/lib/src/pic14/libsdcc/*/.deps
rm -rf %{buildroot}%{_datadir}/%{name}/lib/src/pic14/libm/.deps
rm -rf %{buildroot}%{_datadir}/%{name}/non-free/lib/src/pic16/libdev/.deps
%endif

%files
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/COPYING
%{_docdir}/%{name}/README.txt
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/include
%{_datadir}/%{name}/lib
%exclude %{_datadir}/%{name}/lib/src
%dir %{_datadir}/emacs/site-lisp
%{_datadir}/emacs/site-lisp/*.el

%files libc-sources
%{_datadir}/%{name}/lib/src

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/ucsim
%{_docdir}/%{name}/sdas
%{_docdir}/%{name}/sdccman.pdf

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.5.0
- Rebuilt for Fedora
* Tue Aug 18 2015 normand@linux.vnet.ibm.com
- new patch to build on ppc64le
  sdcc_add_ppc64le_suse_support.patch
* Fri Jun 26 2015 dmitry_r@opensuse.org
- Update to version 3.5.0
  * Changed default language dialect from --std-sdcc89 to --std-sdcc99
  * Reorganized and updated manual
  * Reduced memory consumption (most noticeable for high --max-allocs-per-node)
  * Faster compilation for stm8 (most noticeable for high --max-allocs-per-node)
  * atoll() function for conversion of strings to long long
  * __z88dk_fastcall and __z88dk_callee calling conventions for more
    efficient function calls and better compability with z88dk
  * --lospre-unsafe-read renamed to --allow-unsafe-read
- Drop obsolete
  * sdcc-remove-strndup.patch
  * sdcc-libiberty.patch
* Sun Nov 30 2014 wk@ire.pw.edu.pl
- Fixed build for Tumbleweed and Factory by adding patch
    sdcc-remove-strndup.patch
- added patch sdcc-libiberty.patch
* Thu Jul 31 2014 dmitry_r@opensuse.org
- Change package license to GPL-2.0+ and GPL-3.0+ [bnc#889723]
* Mon Jul 28 2014 dmitry_r@opensuse.org
- spec file cleanup
- Remove non-free libraries
- Move libc sources to separate package
* Thu Oct  4 2012 Wojciech Kazubski <wk@ire.pw.edu.pl> -3.2.0-13
- update to 3.2.0
* Mon Sep  3 2012 Wojciech Kazubski <wk@ire.pw.edu.pl>
- update to 3.1.0
* Fri Nov 30 2007 Tuukka Pasanen <rpms@ilmi.fi>
- New version
* Tue Feb 20 2007 Tuukka Pasanen <rpms@ilmi.fi>
- Initial build
