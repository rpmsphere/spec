%define udev_rules_dir  /lib/udev/rules.d

Name:           wiican
Version:        0.3.2
Release:        1
Summary:        Simple Wiimote usage assistant and mapping manager
License:        GPLv3
Group:          System/Configuration/Hardware
URL:            https://fontanon.org/wiican/
Source0:        https://launchpad.net/wiican/0.3/%{version}/+download/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       dbus-python
Requires:       gnome-bluetooth
Requires:       pygtk2
Requires:       PyYAML
Requires:       notify-python
Requires:       python2-ply
Requires:       gnome-python2-gconf
Requires:       pygobject2
Requires:       cwiid
Requires:       pyxdg
BuildRequires:  python2-devel
BuildRequires:  desktop-file-utils

%description
WiiCan assists on configuration and management of your Wiimote under
GNU/Linux. It tracks Bluetooth connectivity and allows to use and
create mappings to adapt your Wiimote for use on any application.

Actually WiiCan is a system tray icon, programmed in Python. It
connects to bluez and HAL via D-Bus for tracking the available
Bluetooth devices and Wiimote connection status.

%prep
%setup -q -n %{name}

%build
python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install \
        --prefix=%{_prefix} \
        --root %{buildroot}

#autoload uinput module
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.preload.d
echo uinput > %{buildroot}%{_sysconfdir}/modprobe.preload.d/wiican-uinput

#fix udev-rule name
mv %{buildroot}%{udev_rules_dir}/99-uinput.rules \
   %{buildroot}%{udev_rules_dir}/99-wiican-uinput.rules

#fix desktop file
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications/ \
        --remove-category=HardwareSettings \
        --remove-key=GenericName \
        %{buildroot}%{_datadir}/applications/%{name}.desktop
        
%find_lang %{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}*

%files -f %{name}.lang
%doc AUTHORS TODO
%config(noreplace) %{_sysconfdir}/modprobe.preload.d/wiican-uinput
%config(noreplace) %{_sysconfdir}/gconf/schemas/%{name}.schemas
%{python2_sitelib}/%{name}-%{version}-py*.egg-info
%{python2_sitelib}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_bindir}/%{name}-service
%{udev_rules_dir}/99-wiican-uinput.rules
%{_datadir}/icons/hicolor/*/*/%{name}*
%{_datadir}/icons/hicolor/scalable/mimetypes/gnome-mime-application-x-wii.svg
%{_datadir}/dbus-1/services/org.gnome.wiican.service
%{_datadir}/mime/packages/wiican.xml

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2
- Rebuilt for Fedora
* Sun Feb 13 2011 Jani Välimaa <wally@mandriva.org> 0.3.2-1mdv2011.0
+ Revision: 637547
- new version 0.3.2
- drop unneeded patch
- drop old py_requires macro
- clean .spec a bit
* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.3.1-2mdv2011.0
+ Revision: 590091
- rebuild for python 2.7
* Sun Oct 24 2010 Jani Välimaa <wally@mandriva.org> 0.3.1-1mdv2011.0
+ Revision: 587904
- new version 0.3.1
- drop upstream applied patch
* Thu Sep 02 2010 Jani Välimaa <wally@mandriva.org> 0.3.0-2mdv2011.0
+ Revision: 575382
- add utils_keynone.patch from upstream to fix crash on startup
* Sun Aug 29 2010 Jani Välimaa <wally@mandriva.org> 0.3.0-1mdv2011.0
+ Revision: 574228
- new version 0.3.0
* Fri Aug 20 2010 Zombie Ryushu <ryushu@mandriva.org> 0.2.1-3mdv2011.0
+ Revision: 571488
- Fix build Requires
- Fix build Requires
* Thu Aug 05 2010 Jani Välimaa <wally@mandriva.org> 0.2.1-2mdv2011.0
+ Revision: 566465
- fix .desktop file
- load uinput module in %%post
- prettify summary and description
* Thu Aug 05 2010 Jani Välimaa <wally@mandriva.org> 0.2.1-1mdv2011.0
+ Revision: 566435
- fix source tag
- clean/fix spec
  * fix url, group, license and description
  * fix requires
  * fix file list
- add modprobe.preload.d/wiican-uinput file to load uinput module automaticly
- add udev rule to set "correct" /dev/uinput rights
* Wed Aug 04 2010 Zombie Ryushu <ryushu@mandriva.org> 0.2.1-0.1mdv2011.0
+ Revision: 565839
- Fix Python
- Fix Python
- Build Requires Python
- import wiican
