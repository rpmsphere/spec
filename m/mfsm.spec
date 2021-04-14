Name:           mfsm
License:        PERMISSIVE-OSI-COMPLIANT
Group:          System/Monitoring
URL:            http://members.tripod.com/SDHEngSoft/mfsm.html
Version:        1.4
Release:        960.1
Summary:        X Window System Based du
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch:          %{name}-%{version}.patch
Patch1:         %{name}-%{version}-file-close.patch
BuildRequires:  imake
BuildRequires:  libXpm-devel
BuildRequires:  motif-devel

%description
X Window Motif utility that monitors free space and user quotas of file
systems.

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
%define _xorg7_prefix /usr

%prep
%setup -q
%patch
%patch1

%build
xmkmf -a
test -x /usr/sbin/switch_motif_linking && \
  /usr/sbin/switch_motif_linking dynamic
make CCOPTIONS="$RPM_OPT_FLAGS" LDFLAGS="-L/usr/%{_xorg7libs}"
#mv mfsm mfsm.SuSE-dynamic
#test -x /usr/sbin/switch_motif_linking && \
#  /usr/sbin/switch_motif_linking static
#make LDFLAGS="-L/usr/X11R6/lib"
#mv mfsm mfsm.SuSE-static
#make

%install
mkdir -p $RPM_BUILD_ROOT/usr/%{_xorg7bin}
mkdir -p $RPM_BUILD_ROOT/%{_xorg7_mandir}/man1
install -m 0755 mfsm $RPM_BUILD_ROOT/usr/%{_xorg7bin}
install -m 0644 mfsm._man $RPM_BUILD_ROOT/%{_xorg7_mandir}/man1/mfsm.1x
#install -m 0755 mfsm.SuSE-static /usr/%{_xorg7bin}
#ln -s /usr/%{_xorg7bin}/mfsm.SuSE-static /usr/%{_xorg7bin}/mfsm
install -Dm 0644 bitmaps/icon.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.xpm
install -Dm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop
/usr/%{_xorg7bin}/mfsm
#/usr/%{_xorg7bin}/mfsm.SuSE-dynamic
#/usr/%{_xorg7bin}/mfsm.SuSE-static
%doc %{_xorg7_mandir}/man1/mfsm.1x.gz
%doc README THANKS TODO FIXES

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
* Mon Nov  8 2010 coolo@novell.com
- remove support for pre-9.1
* Tue Aug  4 2009 pgajdos@suse.cz
- added missing fclose() [bnc#527724]
* Thu Jul 27 2006 lmichnovic@suse.cz
- builds also with new X.org 7.x, checks the version of X.org
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Sun Jan 15 2006 schwab@suse.de
- Don't strip binaries.
* Wed Jun 15 2005 meissner@suse.de
- use RPM_OPT_FLAGS.
* Thu Feb 26 2004 hmacht@suse.de
- building as non-root
* Sat Aug 16 2003 adrian@suse.de
- add desktop file
* Sat Jan 11 2003 tcrhak@suse.cz
- update to version 1.4
- added BuildRoot
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Tue Jul 31 2001 adostal@suse.cz
- bzip2 source and convert dif to patch
* Mon Nov 20 2000 ro@suse.de
- use openmotif
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Mon Jul 12 1999 uli@suse.de
- now builds with lesstif
* Tue Sep 15 1998 ro@suse.de
- added lib Xp for motif
* Tue Aug 11 1998 ray@suse.de
- new package
