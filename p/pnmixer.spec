Name:           pnmixer
Version:        0.7.2
Release:        3
Summary:        Lightweight mixer applet
Group:          Sound/Utilities
License:        GPLv3
URL:            https://github.com/nicklan/pnmixer/wiki
Source0:        https://github.com/nicklan/pnmixer/archive/v%{version}%{?prel:-%prel}/%{name}-%{version}.tar.gz
Patch0:         0001-Try-to-use-pavucontrol-also-as-a-mixer-app-if-Volume.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig(alsa)
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gtk3-devel
BuildRequires:  pkgconfig(libnotify)
Recommends:     pavucontrol

%description
PNMixer is system tray sound mixer. Currently it supports ALSA and PulseAudio.
It is written in C, depends only on GTK+, and does not require Gnome.

PNMixer is a fork of OBMixer with a number of additions. These include:
* Volume adjustment with the scroll wheel
* Textual display of volume level in popup window
* Continuous volume adjustment when dragging the slider (not just when you let
  go)
* Use system icon theme for icons and use mute/low/medium/high volume icons
* Configurable middle click action (default is mute/unmute)
* Preferences for:
  * volume text display
  * volume text position
  * icon theme
  * amount to adjust per scroll
  * middle click action

%prep
%autosetup -p1 -S git_am

%build
%cmake
%cmake_build

%install
%cmake_install

# minor fixes for the desktop file
desktop-file-install \
    --dir=%{buildroot}%{_sysconfdir}/xdg/autostart \
    --add-category="Audio" \
        *-linux-build/data/desktop/pnmixer.desktop

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README.md
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Mar 15 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.2
- Rebuilt for Fedora
* Fri Feb 14 2020 daviddavid <daviddavid> 0.7.2-3.mga8
+ Revision: 1516888
- use new cmake macros
+ umeabot <umeabot>
- Mageia 8 Mass Rebuild
* Sun Sep 23 2018 umeabot <umeabot> 0.7.2-2.mga7
+ Revision: 1300331
- Mageia 7 Mass Rebuild
* Sat Oct 07 2017 wally <wally> 0.7.2-1.mga7
+ Revision: 1169836
- new version 0.7.2
* Fri Jul 21 2017 wally <wally> 0.7.1-1.mga7
+ Revision: 1125862
- new version 0.7.1
* Tue Feb 28 2017 wally <wally> 0.7-2.mga6
+ Revision: 1088171
- recommend pavucontrol
- add patch to search and prefer pavucontrol if no 'Volume Control Command' is defined in preferences (mga#20369)
* Sat Jan 28 2017 wally <wally> 0.7-1.mga6
+ Revision: 1083867
- new version 0.7
- install also app menu entry
- enable autostart also on MATE
* Fri Feb 12 2016 umeabot <umeabot> 0.6.1-2.mga6
+ Revision: 958544
- Mageia 6 Mass Rebuild
* Mon Oct 05 2015 wally <wally> 0.6.1-1.mga6
+ Revision: 886488
- new version 0.6.1
- switch to gtk3
* Sat Aug 22 2015 wally <wally> 0.6-0.rc2.1.mga6
+ Revision: 868175
- new version 0.6 rc2
* Sat Jul 11 2015 wally <wally> 0.6-0.git20150705.1.mga6
+ Revision: 853291
- latest git snapshot
* Sun Jun 21 2015 wally <wally> 0.6-0.git20150216.1.mga6
+ Revision: 837690
- new git snapshot
* Wed Oct 15 2014 umeabot <umeabot> 0.6-0.git20141005.2.mga5
+ Revision: 742897
- Second Mageia 5 Mass Rebuild
* Sun Oct 05 2014 wally <wally> 0.6-0.git20141005.1.mga5
+ Revision: 736999
- update to latest git snapshot
- rediff automake patch
* Tue Sep 16 2014 umeabot <umeabot> 0.6-0.git20140731.3.mga5
+ Revision: 687696
- Mageia 5 Mass Rebuild
* Fri Aug 01 2014 wally <wally> 0.6-0.git20140731.2.mga5
+ Revision: 658853
- enable notification support
* Thu Jul 31 2014 wally <wally> 0.6-0.git20140731.1.mga5
+ Revision: 658757
- use latest git snapshot
- drop unneeded patches
* Mon Jan 06 2014 wally <wally> 0.5.1-1.mga5
+ Revision: 565074
- add patch to fix build with new automake
- imported package pnmixer
* Sun Sep 01 2013 Mat Booth <fedora@matbooth.co.uk> - 0.5.1-7
- Add missing BRs, rhbz #992808
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Sat Mar 10 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-3
- Build with $RPM_OPT_FLAGS (#800642)
- Minor fixes for desktop file
* Sun Mar 04 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-2
- Fix launcher icon
- Don't install a launcher in the application menu
* Sat Mar 03 2012 Christoph Wickert <cwickert@fedoraproject.org> - 0.5.1-1
- Update to 0.5.1
- Only autostart in LXDE or Xfce
* Fri Dec 09 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.5-1
- Update to 0.5 (#729741)
- Drop on_mixer patch (similar change included)
* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.3-2
- Rebuild for new libpng
* Wed Jun 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.3-1
- Update to 0.3
- Change license tag to GPLv3 (only)
- Patch default mouse scroll step to 5
* Fri Jun 03 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.2-1
- Initial package based on obmixer package
