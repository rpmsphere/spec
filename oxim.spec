%define build_meego 1
%define build_device %{?_with_build_device:1}%{!?_with_build_device:0}

Summary: Open X Input Method Server.
Name: oxim
Version: 1.5.4
Release: 8
License: GPL
Group: System/Internationalization
Source0: %{name}-%{version}.tar.gz
Patch0: oxim-1.4.4-6.start.config.patch
Autoreq: no
Requires: zlib, libXpm >= 2.0.0, libXtst >= 1.0.0, libXft >= 2.0, libXext >= 1.0.0, libXrender >= 0.9
Requires(post,preun): /usr/sbin/alternatives
BuildRequires: gcc-c++, zlib-devel, libchewing-devel >= 0.2.6, libXpm-devel >= 2.0.0, libXtst-devel >= 1.0.0, libXft-devel >= 2.0, libXext-devel, gtk2-devel, sunpinyin-devel >= 2.0.0
BuildRequires: libXrender-devel >= 0.9
%if !%{build_meego}
BuildRequires: qt3-devel
%endif
BuildRequires: gtk3-devel
Obsoletes: xcin >= 3.0.0, oxim-chewing-module, oxim-gtk-immodule, oxim-unicode-module

%description
An X Input Method Server.
gtk-immodule : OXIM context plugin for Gtk input method module.
qt-immodule : OXIM context plugin for QT input method module.
unicode-module : Unicode input method.

%package devel
Summary: Open X Input Method Server, the files for building.
Group: System/Internationalization
Requires: oxim

%description devel
Files provided for build oxim tools.

%package chewing
Summary: Open X Input Method Server for chewing module.
Group: System/Internationalization
Requires: oxim
Requires: libchewing >= 0.2.6

%description chewing
chewing-module : Chewing input method.

%package sunpinyin
Summary: Open X Input Method's SunPinyin wrapper
Group: System/Internationalization
Requires: oxim
Requires: sunpinyin-devel >= 2.0.0

%description sunpinyin
SunPinyin (developed by Sun Asian G11N Center, shipped since Solaris 10,
and opensource'd on OS.o) is a SLM (Statistical Language Model) based IME.
This package includes the wrapper for OXIM(Open X Input Method).

%package unicode
Summary: Open X Input Method Server for unicode module.
Group: System/Internationalization
Requires: oxim

%description unicode
uncide-module : unicode input method.

%package tables-core
Summary: Open X Input Method Server, provided files for core table module.
Group: System/Internationalization
Requires: oxim
#BuildArch: noarch

%description tables-core
chewing-module : Core tables input method.

%prep

rm -rf $RPM_BUILD_ROOT

%setup -q
%ifarch %{arm}
%patch0 -p1 -b .orig
%endif

%build
%ifarch %{arm}
    export CFLAGS="$RPM_OPT_FLAGS -mthumb"
    export CXXFLAGS="$RPM_OPT_FLAGS -mthumb"
    %configure --enable-static=no --enable-qt-immodule=no
%else
%if %{build_meego}
    %configure --enable-static=no --enable-qt-immodule=no
%else
    unset QTDIR && . /etc/profile.d/qt.sh
    %define qt_dir %(echo $QTDIR)
%if %{build_device}
    %configure --enable-static=no --with-qt-dir=${QTDIR} --enable-Device
%else
    %configure --enable-static=no --with-qt-dir=${QTDIR}
%endif
%endif
%endif


%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT make install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} \;

%post
/sbin/ldconfig > /dev/null 2>&1
alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_sysconfdir}/X11/xinit/xinput.d/oxim.conf 99
alternatives --remove xinputrc %{_sysconfdir}/X11/xinit/xinput.d/oxim 2> /dev/null || true

%{_bindir}/update-gtk-immodules %{_host} || :

%if 0%{?fedora}  >=15
#which gtk-query-immodules-3.0-32 && gtk-query-immodules-3.0-32 --update-cache
#which gtk-query-immodules-3.0-64 && gtk-query-immodules-3.0-64 --update-cache
%{_bindir}/gtk-query-immodules-3.0-%{__isa_bits} --update-cache || :
%endif

%preun
if [ "$1" = 0 ]; then
   alternatives --remove xinputrc %{_sysconfdir}/X11/xinit/xinput.d/oxim.conf
fi

%postun

