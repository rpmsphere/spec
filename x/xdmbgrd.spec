Name:           xdmbgrd
BuildRequires:  libX11-devel, libXpm-devel, imake
License:        GPL v2 or later
Group:          System/X11/Displaymanagers
Version:        0.6
Release:        403.1
Summary:        SuSE Linux background
Source:         xdmbgrd-0.6.tar.bz2
Patch:          xdmbgrd-0.6.dif
Patch1:         xdmbgrd-piggyback.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{expand: %%global _exec_prefix %(type -p pkg-config &>/dev/null && pkg-config --variable prefix x11 || echo /usr/X11R6)}

%description
The SuSE Linux background for your XDM workstation.



Authors:
--------
    Werner Fink  <werner@suse.de>

%prep
%setup -q
%patch
%patch1

%build
PATH=$PATH:.
make XLIBD=%{_libdir} openSUSE=SuSE_Linux_6 SLES=SuSE_Linux_7

%install
if test -x %{_bindir}/chooser ; then
	mkdir -p %{buildroot}%{_bindir}
	install -m 0755 BackGround %{buildroot}%{_bindir}
	echo %{_bindir}/BackGround > file-list
else
    if test -x /etc/X11/xdm/chooser ; then
	mkdir -p %{buildroot}/etc/X11/xdm
	install -m 0755 BackGround %{buildroot}/etc/X11/xdm/
	echo /etc/X11/xdm/BackGround           > file-list
    else
	mkdir -p %{buildroot}%{_libdir}/X11/xdm
	install -m 0755 BackGround %{buildroot}%{_libdir}/X11/xdm
	echo %{_libdir}/X11/xdm/BackGround > file-list
    fi
fi

%files -f file-list
%defattr(-,root,root)

%changelog
* Thu Sep 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora

* Mon Jan 12 2009 werner@suse.de
- Detect SLES or openSuSE at run time (bnc#462280)

* Thu Oct  4 2007 bg@suse.de
- Inform piggypack about parisc architecture

* Thu Sep 21 2006 werner@suse.de
- Set branding logo at compile time  (bug #206869)
- Use new logos for openSuSE and SLES

* Tue Aug  1 2006 werner@suse.de
- Make it compatible with X11R7

* Sat May 27 2006 schwab@suse.de
- Don't strip binaries.

* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires

* Thu Mar 11 2004 werner@suse.de
- Update to 0.5 for simply change the SuSE_Linux xpm (bug #35626)

* Sun Oct 19 2003 meissner@suse.de
- norootforbuild, fixed lib64 problem on ppc32.

* Fri Jun 13 2003 coolo@suse.de
- use BuildRoot
- shuffle install section to avoid installing unpackaged files

* Mon Mar  3 2003 werner@suse.de
- Avoid trouble with stupid rpm: use /usr/X11R6/bin/BackGround only

* Mon Mar  3 2003 werner@suse.de
- Part one of fix for bug #24546: symlink /usr/X11R6/bin/BackGround

* Tue Jan 14 2003 nadvornik@suse.cz
- fixed multi-line string literals

* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides

* Tue Apr 30 2002 werner@suse.de
- Add s390x arch to piggyback and make scanning for ld_m more
  flexible for future architectures.

* Thu Apr 25 2002 werner@suse.de
- Make it build even if on x86_64

* Thu Jun 21 2001 sndirsch@suse.de
- adjusted ld input format/emulation for s390 in piggyback

* Fri Jun  9 2000 werner@suse.de
- Make logo embossed instead of low-lying

* Wed May 10 2000 kukuk@suse.de
- xpm is now part of xf86/xshared

* Thu Apr 13 2000 schwab@suse.de
- Support ia64 in piggyback.
- Pass `-no-warn-mismatch' to linker.

* Tue Mar 21 2000 werner@suse.de
- New version 0.4 for better contours of geeko

* Mon Mar 20 2000 werner@suse.de
- New version 0.3
  * new geeko now looking to the `right' side
  * pickypack now using objdump to get the binary format
- Install BackGround depending at the location of chooser, e.g.
  for XFree86 this is /etc/X11/xdm/

* Sat Dec  4 1999 kukuk@suse.de
- fixed piggyback for SPARC

* Tue Sep 21 1999 uli@suse.de
- fixed piggyback for PPC

* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.

* Thu Mar 11 1999 werner@suse.de
- Drop the dots

* Tue Feb  2 1999 ro@suse.de
- patched piggyback to work on alpha and i386

* Tue Feb  2 1999 ro@suse.de
- use alpha for ld-mode on alpha

* Tue Jul 21 1998 werner@suse.de
- Include sources

* Wed Feb  4 1998 ro@suse.de
- generated spec file
