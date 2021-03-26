#
# spec file for package moblin-menus (Version 0.1.6)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           moblin-menus
Summary:        Configuration and data files for the desktop menus
Group:          System/GUI/Other
Version:        0.2.0
Release:        2.1
License:        GPL v2 only
Url:            http://www.moblin.org
Source0:        %{name}-%{version}.tar.bz2
Source1:        moblin-YaST.menu
Patch1:         suse-menus.patch
Provides:       gnome-menus-branding
BuildRequires:  intltool
BuildRequires:  gettext
Provides:       desktop-data

%description
Configuration and data files for the desktop menus in Moblin



%prep
%setup -q -n %{name}-%{version}
#%patch1 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%makeinstall
%find_lang moblin-menus  || echo -n >> moblin-menus.lang
mkdir -p %{buildroot}/%{_datadir}/doc/%{name}-%{version}
for f in `ls %{buildroot}/%{_datadir}/doc/`; do
  if [ -f %{buildroot}/%{_datadir}/doc/$f ]; then
    mv %{buildroot}/%{_datadir}/doc/$f %{buildroot}/%{_datadir}/doc/%{name}-%{version}
  fi
done
mv  %{buildroot}/%{_sysconfdir}/xdg/menus/applications.menu %{buildroot}/%{_sysconfdir}/xdg/menus/moblin-applications.menu
install -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/xdg/menus
#rm %{buildroot}/%{_sysconfdir}/xdg/menus/preferences.menu
#rm %{buildroot}/%{_sysconfdir}/xdg/menus/settings.menu

%clean
rm -rf %{buildroot}

%files -f moblin-menus.lang
%defattr(-,root,root,-)
%dir %{_sysconfdir}/xdg/menus
%{_sysconfdir}/xdg/menus/*-merged
%{_sysconfdir}/xdg/menus/*.menu
#%exclude %{_sysconfdir}/xdg/menus/preferences.menu
#%exclude %{_sysconfdir}/xdg/menus/settings.menu
%dir %{_datadir}/desktop-directories
%{_datadir}/desktop-directories/*.directory

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Thu Oct 14 2010 awafaa@opensuse.org
- Disable suse-menus.patch to enable all apps to be seen in menu
* Mon Jul 19 2010 awafaa@opensuse.org
- Update to version 0.2.0
* Fri Mar 26 2010 awafaa@opensuse.org
- Remove Provides: desktop-data-SLED
* Wed Nov 18 2009 glin@novell.com
- Exclude iagno.desktop. bnc#533202
* Thu Nov 12 2009 glin@novell.com
- Update to version 0.1.6
- Respin suse-menus.patch
* Wed Nov  4 2009 glin@novell.com
- Exclude backup-manager-settings.desktop and
  backup-manager-restore.desktop in System. bnc#552395
- Exclude bluetooth-analyzer.desktop in Other. bnc#542529
* Wed Oct 28 2009 glin@novell.com
- Exclude keyboard.desktop. bnc#549815
* Wed Oct 21 2009 glin@novell.com
- Excluded online_update.desktop, online_update_configuration.desktop,
  and lan.desktop in moblin-YaST.menu. bnc#547873
- Excluded YaST2-remote in application list. bnc#547874
- Excluded customer_center.desktop in moblin-YaST.menu. bnc#547877
- Excluded sound.desktop in moblin-YaST.menu since all sound modules
  are built-in, yast-sound becomes useless.
* Tue Oct 13 2009 glin@novell.com
- Respin suse-menus.patch to show f-spot in Graphics.
  bnc#542799 comment #2
* Tue Oct  6 2009 glin@novell.com
- Respin suse-menus.patch per bnc#542799
* Fri Sep 18 2009 glin@novell.com
- Exclude "Graphics" in "Office" to fix bnc#539861
* Wed Sep 16 2009 glin@novell.com
- Added anjal to Office to fix bnc#538940
* Thu Sep 10 2009 abockover@novell.com
- Provide gnome-menus-branding so we don't have to continue to
  hack around the gnome-menus-branding-SLED settings menu
- Respin suse-menus.patch to remove patches to settings.menu, since
  we exclude it altogether
- Added mmeeks's moblin-YaST.menu to /etc/xdg/menus (bnc#536216)
* Thu Sep 10 2009 glin@novell.com
- Excluded more entries in System/settings.menu to avoid duplicated
  System entries in Application tab.
* Thu Sep 10 2009 glin@novell.com
- Added tsclient to Accessories.
* Wed Sep  9 2009 abockover@novell.com
- More menu cleanup, removed java, added backup manager again
* Wed Aug 19 2009 abockover@novell.com
- Fix various menu issues
* Mon Aug 10 2009 glin@novell.com
- Respin moblin-menus-suse2.patch to enable backup-manager-settings.desktop and backup-manager-restore.desktop.
* Mon Jul 20 2009 jlee@novell.com
- Modified moblin-applications and add settings by include/exclude tag
  to /etc/skel for Novell applications menu.
* Thu Jul 16 2009 michael.meeks@novell.com
- disable qt4 settings in the .menus file as prototype of
  what to do here.
* Fri Jun  5 2009 Andrew Wafaa <awafaa@opensuse.org> 0.1.2
- Remove prefernces.menu and settings.menu and rename applications.menu
- to moblin-applications.menu to prevent file conflicts
* Wed Apr  1 2009 Damien Lespiau <damien.lespiau@intel.com> 0.1.2
- Use a more gnome-ish layout in applications and settings
- disable legacy directories
* Sat Jan 10 2009 Rusty Lynch <rusty.lynch@intel.com> 0.1.1
- Updating to version 0.1.1, which fixes a conflict with gnome-menus 2.4.2
* Thu Jan  8 2009 Rusty Lynch <rusty.lynch@intel.com> 0.1.0
- Initial packaging for v0.1.0
