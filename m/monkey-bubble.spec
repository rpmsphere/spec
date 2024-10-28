Name:             monkey-bubble
Version:          0.4.0
Release:          1
Summary:          Game in the spirit of Frozen Bubble
Group:            Amusements/Games
License:          GPLv2+
URL:              https://home.gna.org/monkeybubble/
Source0:          https://home.gna.org/monkeybubble/downloads/%{name}-%{version}.tar.gz
Source1:          splash.svg
Patch0:           monkey-bubble-0.4.0-help.patch
BuildRequires:    libgnomeui-devel librsvg2-devel gstreamer-devel gettext
BuildRequires:    desktop-file-utils scrollkeeper gnome-doc-utils
BuildRequires:    perl(XML::Parser)
Requires:         scrollkeeper hicolor-icon-theme
Requires(pre):    GConf2
Requires(post):   GConf2 scrollkeeper
Requires(preun):  GConf2
Requires(postun): scrollkeeper

%description
Monkey Bubble is a bust'a'move clone built using Gnome technologies. It
currently supports 1 and 2 player games, is levelcompatible with frozen bubble,
and features svg vector graphics for resolution independent display.

%prep
%setup -q
%patch 0 -p1 -z .help
# replace the broken included splash.svg
cp %{SOURCE1} pixmaps
# adjust desktop, C-code for fdo icon dir and naming
sed -i s/%{name}-icon/%{name}/ %{name}.desktop.in
sed -i 's|/pixmaps/%{name}-icon.png|/icons/hicolor/32x32/apps/%{name}.png|g' \
  src/ui/ui-main.c
sed -i 's|glib/.*\.h|glib.h|' src/net/*.c

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-pointer-sign -Wno-error -Wno-format-security"
export LDFLAGS=-Wl,--allow-multiple-definition
%configure --disable-schemas-install LIBS="-lgtk-x11-2.0 -lglib-2.0 -lxml2 -lrsvg-2 -lm"
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
make install DESTDIR=${RPM_BUILD_ROOT}
%find_lang %{name}

#remove scrollkeeper stuff
rm -rf $RPM_BUILD_ROOT/var

# below is the desktop file and icon stuff.
desktop-file-install --vendor fedora --delete-original \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications      \
  --remove-category GNOME                              \
  --remove-category Application                        \
  --add-category ActionGame                            \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mv ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}-icon.png \
  ${RPM_BUILD_ROOT}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
rmdir ${RPM_BUILD_ROOT}%{_datadir}/pixmaps



%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
/usr/bin/gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi

%postun
scrollkeeper-update -q || :
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/monkey-*
%{_datadir}/%{name}
%{_datadir}/gnome
%{_datadir}/omf/%{name}
%{_datadir}/applications/fedora-%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.4.0-9
- Autorebuild for GCC 4.3
* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.0-8
- Rebuild for buildId
- Update license tag for new license tag guidelines
* Wed Jun 27 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.0-7
- Fix URL (bz 245378)
* Sun Jun 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.0-6
- Remove yelp Requires again <sigh> (bz 243408)
* Fri Jun  8 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.0-5
- Add yelp Requires so that the help will always work (bz 243408)
- Fix display of icon in the windows titlebar
- Fix only part of the splashscreen displaying
* Fri Apr 27 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.0-4
- Fix building with newer docbook / gnome-doc tools
* Sun Sep 10 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.0-3
- Don't own /usr/share/omf (bug 205670)
* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.0-2
- FE6 Rebuild
* Wed Aug  2 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.4.0-1
- New upstream version 0.4.0
- Drop upstreamed patches
* Sat Apr 29 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.2-1
- New upstream version 0.3.2
- Add a patch to make it use gstreamer-0.10 instead of 0.8
- Add a patch to fix some warnings
- Properly install the icon
- Fix the scripts to properly handle the GConf schemas and call
  scrollkeeper-update. Don't call ldconfig as there is no lib.
* Fri Nov 21 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.1.6-0.fdr.4
- Drop .so files (for real this time).
* Mon Nov 17 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.1.6-0.fdr.3
- Drop .so files.
* Wed Nov 12 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.1.6-0.fdr.2
- BuildReqs desktop-file-utils, gettext, pkgconfig.
- BuildReq libcroco-devel.
- Removing .la files.
- No longer including empty NEWS file under docs.
- Excluding /usr/bin/gsttest.
* Mon Oct 13 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:0.1.6-0.fdr.1
- Initial RPM release.
