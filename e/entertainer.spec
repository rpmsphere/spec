%undefine _debugsource_packages
Summary: Media Center application for Linux
Name:    entertainer
Version: 0.4.2
Release: 1
Source0: http://launchpad.net/entertainer/entertainer-0.4/entertainer-0.4.2/+download/%{name}-%{version}.tar.gz
License: GPLv2
Group:   Application/Multimedia
URL:     https://launchpad.net/entertainer
Requires: pygobject2 pygtk2 pygtk2-libglade python2-gstreamer pyclutter python-sqlite2 pycairo python-feedparser python-inotify python-vorbis python-imaging python-imdb notify-python
Requires: python-CDDB python-eyed3
BuildArch: noarch

%description
Entertainer is a simple and easy-to-use media center solution for Gnome
and XFce desktop environments. Entertainer is written completely in Python.
It uses the gstreamer multimedia framework for multimedia playback.
The user Interface is implemented with Clutter UI-library, which creates
sleek OpenGL animated user interfaces. Entertainer also uses other great
projects like SQLite and iNotify for caching media libraries.

%prep
%setup -q

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install  --root=%{buildroot} 

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Entertainer
Name[zh_TW]=娛樂家
Comment=Media Center application
Comment[zh_TW]=娛樂家影音中心
Exec=%{name}
Icon=%{name}
Categories=Application;AudioVideo;
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files 
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%exclude %{_datadir}/icons/hicolor/icon-theme.cache
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/man/man1/*
%{python2_sitelib}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuilt for Fedora
