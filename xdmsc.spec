Name:           xdmsc
License:        YaST License
Group:          System/X11/Utilities
Provides:       Xterminal
Version:        0.4
Release:        281.1
Summary:        Xterminal -- Use SuSE Linux as an X terminal
Source:         Xterminal-0.4.tar.gz
Patch:          Xterminal-0.4.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Some useful scripts for using SuSE Linux as an X terminal.

You will find the documentation in the following directory

/usr/share/doc/packages/xdmsc/



Authors:
--------
    Werner Fink  <werner@suse.de>

%prep
%setup -n Xterminal-0.4
%patch

%build
    make -f Makefile.Linux compile

%install
    rm -rf $RPM_BUILD_ROOT
    make -f Makefile.Linux DESTDIR=$RPM_BUILD_ROOT install

%clean
    rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%config /etc/init.d/rx
/var/adm/fillup-templates/sysconfig.xdmsc

%changelog
* Thu Sep 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora

* Wed Nov 25 2009 werner@suse.de
- Handle next new version strings of the X server of Xorg (bnc#537141)

* Mon Feb 19 2007 werner@suse.de
- Be X11R7 compatible (bug #246744)

* Fri Feb  9 2007 dmueller@suse.de
- build as non-root

* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires

* Tue Nov 29 2005 werner@suse.de
- Handle new version strings of the X server of Xorg.

* Fri Jul  1 2005 werner@suse.de
- Make /etc/X11/xorg.conf the default X11 configuration

* Sun Oct 10 2004 schwab@suse.de
- Fix requires.
- Make noarch.

* Tue Sep  2 2003 kukuk@suse.de
- Add empty Command tag to prevent a SuSEconfig run [Bug #28962]

* Mon Jul 21 2003 werner@suse.de
- Fix bug #28089 : use full path for X server

* Fri Jun 13 2003 coolo@suse.de
- use BuildRoot

* Thu Mar 27 2003 werner@suse.de
- Change README (/etc/rc.config -> /etc/sysconfig/xdmsc)

* Fri Feb 28 2003 werner@suse.de
- Fix bug #22704: Add meta data to sysconfig file xdmsc

* Fri Aug 16 2002 werner@suse.de
- Add PreReq (bug #18017)

* Wed Jul  3 2002 werner@suse.de
- Use /etc/sysconfig/xdmsc (bug #16789)

* Fri Mar  1 2002 werner@suse.de
- New Xservers accept -class only after -query

* Mon Jan 14 2002 ro@suse.de
- variables moved to /etc/sysconfig/xdmsc
- START_ variable left here since this is not a regular
  initscript but started from inittab

* Fri Dec  8 2000 kukuk@suse.de
- Move sbin/init.d -> etc/init.d

* Mon Sep  4 2000 werner@suse.de
- Update to version 0.3
  * Use version of X server before using options

* Mon Jun  5 2000 ro@suse.de
- doc relocation

* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.

* Mon Jul  6 1998 werner@suse.de
- New release: Now only clients (e.g. xterminals) are supported.

* Sun Jun  1 1997 bs@suse.de
- moved fillup stuff to var/adm/fillup-templates

* Wed Apr 16 1997 werner@suse.de
- New package for xdm server and clients.
  - After configuratiuon ist is possible to start out of
    /etc/inittab for calling a chosser menu or a xdm window
    from a xdm server.
  - Usefull scripts to have a xdm server under S.u.S.E. Linux.
