Summary: OXZilla
Name: oxzilla
Version: 0.1.2
Release: 22X
License: Commercial
Group: Development/System
Source0: %{name}-%{version}-ox.tgz
#Patch0:	%{name}-mimetype-oxpackage.patch
Autoreq: no
Requires:	sqlite >= 3.0.0, webkitgtk >= 1.0.0, menu-cache >= 0.2.6, libcurl, libzip, shared-mime-info
Requires:	libXtst >= 1.0.0
Requires:	wireless-tools >= 4.7.2
BuildRequires:	sqlite-devel >= 3.0.0, webkitgtk-devel >= 1.0.0 menu-cache-devel >= 0.2.6 libcurl-devel libzip-devel
BuildRequires:	oxim-devel >= 1.4.4
BuildRequires:  libXtst-devel >= 1.0.0, libtool
# for mock's auto checking
BuildRequires:	wireless-tools >= 4.7.2 

%description
A web-browsing based viewer.

%package gio
Summary: OXZilla plugin for GIO.
Group: System Environment/Libraries
Requires: oxzilla
License: LGPLv2+

%description gio
Files provided for build OXZilla plugin for GIO.

#%package epub
#Summary: OXZilla plugin for EPUB.
#Group: System Environment/Libraries
#Requires: oxzilla
#License: Commerical

#%description epub
#A plugin to manipulate epub.

%package oxim
Summary: OXZilla plugin for OXIM
Group: System Environment/Libraries
Requires: oxzilla
License: Commerical

%description oxim
A plugin to manipulate oxim.

%package jscollections
Summary: OXZilla JavaScript plugins.
Group: Development/Libraries
Requires: oxzilla
License: GPL, MIT, BSD

%description jscollections
A sets of JavaScript collections for OXZilla plugins.

%package wireless
Summary: OXZilla plugin for WIRELESS.
Group: System Environment/Libraries
Requires: oxzilla
License: Commerical

%description wireless
A plugin to manipulate system wireless info.

%package devel
Summary: OXZilla development files
Group: Development/Libraries
Requires: oxzilla
License: Commercial

%description devel
Files provided for build oxzilla plugins.


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
./autogen.sh
%configure \
    --enable-static=no \
    --enable-gio=yes \
    --enable-epub=no \
    --enable-oxim=yes \
    --enable-wireless=yes
%{__make} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT make install-strip
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} \;

%post

%preun

%postun
/sbin/ldconfig > /dev/null 2>&1

%clean 
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/oxzsh
%{_bindir}/oxzencode
%{_libdir}/liboxzilla*
%dir %{_libdir}/oxzilla/jsplugins

%files gio
%{_libdir}/oxzilla/jsplugins/gio.*

#%files epub
#%{_libdir}/oxzilla/jsplugins/epub.*

%files oxim
%{_libdir}/oxzilla/jsplugins/oxim.*

