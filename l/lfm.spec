%undefine _debugsource_packages
Name:		lfm
Version:	2.3
Release:	6.1
Summary:	File Manager for the Console
Source:		https://www.terra.es/personal7/inigoserna/lfm/%{name}-%{version}.tar.gz
Patch1:		lfm-docdir.patch
Patch2:		lfm-remove_shebangs.patch
URL:		https://www.terra.es/personal7/inigoserna/lfm/
Group:		Productivity/File utilities
License:	GNU General Public License version 3 (GPL v3)
BuildRequires:	python2-devel
BuildRequires:	perl
Provides:	pyview = %{version}-%{release}
BuildArch:	noarch

%description
Last File Manager is a simple but powerful file manager for the UNIX console.
It has been developed in Python with the ol' good Midnight Commander as model.

%prep
%setup -q
%patch1
%__perl -ne 'print $1,"\n" if /^\+{3}\s+(.+?)\s+\d/' <"%{PATCH1}" | while read f; do
	 %__sed -i 's|@@DOCDIR@@|%{_docdir}/%{name}|g' "$f"
done
%patch2

%build
python2 setup.py build

%install
python2 setup.py install --root=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog COPYING NEWS README* TODO
%{_bindir}/*
%{_mandir}/man1/lfm.1.*
%{_mandir}/man1/pyview.1.*
%{python2_sitelib}/%{name}*

%changelog
* Wed Oct 10 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3
- Rebuilt for Fedora
* Sun May 22 2011 pascal.bleser@opensuse.org
- update to 2.3:
  * lfm needs python version 2.5 or upper now
  * New features
    + PowerCLI, an advanced command line interface with completion, persistent
    history, variable substitution and many other useful features; as this is a
    very powerful tool, read the documentation for examples
    + history
  - use different types of history lists: path, file, glob, grep, exec, cli
    for the different forms and actions
  - persistent history between sessions => ~/.lfm_history
    (controlled by a flag in configuration)
    + find/grep
  - configuration options for ignorecase and regex
  - sort results
  - show results as FILE:lineno
  - much faster
    + show diff between xxx.orig and xxx files
    + tar files compress/uncompress
    + messages.EntryLine has been rewritten, with many new key shorcuts. This is
    the core behind most of the forms lfm shows when asking for anything.
    Consult the documentation
  * Minor changes
    + reorganize "un/compress file" and "compress directory xxx" in file_menu
    + config: sort entries when saving
    + improve load/save handling of new options not present in ~/.lfmrc
    + added new extensions
    + messages.error rewritten to offer better messages
    + added some new key shortcuts messages.SelectItem
  * lots of bugs fixed:
    + pyview:
  - last char is not shown if file size is small
  - last line and wrap: cursor_down or page_next
  - when number of lines == window height
    + ncurses v5.8 doesn't accept 0 as width or height
    + UI crashes:
  - time string could contain non-ascii characters
  - when filenane length is large in full pane mode
  - MenuWin, SelectItem: ellipsize entries if bigger than screen width
    + find or find&grep:
  - pass "-type f" to find  as ".#filename" are temporary emacs files/links
    that break search
  - show wrong matches if results contain directories or files with spaces
  - file->goto_file: move to correct page
    + copy/move "/file" to "/anydir/anyplace" fails, trying to copy/move to "/"
    + executing non-ascii programname or args
    + convoluted issue with link to directory in corner cases (reported by Xin Wang)
    + rename/backup ".." crashes
    + we should not compress ".."
    + create_link, edit_link: don't show error if canceled
    + only store one copy of the same entry in history
    + tree: "disable" colors of active panel, "enable" at end
    + Config.save: work with unicode, only convert to encoding when saving
* Sat May 22 2010 pascal.bleser@opensuse.org
- initial package (2.2)
