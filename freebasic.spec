%global debug_package %{nil}

Name:		freebasic
Version:	1.07.1
Release:	1
Summary:	FreeBASIC language compiler
License:	GPL
Group:		Education
Source:		FreeBASIC-%version-source.tar.gz
Source1:	FB-manual-%version-html.zip
URL: 		http://freebasic.net
BuildRequires:  freebasic
BuildRequires:  gcc-c++
BuildRequires:  libffi-devel
BuildRequires:  gpm-devel
BuildRequires:  libGL-devel
BuildRequires:  ncurses-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  zlib-devel
BuildRequires:  unzip
Requires: 	gcc

%description	
FreeBASIC - is a completely free, open-source, BASIC compiler,
with syntax similar to MS-QuickBASIC, that adds new features such as
pointers, unsigned data types, inline assembly, object orientation,
and many others.

%prep
%setup -q -n FreeBASIC-%version-source
mkdir doc/html
unzip -q %SOURCE1 -d doc/html
ln -s 00index.html doc/html/index.html
#ifarch aarch64
#sed -i '2755,2756d' src/compiler/fbc.bas
#sed -i 's|sys/io.h|sys/uio.h|' src/rtlib/unix/hinit.c
#endif

%build
%make_build FBCFLAGS="-i /usr/include/freebasic" FBLFLAGS="-p %_libdir/freebasic -prefix %_prefix"

%install
%make_install prefix=%_prefix
install -D doc/fbc.1 %buildroot%_mandir/man1/fbc.1
mkdir -p %buildroot%_datadir/freebasic
cp -a examples %buildroot%_datadir/freebasic

%files
%doc *.txt doc/html/*
%_bindir/fbc
%_includedir/freebasic
/usr/lib/freebasic
%_datadir/freebasic
%_mandir/man1/*

%changelog
* Thu Oct 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.07.1
- Rebuild for Fedora
* Wed Apr 15 2015 Andrey Cherepanov <cas@altlinux.org> 1.02.0-alt2
- Replace old i586-freebasic
* Wed Apr 15 2015 Andrey Cherepanov <cas@altlinux.org> 1.02.0-alt1
- Rebuild in bootstrapped arch
* Tue Apr 14 2015 Andrey Cherepanov <cas@altlinux.org> 1.02.0-alt0.1
- New version
- Bootstrap for x86_64 version
- Disable tests
* Wed Nov 20 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt6
- Simplify build parameters
- Remove deprecated linker flags
* Tue Nov 19 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt5
- Supress linking warnings on 64-bit systems
- Fix strict version in library symlinks
* Fri Nov 15 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt4
- Remove fbhelp binary and its help file
- Add missing libraries
* Thu Nov 14 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt3
- Set required libraries in Arepo
- Build fbhelp
- Pack documentation
* Wed Oct 02 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt2
- Rebuild from sources
- Pack fbc man page and examples
* Wed Oct 02 2013 Andrey Cherepanov <cas@altlinux.org> 0.90.1-alt1
- Build for Sisyphus (bootstrap)
