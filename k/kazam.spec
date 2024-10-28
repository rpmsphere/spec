Name:           kazam
Version:        1.5.7
Release:        1
Summary:        A screencasting program created with design in mind
License:        GPLv3+ and LGPLv3+
Group:          Video/Utilities
# https://launchpad.net/kazam
URL:            https://github.com/henrywoo/kazam
Source0:        https://github.com/henrywoo/kazam/archive/v%{version}/%{name}-%{version}.tar.gz
#Patch1:         kazam-1.5.3-configparser_api_changes_new.patch
#Patch4:         kazam-1.5.3-fix-GtkIconSize-kazam-ui.patch
Patch6:         kazam-1.5.3-gtk-warning-parent-on-widget-with-parent.patch
# Upstream
#
# Mageia
Patch51:        0001-Desktop-file-drop-unity.patch
Patch53:        0001-Do-not-use-hiq-python.patch
Patch54:        0001-Build-desktop-application.patch

BuildRequires:  intltool
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  desktop-file-utils
Requires:       python3-cairo
Requires:       python3-xlib
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-pyxdg
Requires:       python3-distro
Requires:       libgudev
Requires:       gstreamer1-plugins-base
Requires:       libappindicator-gtk3
Requires:       keybinder
BuildArch:      noarch

%description
Kazam is a simple screen recording program that will capture the content of
your screen and record a video file that can be played by any video player
that supports VP8/WebM video format.

Optionally you can record sound from any sound input device that is supported
and visible by PulseAudio.

%prep
%autosetup -p1
sed -i s,"DISTRO = '.*'","DISTRO = '%{_vendor}'",g kazam/version.py
sed -i s,"RELEASE = '.*'","RELEASE = '%{product_version}'",g kazam/version.py

%build
%py3_build

%install
%{__python3} setup.py install --root=%{buildroot}
#%%py3_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README.rst
%license COPYING*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/gnome/scalable/apps/%{name}*.svg
%{_datadir}/icons/hicolor/*/*/%{name}*.png
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Oct 1 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.7
- Rebuilt for Fedora after Sérgio Basto
* Sat Aug 22 2020 Manuel Fombuena <fombuena@outlook.com> - 1.5.3-11.1
- Rebuild version 1.5.3 for Python 3.8
- Fix some more PyGIWarning
- Fix perf_counter (ported from Debian patch)
- Fix GtkIconSize in kazam.ui
- Fix fail to detect OS
- Fix Gtk-WARNING 'Can't set a parent on widget which has a parent'
* Wed Feb 22 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.5
- Rebuilt for Fedora
* Mon Sep 12 2016 daviddavid <daviddavid> 1.4.5-4.mga6
+ Revision: 1051617
- add patch from debian to fix a configparser api changes (fixes mga#19334)
- add another patch to fix some PyGIWarning specifying first a version
* Fri Feb 19 2016 umeabot <umeabot> 1.4.5-3.mga6
+ Revision: 970719
- Mageia 6 Mass Rebuild
* Thu Oct 08 2015 daviddavid <daviddavid> 1.4.5-2.mga6
+ Revision: 887773
- rebuild for python 3.5
- use new python3 macros
* Sat Jul 11 2015 akien <akien> 1.4.5-1.mga6
+ Revision: 853311
- Also drop keywords from desktop file as some translations are invalid
- Drop Unity-specific stuff from desktop file
- imported package kazam
