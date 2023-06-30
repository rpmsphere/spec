Name:           deepin-music-player
Summary:        Deepin Music Player
License:        GPL-3.0+
Group:          Productivity/Multimedia/Sound/Players
Version:        2.0
Release:        6.1
BuildArch:      noarch
URL:            https://packages.linuxdeepin.com/deepin/pool/main/d/deepin-music-player/
Source0:        %{name}-%{version}.tar.gz
Source1:        deepin-music-player.desktop
Source2:        deepin-music-player.png
BuildRequires:  python2-devel
BuildRequires:  desktop-file-utils
Requires:       deepin-ui
Requires:       python-chardet
Requires:       pygtk2
Requires:       python-pillow
Requires:       python-mutagen
Requires:       python-pyquery
Requires:       scipy
Requires:       python2-xlib

%description
Deepin Music Player with brilliant and tweakful UI Deepin-UI based,
gstreamer front-end, with features likes search music by pinyin,
quanpin, colorful lyrics supports, and more powerful functions
you will found.

%prep
%setup -q 

%build
cd locale
msgfmt zh_CN.po -o zh_CN.mo
msgfmt zh_HK.po -o zh_HK.mo
msgfmt zh_TW.po -o zh_TW.mo

%install
chmod 644 AUTHORS
chmod 644 COPYING
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/icons
mkdir -p %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/locale/zh_CN/LC_MESSAGES/
mkdir -p %{buildroot}/%{_datadir}/locale/zh_HK/LC_MESSAGES/
mkdir -p %{buildroot}/%{_datadir}/locale/zh_TW/LC_MESSAGES/
mkdir -p %{buildroot}/%{_bindir}
cp %{S:1} %{buildroot}/%{_datadir}/applications/
cp %{S:2} %{buildroot}/%{_datadir}/icons/
cp -R app_theme %{buildroot}/%{_datadir}/%{name}
cp -R skin %{buildroot}/%{_datadir}/%{name}
cp -R src %{buildroot}/%{_datadir}/%{name}
cp locale/zh_CN.mo %{buildroot}/%{_datadir}/locale/zh_CN/LC_MESSAGES/%{name}.mo
cp locale/zh_HK.mo %{buildroot}/%{_datadir}/locale/zh_HK/LC_MESSAGES/%{name}.mo
cp locale/zh_TW.mo %{buildroot}/%{_datadir}/locale/zh_TW/LC_MESSAGES/%{name}.mo

%find_lang %{name}

cd %{buildroot}/%{_bindir}
ln -s ../share/%{name}/src/main.py %{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/src/*.py %{buildroot}%{_datadir}/%{name}/src/*/*.py

%files -f %{name}.lang
%doc AUTHORS COPYING
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}.png
%{_datadir}/%{name}
%{_bindir}/%{name}

%changelog
* Fri Jun 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
* Tue Jan  8 2013 douglarek@outlook.com
- Add runtime dependence: python-gtk
* Wed Sep 26 2012 hillwood@linuxfans.org
- update to 1.0.1git20120911
- fix bnc#778659
- more changlog please see https://goo.gl/WCVGo
* Tue Sep  4 2012 hillwood@linuxfans.org
- license update: GPL-3.0+
* Tue Sep  4 2012 hillwood@linuxfans.org
- add python-chardet , python-imaging and python2-xlib as require
  packages.
* Sun Sep  2 2012 hillwood@linuxfans.org
- Initial package 1.0git20120716
  Implement logging to tracking events that happen.
  Implement a basic configuration.
  Use listen-music-player play kernel, and thank him for his.
  Determine the Audio file type is supported.
  Add Universal encoding detector of the chardet.
