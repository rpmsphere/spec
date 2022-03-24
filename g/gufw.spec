Name:           gufw 
Version:        21.04.0
Release:        2
Summary:        Uncomplicated Firewall
License:        GPL-3.0
Group:          Productivity/Networking/Security
URL:            http://gufw.org/
Source0:        https://launchpadlibrarian.net/350352643/gufw-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  autoconf
BuildRequires:  intltool
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-netifaces
#BuildRequires:  python3-configparser
Requires:       ufw

%description
An easy, intuitive, way to manage your Linux firewall. It supports common
tasks such as allowing or blocking pre-configured, common p2p, or individual
ports port(s), and many others!

%prep
%setup -q
sed -i 's|share/gufw|lib/python%python3_version/site-packages|' bin/gufw-pkexec

%build

%install
python3 setup.py install --prefix=%{_prefix} --root %{buildroot}

%files
%doc COPYING.GPL3 README
/etc/gufw
/usr/bin/gufw
/usr/bin/gufw-pkexec
/usr/lib/python%python3_version/site-packages/gufw*
/usr/share/applications/gufw.desktop
/usr/share/gufw
/usr/share/icons/hicolor/*/apps/gufw.*
/usr/share/man/man8/gufw.8.*
/usr/share/polkit-1/actions/com.ubuntu.pkexec.gufw.policy
/usr/share/locale/*/LC_MESSAGES/gufw.mo

%changelog
* Wed Dec 15 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 21.04.0
- Rebuilt for Fedora
* Fri Jan 16 2015 p.drouand@gmail.com
- Update to version 15.04.0
  + Fixed #1375468 No reload entry menu
  + Fixed #1388422 NTP rule uses CUPS port
  + Fixed #1342355 #1374998 Typos
  + Fixed #1375010 Translated "Gufw is already running"
  + Fixed #1375957 Tutorial strings in English
  + Updated languages
- Cleanup specfile
- Fix Url
- Use download Url as source
* Thu Dec 11 2014 olaf@aepfle.de
- Correct usage of fdupes macro
* Wed Dec  4 2013 johann.luce@wanadoo.fr
- Update in 14.04.0 version
    Resized rule columns
    Network as default category
    Add window more fast
    Added some games to Games category (Steam, Teeworlds...)
    Fixed bug #1235623 Gtk.FileFilter options for Import/Export windows are not set for translation
    Fixed bug #1234668 gufw.desktop is not set for translation
    Fixed bug #1242821 User can sort Rules and Listening Report
    Fixed bug #1244307 User can search in columns the app value
    Fixed bug #1243782 Opening Webs fail in some cases
    Fixed bug #1244670 Minimal Window size 640x480
    Fixed bug #1243312 Confirm dialog for deleting rule in Preferences
    Fixed bug #1245642 Filter preconfigured rules
    Fixed bug #1251890 Profiles are duplicated when user changed from English to another language
    Fixed bug #1057961 Enable/disable from live report
    Added 'GNOME' in desktop categories
    Removed GObject deprecated lines > Removing python-gobject dependence
    Added set refresh interval in Listening Report
    Updated languages
    Append to log when user disabled the Logging
    Added spinner while the Listening Report is loading
* Fri Sep 20 2013 johann.luce@wanadoo.fr
- Update in 13.10.3 version
* Wed Jul 31 2013 johann.luce@wanadoo.fr
- Fix file COPYING.GPL3 not packaged
* Wed Jul 31 2013 johann.luce@wanadoo.fr
- Update in 13.10.2 version
    Fixed web browser for URL in about
* Fri Jul 19 2013 johann.luce@wanadoo.fr
- Update in 13.10.1 version
    Fixed #765899 Gufw is now completely accessible with Orca Screen Reader
    Fixed #1116571 Added to allow specifying both 'in' and 'out'
  directional rule in one step
    Fixed #1198038 Gufw caused high CPU usage with Listening Report expanded
    Fixed #1024523 UI translated completely
    Fixed little bugs in layout.
    3 New preconfigured Profiles by default: Home, Work and Public.
    Available in English UK, Italian and Romanian.
    Fix some warnings in obs
    Add pyton-netifaces and typelib-1_0-WebKit-3_0
    Add package lang
* Mon Mar 18 2013 johann.luce@wanadoo.fr
- Update in 13.04 version
* Wed Nov 21 2012 johann.luce@wanadoo.fr
-fix problem naming gui-ufw -> gufw
* Mon Jun 11 2012 johann.luce@wanadoo.fr
- Update in 12.10 version
  fix problem with gir-repository for opensuse 12.2
* Tue Apr  3 2012 johann.luce@wanadoo.fr
- Update to 12.04.1 version
* Tue Oct 25 2011 johann.luce@wanadoo.fr
-ompatibilité pour opensuse 11.3
* Tue Oct 25 2011 johann.luce@wanadoo.fr
-update to version 11.10.2
* Tue Oct 11 2011 johann.luce@wanadoo.fr
  change for duplicate error-
* Tue Oct 11 2011 johann.luce@wanadoo.fr
  Compatibilité pour opensuse 11.3-
* Tue Oct 11 2011 johann.luce@wanadoo.fr
  update to version 11.04.2-
* Thu Oct  6 2011 johann.luce@wanadoo.fr
  add tag %%lang() in spec file-
* Wed Oct  5 2011 johann.luce@wanadoo.fr
  OpenSUSE Factory-
* Wed Oct  5 2011 johann.luce@wanadoo.fr
  Compatibilité pour opensuse 11.3-
* Wed Oct  5 2011 johann.luce@wanadoo.fr
  Patch for opensuse commande, desktop-
* Tue Oct  4 2011 johann.luce@wanadoo.fr
  first on opensuse-
