%global _warning_options -fpermissive -Wl,--allow-multiple-definition

Summary:        GUI setup tools Collection for Open X Input Method Server .
Name:           oxim-setup
Version:        1.5.5
Release:        1
License:        LGPLv2+
Group:          System/Internationalization
URL:            https://www.opendesktop.org.tw/
Source0:        oxim-setup-%{version}.tar.gz
Autoreq:        no
Requires:       oxim
BuildRequires:  zlib-devel, gtk2-devel, libglade2-devel, oxim-devel
BuildRequires:  libX11-devel, libXpm-devel
#BuildRequires: gambas2-devel, gambas2-runtime
BuildRequires:  qt3-devel, qt4-devel, libcurl-devel

%description
OXIM-SETUP is A GUI interface built on PHP-GTK enviornment.
This tool can help OXIM user to change common settings, download/Install
Input-Method tab files, and User-Defined pharse settings.
OXIM-SETUP includes PHP, GTK, QT3 supporting enviornment.

%prep
%setup -q
sed -i 's|curl/types.h|curl/curl.h|' src/oxim-setup-gtk/src/main.c

%build
echo $QTDIR
export CXXFLAGS="-Wno-format-security -Wl,--allow-multiple-definition -fpermissive"
%configure --enable-static=no --enable-setup-qt3=no --enable-setup-qt4=no --enable-setup-gambas=no --enable-qt-immodule=no
make -i
sed -i 's|-Werror=format-security|-Wno-format-security -Wl,--allow-multiple-definition -fpermissive|g' libtool Makefile */Makefile */*/Makefile
%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT make install
%ifarch x86_64
%{__sed} -i 's|/usr/lib|/usr/lib64|' $RPM_BUILD_ROOT%{_bindir}/oxim-setup
%{__sed} -i 's|/usr/lib|/usr/lib64|' $RPM_BUILD_ROOT%{_libdir}/oxim-setup/oxim-setup-php/init.php
%endif
%{__sed} -i 's|/usr/bin/env python|/usr/bin/python2|' $RPM_BUILD_ROOT%{_libdir}/oxim-setup/oxim-setup-pygtk/oxim-pytgtk-gui.py $RPM_BUILD_ROOT%{_libdir}/oxim-setup/oxim-setup-pygtk/oxim-setup

%post
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%postun
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%files
%doc AUTHORS COPYING ChangeLog NEWS README
#%{_bindir}/oxim-reload
%{_bindir}/oxim-setup
#%{_libdir}/oxim-setup/oxim-setup-gambas/oxim-setup
#%{_libdir}/oxim-setup/oxim-setup-qt3/oxim-setup
#%{_libdir}/oxim-setup/oxim-setup-qt4/oxim-setup
%exclude %{_libdir}/oxim-setup/oxim-setup-php/oxim-setup.php
%{_libdir}/oxim-setup/oxim-setup-php/oxim-setup
%{_libdir}/oxim-setup/oxim-setup-php/init.php
%{_libdir}/oxim-setup/oxim-setup-php/oxim-setup.glade
%{_libdir}/oxim-setup/oxim-setup-php/gui/*
%{_libdir}/oxim-setup/oxim-setup-php/images/*
%{_libdir}/oxim-setup/oxim-setup-php/lib/*
%{_libdir}/oxim-setup/oxim-setup-gtk/oxim-setup
%{_libdir}/oxim-setup/oxim-setup-gtk/gtkrc
%{_libdir}/oxim-setup/oxim-setup-gtk/icon_textview_icon1.png
%{_libdir}/oxim-setup/oxim-setup-gtk/icon_textview_icon2.png
%{_libdir}/oxim-setup/oxim-setup-gtk/icon_textview_icon3.png
%{_libdir}/oxim-setup/oxim-setup-gtk/icon_textview_icon4.png
%{_libdir}/oxim-setup/oxim-setup-gtk/icon_textview_icon5.png
%{_libdir}/oxim-setup/oxim-setup-gtk/icon_textview_icon6.png
%{_libdir}/oxim-setup/oxim-setup-gtk/oxim-setup-glade.xml
%{_libdir}/oxim-setup/oxim-setup-pygtk/*
%{_libdir}/oxim-setup/oxim-setup-java/*
%{_libdir}/oxim-setup/oxim-setup-oxzilla/*
%{_datadir}/applications/oxim-setup.desktop
%{_datadir}/pixmaps/oxim-setup.png
%{_mandir}/man1/oxim-setup.1.gz
%exclude %{_datadir}/gettext
%{_datadir}/locale/*/LC_MESSAGES/oxim-setup.mo
#%{_libdir}/oxim-setup/oxim-setup-gambas/.lang/*.mo

%changelog
* Mon Sep 17 2012 Kevin Chen <kevin.chen@ossii.com.tw> 1.5.5
- Update java version.
* Fri Jul 20 2012 John Wu <john.wu@ossii.com.tw> 1.5.4
- Add qt4, java and oxzilla versions.
* Mon Aug 22 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.3-1
- Added: IQQI mo defines.
* Wed Jun 29 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.2-1
- Update to 1.5.2.
* Tue Mar 01 2011 Wind Win <yc.yan@ossii.com.tw> 1.4.5-2
- Add -lz to Makefile.am (gtk module)
* Tue Mar 01 2011 Wind Win <yc.yan@ossii.com.tw> 1.4.5-1
- Add oxim-setup-oxzilla for first checking.
* Thu Nov 27 2008 Wind Win <yc.yan@ossii.com.tw> 1.2.0-4
- Build for most fixes.
* Thu Oct 30 2008 Wind Win <yc.yan@ossii.com.tw> 1.2.0-2
- Modify desktop file to run oxim-setup correctly.
* Mon Oct 27 2008 Wind Win <yc.yan@ossii.com.tw> 1.2.0-1
- Upgrade version.
* Wed Oct 1 2008 Wind Win <yc.yan@ossii.com.tw> 1.1.6-4
- Add I18N for zh_TW and zh_CN.
- Update again.
* Thu Sep 18 2008 Wind Win <yc.yan@ossii.com.tw> 1.1.6-3
- Rename every part of oxim-setup-(dist) program to oxim-setup
- (oxim-setup-qt3) Translate Chinese to English.
* Tue Sep 9 2008 Wind Win <yc.yan@ossii.com.tw> 1.1.6-2
- Add man page file - oxim-setup.1
- Pass build source when gambas enviorment not found.
- Update Doc contents.
* Fri Sep 5 2008 Wind Win <yc.yan@ossii.com.tw> 1.1.6-1
- Initial RPM build.
