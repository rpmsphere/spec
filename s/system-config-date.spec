%{!?python2_sitelib: %global python2_sitelib %(python2 -c "from distutils.sysconfig import get_python_lib; print get_python_lib(0)")}
%{!?python2_version: %global python2_version %(python2 -c "from distutils.sysconfig import get_python_version; print get_python_version()")}

# Command line configurables

%if 0%{?fedora}%{?rhel} == 0 || 0%{?fedora} >= 8 || 0%{?rhel} >= 6
%bcond_without newt_python
%else
%bcond_with newt_python
%endif

# Enterprise versions pull in docs automatically
%if 0%{?rhel} > 0
%bcond_without require_docs
%else
%bcond_with require_docs
%endif

# Use systemd instead of traditional init
%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 15 || 0%{?rhel} >= 7
%bcond_without systemd
%else
%bcond_with systemd
%endif

Summary: A graphical interface for modifying system date and time
Name: system-config-date
Version: 1.10.9
Release: 2.1
URL: https://fedorahosted.org/%{name}
License: GPLv2+
Group: System Environment/Base
BuildArch: noarch
Source0: https://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2
# Until version 1.9.34, system-config-date contained online documentation.
# From version 1.9.35 on, online documentation is split off into its own
# package system-config-date-docs. The following ensures that updating from
# earlier versions gives you both the main package and documentation.
Obsoletes: system-config-date < 1.9.35
%if %{with require_docs}
Requires: system-config-date-docs
%endif
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: python2
BuildRequires: python2-devel

Requires: python >= 2.0
Requires: python-slip >= 0.2.21
Requires: pygtk2 >= 2.12.0
Requires: pygtk2-libglade
Requires: gnome-python2-canvas
Requires: polkit

%if %{with systemd}
Requires: systemd-units
%else
Requires: chkconfig
%endif

%if %{with newt_python}
Requires: newt-python
%else
Requires: newt
%endif
Requires: hicolor-icon-theme
# system-config-date can act as a plugin to set the time/date, configure NTP or
# the timezone for firstboot if the latter is present, but doesn't require it.
# It won't work with old versions of firstboot however.
Conflicts: firstboot <= 1.3.26

%description
system-config-date is a graphical interface for changing the system date and
time, configuring the system time zone, and setting up the NTP daemon to
synchronize the time of the system with an NTP time server.

%prep
%setup -q
sed -i 's|/usr/bin/python|/usr/bin/python2|' system-config-date src/system-config-date.py src/setup.py* 
sed -i 's|python |python2 |' py_rules.mk

%build
make \
%if 0%{?fedora} > 0
    POOL_NTP_ORG_VENDOR=fedora \
%endif
%if 0%{?rhel} > 0
    POOL_NTP_ORG_VENDOR=rhel \
%endif
    %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
desktop-file-install --vendor system --delete-original       \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  --add-category X-Red-Hat-Base                             \
  $RPM_BUILD_ROOT%{_datadir}/applications/system-config-date.desktop

