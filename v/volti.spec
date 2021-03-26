%global debug_package %{nil}
Name:		volti
Version:	0.2.3
Release:	6.1
Summary:	Applet for controlling audio volume
License:	GPLv3
Group:		Sound
URL:		http://code.google.com/p/volti/
Source0:	http://code.google.com/p/volti/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:  desktop-file-utils
Requires:	pygtk2
Requires:	pygobject2
Requires:	python-alsaaudio
Requires:	python-dbus
Requires:	python2-xlib

%description
GTK+ application for controlling audio volume from system
tray/notification area.

Features:
* no pulseaudio, gstreamer, phonon etc. only alsa is needed 
* uses external mixer that you can choose, it goes nicely with gnome-alsamixer 
* left click opens volume scale (slider) 
* scroll wheel on tray icon changes volume, increment in percents is 
configurable 
* you can configure middle click to toggle 'mute' or 'show mixer' 
* nice tooltip with card and volume info 
 
%prep
%setup -q 

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}
#sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

desktop-file-install --vendor="" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name}

sed -i 's|/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files -f %{name}.lang
%doc README COPYING ChangeLog
%{_bindir}/%{name}
%{_bindir}/%{name}-mixer
%{_bindir}/%{name}-remote
%{_datadir}/%{name}/preferences.glade
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/icons
%{_mandir}/man1/*.1*
%{python2_sitelib}/*

%changelog
* Sat Aug 03 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.3
- Rebuild for Fedora
* Wed Jan 25 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.2.3-3
+ Revision: 768154
- imported package volti
* Tue Mar 15 2011 dillj <the.lid7@gmail.com> 0.2.3-2-unity2011
- rebuild
* Tue Jan 04 2011 KDulcimer <kdulcimer@unity-linux.org> 0.2.3-1
- 0.2.3
* Sat Dec 18 2010 KDulcimer <kdulcimer@unity-linux.org> 0.2.2-2
- Correct requires
* Wed Dec 15 2010 KDulcimer <kdulcimer@unity-linux.org> 0.2.2-1
- Import spec to Unity
- 0.2.2
* Sun Sep 12 2010 Texstar <texstar at gmail.com> 0.2.1-2pclos2010
- Update
* Sun May 30 2010 slick50 <lxgator@gmail.com> 0.2.1-1pclos2010
- 0.2.1
* Sat Apr 17 2010 slick50 <lxgator@gmail.com> 0.2.0-1pclos2010
- 0.2.0
* Tue Mar 23 2010 slick50 <lxgator@gmail.com> 0.1.9-1pclos2010
- 0.1.9
* Thu Feb 11 2010 slick50 <lxgator@gmail.com> 0.1.7-1pclos2010
- 0.1.7
* Sat Jan 16 2010 slick50 <lxgator@gmail.com> 0.1.6-1pclos2010
- initial pkg
