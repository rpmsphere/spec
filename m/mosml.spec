%undefine _debugsource_packages

Name: mosml
Version: 2.10.1
Release: 2
Summary: Moscow ML
License: GPL
Group: Development/ML
URL: https://mosml.org/
Source0: %name-%version.tar
Patch0:  %name-alt-header.patch
BuildRequires: gmp-devel

%description
Moscow ML provides a light-weight implementation of full Standard ML,
including Modules and some extensions.  Standard ML is a strict
functional language widely used in teaching and research.

Moscow ML is based on the Caml Light system, which gives fast
compilation and modest storage consumption.

   * The full SML Modules language (structures, signatures, and functors)
     is now supported, thanks to Claudio Russo.
   * Also, several extensions to the SML Modules language are provided:
      - higher-order functors: functors may be defined within structures
        and functors
      - first-class modules: structures and functors may be packed and
        then handled as Core language values, which may then be unpacked
        as structures or functors again
      - recursive modules: signatures and structures may be recursively
        defined
   * Despite that improvements, Moscow ML remains backwards compatible.
   * Value polymorphism has become friendlier: non-generalizable free
     type variables are left free, and become instantiated (once only)
     when the bound variable is used
   * Added facilities for creating and communicating with subprocesses
     (structure Unix and Signal from SML Basis Library).
   * Added facilities for efficient functional generation of HTML code
     (structure Msp); also supports the writing of ML Server Page scripts.
   * Added facilities setting and accessing `cookies' in CGI scripts
     (structure Mosmlcookie), thanks to Hans Molin, Uppsala, Sweden.
   * The Gdimage structure now produces PNG images (using Thomas
     Boutell's gd library).

%set_verify_elf_method rpath=relaxed unresolved=relaxed

%prep
%setup
%patch 0 -p1

%build
%define docdir %_docdir/%name
#mkdir -p %buildroot%docdir

cd src
make PREFIX=%_datadir BINDIR=%_bindir LIBDIR=%_libdir/mosml DOCDIR=%buildroot/%docdir world
cd compiler
make promote
cd ../
make PREFIX=%_datadir BINDIR=%_bindir LIBDIR=%_libdir/mosml DOCDIR=%buildroot/%docdir again

%install
cd src
make PREFIX=%buildroot/usr BINDIR=%buildroot/%_bindir LIBDIR=%buildroot/%_libdir/mosml DOCDIR=%buildroot/%docdir install
rm -f %buildroot/%_libdir/mosml/camlrunm
cd ..
cp -a README copyrght doc/* examples %buildroot/%docdir

%files
%docdir
%_bindir/*
%_includedir/*
%_libdir/mosml
%_datadir/mosml

%changelog
* Sun Oct 30 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.10.1
- Rebuilt for Fedora
* Tue Oct 09 2018 Andrey Bergman <vkni@altlinux.org> 2.10.1-alt2
- Add unpackaged files.
* Sat Sep 03 2016 Andrey Bergman <vkni@altlinux.org> 2.10.1-alt1
- Initial release for Sisyphus.
