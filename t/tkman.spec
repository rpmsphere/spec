Name:           tkman
License:        Artistic-1.0
Group:          System/Base
Requires:       tcl tk rman
Version:        2.2
Release:        158.1
Summary:        Manual-browser for X
URL:            https://tkman.sourceforge.net
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}.patch
Patch1:         tkman-CVE-2008-5137.patch
BuildArch:      noarch

%description
A manual browser for X with hyperlinks, history, and more.

Authors:
--------
    T.A. Phelps

%prep
%setup -q
%patch0
%patch1 -p 1

%build
make

%install
mkdir -p %buildroot/usr/bin
make DESTDIR=%buildroot install

%files
%{_bindir}/*
%doc ANNOUNCE-tkman.txt CHANGES README-tkman manual.html

%changelog
* Sun Apr 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuilt for Fedora
* Tue Sep 29 2009 max@suse.de
- Fix a symlink vulnerability by adopting the respective Debian
  patch (bnc#538006, CVE-2008-5137).
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Jan 25 2005 max@suse.de
- New version: 2.2
* Tue Feb 24 2004 hmacht@suse.de
- building as non-root
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Mon Dec 17 2001 max@suse.de
- Using BuildRoot now.
* Wed Apr 11 2001 max@suse.de
- Added Group: X11/Utilities
- Added Buildarchitectures: noarch
* Mon Jun 26 2000 max@suse.de
- replaced version 2.1b4 with final 2.1
* Fri May 26 2000 max@suse.de
- new version 2.1b4
- runs only with Tcl/Tk 8.3 or newer
* Wed Oct 13 1999 max@suse.de
- new version 2.1b2
- removed old tkman package and renamed tkman8 to tkman
- ready for the new Tcl/Tk packages
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Wed Mar 17 1999 ro@suse.de
- diff cleanup
* Tue Aug 26 1997 hf@suse.de
  Recompiled for -Latin1 Bug.
* Tue Jul  1 1997 hf@suse.de
  Added a new Option -Latin1.
* Thu May 22 1997 hf@suse.de
  A new version of tkman works with tcl8.0 and tk8.0.
  Have a new feature, you have sections in man-pages.
* Thu Apr 24 1997 hf@suse.de
  A new version of tkman works with tcl7.6 and tk4.2.
  Have a new feature, if you have a search word you can go
  down and up in the text.
