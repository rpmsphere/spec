Name:           ding
BuildRequires:  tk
License:        GPLv2+
Group:          Productivity/Office/Dictionary
Requires:       tcl tk
Summary:        An X Window System Dictionary Tool
Version:        1.8.1
Release:        1
URL:            http://www-user.tu-chemnitz.de/~fri/ding/
Source0:        ftp://ftp.tu-chemnitz.de/pub/Local/urz/ding/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         ding-install.diff
Patch1:         ding-tk-version.diff
BuildArch:      noarch

%description
Ding is a smart X Window System English-to-German dictionary.  It works
with a local database file. For full functionality, agrep should be
installed.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%install
install -d $RPM_BUILD_ROOT%_bindir
install -d $RPM_BUILD_ROOT%_datadir/dict
./install.sh <<EOF
y
$RPM_BUILD_ROOT%_bindir
$RPM_BUILD_ROOT%_datadir/dict
y
EOF
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%_datadir/applications/%name.desktop
install -Dm644 ding.png $RPM_BUILD_ROOT%_datadir/pixmaps/%name.png

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README CHANGES
%_bindir/ding
%_datadir/dict/de-en.txt
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png

%changelog
* Fri Oct 04 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.1
- Rebuild for Fedora
* Sun Sep 18 2011 jengelh@medozas.de
- Remove redundant tags/sections from specfile
  (cf. packaging guidelines)
* Fri Nov  5 2010 hvogel@novell.com
- Upodate to version 1.7
  * Copy to clipboard, not just primary selection (Unix)
  * Bugfixes, robustness increased
  * Enhanced English-German dictionary (270,000 entries)
* Wed Aug  5 2009 hvogel@suse.de
- Update to verion 1.6
  - Catch more faulty inputs
  - Update of the dictionary
* Tue Oct 28 2008 coolo@suse.de
- remove quotes from GenericName
* Fri Apr 18 2008 hvogel@suse.de
- Require american/german ispell packages for spellchecking
* Sat Apr 21 2007 bwalle@suse.de
- update to 1.5
  o New version of German-English translation file, now over
    216,000 entries
  o Some more keyboard shortcuts: ^W, ^U
  o bug fix in internal search
  o changed colors when selecting text in result
  o copy to clipboard in popup/file menu
  o remote invoking changes the query entry (Debian bug #292978)
  o internal search mode works again (tcl_nonwordchars)
  o Minor bug fixes (install.sh)
* Sat Apr  7 2007 bwalle@suse.de
- added application icon  (accepted already upstream, but due to
  long release cycles added to the package)
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Sep  5 2005 hvogel@suse.de
- require tk for the wish binary [#115259]
* Mon May  9 2005 hvogel@suse.de
- update to version 1.4
* Thu Mar 18 2004 hvogel@suse.de
- add desktop file (Bug #36504)
- move ding to /usr
* Mon Feb 16 2004 hvogel@suse.de
- update to version 1.3
- in fact ding is noarch
* Thu Nov 13 2003 hvogel@suse.de
- make use of %%defattr in %%files
* Thu Nov 13 2003 hvogel@suse.de
- dont build as root
* Mon May 26 2003 sndirsch@suse.de
- adjusted install.sh for using BuildRoot; ding works again
* Wed Apr 16 2003 coolo@suse.de
- use BuildRoot
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Fri Aug  2 2002 freitag@suse.de
- update to version 1.2
  removed tcl from the neededforbuild and put tcl to requires.
  Moved dictionary file to /usr/share/dicts
* Mon Aug 13 2001 freitag@suse.de
- removed kde1 desktopfiles and made an entry to the database for
  better appearance o the desktop.
  bzipped the source
* Sat Dec  9 2000 nashif@suse.de
- sorted
* Thu May 25 2000 freitag@suse.de
- update to version 1.1
* Mon Feb 28 2000 freitag@suse.de
- Group Tag inserted and ftp-Source
* Tue Dec 14 1999 freitag@suse.de
- initial version 1.0
