Name:           caffeine-indicator
Version:        2.9.3
Release:        1
Summary:        Prevent screensaving and powersaving
Group:          User Interface/Desktops
License:        GPLv3
URL:            https://launchpad.net/caffeine
Source0:        http://launchpad.net/caffeine/%{version}/+download/caffeine_%{version}.tar.gz
BuildRequires:  python3-devel
BuildArch:      noarch
Requires:       python3-ewmh
Requires:       python3-xlib
Requires:       perl-Net-DBus
Requires:       python3-pyxdg
#Requires:       notify-python
#Requires:       python-appindicator
#Requires:       gnome-python2-gconf

%description
Caffeine is a small daemon that prevents the desktop from becoming idle (and
hence the screen saver and/or blanker from activating) when the active
window is full-screen.

%prep
%setup -q -n caffeine
sed -i 's|©|(c)|' caffein*

%build
python3 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python3 setup.py install --root=$RPM_BUILD_ROOT --prefix=/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING COPYING.LESSER README
/etc/xdg/autostart/caffeine.desktop
%{_bindir}/*
%{_mandir}/man1/*.1.gz
%{_datadir}/applications/*.desktop  
%{_datadir}/icons/*/*/*/*
%{_datadir}/locale/*/LC_MESSAGES/caffeine-indicator.mo
%{_datadir}/pixmaps/*
%{python3_sitelib}/*
%{_datadir}/caffeine-indicator/glade/GUI.glade

%changelog
* Tue Jan 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.9.3
- Rebuilt for Fedora
* Sat Jan 30 2010 Isaac Fischer <xwaver@gmail.com> - 1.0.1-1  
- initial spec