%find_lang %name
%find_lang %{name}-timezones

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/%{name}.py

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang -f %{name}-timezones.lang
%doc COPYING
%{_bindir}/system-config-date
%{_datadir}/system-config-date
%{_datadir}/applications/system-config-date.desktop
%{_datadir}/icons/hicolor/*/apps/system-config-date.*
%{_mandir}/man8/system-config-date*
%{_mandir}/fr/man8/system-config-date*
%{_mandir}/ja/man8/system-config-date*
%{_datadir}/polkit-1/actions/org.fedoraproject.config.date.policy
%{python2_sitelib}/scdate
%{python2_sitelib}/scdate-%{version}-py%{python2_version}.egg-info
#%{python2_sitelib}/scdate.dbus-%{version}-py%{python2_version}.egg-info

%changelog
* Fri Sep 22 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.10.9
- Rebuilt for Fedora

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Nils Philippsen <nils@redhat.com> - 1.10.9-1
- cope with unavailable display in pygtk >= 2.10 (#1197480)

* Tue Jun 16 2015 Nils Philippsen <nils@redhat.com> - 1.10.8-1
- don't use exec in pkexec wrapper script (#1185857)

* Fri Jan 10 2014 Nils Philippsen <nils@redhat.com> - 1.10.7-1
- cope with systemd executables in several possible locations (#1048136)
- pull updated translations

* Fri Oct 04 2013 Rex Dieter <rdieter@fedoraproject.org> 1.10.6-2
- use optimized icon scriptlets

* Mon Jun 17 2013 Nils Philippsen <nils@redhat.com> - 1.10.6-1
- pull updated translations (#950571)

* Tue Dec 11 2012 Nils Philippsen <nils@redhat.com> - 1.10.5-1
- pull updated and new translations (#878319)
- catch (rare) errors from fork()
- catch unavailable display (#766936)
- pull updated time zones

* Thu Dec 06 2012 Nils Philippsen <nils@redhat.com> - 1.10.4-1
- hide SIGINT from firstboot exception handler (#862828)
- pull updated translations

* Thu Nov 08 2012 Nils Philippsen <nils@redhat.com> - 1.10.3-1
- tighten policy

* Thu Oct 25 2012 Nils Philippsen <nils@redhat.com> - 1.10.2-1
- pkexec the right executable

* Tue Oct 23 2012 Nils Philippsen <nils@redhat.com> - 1.10.1-1
- don't trip over missing /etc/sysconfig/network file (#857412)
- pull updated translations
- install and use timezone translations properly

* Mon Oct 22 2012 Nils Philippsen <nils@redhat.com> - 1.10.0-1
- use pkexec instead of consolehelper
- read/write /etc/localtime as symbolic link and only fall back to using
  /etc/sysconfig/clock if it is present (#824033)

* Tue Sep 11 2012 Nils Philippsen <nils@redhat.com> - 1.9.68-1
- pull updated translations

* Tue Oct 18 2011 Nils Philippsen <nils@redhat.com> - 1.9.67-1
- enable tree lines in TZ treeview (#746731)
- pull updated translations

* Wed Oct 05 2011 Nils Philippsen <nils@redhat.com> - 1.9.66-1
- improve enabling/disabling, starting/stopping NTP daemons, take care of the
  respective "other" NTP daemon as well (#743533)
- pull updated translations

* Fri Sep 09 2011 Nils Philippsen <nils@redhat.com> - 1.9.65-1
- cope with neither ntpd nor chrony being installed (#734993)
- pull updated translations

* Tue Aug 23 2011 Nils Philippsen <nils@redhat.com> - 1.9.64-1
- pull updated translations

* Fri Aug 19 2011 Nils Philippsen <nils@redhat.com> - 1.9.63-1
- don't bail out if ntpdate can't be run (#731667)
- cope with systemd or SysVinit, alternatively

* Tue Aug 16 2011 Nils Philippsen <nils@redhat.com> - 1.9.63-1
- add support for chrony (#616385, patch by Miroslav Lichvár)

* Tue Aug 16 2011 Nils Philippsen <nils@redhat.com> - 1.9.62-1
- improve building/cleaning message files (Martin Pitt)
- properly tie dialogs to toplevels, set slightly better dialog titles, set
  dialogs transient for notebook due to firstboot (#528157)
- use branded name in desktop file (#727204)
- use Transifex and pull updated translations

* Tue Aug 24 2010 Nils Philippsen <nils@redhat.com> - 1.9.61-1
- pick up updated translations

* Fri Aug 06 2010 Nils Philippsen <nils@redhat.com> - 1.9.60-1
- recreate TZ translations after each language change

* Thu Aug 05 2010 Nils Philippsen <nils@redhat.com>
- make time zones translations work in anaconda

* Wed Jun 30 2010 Nils Philippsen <nils@redhat.com> - 1.9.59-1
- require docs in enterprise builds
- configure iburst mode instead of ntpdate upon boot (original patch by Radek
  Nováček)
- fix configuring ntp.conf template

* Tue Jun 22 2010 Nils Philippsen <nils@redhat.com> - 1.9.58-1
- pick up additional translations

* Mon Jun 14 2010 Nils Philippsen <nils@redhat.com>
- use better ugettext to allow anaconda to use the time zone widget even with
  encodings other than UTF-8

* Thu Apr 22 2010 Nils Philippsen <nils@redhat.com> - 1.9.57-1
- use themed icon for window

* Wed Apr 21 2010 Nils Philippsen <nils@redhat.com>
- use new icons matching the rest of the icon theme (#583802, provided by Lapo
  Calamandrei)

* Wed Apr 07 2010 Nils Philippsen <nils@redhat.com> - 1.9.56-1
- pick up translation updates

* Tue Mar 23 2010 Nils Philippsen <nils@redhat.com> - 1.9.55-1
- pick up translation updates

* Mon Mar 22 2010 Nils Philippsen <nils@redhat.com>
- fix UnicodeDecodeError (#539904)

* Thu Feb 25 2010 Nils Philippsen <nils@redhat.com> - 1.9.54-1
- remove obsolete obsolete lines
- remove duplicate file listing

* Mon Feb 08 2010 Nils Philippsen <nils@redhat.com>
- don't require libselinux-python directly anymore, this code was moved to
  slip.util.files (#562331)

* Tue Nov 03 2009 Nils Philippsen <nils@redhat.com>
- fix duplicate keyboard shortcut (#532686), add missing keyboard shortcut

* Tue Oct 20 2009 Nils Philippsen <nils@redhat.com> - 1.9.53-1
- make translating time zones more robust (#525921)

* Thu Oct 01 2009 Nils Philippsen <nils@redhat.com> - 1.9.52-1
- pull in fixed Malayalam translations (#526636)

* Wed Sep 30 2009 Nils Philippsen <nils@redhat.com> - 1.9.51-1
- deal better with untranslated time zones (#524823)

* Mon Sep 28 2009 Nils Philippsen <nils@redhat.com> - 1.9.50-1
- pick up new translations

* Mon Sep 14 2009 Nils Philippsen <nils@redhat.com> - 1.9.49-1
- pick up updated translations

* Mon Sep 07 2009 Nils Philippsen <nils@redhat.com> - 1.9.48-1
- use string object methods instead of string module
- get rid of timeconfig and compat program names
- move backend code into scdate.core module

* Wed Sep 02 2009 Nils Philippsen <nils@redhat.com> - 1.9.47-1
- import gettext from each module again (#520799)

* Wed Sep 02 2009 Nils Philippsen <nils@redhat.com> - 1.9.46-1
- use new gtk tooltip API

* Tue Sep 01 2009 Nils Philippsen <nils@redhat.com>
- use slip.util.files.linkorcopyfile() (#512046)
- initialize gettext correctly in all places

* Fri Aug 28 2009 Nils Philippsen <nils@redhat.com> - 1.9.45-1
- initialize gettext correctly

* Fri Aug 28 2009 Nils Philippsen <nils@redhat.com> - 1.9.44-1
- don't unnecessarily initialize gettext

* Fri Aug 28 2009 Nils Philippsen <nils@redhat.com> - 1.9.43-1
- use str instead of unicode as N_ implementation

* Wed Aug 26 2009 Nils Philippsen <nils@redhat.com> - 1.9.42-1
- provide missing N_()

* Wed Aug 26 2009 Nils Philippsen <nils@redhat.com> - 1.9.41-1
- use gettext instead of rhpl

* Wed Aug 26 2009 Nils Philippsen <nils@redhat.com> - 1.9.40-1
- explain obsoleting old versions

* Wed Jul 29 2009 Nils Philippsen <nils@redhat.com>
- improve manual and NTP settings (#507619)
- improve frames and expander (#507623)
- display current date and time always
- fix explanation labels on "Date and Time" page
- fix non-zero page size deprecation warnings

* Thu Jul 09 2009 Nils Philippsen <nils@redhat.com> - 1.9.39-1
- use POOL_NTP_ORG_VENDOR in Makefile to set default NTP servers (#510309)

* Thu Jun 04 2009 Nils Philippsen <nils@redhat.com>
- don't BR: anaconda

* Thu May 28 2009 Nils Philippsen <nils@redhat.com>
- require libselinux-python
- use simplified source URL

* Mon Apr 20 2009 Nils Philippsen <nils@redhat.com> - 1.9.38-1
- restore SELinux context of /etc/localtime (#490323, patch by Daniel Walsh)

* Tue Apr 14 2009 Nils Philippsen <nils@redhat.com> - 1.9.37-1
- pick up updated translations

* Mon Dec 22 2008 Nils Philippsen <nils@redhat.com> - 1.9.36-1
- fix typo in Source0 URL

* Mon Dec 15 2008 Nils Philippsen <nils@redhat.com>
- remove obsolete "dynamic" keyword (#476046)

* Thu Nov 27 2008 Nils Philippsen <nils@redhat.com> - 1.9.35-1
- add source URL

* Wed Nov 26 2008 Nils Philippsen <nils@redhat.com>
- obsolete and conflict with system-config-date < 1.9.35 (docs split)

* Tue Nov 25 2008 Nils Philippsen <nils@redhat.com>
- prune online documentation

* Wed Nov 05 2008 Nils Philippsen <nils@redhat.com> - 1.9.34-1
- avoid map traceback on non-geographic timezones (#467231)

* Thu Oct 30 2008 Nils Philippsen <nils@redhat.com> - 1.9.33-1
- require usermode-gtk instead of usermode

* Tue Jul 01 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.32-1
- fix Arabic timezone translation (#453202, patch by Muayyad Alsadi)

* Mon May 05 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.31-1
- translate underscores to spaces when reading in zone names (#444093, patch by
  Jeremy Katz)

* Tue Apr 08 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.30-1
- pick up updated translations

* Mon Apr 07 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.29-1
- further NTP backend cleanup (#441040)

* Thu Apr 03 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.28-1
- update ntp.conf template
- simplify NTP backend code
- use dynamic keyword for servers (#229217)

* Mon Mar 31 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.27-1
- handle missing UTC information in /etc/adjtime, disable UTC/non-UTC selection
  if hwclock doesn't work (#438124)

* Wed Mar 26 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.26-1
- rename timezones/sr@Latn.po to sr@latin.po (#426591)

* Tue Mar 25 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.25-1
- use hard links to avoid excessive disk space requirements (#438722)

* Tue Mar 18 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.24-1
- pick up updated translations
- enable all languages for online doc translation
- various online doc fixes
- zoom in on click into map (#437767)
- draw label into map for currently selected city

* Tue Mar 04 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.23-1
- handle ntpdate service (#229217, patch by Miroslav Lichvar)
- change all runlevels instead of only 3 and 5

* Tue Feb 05 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.22-1
- keep UTC info in /etc/adjtime, drop ARC support (patch by Bill Nottingham)

* Sat Jan 19 2008 Nils Philippsen <nphilipp@redhat.com>
- add BR: docbook-dtds, scrollkeeper/rarian-compat

* Fri Jan 18 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.21-1
- online help: reorg, make xmllint happy

* Fri Jan 11 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.20-1
- use config-util for userhelper configuration from Fedora 9 on (#428394)

* Thu Jan 10 2008 Nils Philippsen <nphilipp@redhat.com> - 1.9.19-1
- only attempt to use yelp to display online help (as xdg-open does just the
  same), drop requirements on xdg-utils and yelp for now, update error message
  shown if yelp isn't found (#420101)

* Thu Dec 27 2007 Nils Philippsen <nphilipp@redhat.com> - 1.9.18-1
- rename sr@Latn to sr@latin (#426591)

* Thu Nov 22 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.17-1
- some doc changes

* Wed Nov 21 2007 Nils Philippsen <nphilipp@redhat.com>
- migrate documentation to yelp/DocBook XML
- add docs translation rules

* Wed Oct 31 2007 Nils Philippsen <nphilipp@redhat.com>
- mention XEN/virtualization issues if hwclock fails (#357311)

* Tue Oct 30 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.16-1
- use warning dialog, exit gracefully if hwclock fails to allow operation in a
  XEN guest (#357311)

* Tue Oct 23 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.15-1
- cope with comments in /etc/ntp/step-tickers (#333881)

* Mon Oct 15 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.14-1
- avoid traceback when neither xdg-open nor htmlview is found

* Mon Oct 15 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.13-1
- change hicolor-icon-theme requirement to be "uncolored" (without
  "(post)"/"(postun)")
- use full path to call gtk-update-icon-cache
- don't let gtk-update-icon-cache fail scriptlets
- use "make %%{?_smp_mflags}"
- remove "ExclusiveOS: Linux"
- remove obsolete no.po translation file
- use "%%defattr(-,root,root,-)"
- add release tags to changelog versions to appease rpmlint

* Tue Oct 09 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.12-1
- use xdg-open if available
- don't throw exceptions when selecting non-geographic time zones (#293241)
- fix permissions of timeconfig tool (#241737)

* Mon Oct 08 2007 Nils Philippsen <nphilipp@redhat.com>
- add "make diff" ("dif") and "make shortdiff" ("sdif")
- make canvas scroll buttons work (#324941)

* Tue Oct 02 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.11-1
- don't remove notebook pages when acting as a firstboot module (#296711)
- pick up updated translations

* Tue Oct 02 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.10-1
- pick up updated translations

* Sun Sep 16 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.9-1
- pick up updated translations

* Sat Sep 15 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.8-1
- pick up updated translations

* Mon Sep 10 2007 Nils Philippsen <nphilipp@redhat.com>
- make use of force tagging (since mercurial 0.9.4)

* Mon Aug 27 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.7-1
- replace "timezone" by "time zone" where visible (#253428)
- updated translations (#253829)

* Fri Aug 17 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.5-1
- fix python string placeholders in id and ms translations (#250495, #250500)

* Thu Aug 16 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.4-1
- display error message if setting time and date fails (#251818)
- require newt-python from Fedora 8 on (#251362)

* Tue Aug 14 2007 Nils Philippsen <nphilipp@redhat.com>
- use different shortcuts for enabling NTP and editing a server (#252043)

* Mon Aug 13 2007 Nils Philippsen <nphilipp@redhat.com>
- use correct "time zone" term (#251868)
- check hour, minute, second values when changed (#251821)

* Fri Aug 10 2007 Nils Philippsen <nphilipp@redhat.com>
- don't use python2 binary

* Fri Aug 03 2007 Nils Philippsen <nphilipp@redhat.com>
- fix licensing and author blurbs
- tag as GPLv2+

* Tue Jul 31 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.3-1
- fix canvas tooltip

* Mon Jul 30 2007 Nils Philippsen <nphilipp@redhat.com>
- use smoother zoom steps when using the mouse wheel
- hide city label when using the mouse wheel to zoom

* Fri Jul 27 2007 Nils Philippsen <nphilipp@redhat.com>
- use scroll wheel to adjust zoom factor

* Fri Jul 27 2007 Thomas Woerner <twoerner@redhat.com>
- fixed map panning

* Mon Jul 23 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.2-1
- fix python formatting in Japanese translation (#248667, Jens Petersen)
- make "make archive" work with Hg repo

* Wed Jun 27 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.1-1
- fix desktop file category (#245891)

* Wed May 02 2007 Nils Philippsen <nphilipp@redhat.com> 1.9.0-1
- pick up updated translations (#237930)

* Sat Apr 28 2007 Nils Philippsen <nphilipp@redhat.com>
- don't use underscore in default timezone in textmode tool

* Fri Apr 27 2007 Nils Philippsen <nphilipp@redhat.com>
- add scrollbars to timezone canvas (#230690)
- scroll to city selected via treeview
- don't resize window due to excessively long comments of cities

* Wed Apr 25 2007 Nils Philippsen <nphilipp@redhat.com> 1.8.96-1
- handle missing /etc/ntp.conf gracefully (#237777)
- versionize obsoletes
- pick up updated translations

* Tue Apr 24 2007 Nils Philippsen <nphilipp@redhat.com> 1.8.95-1
- move zoom scale to the left of the canvas

* Thu Apr 05 2007 Nils Philippsen <nphilipp@redhat.com> 1.8.94-1
- use underscores instead of spaces in timezone filenames (#235064)

* Mon Mar 26 2007 Nils Philippsen <nphilipp@redhat.com> 1.8.93-1
- explain why system-config-date conflicts with old versions of firstboot

* Mon Mar 26 2007 Nils Philippsen <nphilipp@redhat.com> 1.8.92-1
- use correct modes when installing, to avoid fixing modes when packaging and
  to be able to strip down %%files
- don't ship unneeded regions file

* Thu Mar 22 2007 Nils Philippsen <nphilipp@redhat.com> 1.8.91-1
- update URL

* Tue Mar 20 2007 Nils Philippsen <nphilipp@redhat.com>
- mention that we are upstream
- use preferred buildroot
- use Category: ... System; ... in desktop file
- clean buildroot before installing
- fix licensing blurb in PO files
- require python >= 2.0 instead of python2
- recode spec file to UTF-8
- don't mark ntp.template as %%config

* Mon Mar 19 2007 Nils Philippsen <nphilipp@redhat.com> 1.8.90-1
- add tooltip to zoomed-in canvas to describe panning

* Sun Mar 18 2007 Nils Philippsen <nphilipp@redhat.com>
- display to-be-selected city inside map instead of status bar (#211550)
- remove remaining regions cruft
- make currently selected city non-selectable

* Sat Mar 17 2007 Nils Philippsen <nphilipp@redhat.com>
- implement panning of zoomed timezone map

* Wed Mar 14 2007 Nils Philippsen <nphilipp@redhat.com>
- add zoom slider instead of regions (#211543, #211546)

* Fri Feb 23 2007 Nils Philippsen <nphilipp@redhat.com> 1.8.13-1
- pick up updated translations (#229727)

* Tue Jan 16 2007 Nils Philippsen <nphilipp@redhat.com> 1.8.12-1
- pick up updated translations (#220952)

* Mon Jan 08 2007 Nils Philippsen <nphilipp@redhat.com>
- ask whether the configuration should be revisited on NTP problems (#220952)

* Fri Jan 05 2007 Nils Philippsen <nphilipp@redhat.com>
- don't attempt to show error dialog from signal handler (#220952)

* Fri Dec 15 2006 Nils Philippsen <nphilipp@redhat.com> 1.8.11-1
- provide more info when encountering bad timezone translations (i.e. not split
  into Region,Continent/Location) (#219773)
- pick up updated translations (#216073)

* Wed Dec 13 2006 Nils Philippsen <nphilipp@redhat.com>
- fix keyboard shortcuts in Czech translation (#190355)

* Wed Dec 13 2006 Nils Philippsen <nphilipp@redhat.com> 1.8.10-1
- pick up updated translations (#216073)

* Fri Nov 24 2006 Nils Philippsen <nphilipp@redhat.com> 1.8.9-1
- pick up updated translations (#216073)

* Tue Nov 21 2006 Nils Philippsen <nphilipp@redhat.com>
- revamp timezone potfile generation a bit
- pick up new timezones for translation (#216073)

* Tue Oct 17 2006 Nils Philippsen <nphilipp@redhat.com> 1.8.8-1
- enable Hebrew, Marathi and Urdu translations
- pick up updated translations (#211074)
- add dist tag

* Fri Oct 13 2006 Bill Nottingham <notting@redhat.com> 1.8.7-1
- use valid charsets for translation (#210720)

* Fri Sep 15 2006 Nils Philippsen <nphilipp@redhat.com> 1.8.6-1
- pick up updated strings and translations (#192075, #204441)

* Fri Aug 25 2006 Nils Philippsen <nphilipp@redhat.com> 1.8.5-1
- hide 'Enable NTP Broadcast' checkbutton as more action is needed than a mere
  change in ntp.conf

* Mon Jul 17 2006 Nils Philippsen <nphilipp@redhat.com> 1.8.4-1
- pick up updated translations

* Tue Mar 14 2006 Nils Philippsen <nphilipp@redhat.com> 1.8.3-1
- feed timezone po files from anaconda (#131528, patch by Andrew Martynov)

* Mon Mar 06 2006 Nils Philippsen <nphilipp@redhat.com> 1.8.2-1
- don't write into /tmp
- make synchronizing with time servers configurable (#157485)

* Fri Mar 03 2006 Nils Philippsen <nphilipp@redhat.com> 1.8.1-1
- require hicolor-icon-theme (#182859, #182860)

* Mon Jan 30 2006 Nils Philippsen <nphilipp@redhat.com> 1.8.0-1
- bump minor version
- add requirements for pygtk2-libglade, gnome-python2-canvas (#179215)

* Fri Jan 20 2006 Nils Philippsen <nphilipp@redhat.com> 1.7.99.17-1
- zoom out in TZ map on Escape (#178093)

* Wed Jan 18 2006 Nils Philippsen <nphilipp@redhat.com> 1.7.99.16-1
- don't crash when selecting a timezone (#178086, patch by Chris Lumens)

* Tue Jan 17 2006 Nils Philippsen <nphilipp@redhat.com> 1.7.99.15-1
- fix setting timezone from firstboot (#177779, patch by Chris Lumens)

* Mon Jan 16 2006 Nils Philippsen <nphilipp@redhat.com> 1.7.99.14-1
- put Etc/... timezones into "Non-geographic timezones" (#148025)
- default to already set timezone on startup (#177815)

* Tue Jan 10 2006 Nils Philippsen <nphilipp@redhat.com>
- Add translation string for UTC-relative and other non-geographic timezones

* Mon Jan 09 2006 Chris Lumens <clumens@redhat.com> 1.7.99.13-1
- Rename mainWindow to scdMainWindow to avoid import problems in firstboot.

* Wed Jan 04 2006 Nils Philippsen <nphilipp@redhat.com> 1.7.99.12-1
- show actually chosen region, not just something that's in the vicinity

* Fri Dec 30 2005 Nils Philippsen <nphilipp@redhat.com>
- fix highlighted regions when leaving and entering the timeone map canvas
- make timezone list a treeview
- update timezone po source file

* Thu Dec 15 2005 Jeremy Katz <katzj@redhat.com> - 1.7.99.11-1
- fix timezone map to not be painfully slow

* Wed Dec 14 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.99.10-1
- make TimezoneMap more easily subclassable (Chris Lumens), use uniform
  paren-spacing

* Thu Dec 08 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.99.9-1
- draw frame around highlighted region

* Thu Nov 24 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.99.8-1
- reshow shaded map when reentering map widget from outside
- clear status line when outside region area in zoomed mode

* Thu Nov 24 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.99.7-1
- only select region if pointer is inside region
- replace aa-based shading to avoid aa-related deficiencies of GnomeCanvas
- show shaded border around zoomed in region to zoom out without selecting a
  city

* Wed Nov 23 2005 Nils Philippsen <nphilipp@redhat.com>
- don't let cities get miraculously lost (#173944, patch by Chris Lumens)

* Mon Nov 21 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.99.6-1
- fix zooming problems with enlarged window (#172982)
- apply workaround by Alex Larsson to avoid hanging when clicking on Asia
  region (#172977)
- add Middle America region, make Antarctica regions overlapping

* Thu Nov 10 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.99.5-1
- when choosing a region, shade off the rest of the map when hovering over a
  region

* Wed Nov 09 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.99.4-1
- implement simple timezone zooming

* Fri Oct 21 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.99.3-1
- revamp pot file generation (#171330)

* Fri Oct 14 2005 Nils Philippsen <nphilipp@redhat.com>
- don't use pam_stack (#170623)

* Fri Oct 07 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.99.2-1
- write comment about the ZONE parameter into /etc/sysconfig/clock (#123101)
- handle comments when reading /etc/sysconfig/clock
- consistently use spaces for indentation in timezoneBackend.py

* Thu Sep 22 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.99.1-1
- check whether NTP server is reachable on changes (#135747)

* Tue Aug 09 2005 Nils Philippsen <nphilipp@redhat.com>
- remove workaround causing deprecation warnings for bug that doesn't exist
  anymore (#162840)

* Thu Aug 04 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.99.0-1
- add and edit NTP servers inline in the list
- always display clock left-to-right (#165109)
- try to be smart about restrict lines when changing or deleting hosts
- include *.pyo files (#165097)
- don't remove *.pyc files in %%preun because they're in the file list
- don't include timetool symlink anymore
- don't install firstboot module symlink, this is dealt with in the firstboot
  package for quite a while

* Wed Aug 03 2005 Nils Philippsen <nphilipp@redhat.com>
- implement --help, catch unrecognized options (#164791)

* Fri May 06 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.18-1
- make desktop file translatable (#156792)
- avoid DeprecationWarnings
- use DESTDIR consistently (#156782)

* Tue Apr 19 2005 Matthias Clasen <mclasen@redhat.com> 1.7.17-2
- Silence %%post

* Fri Apr 15 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.17-1
- make more strings translatable (#154873)

* Fri Apr 01 2005 Nils Philippsen <nphilipp@redhat.com> 1.7.16-2
- use True, False instead of gtk.TRUE, gtk.FALSE to avoid deprecation warnings
  (#153037, patch by Colin Charles)

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 1.7.15-2
- Update the GTK+ theme icon cache on (un)install

* Sat Jan 15 2005 Nils Philippsen <nphilipp@redhat.com>
- use current default ntp.conf as template (#132787, #135142)

* Mon Dec 13 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.15-1
- don't lookup names or IP addresses as this may result in hangs (#142583)

* Mon Nov 29 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.14-1
- bump version

* Fri Nov 26 2004 Nils Philippsen <nphilipp@redhat.com>
- don't use duplicate accelerators (#134172, #140241)

* Fri Nov 26 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.13-1
- enable Gujarati and Tamil translations (#140881)

* Mon Nov 22 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.12-1
- remove wrongly encoded character (#140318) and duplicate word from French
  man page

* Wed Sep 29 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.11-1
- avoid GtkDeprecationWarning on gtk.mainquit on new pygtk (#134043)

* Tue Sep 28 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.10-1
- make timezone page contents actually be shown in firstboot

* Tue Sep 28 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.9-1
- enable choosing which notebook page(s) to show (for firstboot, #133748)
- some minor firstboot API changes, conflict with firstboot <= 1.3.26
- some minor UI tweaks
- remove pool.ntp.org from list of NTP server choices as system-config-date
  doesn't handle multi-IP machines really well ATM

* Fri Sep 17 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.8-1
- use pool.ntp.org as first choice of NTP servers (#132787)

* Thu Sep 16 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.7-2
- buildrequire python

* Tue Sep 14 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.7-1
- byte-compile python files
- first shot at something like an interface for firstboot

* Mon Sep 13 2004 Nils Philippsen <nphilipp@redhat.com>
- get widget sensitivity correct on startup (#132431)

* Fri Sep 03 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.5-1
- actually display time zone map (#131641)
- put NTP stuff into own tab to better accommodate firstboot (#131314)
- add accelerators to Date & Time tab

* Fri Aug 27 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.4-1
- handle multiple servers, broadcastclient (#115148),
  local time source (#72110)

* Tue Aug 03 2004 Nils Philippsen <nphilipp@redhat.com> 1.7.3.1-1
- fix Japanese man page (#128766)

* Wed Apr 14 2004 Brent Fox <bfox@redhat.com> 1.7.3-3
- update desktop file (bug #120709)

* Tue Apr  6 2004 Brent Fox <bfox@redhat.com> 1.7.3-2
- fix desktop file icon path (bug #120176)

* Wed Mar 24 2004 Brent Fox <bfox@redhat.com> 1.7.3-1
- just copy over file, don't remove it (bug #119076)

* Fri Mar  5 2004 Brent Fox <bfox@redhat.com> 1.7.2-1
- preserve old restrict lines (bug #72110)

* Tue Feb  3 2004 Brent Fox <bfox@redhat.com> 1.7.1-2
- correct typo in URL in specfile

* Thu Jan  8 2004 Brent Fox <bfox@redhat.com> 1.7.1-1
- apply patch from bug #109803

* Wed Nov 19 2003 Brent Fox <bfox@redhat.com> 1.6.1-1
- rebuild

* Wed Nov 12 2003 Brent Fox <bfox@redhat.com> 1.6.0-1
- rename to system-config-date
- add Obsoletes for redhat-config-date
- adapt to Python2.3

* Mon Nov  3 2003 Brent Fox <bfox@redhat.com> 1.5.27-1
- add flag to allow timezone page to come up first

* Wed Oct 29 2003 Brent Fox <bfox@redhat.com> 1.5.26-1
- add French translation for man page from Frederic.Hornain@GB.BE

* Sun Oct 26 2003 Brent Fox <bfox@redhat.com> 1.5.25-1
- fix some other timezone po file encoding problems

* Sun Oct 26 2003 Brent Fox <bfox@redhat.com> 1.5.24-1
- make sure is.po file is UTF-8 encoded.  (bug #107439) Similar to bug #107033

* Wed Oct 15 2003 Brent Fox <bfox@redhat.com> 1.5.23-1
- UTF8-ify po/timezones/de.po (bug #107033)

* Fri Sep 19 2003 Brent Fox <bfox@redhat.com> 1.5.22-2
- rebuild

* Fri Sep 19 2003 Brent Fox <bfox@redhat.com> 1.5.22-1
- call timeconfig if the GUI cannot be started (bug #104718)

* Thu Sep 11 2003 Brent Fox <bfox@redhat.com> 1.5.21-2
- bump relnum and rebuild

* Thu Sep 11 2003 Brent Fox <bfox@redhat.com> 1.5.21-1
- rebuild with fixed po file encodings (bug #104019)

* Wed Sep 10 2003 Brent Fox <bfox@redhat.com> 1.5.20-1
- add a Requires for newt (bug #104148)

* Fri Aug 29 2003 Brent Fox <bfox@redhat.com> 1.5.19-2
- bump relnum and rebuild

* Fri Aug 29 2003 Brent Fox <bfox@redhat.com> 1.5.19-1
- if timezone in /etc/sysconfig/clock is not in zone.tab, default to America/New_York (bug #101575)

* Thu Aug 14 2003 Brent Fox <bfox@redhat.com> 1.5.18-1
- tag on every build

* Wed Jun 25 2003 Brent Fox <bfox@redhat.com> 1.5.15-2
- bump version number and rebuild

* Wed Jun 25 2003 Brent Fox <bfox@redhat.com> 1.5.15-1
- don't move /usr/share/zoneinfo/UTC into /etc/localtime (#91228)

* Mon Jun 16 2003 Brent Fox <bfox@redhat.com> 1.5.14-2
- bump number and rebuild

* Mon Jun 16 2003 Brent Fox <bfox@redhat.com> 1.5.14-1
- Add a function to get timezone date page (bug #91984)

* Tue May 27 2003 Brent Fox <bfox@redhat.com> 1.5.13-1
- if /var/spool/postfix/etc/localtime exists, copy the new timezone file there (bug #88249)

* Tue May 27 2003 Brent Fox <bfox@redhat.com> 1.5.12-1
- add a header comment to ntpservers file (bug #91619)

* Tue May 27 2003 Brent Fox <bfox@redhat.com> 1.5.11-2
- bump rel num and rebuild

* Thu May 22 2003 Brent Fox <bfox@redhat.com> 1.5.11-1
- check for the existence of hwclock before running (bug #91323)

* Thu May 22 2003 Brent Fox <bfox@redhat.com> 1.5.10-1
- pull zonetab classes out into separate file to fix bug (#90185)

* Tue May 20 2003 Brent Fox <bfox@redhat.com> 1.5.9-11
- copy actual timezone into /etc/localtime instead of making a symlink (bug #91228)

* Fri May 16 2003 Brent Fox <bfox@redhat.com> 1.5.9-10
- when using UTC, make /etc/localtime point to /usr/share/zoneinfo/UTC (bug #89132)

* Fri May 16 2003 Brent Fox <bfox@redhat.com> 1.5.9-9
- Added mnemonics to widgets that didn't have them (bug #91026)
- convert some timezone po files to utf-8 (bug #88461)

* Wed Feb 26 2003 Brent Fox <bfox@redhat.com> 1.5.9-8
- add requires for ntp (bug #85229)

* Fri Feb 21 2003 Brent Fox <bfox@redhat.com> 1.5.9-7
- remove dependency for gnome-python2-canvas, pygtk and ntp (bug #84837)

* Wed Feb 12 2003 Jeremy Katz <katzj@redhat.com> 1.5.9-6
- set codeset so that textmode works (#83518)

* Tue Feb 11 2003 Brent Fox <bfox@redhat.com> 1.5.9-5
- rebuild with latest docs

* Tue Feb 11 2003 Tammy Fox <tfox@redhat.com>
- updated docs

* Tue Feb  4 2003 Brent Fox <bfox@redhat.com> 1.5.9-4
- fall back to IP if we can't resolve it back to a hostname (bug #83463)

* Mon Feb  3 2003 Brent Fox <bfox@redhat.com> 1.5.9-3
- catch bogus ntp server names and raise a dialog

* Mon Feb  3 2003 Brent Fox <bfox@redhat.com> 1.5.9-2
- don't change value of ARC accidentally (bug #82281)

* Thu Jan 30 2003 Brent Fox <bfox@redhat.com> 1.5.9-1
- bump and build

* Wed Jan 29 2003 Brent Fox <bfox@redhat.com> 1.5.8-1
- use the new Red Hat ntp servers

* Thu Jan 16 2003 Brent Fox <bfox@redhat.com> 1.5.7-6
- catch error with no NTP server

* Wed Jan 15 2003 Brent Fox <bfox@redhat.com> 1.5.7-5
- write IPs to the server line instead of domain names (bug #70557)

* Tue Jan 14 2003 Brent Fox <bfox@redhat.com> 1.5.7-4
- list only stratum 2 ntp servers (bug #81629)

* Fri Jan 10 2003 Brent Fox <bfox@redhat.com> 1.5.7-3
- better check on ntp status by looking at initscrip return code
- sent ntp initscript output to /dev/null when calling os.system()

* Thu Jan  9 2003 Brent Fox <bfox@redhat.com> 1.5.7-2
- change to condrestart

* Fri Jan  3 2003 Brent Fox <bfox@redhat.com> 1.5.7-1
- create a TUI to replace timeconfig
- obsolete timeconfig

* Thu Jan  2 2003 Brent Fox <bfox@redhat.com> 1.5.6-3
- write an ipaddress for the restrict line (bug #80593)

* Mon Dec 23 2002 Brent Fox <bfox@redhat.com> 1.5.6-2
- handle missing ntpservers file
- don't pass in parent, it breaks firstboot
- handle busted ntp initscript

* Fri Dec 13 2002 Brent Fox <bfox@redhat.com> 1.5.5-2
- Print an error message if run from the console

* Fri Nov 15 2002 Brent Fox <bfox@redhat.com> 1.5.5-1
- Handle empty server lines in /etc/ntp.conf

* Tue Nov 12 2002 Brent Fox <bfox@redhat.com> 1.5.4-2
- Rebuild with latest translations

* Wed Oct 30 2002 Brent Fox <bfox@redhat.com>
- Add a build requires for python-tools

* Fri Oct 25 2002 Brent Fox <bfox@redhat.com> 1.5.4-1
- Write out an appropriate restrict line to /etc/ntp.conf
- Fixes bug 70557

* Tue Oct 22 2002 Brent Fox <bfox@redhat.com> 1.5.3-1
- Apply patch from katzj to fix bug 76313
- Fix bug 72149 correctly this time (hopefully)

* Mon Oct 14 2002 Brent Fox <bfox@redhat.com> 1.5.2-12
- Move ntpservers file into /etc/ntp.  Fixes bug 74339

* Thu Oct 10 2002 Brent Fox <bfox@redhat.com> 1.5.2-11
- Fix bug 72149.  Always apply timezone changes
- Fix bug 73498.  Apply UTC changes properly

* Tue Sep 03 2002 Brent Fox <bfox@redhat.com> 1.5.2-10
- convert desktop file to UTF8
- pull in latest translations

* Fri Aug 30 2002 Brent Fox <bfox@redhat.com> 1.5.2-9
- run chkconfig on starting/stopping ntpd

* Thu Aug 29 2002 Brent Fox <bfox@redhat.com> 1.5.2-8
- set the flag to close parent on non-NTP setups
- create an updateSpinButton function

* Tue Aug 27 2002 Brent Fox <bfox@redhat.com> 1.5.2-7
- Retrieve the only the first NTP server if there's more than one
- Only modify the first server entry if there's more than one

* Tue Aug 27 2002 Brent Fox <bfox@redhat.com> 1.5.2-6
- Handle the case of having no server line in ntp.conf

* Mon Aug 26 2002 Brent Fox <bfox@redhat.com> 1.5.2-5
- Raise error dialogs if NTP servers can't be contacted

* Wed Aug 21 2002 Brent Fox <bfox@redhat.com> 1.5.2-4
- pull translation domains from rhpl

* Wed Aug 21 2002 Brent Fox <bfox@redhat.com> 1.5.2-3
- Fix timezone selection bug

* Mon Aug 19 2002 Brent Fox <bfox@redhat.com> 1.5.2-2
- Convert desktop file to UTF-8

* Mon Aug 19 2002 Brent Fox <bfox@redhat.com> 1.5.2-1
- Limit ping timeout to 5 seconds.  We need a better solution for this in the future

* Tue Aug 13 2002 Brent Fox <bfox@redhat.com> 1.5.1-2
- Make spin buttons keyboard sensitive.  Fixes bug 68967

* Mon Aug 12 2002 Tammy Fox <tfox@redhat.com> 1.5.1-1
- replace System with SystemSetup in desktop file categories

* Tue Aug 06 2002 Brent Fox <bfox@redhat.com> 1.5-2
- use template ntp.conf file if the original has been removed for some reason

* Mon Aug 05 2002 Brent Fox <bfox@redhat.com> 1.5-1
- Fix translations for timezone list

* Fri Aug 02 2002 Brent Fox <bfox@redhat.com> 1.4-8
- Use new pam timestamp rules

* Wed Jul 31 2002 Brent Fox <bfox@redhat.com>1.4-7
- Put an end-of-line in /etc/ntp/step-tickers

* Thu Jul 25 2002 Brent Fox <bfox@redhat.com> 1.4-6
- Default to New York if the timezone in /etc/sysconfig/clock is bogus

* Wed Jul 24 2002 Brent Fox <bfox@redhat.com> 1.4-5
- Fixed console file bad link

* Tue Jul 23 2002 Tammy Fox <tfox@redhat.com> 1.4-4
- Change desktop file name (bug #69470)
- Spec file fixes

* Thu Jul 18 2002 Brent Fox <bfox@redhat.com> 1.4-3
- Update for pygtk2 API change

* Wed Jul 17 2002 Brent Fox <bfox@redhat.com> 1.4-2
- Fix padding problem

* Fri Jul 12 2002 Tammy Fox <tfox@redhat.com> 1.4-1
- Updated docs for gtk2 interface
- Add note about security level and ntpd (bug #68039)
- Move desktop file to /usr/share/applications only

* Thu Jul 11 2002 Brent Fox <bfox@redhat.com> 1.3-4
- Remove some lingering references to dateconfig
- Create symbolic link from dateconfig to redhat-config-date

* Wed Jul 10 2002 Brent Fox <bfox@redhat.com> 1.3-1
- Rename dateconfig to redhat-config-date
- Check to see if we can ping ntp server before starting ntpd

* Tue Jul 9 2002 Brent Fox <bfox@redhat.com> 1.2-1
- Pull out ntp servers into a separate file
- Write /etc/ntp/step-tickers file

* Mon Jul 1 2002 Brent Fox <bfox@redhat.com> 1.1-3
- If an NTP server is already specified, add it to the combo list

* Fri Jun 28 2002 Brent Fox <bfox@redhat.com> 1.1-2
- Changed spacing of buttons on bottom of the window

* Thu Jun 27 2002 Tammy Fox <tfox@redhat.com> 1.1-2
- Added border widths to clean up interface
- Hooked up help
- Removed Apply button

* Thu Jun 27 2002 Brent Fox <bfox@redhat.com> 1.1-1
- Updated pot file and respective po files

* Sat Jun 22 2002 Brent Fox <bfox@redhat.com> 1.0.3-1
- Fixed bug 66655
- Fixed problem with selecting the current timezone in timezone_gui

* Mon Jun 17 2002 Brent Fox <bfox@redhat.com> 1.0.2-1
- Reenable the icon

* Thu May 30 2002 Brent Fox <bfox@redhat.com> 1.0.1-5
- Fixed translation bug

* Thu May 30 2002 Brent Fox <bfox@redhat.com> 1.0.1-4
- Removed Requires for pygnome

* Mon May 20 2002 Brent Fox <bfox@redhat.com> 1.0.1-3
- Pulled in documentation bugfix for bug #65228

* Mon May 13 2002 Brent Fox <bfox@redhat.com>
- Added Swedish translations to desktop file from menthos@menthos.com

* Thu May 2 2002 Brent Fox <bfox@redhat.com> 1.0.1-2
- Update for timezone translations

* Mon Apr 15 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.0.1-1
- Update for translations

* Mon Feb 25 2002 Brent Fox <bfox@redhat.com>
- Bump version to 1.0 

* Tue Feb 12 2002 Brent Fox <bfox@redhat.com>
- Finished port to Python2.2/GTK2
- Handle starting ntpd more gracefully
- Made variable naming more consistent

* Tue Jan 22 2002 Brent Fox <bfox@redhat.com>
- Replaced C code for timezone map with Python from anaconda
- Remove timezonemapmodule from /usr/lib/dateconfig

* Thu Oct 18 2001 Brent Fox <bfox@redhat.com>
- Put timezonemapmodule in /usr/lib/dateconfig

* Thu Aug 30 2001 Trond Eivind Glomsrød <teg@redhat.com> 0.7.4-6
- Fix some character sets for translations (#52851)
- dateconfig.png isn't a config file, mark the config files as noreplace

* Mon Aug 27 2001 Tammy Fox <tfox@redhat.com>
- Updated docs for UTC button

* Thu Aug 16 2001 Brent Fox <bfox@redhat.com>
- Fix sizing for non-US languages

* Mon Aug 6 2001 Brent Fox <bfox@redhat.com>
- added redhat-config-time and redhat-config-date scripts

* Fri Aug 3 2001 Brent Fox <bfox@redhat.com>
- created an icon 
- fixed install process to install icon and drop a file in /etc/X11/sysconfig

* Fri Aug  3 2001 Preston Brown <pbrown@redhat.com>
- set hardware clock as well.

* Fri Jul 27 2001 Yukihiro Nakai <ynakai@redhat.com>
- Add Japanese translation.

* Fri Jul 20 2001 Tammy Fox <tfox@redhat.com>
- added i18n stuff
* Wed Jul 04 2001 Karsten Hopp <karsten@redhat.de>
- fix install-path (INSTROOT)
* Wed Jun 27 2001 Tammy Fox <tfox@redhat.com>
- added help and help button
* Sun Jun 24 2001 Brent Fox <bfox@redhat.com>
- got starting and stopping of ntpd working
- enabled detection of whether ntpd is currently running 
- added msf to author list
* Thu Jun 21 2001 Brent Fox <bfox@redhat.com>
- fixed problem with system path in timezone_gui.py
* Wed Jun 13 2001 Tammy Fox <tfox@redhat.com>
- improved man page
* Tue Jun 12 2001 Tammy Fox <tfox@redhat.com>
- added console access, fixed Makefile and spec file
* Mon Jun 11 2001 Brent Fox <bfox@redhat.com>
- added ntp section and timezone section
* Sun Jan 28 2001 Brent Fox <bfox@redhat.com>
- initial coding and packaging

