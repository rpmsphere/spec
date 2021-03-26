%global debug_package %{nil}

Name:           xroach
BuildRequires:  libX11-devel, libXext-devel, imake
License:        PERMISSIVE-OSI-COMPLIANT
Group:          Amusements/Toys/Background
Version:        12.6.97
Release:        2474.1
Summary:        Some cockroaches on your root window
Source:         %{name}.tar.bz2
Source1:        xroach-toon_root.c
Source2:        xroach-README.SuSE
Patch:          xroach.dif
Patch1:         xroach-return.dif
%define _xorg7libs %_lib
%define _xorg7libs32 lib
%define _xorg7bin bin
%define _xorg7_mandir %_mandir
%define _xorg7pixmaps include
%define _xorg7libshare share
%define _xorg7_xkb /usr/share/X11/xkb
%define _xorg7_termcap /usr/lib/X11/etc
%define _xorg7_serverincl /usr/include/xorg
%define _xorg7_fonts /usr/share/fonts
#define _xorg7_config /usr/share/X11/config #use libshare macro
%define _xorg7_prefix /usr

%description
Xroach displays disgusting cockroaches on your root window. These
creepy crawlies scamper around until they find a window to hide under.
Whenever you move or iconify a window, the exposed orthopteras again
scamper for cover.

%prep
%setup -n xroach
%patch
%patch1
cp %{SOURCE1} toon_root.c
cp %{SOURCE2} README.SuSE

%build
export CFLAGS="$RPM_OPT_FLAGS"
xmkmf -a
make %{?jobs:-j%jobs}

%install
make DESTDIR="$RPM_BUILD_ROOT" install
make DESTDIR="$RPM_BUILD_ROOT" install.man
%if %{fedora}<21
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
mv $RPM_BUILD_ROOT/usr/man/man1/* $RPM_BUILD_ROOT/usr/share/man/man1
%endif

%files
%doc README.SuSE
/usr/%{_xorg7bin}/xroach
%doc %{_xorg7_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Sep 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 12.6.97
- Rebuild for Fedora
* Mon Nov  8 2010 coolo@novell.com
- remove support for pre-9.1
* Fri Jul 28 2006 lmichnovic@suse.cz
- builds also with new X.org 7.x, detecting prefix in X.org
- building with icecream
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Apr  7 2005 coolo@suse.de
- fix gcc4 warnings
* Fri Jun 25 2004 hmacht@suse.de
- building as non-root user
* Tue May 18 2004 ltinkl@suse.cz
- fix return values
- use RPM_OPT_FLAGS
- repackage to tar.bz2
* Wed Nov 28 2001 cihlar@suse.cz
- fixed to work under KDE - fix based on xpenguins
- added README.SuSE
* Wed Nov 22 2000 cihlar@suse.cz
- fixed copyright
* Fri May 19 2000 cihlar@suse.cz
- Group sorted
* Fri Mar 10 2000 cihlar@suse.cz
- removed makefile.linux
- added BuildRoot to spec file
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Thu Jun 12 1997 rj@suse.de
- new package (06/12/1997)
