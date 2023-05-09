Name:           ups
Version:        3.38
Release:        18.1
Epoch:          26
Summary:        A native X Window based debugger for C, C++ and Fortran
Group:          Development/Debuggers
License:        GPLv2+ and LGPLv2+
URL:            http://ups.sourceforge.net/
Source0:        http://downloads.sourceforge.net/ups/ups-3.38-beta2.tar.gz
Patch0:         ups-cvs.patch
Patch1:         ups-struct-patch
Patch2:         ups-pisameas-patch
Patch6:         ups-loclist.patch
Patch7:         ups-solib.patch
Patch8:         ups-threads.patch
Patch9:         ups-dwarf.patch
BuildRequires:  libX11-devel, xorg-x11-proto-devel
BuildRequires:  libXt-devel, libICE-devel, libSM-devel
BuildRequires:  elfutils-libelf-devel

%description
Ups is a source level C and C++ debugger that runs under X11.
Fortran is also supported on some systems.
 
It runs in a window with two major regions: one showing the
current state of the target program data and the other showing
the currently executing source code.  A key feature of ups is
that the variables display is persistent: when you add a variable
to the display it stays there as you step through the code.  The
current stack trace (which function called which) is always visible.
 
Ups includes a C interpreter which allows you to add fragments
of code simply by editing them into the source window (the source
file itself is not modified).  This lets you add debugging printf
calls without recompiling, relinking (or even restarting) the
target program.  You can also add conditional breakpoints in a
natural way - you just add a statement like "if (i == 73) #stop"
at the appropriate place in the source window.

%prep
%define _default_patch_fuzz 2
%setup -q -n ups-3.38-beta2
%patch0 -p1 -b .cvs
%patch1 -p1 -b .struct
%patch2 -p1 -b .pisameas
%patch6 -p1 -b .loclist
%patch7 -p0 -b .solib
%patch8 -p0 -b .threads
%patch9 -p0 -b .dwarf
sed -i 's|_IO_2_1_\([a-z]*\)_|\1|g' ups/cx_libvars.h
sed -i '226,231d' ups/ao_elfcore.c
%ifarch aarch64
#sed -i 's|user_fpregs_struct|user_regs_struct|' ups/mreg.h
%endif

%build
CFLAGS="$RPM_OPT_FLAGS -D_LARGEFILE64_SOURCE -Wno-format-security"
%configure --enable-math --enable-longlong
make
iconv -f iso-8859-1 -t utf-8 -oCHANGES.utf8 CHANGES
mv -f CHANGES.utf8 CHANGES

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 ups/ups $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 644 ups/doc/ups.man $RPM_BUILD_ROOT/%{_mandir}/man1/ups.1
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/X11/app-defaults
install -m 644 Ups $RPM_BUILD_ROOT/%{_datadir}/X11/app-defaults

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README* CHANGES BUGS FAQ
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/X11/app-defaults/Ups

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 3.38
- Rebuilt for Fedora
* Thu Mar 18 2010 Steve Webb <bigwebb@gmail.com>
- http://badcheese.com/2010/08/03/ups-debugger.html
- Initial package
