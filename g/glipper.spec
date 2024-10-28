Name:           glipper
Version:        2.4
Release:        14.1
Summary:        Clipboard Manager for GNOME
License:        GPL-2.0
Group:          Productivity/Other
URL:            https://launchpad.net/glipper
Source0:        https://launchpad.net/glipper/trunk/2.4/+download/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  GConf2-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python2-distutils-extra
BuildRequires:  python2-devel
Requires:       pygobject2
Requires:       pygtk2
Requires:       python2-keybinder
Requires:       python2-pyxdg
BuildArch:      noarch

%description
Glipper is a clipboardmanager for GNOME. It maintains a history of text
copied to the clipboard from which you can choose. Glipper uses plugins
to give the user all the extra functionality.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root %{buildroot} --prefix %{_prefix}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
# Fix installation of gconf schema
mkdir -p %{buildroot}/etc/gconf
mv %{buildroot}%{_datadir}/gconf/schemas %{buildroot}/etc/gconf

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc AUTHORS COPYING README
%{_datadir}/help/*/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_sysconfdir}/xdg/autostart/glipper-autostart.desktop
%{python2_sitelib}/%{name}/
%{python2_sitelib}/%{name}-%{version}-*.egg-info
%{_sysconfdir}/gconf/schemas/glipper.schemas
%{_datadir}/locale/*/LC_MESSAGES/glipper.mo

%changelog
* Mon Oct 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4
- Rebuilt for Fedora
* Sun Sep 16 2012 dimstar@opensuse.org
- Update to version 2.4:
  + lp#904367: high priority crash.
  + Bugs fixed: lp#936650
* Fri Apr  6 2012 vuntz@opensuse.org
- Update to version 2.3. Changes since version 1.0 include:
  + Remove GNOME applet and use app indicator or status icon.
  + Get rid of many dependencies.
  + Various fixes.
- Complete change BuildRequires following move from autotools to
  python-distutils:
  + Removed: gnome-doc-utils-devel, gnome-python-desktop,
    gtk2-devel, python-crypto, python2-devel, python-gtk-devel,
    python-gnome-devel.
  + Added: python-base, python2-distutils-extra.
- Add hicolor-icon-theme BuildRequires for directory ownership and
  definition of %%icon_theme_cache_* macros.
- Add update-desktop-files BuildRequires for
  %%suse_update_desktop_file.
- Remove now unneeded devel subpackage and add Obsoletes for it to
  main package.
- Remove now unneeded gnome-python-desktop and python-gnome
  Requires.
- Add new Requires and Recommends, following upstream
  recommendations:
  + Requires: python-gobject2, python-keybinder, python-xdg.
  + Recommends: python-appindicator, python-crypto, python-prctl.
- Change %%build and %%install to use python-distutils commands, and
  fix debian-ism in installation of gconf schemas.
- Update summary and description.
- Make package noarch.
* Sun Feb 13 2011 vuntz@opensuse.org
- Call relevant macros in %%post/%%postun:
  + %%icon_theme_cache_post/postun because the package ships themed
    icons.
- Pass %%{?no_lang_C} to %%find_lang so that english documentation
  can be packaged with the program, and not in the lang subpackage.
- Change Requires of lang subpackage to Recommends, since the
  english documentation is not there anymore.
* Fri Aug 28 2009 puzel@novell.com
- use new python macros
* Sun Jun 14 2009 vuntz@novell.com
- Clean up package for Contrib.
* Tue May 20 2008 zdenekzapp@gmail.com
- Initial package.
