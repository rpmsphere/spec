Name:           ciosk-desktop
Version:        20171016
Release:        1
Summary:        Desktop for Kiosk
Group:		User Interface/Desktops
License:        MIT, CC BY-SA 3.0
URL:            https://github.com/bluebat/ciosk-desktop
Source0:        https://github.com/bluebat/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:	noarch
#Requires:       chinese-opendesktop-release
Requires:       xprintidle
Requires:       trayclock
#Requires:       flash-player-ppapi
#Requires:       intel-graphics-update-tool
Requires:       joe
Requires:       util-linux-user
Requires:       glibc-all-langpacks
Requires:       sddm
Requires:       xorg-x11-server-utils
Requires:       pulseaudio-module-x11
Requires:       openbox
Requires:       network-manager-applet
Requires:       volumeicon
Requires:       feh
Requires:       system-switch-displaymanager
Requires:       chromium
Requires:       stalonetray
Requires:       alltray
Requires:       yad
Requires:       scrot
Requires:       NetworkManager-tui
Requires:       NetworkManager-wifi
Requires:       wireless-tools
#Requires:       *-firmware
Requires:       xorg-x11-drv-ati
Requires:       xorg-x11-drv-evdev
Requires:       xorg-x11-drv-fbdev
Requires:       xorg-x11-drv-intel
Requires:       xorg-x11-drv-libinput
Requires:       xorg-x11-drv-nouveau
Requires:       xorg-x11-drv-vesa
Requires:       adobe-source-code-pro-fonts
Requires:       adobe-source-han-sans-cn-fonts
Requires:       adobe-source-han-sans-tw-fonts
Requires:       naver-nanum-gothic-fonts
Requires:       thai-scalable-waree-fonts
Requires:       lohit-devanagari-fonts
Requires:       lohit-bengali-fonts
Requires:       lohit-tamil-fonts
Requires:       lklug-fonts
Requires:       senamirmir-washra-hiwua-fonts
Requires:       layla-digital-fonts
Requires:       tibetan-machine-uni-fonts
Requires:       sil-padauk-book-fonts
Requires:       ibus-cangjie-engine-cangjie
Requires:       ibus-cangjie-engine-quick
Requires:       ibus-chewing
Requires:       ibus-libpinyin
Requires:       ibus-hangul
Requires:       ibus-kkc
Requires:       ibus-unikey
Requires:       ibus-m17n

%description
Including an X session, a SDDM theme, flag icons and some configuration files.

%prep
%setup -q

%build

%install
%make_install

%files
%doc README.md
%{_sbindir}/ciosk-desktop
%{_sysconfdir}/X11/xorg.conf.d/80-ciosk.conf
%{_sysconfdir}/rc.d/rc.local
%config(noreplace) %{_sysconfdir}/ciosk-desktop.conf

%{_datadir}/xsessions/ciosk.desktop
%{_bindir}/ciosk-session
%{_datadir}/ciosk-session
%config(noreplace) %{_sysconfdir}/ciosk-session.conf

%license LICENSE
%dir %{_datadir}/sddm/themes/ciosk
%{_datadir}/sddm/themes/ciosk/README.md
%{_datadir}/sddm/themes/ciosk/metadata.desktop
%{_datadir}/sddm/themes/ciosk/data
%{_datadir}/sddm/themes/ciosk/*.qml
%{_datadir}/sddm/themes/ciosk/*.png
%config(noreplace) %{_datadir}/sddm/themes/ciosk/theme.conf

%license LICENSE.CC-BY-SA
%{_datadir}/free-country-flags

%changelog
* Mon Oct 16 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 20171016
- Initial package