%files jscollections
%{_libdir}/oxzilla/js/*

%files wireless
%{_libdir}/oxzilla/jsplugins/wireless.*

%files devel
%{_libdir}/pkgconfig/*
%{_includedir}/%{name}/*
%{_bindir}/oxzilla-new-functions
%{_datadir}/%{name}/*


%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Fri Jul  8 2011 Wilson Tien <wilson@ossii.com.tw> - 0.1.2-22X
- src/oxzilla/oxzilla.c: decode the AES coded OXZ file (which is a ZIP file 
  of the oxzilla application) on the fly, then use FUSE to mount the decoded
  ZIP image (in memory). FUSE is using thread, so there must be two processes,
  one to maintain the FUSE mounted work, and the other to execute normal
  oxzilla application in the UNZIPPED directory.

* Thu Jun 16 2011 Wilson Tien <wilson@ossii.com.tw> - 0.1.2-22
- src/oxzilla/oxzilla.c: add AES 128b decoding mechanism for program ends 
  with .oxz.
- src/oxzilla/oxzencode.c, src/oxzilla/Makefile.am: add AES 128b encoding 
  program `oxzencode' be part of oxzilla package. USE libgcrypt. 
- src/include/key.h: define AES 128b KEY to be used by oxzilla(consumer)
   and oxzencode(producer).

* Tue Jun 14 2011 Wilson Tien <wilson@ossii.com.tw> - 0.1.2-21
- src/jsplugin/wireless/wireless.c: each new node need to do initialization.

* Mon Jun 13 2011 Wind Win <yc.yan@ossii.com.tw> - 0.1.2-20
- Add parameter: -d --desktop Let OXZilla lunched as DESKTOP mode.

* Mon Jun 13 2011 Wind Win <yc.yan@ossii.com.tw> - 0.1.2-19
- Add parameter: -o --override_redirect Let OXZilla not under the 
  control of the window manager.

* Thu Jun  2 2011 Wind Win <yc.yan@ossii.com.tw> - 0.1.2-18
- Add BuildRequire: WirelessTools for mock's checking.

* Fri May 26 2011 Wilson Tien <wilson@ossii.com.tw> - 0.1.2-17
- src/jsplugin/wireless/wireless.c, src/jsplugin/wireless/Makefile.am: 
  provide a wireless plugin, now the system wireless can be accessed by 
  'get_wireless_list()'. It returns a vector of entries representing each 
  wireless entry, each entry contains 3 elements: 1st is the name of the 
  wireless connection, 2nd is whether this connection requires encryption 
  or not, 3rd is the mode whether it is wep, wpa, wpa2 for encryption 
  connection, or none for non-encryption connection.
- src/jsplugin/wireless/iwlib.h, src/jsplugin/wireless/wireless.h: Code
  copied directly from wireless_connection package without change.
- Makefile.am, configure.ac: modified oxzilla package info to support 
  wireless plugin.

* Thu May 26 2011 WindWin <yc.yan@ossii.com.tw> - 0.1.2-16
- oxim_keyboard.js: fix bug.

* Tue May 24 2011 WindWin <wilson@ossii.com.tw> - 0.1.2-15
- oxim_keyboard.js: add support for <textarea>. 

* Tue May  13 2011 Wind Win <yc.yan@ossii.com.tw> - 0.1.2-14
- src/jsbuildin/oxzFunc-exec.c: implement exec_sync_with_output(), that will 
  return null if failed, o/w return stdout output as vector.

* Thu May 12 2011 Wilson Tien <wilson@ossii.com.tw> - 0.1.2-13
- src/jsbuildin/oxzFunc-exec.c: change it back to use execvp for async-exec. 
  parse argv[0] for backward compatibility.

* Tue May  3 2011 Wind Win <yc.yan@ossii.com.tw> - 0.1.2-12
- Bug fix: -j with filename error on malloc.


* Tue May  3 2011 Wind Win <yc.yan@ossii.com.tw> - 0.1.2-11
- Added function: file_monitor.
- Added js: oxim_keyboard.js

* Tue Mar  1 2011 Wilson Tien <wilson@ossii.com.tw> - 0.1.2-9
- src/jsplugins/epub/epub.c: Fix problem in the epub plugin when rootfile 
  (inside META/container.xml) is namespace qulified. That will cause 
  oxepubview to crash since it does not know what to do when rootfile 
  cannot be found.

* Tue Mar  1 2011 Wilson Tien <wilson@ossii.com.tw> - 0.1.2-8
- src/jsbuildin/oxzFunc-exec.c: Make exec_sync() return the excuted program
  exit code. if abnormally exit (such as Ctl-c), it will return null. 
  Change exec_async() to use execvp() instead and always return null.

* Tue Feb  1 2011 Wilson Tien <wilson@ossii.com.tw> - 0.1.2-7
- src/jsbuildin/Makefile.am, src/jsbuildin/Makefile.in, 
  src/jsbuildin/oxzFunc-loadmodule.c, src/jsbuildin/oxzJSBuildin-init.c:
  Create a new Javascript buildin `loadmodule' which will load specified
  plugin. An environmental variable `OXZILLA_PLUGIN_PATH' is introduced to 
  specify the order to search for the plugin, if this is not set, then try
  ${HOME}/.oxzilla/jsplugins first, then /usr/lib/oxzilla/jsplugins.
- src/lib/Makefile.in, src/lib/Makefile.am, src/lib/oxzWebView.c,
  src/oxzilla/oxzsh.c: Disable the scanning of plugins (oxZJSPluginsInit).

* Mon Jan 24 2011 Wind Win <yc.yan@ossii.com.tw> 0.1.2-6
- fix: hang up when play flash movie.
- add: -j first run javascript file content when oxzilla run.

* Thu Jan 20 2011 Wind Win <yc.yan@ossii.com.tw> 0.1.2-5
- enable plugin.

* Fri Dec 24 2010 Kylix Lo <kylix.lo@ossii.com.tw> 0.1.2-4
- Add BuildRequires oxim-devel >= 1.4.4

* Fri Dec 17 2010 Wind Win <yc.yan@ossii.com.tw> 0.1.2-1
- Add EZip.class.js
- Add ContentScroller.class.js
- Update ezip module
- Class-zip module bug modify.

* Thu Nov 25 2010 Sean Lin <sean@ossii.com.tw> 0.1.1-20
- Add jquery-1.4.4 support.

* Wed Mar 31 2010 Wind Win <yc.yan@ossii.com.tw> 0.1.1-17
- Fix wrong screen's width&height when use --fullscreen.

* Tue Mar 30 2010 Wind Win <yc.yan@ossii.com.tw> 0.1.1-15
- Add jsplugin: EPUB.

* Fri Mar 26 2010 Wind Win <yc.yan@ossii.com.tw> 0.1.1-12
- fix bug: program unnormal exit when system's menu contains only a null ('\0') char.

* Mon Mar 22 2010 Wind Win <yc.yan@ossii.com.tw> 0.1.1-9
- Add jquery plugin: colorbox.

* Fri Mar 5 2010 Wind Win <yc.yan@ossii.com.tw> 0.1.1-5
- Make corrected of every GROUP of packages.
- Add jsplugin: GIO.

* Thu Nov 19 2009 Wind Win <yc.yan@ossii.com.tw> 0.1-1
- Building on first time.
