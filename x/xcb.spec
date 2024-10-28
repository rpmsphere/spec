Name:           xcb
%define _appdefdif %_prefix/share/X11/app-defaults
BuildRequires:  libX11-devel, libXt-devel, libXaw-devel, imake
URL:            https://www.goof.com/pcg/marc/xcb.html
License:        MIT
Group:          System/X11/Utilities
Version:        2.5
Release:        377.1
Summary:        X11 cut&paste utility
Source:         %{name}-%{version}.tar.bz2

%description
Xcb provides access to the cut buffers built into every X server. It
allows the buffers to be manipulated either via the command line or
with the mouse in a point and click manner.  The buffers can be used as
holding pens to store and retrieve arbitrary data fragments, so any
number of different pieces of data can be saved and recalled later. The
program is designed primarily for use with textual data.

%prep
%setup -q

%build
xmkmf -a
make CCOPTIONS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make "DESTDIR=$RPM_BUILD_ROOT" install
make "DESTDIR=$RPM_BUILD_ROOT" install.man
%if %{fedora}<21
mkdir -p $RPM_BUILD_ROOT/usr/share/X11/app-defaults
mv $RPM_BUILD_ROOT/usr/lib/X11/app-defaults/* $RPM_BUILD_ROOT/usr/share/X11/app-defaults
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT%_datadir/man
%endif
rm -rf $RPM_BUILD_ROOT/usr/lib

%files
%_bindir/xcb
%_appdefdif/Xcb
%doc %_mandir/man1/xcb.1x*

%changelog
* Tue Sep 27 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5
- Rebuilt for Fedora
* Mon Nov  8 2010 coolo@novell.com
- remove support for pre-9.1
* Mon Jul 24 2006 mmarek@suse.de
- fix filelist for build with modular Xorg
- use RPM_OPT_FLAGS
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Aug  3 2005 anicka@suse.cz
- update to 2.5 from CVS
* Tue Feb 17 2004 postadal@suse.cz
- updated to branched version 2.4 (by Marc Lehmann <pcg@goof.com>)
  * fixes and better i18n support
- added norootforbuild flag to the spec file
- replaced xf86 by x-devel-packages in neededforbuild flag
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Tue Nov 21 2000 cihlar@suse.cz
- fixed copyright
* Fri May 19 2000 cihlar@suse.cz
- Group sorted
* Tue Apr 11 2000 cihlar@suse.cz
- added BuildRoot
- removed Makefile.Linux
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
