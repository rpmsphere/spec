Name:           deepin-media-player
Summary:        Deepin Media Player
Version:        2.0
Release:        7.1
License:        GPL-3.0
BuildArch:      noarch
URL:            https://github.com/linuxdeepin/deepin-media-player
Group:          Productivity/Multimedia/Video/Players
Source0:        %{name}-%{version}.tar.gz
Source1:        deepin-media-player.desktop
Source2:        deepin-media-player.png
BuildRequires:  desktop-file-utils
BuildRequires:  python2-devel
Requires:       deepin-ui
Requires:       python-pyquery 
Requires:       python-mutagen 
Requires:       scipy 
Requires:       python-chardet 
Requires:       python-pillow 
Requires:       python-formencode
Requires:       mplayer2

%description
New multimedia player with brilliant and tweakful UI.PyGtk and Deepin-ui
Mplayer2 front-end, with features likes smplayer, but has a brilliant
and tweakful UI.

%prep
%setup -q
sed -i 's|coding:utf-8|/usr/bin/python2|' src/test_client.py

%build
chmod 644 AUTHORS
chmod 644 COPYING
chmod 644 README
cd locale
rm -rf *.po
rm -rf deepin-media-player.pot
cd ../src
chmod 755 *.py
cd ../tools
chmod 755 *.py

%install
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/icons
mkdir -p %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_bindir}
cp %{S:1} %{buildroot}/%{_datadir}/applications/
cp %{S:2} %{buildroot}/%{_datadir}/icons/
cp -R locale %{buildroot}/%{_datadir}
cp -R app_theme %{buildroot}/%{_datadir}/%{name}
cp -R skin %{buildroot}/%{_datadir}/%{name}
cp -R src %{buildroot}/%{_datadir}/%{name}

%find_lang %{name}

cd %{buildroot}/%{_bindir}
ln -s ../share/%{name}/src/main.py %{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/src/%{name}.py
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/src/*.py

%files -f %{name}.lang
%doc AUTHORS COPYING
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}.png
%{_datadir}/%{name}
%{_bindir}/%{name}

%changelog
* Fri Jun 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuild for Fedora
* Mon Dec 17 2012 hillwood@linuxfans.org
- update to 2.0git20121115, see more at http://goo.gl/mIk8b
- fix mplayer2 command
* Sat Oct  6 2012 hillwood@linuxfans.org
- Update to 1.0.2git20120911
  * Add new subtitles functions
  Subtitles Search
  Subtitle Selection
    Subtitles manually load
    Subtitles resizing
    Subtitle synchronization functions
    Subtitles progress trim
- Fix desktop Categories
* Tue Sep  4 2012 hillwood@linuxfans.org
- Initial package 1.0git20120817
