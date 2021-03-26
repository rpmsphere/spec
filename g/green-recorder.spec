Name: green-recorder
Version: 3.2.3
Release: 1
Summary: A simple yet functional desktop recorder for Linux systems
License: GPLv3
Group: Video
URL: https://github.com/damianmoore/%name
BuildArch: noarch
Source: %name-master.zip
Requires: python3-gobject
Requires: python3-pydbus
Requires: python3-urllib3
Requires: ImageMagick
Requires: xdg-utils

%description
A simple desktop recorder for Linux systems. Supports both Xorg
server and Wayland (GNOME).

The following formats are currently supported: mkv, avi, mp4, wmv,
gif and nut (And only WebM for Wayland's GNOME session). You can
stop the recording process easily by right-clicking the icon and
choosing "Stop Record". Or middle-clicking the recording icon in
the notifications area (but doesn't work on all interfaces).

You can choose the audio input source you want from the list. You
can also set the default values you want from the preferences
window. And a lot more.

%prep
%setup -q -n %{name}-master

%build
%py3_build

%install
%py3_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%python3_sitelib/*
%_datadir/%name
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png

%changelog
* Thu Aug 27 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.3
- Rebuild for Fedora
* Thu Mar 12 2019 secureworkstation - 3.2.2
- Rebase to damianmoore's GitHub branch which builds with Python 3