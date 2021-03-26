Name:           fskbsetting
Version:        0.3.4
Release:        12.1
License:        GPL-3.0
Summary:        GUI Front-end for setxkbmap Command
URL:            https://sourceforge.net/projects/fskbsetting
Group:          System/X11/Utilities
Source0:        https://sourceforge.net/projects/fskbsetting/files/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  wxGTK3-devel
Requires: xorg-x11-xkb-utils

%description
fsKBSetting is GUI front-end for setxkbmap command.

%prep
%setup -q

%build
autoreconf --force --install --symlink
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README* TRANSLATORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png

%changelog
* Mon Feb 22 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.4
- Rebuild for Fedora
* Sun Feb 14 2016 umeabot <umeabot> 0.3.4-2.mga6
+ Revision: 960202
- Mageia 6 Mass Rebuild
* Fri Nov 06 2015 alexl <alexl> 0.3.4-1.mga6
+ Revision: 898082
- version 0.3.4   
- del upstreamed stuff
- update license tag  
- new url
- hicolor-icon-theme, x11-data-xkbdata are requires
- s/makeinstall_std/make_install/
* Wed Oct 15 2014 umeabot <umeabot> 0.3.2-5.mga5
+ Revision: 743781
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.3.2-4.mga5
+ Revision: 679367
- Mageia 5 Mass Rebuild
* Mon Aug 04 2014 alexl <alexl> 0.3.2-3.mga5
+ Revision: 659606
- added setxkbmap to requires
- created autostart dir if dir not exists (added create-autostart-dir.patch)
- fixed condition if file exists (added if-file-exists.patch)
* Sun Aug 03 2014 alexl <alexl> 0.3.2-2.mga5
+ Revision: 659326
- translated desktop file
- added rename.patch, desktop.patch, hotkeys.patch
- added fskbsetting.png
- changed sample.xpm   
* Sun Apr 06 2014 alexl <alexl> 0.3.2-1.mga5
+ Revision: 612274
- imported package fskbsetting
* Thu Mar  8 2012 lazy.kent@opensuse.org
- Use defines for wxWidgets.
- Install icon to icons/hicolor (build requires
  hicolor-icon-theme).
- Added icon_theme_cache_post/un macros.
- Use makeinstall macro.
- Removed check for unsupported openSUSE versions.
* Mon Nov  7 2011 lazy.kent@opensuse.org
- Corrected License tag.
- Use full URL as a source.
- spec clean up.
* Sat Jan 22 2011 lazy.kent@opensuse.org
- build requires wxWidgets-devel for openSUSE 11.4
- autostart patch from Mandriva project
- added COPYING
* Sat Aug 21 2010 lazy.kent.suse@gmail.com
- added "Menu" hotkey
* Mon Jul 12 2010 lazy.kent.suse@gmail.com
- initial package created - 0.3
- corrected desktop-file
- added icon
