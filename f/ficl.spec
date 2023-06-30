Summary: An embeddable Forth interpreter
Name: ficl
Version: 4.1.0
Release: 4.1
License: Freeware
Group: Development/Libraries
URL: https://ficl.sourceforge.net
Source0: https://ncu.dl.sourceforge.net/project/ficl/ficl-all/ficl4.1/%{name}-%{version}.tar.gz

%description
Ficl (Forth inspired command language) is an ANS Forth interpreter written
in C. Unlike traditional Forths, this interpreter is designed to be embedded
into other systems as a command/macro/development prototype language. Ficl
provides object extensions that can be used to wrap methods and structures
of the host system without altering them.

Where Forths usually view themselves as the center of the system and expect
the rest of the system to be coded in Forth, Ficl acts as a component of
the system. It is easy to export code written in C or ASM to Ficl in the
style of TCL, or to invoke Ficl code from a compiled module. This allows
you to do incremental development in a way that combines the best features
of threaded languages (rapid development, quick code/test/debug cycle,
reasonably fast) with the best features of C (everyone knows it, easier
to support large blocks of code, efficient, type checking).

In addition, Ficl provides a simple object model that can act as an object
oriented adapter for code written in C (or asm, Forth, C++...). 

%prep
%setup -q

%build
make CFLAGS="${RPM_OPT_FLAGS} -fPIC -Dlinux -I. -I./ficlplatform" lib ficl

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/ficl

install ficl ${RPM_BUILD_ROOT}%{_bindir}

for f in libficl.so.* libficl.a
do
   install $f ${RPM_BUILD_ROOT}%{_libdir}
done

for f in *.h ficlplatform/unix.h
do
   install -m 0644 $f ${RPM_BUILD_ROOT}%{_includedir}/ficl
done

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc doc ReadMe.txt
%{_bindir}/*
%{_libdir}/libficl.*
%{_includedir}/ficl

%changelog
* Sat Feb 19 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1.0-1
- Rebuilt for Fedora
* Thu Jun 26 2003 Jeff Johnson <jbj@redhat.com> 4.0.31-1
- upgrade to 4.0.31.
* Fri Apr 13 2001 Jeff Johnson <jbj@redhat.com>
* Create.