%{_bindir}/update-gtk-immodules %{_host} || :

%if 0%{?fedora}  >=15
%{_bindir}/gtk-query-immodules-3.0-%{__isa_bits} --update-cache || :
%endif
/sbin/ldconfig > /dev/null 2>&1

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%doc {README,COPYING,AUTHORS}
%dir %{_sysconfdir}/oxim
%config %{_sysconfdir}/oxim/*
#%{_bindir}/oxim-conv
%{_bindir}/oxim2tab
%{_bindir}/oxim
%{_bindir}/oxim-agent
%{_libdir}/liboxim.so*
%dir %{_libdir}/oxim
%dir %{_libdir}/oxim/modules
%{_libdir}/oxim/modules/gen-inp.so
%{_libdir}/oxim/modules/gen-inp-v1.so
%dir %{_libdir}/oxim/tables
%{_libdir}/oxim/tables/default.phr
%{_libdir}/oxim/tables/symbol.list
%dir %{_libdir}/oxim/panels
%{_libdir}/oxim/panels/default.*
%{_sysconfdir}/X11/xinit/xinput.d/oxim.conf

%{_libdir}/oxim/immodules/gtk*-im-oxim.so
%{_libdir}/gtk-*.0/immodules/gtk*-im-oxim.so

%dir %{_libdir}/oxim/immodules

%ifnarch %{arm}
%if !%{build_meego}
%{_libdir}/oxim/immodules/qt-im-oxim.so

#%{qt_dir}/plugins/inputmethods/*.so
/*/*/*/plugins/inputmethods/*.so
#%{_qt4_prefix}/plugins/inputmethods/*.so
%endif
%endif

%{_mandir}/man1/oxim.1.gz

%{_datadir}/locale/*/LC_MESSAGES/oxim.mo

