Name:           xprompt
%define _prefix %(pkg-config --variable prefix x11 || echo /usr/X11R6)
%if "%_prefix" == "/usr/X11R6"
%define _mandir %_prefix/man
%endif
BuildRequires:  pkgconfig, libX11-devel, libXt-devel, libXaw-devel, xmkmf
License:        BSD 3-Clause
Group:          System/X11/Utilities
Version:        91.9.28
Release:        2406.1
Summary:        Small tool for prompting users
Source:         xprompt-28sep91.tar.gz
Patch:          xprompt-warn.diff

%description
Small tool to ask the user for one or more responses (e.g., from batch
files).



Authors:
--------
    Barry Brachman <brachman@cs.ubc.ca>

%prep
%setup -n xprompt-28sep91
%patch

%build
xmkmf -a
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%_bindir/*
##%_mandir/man1/*

%changelog
* Thu Sep 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 91.9.28
- Rebuilt for Fedora

* Mon Jul 24 2006 schwab@suse.de
- Fix building with Xorg 7.

* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires

* Thu Sep 16 2004 schwab@suse.de
- Fix more warnings.

* Thu Sep 16 2004 schwab@suse.de
- Fix declaration.

* Wed Apr 21 2004 schwab@suse.de
- Pacify autobuild.

* Sat Feb 28 2004 schwab@suse.de
- Add %%defattr.

* Thu May 15 2003 coolo@suse.de
- noone noticed? I forgot the buildroot tag

* Wed Apr 23 2003 coolo@suse.de
- use BuildRoot
- little cleanup

* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides

* Thu Nov 23 2000 fehr@suse.de
- add group tag

* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
