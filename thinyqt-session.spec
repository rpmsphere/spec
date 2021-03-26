Name:           thinyqt-session
Version:        0.4
Release:        1
Summary:        A Thin and Tiny Session for X with Qt
Group:		User Interface/Desktops
License:        CC0
URL:            https://github.com/bluebat/thinyqt-session
Source0:        %{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:       notification-daemon
Requires:       pulseaudio-module-x11
Requires:       eggwm
Requires:       quickterminal
Requires:       nm-tray
Requires:       NetworkManager-wifi
#Requires:       blueman
#Requires:       NetworkManager-bluetooth
Requires:       xsettingsd
Requires:       imsettings-qt
Requires:       gsettings-qt
Requires:       kmix
Requires:       pavucontrol-qt
Requires:       hdepanel
#Requires:       system-config-date
Requires:       ntpdate
Requires:       desktop-backgrounds-compat
Requires:       dsbbg
Requires:       feh
Requires:       xorg-x11-drivers
Requires:       memtray
Requires:       qshutdown
Requires:       qscreenshot
Requires:       qview
Requires:       rpmsphere-release
Recommends:     joe
Recommends:     wget
Recommends:     sayonara
Recommends:     qtfm
Recommends:     qutebrowser
Recommends:     extcalc
#Recommends:     system-config-printer
Recommends:     qrandr
Recommends:     qtpdf
Recommends:     qedit
Recommends:     qtcam
Recommends:     qftp-x11
Recommends:     qutim
Recommends:     kdocker
Recommends:     xinput_calibrator
Recommends:     upower

%description
ThinyQt is a simple X session, using eggwm as Window Manager with some
Qt-based packages and supporting $HOME/.xprofile.

%prep
%setup -q

%build

%install
make install DESTDIR=%{buildroot}

%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/xsessions/thinyqt.desktop
%{_datadir}/%{name}

%changelog
* Thu May 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Initial package
