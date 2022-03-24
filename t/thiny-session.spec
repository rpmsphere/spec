Name:           thiny-session
Version:        0.7.6
Release:        1
Summary:        A Thin and Tiny Session for X
Group:		User Interface/Desktops
License:        CC0
URL:            https://github.com/bluebat/thiny-session
Source0:        %{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:       notification-daemon
#Requires:       pulseaudio-module-x11
Requires:       metacity
Requires:       greybird-metacity-theme
Requires:       guake
Requires:       network-manager-applet
Requires:       NetworkManager-wifi
#Requires:       blueman
#Requires:       NetworkManager-bluetooth
Requires:       xsettingsd
Requires:       imsettings-gsettings
Requires:       volumeicon
Requires:       pavucontrol
Requires:       tint2
#Requires:       system-config-date
Requires:       /usr/sbin/ntpdate
Requires:       desktop-backgrounds-compat
Requires:       nitrogen
Requires:       xorg-x11-drivers
Requires:       alltray
Requires:       gshutdown
Requires:       sxhkd
Requires:       scrot
Requires:       viewnior
Recommends:     joe
Recommends:     wget
Recommends:     gst123
Recommends:     spacefm
Recommends:     midori
Recommends:     galculator
Recommends:     system-config-printer
Recommends:     arandr
Recommends:     mupdf
Recommends:     leafpad
Recommends:     camorama
Recommends:     xinput_calibrator
Recommends:     gftp
Recommends:     upower

%description
Thiny is a simple X session, using metacity as Window Manager with some
GTK-based packages and supporting $HOME/.xprofile.

%prep
%setup -q

%build

%install
make install DESTDIR=%{buildroot}

%post
sed -i 's|xorg|display-manager|' /usr/lib/systemd/system/sxhkd.service

%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/xsessions/thiny.desktop
%{_datadir}/%{name}

%changelog
* Sun Dec 5 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.6
- Update package
* Sun Aug 10 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Initial package
