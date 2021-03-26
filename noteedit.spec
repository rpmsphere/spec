#
# spec file for package noteedit (Version 2.8.1)
#
# Copyright (c) 2008 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           noteedit
Version:        2.8.1
Release:        230.184
#
License:        GPL-2.0+
#
Summary:        Score Editor with Extensive MIDI and MusiXTeX Functionality
#
Url:            http://noteedit.berlios.de/
Group:          Productivity/Multimedia/Sound/Midi
Source:         noteedit-%{version}.tar.bz2
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch1:         noteedit-2.8.1-header_protectors.patch
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch4:         noteedit-2.8.0_uninitialized.patch
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch5:         noteedit-2.8.1-desktop_file.patch
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch6:         noteedit-2.8.1-compilefixes.patch
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch7:         noteedit-2.8.1_uninitialized_variables.patch
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch8:         noteedit-2.8.1_gcc43_misc_fixes.patch
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch9:         %{name}-%{version}-undefined-code.patch
#
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  kdelibs3-devel
BuildRequires:  tse3-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
NoteEdit is a score editor based on the MIDI library TSE3. It can read
and write MIDI files and process events sent from an external MIDI
keyboard. The configured MIDI devices can be used to play the score.
The score can be saved as a MusiXTeX file for printout.

%prep
%setup -q
%patch1
%patch4
%patch5
%patch6 -p1
%patch7
%patch8
%patch9

%build
. /etc/opt/kde3/common_options
export CFLAGS="${CFLAGS} -fpermissive"
export CXXFLAGS="${CFLAGS}"
update_admin --no-unsermake
./configure \
    $configkde \
    --with-libtse3-libs=%{_libdir} \
    --libdir=/opt/kde3/%{_lib} \
    --with-qt-libraries=/usr/lib/qt3/%{_lib}
%{__make} %{?jobs:-j %jobs}

