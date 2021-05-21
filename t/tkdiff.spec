Name:           tkdiff
BuildArch:      noarch
License:        GPL2.0+
Group:          Productivity/Text/Utilities
Requires:       tk diffutils
Version:        4.3.5
Release:        1
Summary:        2 and 3-way diff/merge tool
URL:            http://tkdiff.sourceforge.net/
#Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source0:        tkdiff-4-3-5.zip
Source1:        README.SuSE

%description
TkDiff is a graphical 2 and 3-way diff/merge tool.

%prep
%setup -q -n tkdiff-4-3-5
cp %{SOURCE1} .

%build

%install
install -d -m 755 $RPM_BUILD_ROOT/usr/bin
install -m 755 tkdiff $RPM_BUILD_ROOT/usr/bin/tkdiff

%files
%doc README.SuSE
/usr/bin/tkdiff

%changelog
* Tue Oct 08 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.3.5
- Rebuilt for Fedora
* Mon Nov 28 2011 pascal.bleser@opensuse.org
- update to 4.2:
  * works with Subversion 1.7
  * make opening file dialog know where it started from, and start in the same
    directory as the first file when looking for the second one
  * you can now specify a preference for filetypes for the file open/save
    dialogs
  * detect PVCS by environment variable (patch 1839361 by nafmo)
  * update BitKeeper support (patch 3053551 by wscott)
  * mercurial support (patch 1867700 by damonmc)
  * rudimentary Git support (patch 1836293 by cecilh3)
  * add help menu items to report versions of wish and diff
  * gave it a debug (-d) option
* Thu Jul 21 2011 rcoe@wi.rr.com
- patch to add git support from sf.net#1836293
* Tue Nov 27 2007 lmichnovic@suse.cz
- update to version 4.1.4
  * Ignore -u option from svn for usage "svn diff --diff-cmd=tkdiff"
  * Perforce support for P4CONFIG environment variable
  * Remove an old font work-around for Mac, but add a new one for tk8.5
  on Windows
  * Fix duplicate keyboard accelerator for Preferences
* Fri Aug 11 2006 lmichnovic@suse.cz
- changed bindir to /usr/bin
* Tue Jun 20 2006 lmichnovic@suse.cz
- update to verson 4.1.3
  * Fixed incompatibility with older versions of Tcl/Tk
    ("-state disabled").
  * Applied Warren Jones' subversion patch, which prevents the svn
    error that occurs when you omit a revision number.
  * Can now do "tkdiff OLD-URL[@OLDREV] NEW-URL[@NEWREV]" in svn.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan  2 2006 lmichnovic@suse.cz
- update to version 4.1.1 which includes security patch for temp files
  (CVE-2005-4434) [#141076]
- updated copyright in README.SuSE file
* Thu Sep 29 2005 dmueller@suse.de
- add norootforbuild
* Mon Nov 15 2004 ltinkl@suse.cz
- updated to 4.0.2
* Sun Oct 10 2004 schwab@suse.de
- Fix requires.
* Fri Sep  6 2002 pmladek@suse.cz
- fixed usage of -pad
* Fri Aug 17 2001 pmladek@suse.cz
- updated to version 3.09
- README.SuSE moved to sources
* Wed Mar 28 2001 nadvornik@suse.cz
- update to 3.08
* Thu Nov 23 2000 ro@suse.de
- fixed requires
* Thu Oct 12 2000 nadvornik@suse.cz
- new package
