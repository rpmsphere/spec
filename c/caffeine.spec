Name:           caffeine
Version:        2.9.3
Release:        4.1
Summary:        Prevent screensaving and powersaving
Group:          User Interface/Desktops
License:        GPLv3
URL:            https://launchpad.net/caffeine
Source0:        http://launchpad.net/caffeine/%{version}/+download/%{name}_%{version}.tar.gz
BuildRequires: python-devel, python3
BuildArch:      noarch
#Requires:       python-pyewmh
Requires:       python-xlib
Requires:       perl-Net-DBus
Requires:       pyxdg
Requires:       notify-python
Requires:       python-appindicator
Requires:       gnome-python2-gconf

%description
Caffeine is a small daemon that prevents the desktop from becoming idle (and
hence the screen saver and/or blanker from activating) when the active
window is full-screen.

%prep
%setup -q -n %{name}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --prefix=/usr

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
%{python_sitelib}/*
%{_datadir}/caffeine-indicator/glade/GUI.glade

%changelog
* Tue Jan 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.9.3
- Rebuild for Fedora
* Sat Jan 30 2010 Isaac Fischer <xwaver@gmail.com> - 1.0.1-1  
- initial spec