%install
%makeinstall
#  This is a work around for bug #143742. dont remove it!
%{__install} -D -m 0644 noteedit/icons/hi32-app-noteedit.png %{buildroot}%{_datadir}/pixmaps/NoteEdit.png
test -f %{buildroot}opt/kde3/%{_lib}/libnoteedit.so && rm %{buildroot}opt/kde3/%{_lib}/libnoteedit.so
%suse_update_desktop_file %{name} Sequencer
%find_lang %{name}
%fdupes -s %{buildroot}opt/kde3/share/
#
find doc/ -name Makefile\* -print0 | xargs -r0 rm -v

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %name.lang
%defattr(-,root,root)
/opt/kde3/bin/noteedit
/opt/kde3/share/appl*/*/*
/opt/kde3/share/apps/noteedit
/opt/kde3/%{_lib}/libnoteedit.so*
/opt/kde3/%{_lib}/libnoteedit.la
%{_datadir}/pixmaps/NoteEdit.png
%doc AUTHORS README VERSION COPYING LICENSE.GPL INSTALL FAQ doc/* noteedit/examples

%changelog
* Sat Jan 12 2013 lars@linux-schulserver.de
- ran spec-cleaner
* Thu Feb 16 2012 lars@linux-schulserver.de
- add fpermissive (and/or let noteedit die...)
* Tue Nov 18 2008 pgajdos@suse.cz
- delete array -> delete [] array [bnc#445085]
* Mon Mar 17 2008 pgajdos@suse.cz
- installs noteedit/examples directory from now [bnc#368459]
* Fri Nov 16 2007 mrueckert@suse.de
- updated noteedit-2.8.1_gcc43_misc_fixes.patch:
  more gcc 4.3 fixes. still lots of non fatal warnings
* Fri Nov  9 2007 mrueckert@suse.de
- updated noteedit-2.8.0-desktop_file.patch
  new name noteedit-2.8.1-desktop_file.patch:
  additional cleanup of the desktop file
- added noteedit-2.8.1_gcc43_misc_fixes.patch:
  fix the errors with gcc 4.3
- clean up documentation
- run fdupes
* Fri Mar 30 2007 stbinner@suse.de
- add bison and flex to build requires
* Mon Oct 16 2006 mrueckert@suse.de
- update to 2.8.1:
  many bug fixes and enhancements.
  including the fix for broken keyboard handling. [#210971]
- removed patches:
  | noteedit-2.8.0-gcc4.patch
  | noteedit-2.8.0_nscaleedit_h.patch
  | noteedit-2.8.0-yflags.patch
- update noteedit-*-header_protectors.patch:
  rediff for new version
- added noteedit-2.8.1-compilefixes.patch:
  patch from packman rpm
- added noteedit-2.8.1_uninitialized_variables.patch:
  initialize the last struct member.
* Wed Feb 15 2006 stbinner@suse.de
- add GenericName to .desktop file
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan 23 2006 mrueckert@suse.de
- added tse3-devel to the nfb
* Wed Jan 18 2006 mrueckert@suse.de
- rename the icon to NoteEdit to work around #143742
* Mon Jan 16 2006 mrueckert@suse.de
- new patches:
  - noteedit-2.8.0-gcc4.patch
    make it recognize gcc 4
  - noteedit-2.8.0-header_protectors.patch
    protect some headers so we dont include them twice
  - noteedit-2.8.0_nscaleedit_h.patch
    remove some unneeded includehints
  - noteedit-2.8.0_uninitialized.patch
    fix one uninitialized variable
  - noteedit-2.8.0-yflags.patch
    dont use YFLAGS use AM_YFLAGS
* Mon Jan 16 2006 mrueckert@suse.de
- update to 2.8.0
* Mon Dec 19 2005 stbinner@suse.de
- fix file list
* Fri Apr 29 2005 pmladek@suse.cz
- enabled build with gcc4
- enabled parallel build
* Thu Feb 17 2005 adrian@suse.de
- menu entry moved to xdg dir
* Mon Jan 10 2005 ro@suse.de
- install application icon
* Thu Aug 26 2004 mana@suse.de
- Update to version 2.7.3
* Thu Apr  8 2004 jw@suse.de
- New version 2.5.3
* Sat Jan 10 2004 adrian@suse.de
- fix Categorie
* Wed Nov  5 2003 ro@suse.de
- fix noteedit/icons/Makefile.in (recursive variable definition)
* Mon Aug 11 2003 mana@suse.de
- New version 2.3.1
* Mon Aug 11 2003 adrian@suse.de
- add Categories
* Mon Aug  4 2003 ro@suse.de
- try to fix build on lib64
* Thu Jul 24 2003 mana@suse.de
- Update to 2.2.3
* Mon Jun 23 2003 coolo@suse.de
- use %%find_lang
* Sun Jun  1 2003 ro@suse.de
- add .la file to filelist
* Mon Feb  3 2003 mana@suse.de
- update to version 2.0.19 fixes several bugs concerning:
  - autobeam and graces
  - restoring dynamics ending at grace
  - restoring "play transposed"
  - slures
* Wed Jan  8 2003 mana@suse.de
- update to version 2.0.17:
  - Script based MusiXTeX export
  - Many bugfixes (mainly concerning slures)
* Wed Nov 13 2002 ro@suse.de
- fix configure test for bison
* Tue Sep  3 2002 mana@suse.de
- Version 2.0.14 integrates some of the patches into new tarball
- Fixed index.doc
- removed obsolete patches
* Fri Aug 30 2002 ro@suse.de
- use disable-final and fix resulting makefile problems
- disable bison-fix.dif
  (problematic and not needed with disable-final)
- added missing icons (Makefile-fix)
- added hungarian translation
* Fri Aug 16 2002 tiwai@suse.de
- updated to version 2.0.10.
  including the fix for memory leaks.
* Tue Jul 16 2002 tiwai@suse.de
- updated to version 2.0.5.
  fixed weird bugs regarding bison and compilation.
* Tue May 28 2002 meissner@suse.de
- %%_lib and gcc3 fixes.
* Mon Feb 18 2002 mana@suse.de
- update to 1.17.1
- Icons look now much better
- Makefiles fixed by author (no further patch for autoconf required)
- Many other bugs fixed by author
* Tue Jan 22 2002 mana@suse.de
- update to 1.17.0
- many new features
- doc/ now included in noteedit source
* Fri Nov  9 2001 ro@suse.de
- use qt-devel-packages in neededforbuild
* Mon Sep  3 2001 mana@suse.de
- update to 1.13.5
- better y positioning with mouse
- PMX export errors fixed: offbeat, key signature --> accidentals
- keyboard insertion bug fixed
- bison/flex compatible
- LilyPond export bug (concerning LilyPond non-treble-clefs) fixed
* Tue Aug 14 2001 mana@suse.de
- update to 1.13.3
* Tue Jul 31 2001 mana@suse.de
- update to 1.12.3
* Mon May  7 2001 mana@suse.de
- added missing documentation
* Wed Apr 11 2001 schwab@suse.de
- Fix missing declarations.
* Tue Mar 27 2001 mana@suse.de
- update to 1.10.6
* Wed Mar 21 2001 ro@suse.de
- fixed mesa-packs in neededforbuild
* Wed Mar 21 2001 mana@suse.de
- update to 1.10.5
- noteedit is now a KDE application, changed installdirs to /opt/kde2/...
* Wed Jan 31 2001 mana@suse.de
- created package for noteedit 1.9.6
