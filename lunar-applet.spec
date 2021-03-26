%define         schema_name lunar
Name:           lunar-applet
Version:        1.6
Release:        1
Summary:        A GNOME Timer applet replacement
Summary(zh_CN): Lunar applet - GNOME 面板插件，为时钟增加了农历日期显示的功能
Summary(zh_TW): 增加農曆顯示功能的 GNOME 面板時鐘小工具
Group:          User Interface/Desktops
License:        GPL
URL:            http://dev.inlsd.org/projects/lunar-applet
Source0:        http://ftp.inlsd.org/lunar-applet/lunar-applet-%{version}.tar.gz
BuildRequires:  intltool >= 0.35 gettext pkgconfig >= 0.9
BuildRequires:  GConf2-devel mate-panel-devel evolution-data-server-devel gnome-doc-utils
Requires:       GConf2

%description
A GNOME Timer applet replacement. It provides
the chinese traditional(lunar) calendar.

%description -l zh_CN
Lunar applet 是 GNOME 面板上的一个小插件,
在原来的"时钟"插件代码的基础上修改而成, 增
加了农历日期显示的功能.

%description -l zh_TW
Lunar applet 是 GNOME 面板上的一個小工具，
在原來的時鐘小工具代碼的基礎上修改而成，增加
農曆日期顯示的功能。

%prep
%setup -q
sed -i 's|libpanelapplet-2.0|libmatepanelapplet-4.0|' configure*
sed -i 's|2.14.3|1.20.3|' configure*

%build
%configure --enable-eds --disable-static --disable-schemas-install
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ "$1" -gt 1 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{schema_name}.schemas >/dev/null || :
    # If the schema file has ever been renamed::
    #gconftool-2 --makefile-uninstall-rule \
    #  %{_sysconfdir}/gconf/schemas/[OLDNAME].schemas > /dev/null || :
    killall -HUP gconfd-2 || :
fi

%post
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
  %{_sysconfdir}/gconf/schemas/%{schema_name}.schemas > /dev/null || :
killall -HUP gconfd-2 || :

%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/%{schema_name}.schemas > /dev/null || :
    killall -HUP gconfd-2 || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%config(noreplace) %{_sysconfdir}/gconf/schemas/%{schema_name}.schemas
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/lunar-applet
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/gtk-doc/html/gtkchinesecalendar/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Wed Dec 05 2007 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6-1
- rebuild 1.6 for M6(CentOS5)

* Sat Apr 14 2007 bbbush <bbbush.yuan@gmail.com> - 1.5-1
- initial import