%files devel
%{_includedir}/%{name}/*
%{_libdir}/pkgconfig/*

%files chewing
%{_libdir}/oxim/modules/chewing.so

%files sunpinyin
%{_libdir}/oxim/modules/sunpinyin.so

%files unicode
%{_libdir}/oxim/modules/unicode.so

%files tables-core
%dir %{_libdir}/oxim/tables
%{_libdir}/oxim/tables/cnscj.tab
%{_libdir}/oxim/tables/cnsphone.tab


%changelog
* Mon Jan 09 2012 Wind Win <yc.yan@ossii.com.tw> 1.5.4-7
- Option Added: build_device.

* Mon Dec 05 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.4-6
- Define: build_meego added.(no qt3)

* Wed Oct 19 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.4-4
- Restore tray display to untrasparent.

* Tue Oct 18 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.4-3
- Modified for iqqi.

* Fri Oct  7 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.4-2
- Modified for iqqi.

* Thu Oct  6 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.4-1
- Modified for iqqi.

* Mon Sep 19 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.3-9
- Most bug fixes for iqqi.

* Thu Sep 15 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.3-8
- Modified for iqqi.

* Fri Sep 9 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.3-7
- Fix bug for virtual keyboard showing.(run tegaki-oxim -d for keyboard_show)

* Thu Sep 8 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.3-6
- gui_keyboard.c: fixed for wrong dock window position upon kde and lxde.

* Mon Aug 29 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.3-5
- Added for extended panel support(transparent of tray icon).

* Mon Aug 29 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.3-4
- bug fixed.

* Mon Aug 29 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.3-3
- oxim-agent -s bug fixed.

* Mon Aug 22 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.3-2
- Some Bug fixes.

* Mon Aug 15 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.3-1
- Module: sunpinyin added.

* Mon Aug 15 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.2-12
- Fix for wrong candidate area of virtual keyboard.

* Thu Aug 11 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.2-11
- Lot of Bug fixes.

* Wed Aug 10 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.2-10
- Lot of Bug fixes.

* Thu Jul 21 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.2-8
- New packages from original: oxim-unicode, oxim-tables-core.

* Wed Jul 20 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.2-7
- New feature added for keyboard: detect iqqi mode.

* Wed Jul 13 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.2-6
- New feature added for keyboard: detect screen width to auto render keyboard layout.

* Tue Jul 12 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.2-5
- Fix for incorrect of preedit window's cursor location when launch virtual keyboard.

* Thu Jul  7 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.2-4
- Fix for dock keyboard's input(key/mouse) known for window manager.

* Tue Jul  5 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.2-3
- Add check for 1024, 768 resolution (oxvkb).

* Tue Jun 28 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.2-2
- Fixed for gtk-query-immodule error on mocking.

* Mon Jun 27 2011 Wind Win <yc.yan@ossii.com.tw> 1.5.2-1
- Add for Gtk3 IMModule.

* Thu May 12 2011 Wind Win <yc.yan@ossii.com.tw> 1.4.5-12
- Fixed for gui_keyboard: wrong position when drag.

* Mon May  9 2011 Wind Win <yc.yan@ossii.com.tw> 1.4.5-10
- Fixed for virtual keyboard: Auto fix position at middle center.
- Fixed for virtual beyboard: Hide status bar and turn xim to english mode when hide keyboard.

* Wed Apr 27 2011 Wind Win <yc.yan@ossii.com.tw> 1.4.5-10
- oxim-agent new action: -e keyboard_show and -e keyboard_hide

* Wed Apr 27 2011 Wind Win <yc.yan@ossii.com.tw> 1.4.5-8
- bug fix for keyboard.

* Fri Apr 22 2011 Wind Win <yc.yan@ossii.com.tw> 1.4.5-7
- Feature Added for oxvkb.

* Wed Mar 30 2011 Wind Win <yc.yan@ossii.com.tw> 1.4.5-6
- Bug modify.

* Fri Mar 25 2011 Wind Win <yc.yan@ossii.com.tw> 1.4.5-5
- Bug modify.

* Wed Feb 23 2011 Wind Win <yc.yan@ossii.com.tw> 1.4.5-4
- Add -t for tray switch. (oxim)
- fix some bugs.

* Wed Jan 19 2011 Wind Win <yc.yan@ossii.com.tw> 1.4.5-3
- fix XIM_OPEN bug. ( realloc )
- new Panel for keyboard featues.

* Tue Jan 04 2011 Chih-Chun Tu <vincent.tu@ossii.com.tw> 1.4.4-6
- Rebuild for arm arch
- Disable qt3, qt3-devel for arm arch
- Disable IMSETTINGS in oxim-start.sh.in for arm arch

* Fri Dec 24 2010 Chris Lin <chris.lin@ossii.com.tw> 1.4.4-5
- Modify /etc/X11/xinit/xinput.d/oxim -> oxim.conf

* Thu Dec 16 2010 Chris Lin <chris.lin@ossii.com.tw> 1.4.4-4
- Modify gui_keyboard.c.
- Modify ICON.

* Fri Dec 03 2010 Chris Lin <chris.lin@ossii.com.tw> 1.4.4-3
- Rebuild for Fedora 14 64-bit.
- Modify Makefile.am instead of XTEST_LIBS to fix link error of libXext.so.6.

* Wed Sep 15 2010 Kylix Luo <kylix.luo@ossii.com.tw> 1.4.4-2
- Rebuild for Fedora 13 64-bit.
- Add -lXext into XTEST_LIBS to fix link error of libXext.so.6.
- Add gcc-c++ into BuildRequires.

* Thu Apr 22 2010 Wind Win <yc.yan@ossii.com.tw> 1.4.4-1
- Rebuild for new version.

* Wed Mar 18 2009 Wind Win <yc.yan@ossii.com.tw> 1.2.2-1
- Fix for some word correcting.
- Rebuild for new version.

* Thu Nov 27 2008 Wind Win <yc.yan@ossii.com.tw> 1.2.0-4
- Build for most fixes.

* Thu Nov 6 2008 Wind Win <yc.yan@ossii.com.tw> 1.2.0-3
- Rebuild for CVS update.

* Mon Oct 27 2008 Wind Win <yc.yan@ossii.com.tw> 1.2.0-2
- Modify for support I18N of oxim tables' name.

* Tue Oct 14 2008 Wind Win <yc.yan@ossii.com.tw> 1.2.0-1
- Add I18N - zh_TW & zh_CN gettext mo&po files. 
- Add BuildRequire packages.(libXpm, libXft, libXtst)

* Tue Sep 16 2008 Wind Win <yc.yan@ossii.com.tw> 1.1.6-2
- Add man page file - oxim.1

* Fri Sep 5 2008 Wind Win <yc.yan@ossii.com.tw> 1.1.6-1
- Initial RPM build.
