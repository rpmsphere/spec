Name: mikutube
Version: 1.8.0.2
Release: 7.1
Summary: The video of Hatsune Miku is downloaded from youtube
Source: %{name}-%{version}.tar.gz
Source1: mikutube.desktop
Patch:   systray.patch
URL: https://kaoru-linux.cocolog-nifty.com/blog/
Group: Productivity/Multimedia/Video/Players
License: GNU General Public License v3
BuildArch: noarch
Requires: pygtk2, gnome-python2-desktop, notify-python
Requires: python-gdata, python2-gstreamer
Requires: mplayer, ffmpeg, gstreamer-ffmpeg
Requires: youtube-dl
Vendor: kaoru konno (kaorin)

%description
MikuTube is an application that continuously reproduces the animation acquired
from YouTube according to a specified key word.

%prep
%setup -q -c -n %{name}-%{version}
%patch

%build

%install
%__install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
%__install -m 755 MikuTube.py $RPM_BUILD_ROOT%{_datadir}/%{name}
%__install -m 644 README.txt $RPM_BUILD_ROOT%{_datadir}/%{name}
%__install -m 644 splash.jpg $RPM_BUILD_ROOT%{_datadir}/%{name}
%__install -m 644 MikuTube.png $RPM_BUILD_ROOT%{_datadir}/%{name}

%__install -dm 755 $RPM_BUILD_ROOT%{_datadir}/applications
%__install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/mikutube.desktop

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.0.2
- Rebuilt for Fedora
* Tue May 01 2012 kobayashi
- Update 1.8.0.2
- Add system tray patch. 
* Sat Mar 03 2012 kobayashi
- Update 1.8.0.0
- Symbolic link to Mikutube.py is removed. 
* Mon May 15 2011 kobayashi
- Update 1.6.3.0
* Thu Dec 23 2010 kobayashi
- Update 1.6.2.0 no Requires: youtube-dl
* Wed Apr 29 2010 kobayashi
- new package from Upstream
