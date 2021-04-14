Name: svplayer
Summary: A simple but powerful television and video player
Version: 0.6.0
Release: 4.1
Group: Applications/Multimedia
License: GPLv2+
URL: http://www.salstar.sk/svplayer/
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: pygtk2
Requires: pygobject3
Requires: gstreamer
Requires: python-lirc
Requires: youtube-dl
Requires: python-gdata
Requires: python-pillow
Requires: python-simplejson

%description
Features:
- play any file which can be played with vlc (www.videolan.org),
  gstreamer (www.gstreamer.net) or mplayer (www.mplayerhq.hu)
- simple interface, maximal video size
- file browser to play any file
- youtube player (needs youtube-dl)
- image player to play yout favorite galleries
- lirc (infrared remote) support
- multiple profile support (all channels, channels for childrens, radio
  stations, SAP, ...)

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -a *.py rsync mobile players %{buildroot}%{_datadir}/%{name}
sed -i 's|Icon=totem|Icon=/usr/share/svplayer/mobile/favicon.png|' SVPlayer.desktop
install -Dm644 SVPlayer.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -d %{buildroot}%{_bindir}
ln -s ../share/%{name}/%{name}.py %{buildroot}%{_bindir}/%{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%files
%doc README TODO COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.0
- Rebuilt for Fedora
