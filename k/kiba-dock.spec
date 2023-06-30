Name: kiba-dock
Version: 0.svn584
Release: 1
Summary: Funky application dock for X11
Group: System/X11
URL: https://www.kiba-dock.org/
Source: kiba-%{version}.tar.bz2
Source1: kiba-dock-0.svn584.zh_TW.po
Source2: kiba-plugins-0.svn584.zh_TW.po
Source3: kiba-dbus-plugins-0.svn584.zh_TW.po
License: GPL
BuildRequires: intltool, libtool, automake, autoconf
BuildRequires: gtk2-devel, libxml2-devel, dbus-glib-devel, librsvg2-devel
Requires: gconf-editor, feedparser, dbus-python

%description
Kiba-dock is a dock based on the Gtk libraries, using cairo for smooth animation.
Akamaru is a simple, but fun, physics engine prototype.

%prep
%setup -q -n kiba-%{version}
echo zh_TW >> kiba-dock/po/LINGUAS
%__cp %{SOURCE1} kiba-dock/po/zh_TW.po
echo zh_TW >> kiba-plugins/po/LINGUAS
%__cp %{SOURCE2} kiba-plugins/po/zh_TW.po
echo zh_TW >> kiba-dbus-plugins/po/LINGUAS
%__cp %{SOURCE3} kiba-dbus-plugins/po/zh_TW.po

%build
cd akamaru
sed -i 's/AC_SUBST("$AKAMARU_REQUIRES")/AC_SUBST(AKAMARU_REQUIRES)/' configure.in
./autogen.sh -V
%configure
%__make

export KIBA_DOCK_CFLAGS='-Wno-error -I../../kiba-dock/include -I/usr/include/librsvg-2 -I/usr/include/gtk-2.0 -I/usr/include/glib-2.0 -I/usr/include/cairo'
#export KIBA_DOCK_LIBS='-L../../kiba-dock/src/.libs -lrsvg-2'
export KIBA_DOCK_LIBS='-lrsvg-2'
cd ../kiba-dock
sed -i -e 's/AC_SUBST("$PKG_CONFIG_PATH")/AC_SUBST(PKG_CONFIG_PATH)/' -e 's/AC_SUBST("$KIBA_DOCK_REQUIRES")/AC_SUBST(KIBA_DOCK_REQUIRES)/' configure.ac
./autogen.sh -V
%configure --enable-akamaru --enable-svg
sed -i 's|-Werror=format-security|-lX11 -ldl|' */Makefile
%__make

cd ../kiba-plugins
sed -i 's/AC_SUBST("$KIBA_PLUGINS_REQUIRES")/AC_SUBST(KIBA_PLUGINS_REQUIRES)/' configure.in
./autogen.sh -V
%configure --with-pic
sed -i 's|-Werror=format-security|-lX11 -ldl|' */Makefile
sed -i 's|librsvg-2 |librsvg-2.0 |' */Makefile
%__make

cd ../kiba-dbus-plugins
./autogen.sh -V
%configure --with-pic
%__make

%install
rm -rf %{buildroot}
%makeinstall -C akamaru
sed -i 's|kiba-desktop-editor.h kiba-desktop-icon.h kiba-icon-view-win.h|kiba-desktop-editor.h kiba-icon-view-win.h|' kiba-dock/include/Makefile
%makeinstall -C kiba-dock
%make_install -C kiba-plugins
%make_install -C kiba-dbus-plugins

cp -a %{buildroot}/kiba-dock/* %{buildroot}%{_datadir}/kiba-dock
rm -rf %{buildroot}/kiba-dock
#cp -a %{buildroot}%{buildroot}/usr %{buildroot}
#rm -rf %{buildroot}/var

sed -i -e '/Name=Kiba-Settings/a Name[zh_TW]=桌面停駐區' -e 's/Utility;//' \
	%{buildroot}%{_datadir}/applications/kiba-settings.desktop

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/dbus_scripts/*.py

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/%{name}
%{_bindir}/kiba-settings
%{_bindir}/populate-dock.sh
%{_datadir}/pixmaps/kiba-dock.png
%{_datadir}/kiba-dock
%exclude %{_datadir}/applications/kiba-dock.desktop
%{_datadir}/applications/kiba-settings.desktop
%{_datadir}/locale/*/LC_MESSAGES/kiba-dock.mo

%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/kiba-dock.pc

%{_libdir}/libakamaru.so*
%exclude %{_libdir}/libakamaru.a
%exclude %{_libdir}/libakamaru.la
%{_includedir}/akamaru/*
%{_libdir}/pkgconfig/akamaru.pc

%{_datadir}/locale/*/LC_MESSAGES/kiba-plugins.mo
%{_libdir}/kiba-dock/*.so
%exclude %{_libdir}/kiba-dock/*.a
%exclude %{_libdir}/kiba-dock/*.la

%{_datadir}/locale/*/LC_MESSAGES/kiba-dbus-plugin.mo

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0-0.20070201
- Rebuilt for Fedora
* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0-0.20070201.6mdv2008.1
+ Revision: 136523
- restore BuildRoot
+ Thierry Vignaud <tvignaud@mandriva.com>
- kill re-definition of %%buildroot on Pixel's request
* Tue Mar 27 2007 Colin Guthrie <cguthrie@mandriva.org> 0-0.20070201.6mdv2007.1
+ Revision: 149039
- Make sure the main package requires it plugins/libraries
* Wed Feb 07 2007 Colin Guthrie <cguthrie@mandriva.org> 0-0.20070201.5mdv2007.1
+ Revision: 117258
- Fix usage on x86_64
* Wed Feb 07 2007 Lev Givon <lev@mandriva.org> 0-0.20070201.4mdv2007.1
+ Revision: 117250
- Rebuild.
- Change devel(libgtop-2.0) buildreq to libgtop2.0-devel so that the
  package can build on x86_64.
- Add librsvg-devel buildreq.
  Check Python version before patching so that the package can build on 2007.0.
  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Add patch0: fix python installation
  + Sébastien Savarin <plouf@mandriva.org>
    - realy add macro for python
    - add macro for python
    - Add deps on gconf-editor
    - Sync with svn 20070201
  + Colin Guthrie <cguthrie@mandriva.org>
    - Rebuild
    - Fix version number.
    - Import kiba-dock
