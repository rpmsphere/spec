%global debug_package %{nil}

Name:		ackit
Version:	6.1pre1
Release:	1
Summary:	The Amsterdam Compiler Kit
Group:		Development/Languages
URL:		https://github.com/davidgiven/ack
License:	BSD
Source:		ack-default.zip
BuildRequires: flex-devel
BuildRequires: ed
BuildRequires: byacc

%description
The Amsterdam Compiler Kit is a complete compiler toolchain consisting of
front end compilers for a number of different languages, code generators,
support libraries, and all the tools necessary to go from source code to
executable on any of the platforms it supports.

Languages:
ANSI C, Pascal, Modula 2. K&R is supported via the ANSI C compiler.

%prep
%setup -q -n ack-default
##sed -i 's@^DEFAULT_PLATFORM = ".*@DEFAULT_PLATFORM = "linux386"@' config.pm
##sed -i 's@^PREFIX = ".*@PREFIX = "/usr"@' config.pm
##echo 'PREFIX = "%buildroot%_prefix"' > buildroot.pm
##for f in `fgrep -rl lib.bin .`; do
##sed -i 's/lib[.]bin/libexec/g' $f
##done
#sed -i 's|dir $g|dir $(firstword $g)|' util/ack/build.mk

%build
#sed -i 's|define file|define myfile|' first/core.mk
#sed -i 's|call file|call myfile|' `find . -name build.mk`
sed -i 's|CC = gcc|CC = gcc -Wl,--allow-multiple-definition|' Makefile
make -i
##./pm configure
##./pm

%install
mkdir -p %{buildroot}/usr
make PREFIX=%{buildroot}/usr install
##./pm -fpmfile -f buildroot.pm install
##mkdir -p %buildroot%_datadir
##mv %buildroot%_prefix/man %buildroot%_datadir/

%files
%_bindir/*
/usr/lib/ack
%_mandir/*/*
%_datadir/ack
#_includedir/*

%changelog
* Thu Dec 19 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 6.1pre1
- Rebuild for Fedora
* Wed Mar 02 2011 Fr. Br. George <george@altlinux.ru> 6.0pre4-alt1
- Initial build from scratch
