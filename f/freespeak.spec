Name:          freespeak
Version:       0.3.0
Release:       9.1
Summary:       A free frontend to online translator engines
Group:         Graphical Desktop/Applications/Educational
URL:           http://freespeak.berlios.de/
Source0:       http://download.berlios.de/freespeak/freespeak-%{version}.tar.gz
Source1:       freespeak.1
License:       GPL
BuildRequires: libpng-devel
BuildRequires: gconf-editor
BuildRequires: gnome-doc-utils
BuildRequires: intltool
BuildRequires: python2-devel
BuildRequires: pygobject2
BuildRequires: pygtk2-devel
BuildRequires: dbus-python-devel
#BuildRequires: gnome-python2-devel
#BuildRequires: gnome-python2-extras
#BuildRequires: python2-xlib
BuildRequires: python-lxml sane-backends-devel
Requires:      gnome-doc-utils
Requires:      intltool
Requires:      pygtk2
Requires:      pygobject2
Requires:      gnome-python2
Requires:      gnome-python2-extras
Requires:      dbus-python
Requires:      python-lxml
Requires:      python2-xlib
BuildRequires: udisks2
BuildArch:     noarch

%description
FreeSpeak is a free (as in freedom, developed and released under the terms of GPL)
frontend to online translator engines (such as Google, Yahoo, etc.).
It is written in Python, it uses the GTK toolkit and some GNOME infrastructure features.

Features:
* tabbed consulting
* text/web translations and suggestions for developers
* automatically copy and paste from/to clipboard
* expandible in a very easy way by writing translator modules (currently Google, Yahoo, Open-Tran and FreeTranslation)
* easy to use and to configure
* localized (currently English and Italian)
* good integration with free desktop environments (mostly in GNOME)
* desktop-wide global keybinding for activating a translation
.
%prep
%setup -q 

%build
%configure --disable-scrollkeeper
make

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
install -pm 644 %{S:1} $RPM_BUILD_ROOT%{_mandir}/man1/
%find_lang %{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf "$RPM_BUILD_ROOT"

%post
GCONF_CONFIG_SOURCE=`/usr/bin/gconftool-2 --get-default-source` \
/usr/bin/gconftool-2 --makefile-install-rule  \
%{_sysconfdir}/gconf/schemas/freespeak.schemas;
killall -HUP gconfd-2;

%preun
GCONF_CONFIG_SOURCE=`/usr/bin/gconftool-2 --get-default-source` \
/usr/bin/gconftool-2 --makefile-uninstall-rule  \
%{_sysconfdir}/gconf/schemas/freespeak.schemas;
killall -HUP gconfd-2;

%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/gconf/schemas/freespeak.schemas
%{_bindir}/freespeak
%{_datadir}/applications/freespeak.desktop
%{_datadir}/icons/hicolor/*x*/apps/freespeak.png
%exclude %{_datadir}/icons/hicolor/icon-theme.cache
%dir %{python2_sitelib}/freespeak
%{python2_sitelib}/freespeak/*.py
%{python2_sitelib}/freespeak/*.pyc
%{python2_sitelib}/freespeak/*.pyo
%{python2_sitelib}/freespeak/translators
%{python2_sitelib}/freespeak/ui
%dir %{_datadir}/freespeak/art
%{_datadir}/freespeak/art/*.png
%{_datadir}/omf/freespeak
%{_datadir}/gnome/help/freespeak/C
%{_mandir}/man1/freespeak.1.gz
%doc AUTHORS COPYING ChangeLog NEWS README TODO

%changelog
* Fri Jun 17 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuild for Fedora
* Mon Jan 18 2010 Automatic Build System <autodist@mambasoft.it> 0.3.0-1mamba
- automatic update by autodist
* Sat Nov 29 2008 gil <puntogil@libero.it> 0.2.0-1mamba
- package created by autospec
