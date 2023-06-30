Summary(ru_RU.KOI8-R): FM-тюнер для GNOME.
Summary: Graphical FM-Tuner program for GNOME
Name: gnomeradio
Version: 1.8
Release: 19.2
License: GPLv2+
Group: Sound
URL: https://projects.gnome.org/gnomeradio/
Source0: https://www.wh-hms.uni-ulm.de/~mfcn/gnomeradio/packages/%{name}-%{version}.tar.gz
Source1: gnomeradio.sh
Patch0: %{name}-v4l2.patch
Patch1: %{name}-ld.patch
Patch2: hardening-format-security.diff
# https://git.gnome.org/browse/gnomeradio/commit/?id=7694c70f99731724dad64444484d070ff760db89
Patch3: %{name}-crash.patch
Patch4: %{name}-gnome-3.0.patch
Patch5: %{name}-gtk.patch
# This removes the libgnomeui and uses only gtk functionality.
# With this patch, we can build this code against gtk3. It launches
# but I do not have a radio card, so I couldn't get very far with it.
# ~spot 2011-04-25
Patch6: %{name}-1.8-nogtk2.patch
Patch7: %{name}-1.8-gui.patch
Patch8: %{name}-1.8-expose-event.patch
BuildRequires: desktop-file-utils
BuildRequires: dbus-glib-devel
BuildRequires: gettext
BuildRequires: gnome-doc-utils
BuildRequires: gnome-vfs2-devel
BuildRequires: gstreamer-devel
BuildRequires: gstreamer-plugins-base-devel
BuildRequires: intltool
BuildRequires: libgnome-media-profiles-devel
# BuildRequires: libgnomeui-devel
BuildRequires: lirc-devel
BuildRequires: scrollkeeper
BuildRequires: python udisks2
Requires(pre): GConf2
Requires(preun): GConf2
Requires(post): GConf2
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
Gnomeradio is a FM-radio tuner for the GNOME desktop. It should work with
every FM tuner card that is supported by video4linux. Remote controls are
supported via LIRC-support. Gnomeradio can also record radio as a Wave or
Ogg files.

%prep
%setup -q
%patch0 -p1 -b .v4l2
%patch1 -p1 -b .ld
%patch2 -p1 -b .format-security
%patch3 -p1 -b .crash
%patch4 -p1 -b .gnome-3.0
%patch5 -p1 -b .gtk
%patch6 -p1 -b .nogtk2
%patch7 -p1 -b .gui.patch
%patch8 -p1 -b .expose-event
%{__install} -m 755 %{SOURCE1} .

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure \
	--disable-schemas-install \
	--disable-install-schemas \
	--disable-scrollkeeper

%{__make} %{?_smp_mflags}

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%{__make} DESTDIR=%{buildroot} install
%find_lang %{name}

echo "Encoding=UTF-8" >> %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications \
	--add-category=Audio \
	--add-category=Tuner \
	--add-category=GNOME \
	--add-category=GTK \
	--delete-original \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

# Fix docs encoding
for file in AUTHORS ChangeLog README ; do
iconv -f iso8859-1 -t utf8 $file > $file.utf8 && touch -r $file $file.utf8 && mv $file.utf8 $file
done

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
    killall -HUP gconfd-2 >/dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
    killall -HUP gconfd-2 >/dev/null || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
killall -HUP gconfd-2 >/dev/null || :


%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README README.lirc README.recording gnomeradio.sh
%{_datadir}/gnome/help/%{name}/
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/omf/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Thu Jun 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8
- Rebuilt for Fedora
* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.8-alt2_24
- update to new release by fcimport
* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt2_22
- update to new release by fcimport
* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt2_21
- update to new release by fcimport
* Sat Apr 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt2_20
- update to new release by fcimport
* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.8-alt2_19
- update to new release by fcimport
* Fri Dec 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.8-alt2_18
- initial fc import
* Sun May 02 2010 Yuri N. Sedunov <aris@altlinux.org> 1.8-alt2
- updated buildreqs
* Wed Jul 08 2009 Yuri N. Sedunov <aris@altlinux.org> 1.8-alt1
- 1.8 release
* Sat Jun 28 2008 Yuri N. Sedunov <aris@altlinux.org> 1.7-alt1.svn20080623
- new svn version
- removed old reqs and post{,un} scripts
- updated {pre,post,build}reqs.
- use macros from rpmb-build-gnome and rpm-build-licenses
- URL improved.
* Mon Apr 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.6-alt1
- 1.6
* Thu Jan 27 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.5-alt1
- First build for Sisyphus.
