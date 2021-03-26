%define _qt4_qmake qmake-qt4
%define _qt4_datadir %{_datadir}/qt4
%define _qt4_plugindir %{_libdir}/qt4/plugins
%define _qt4_translationdir %(qmake-qt4 -query QT_INSTALL_TRANSLATIONS)

Name:       libmeegotouch
Summary:    MeeGo Touch Framework
Version:    0.21.17
Release:    1
Group:      System Environment/Libraries
License:    LGPLv2
URL:        http://meego.gitorious.org/meegotouch/libmeegotouch
# extracted from http://repo.meego.com/MeeGo/builds/1.0.99/1.0.99.0.20101005.1/core/repos/source/libmeegotouch-0.20.25-7.1.src.rpm
Source0:    %{name}-%{version}.tar.bz2
Source1:    libmeegotouch.sh
Source2:    mthemedaemon.desktop
Patch1:     libmeegotouch-0.21.17-fedora.patch
Patch2:     libmeegotouch-0.21.17-genrb.patch
Requires:   meegotouch-theme >= 0.20.79
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(QtOpenGL)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(gstreamer-base-0.10)
BuildRequires:  pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  icu

%description
Qt based MeeGo Touch Framework for developing touch based user interfaces.

%package devel
Summary:    MeeGo Touch Framework development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the files necessary to develop applications using
the Meego Touch Framework.

%package -n meegotouch-demos
Summary:    MeeGo Touch Framework demos
Group:      System Environment/Libraries
Requires:   %{name} = %{version}-%{release}
BuildRequires:   desktop-file-utils

%description -n meegotouch-demos
This package contains demos for the MeeGo Touch Framework.

%package -n meegotouch-demos-tests
Summary:    MeeGo Touch Framework demos tests
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   meegotouch-demos

%description -n meegotouch-demos-tests
This package contains demos tests for the MeeGo Touch Framework.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
sed -e's#^\(.*M_TRANSLATION_DIR = \).*$#\1%{_qt4_translationdir}/meegotouch#g' -i ./mkspecs/features/meegotouch_defines.prf.in
sed -i 's|_exit|exit|' src/corelib/core/mapplication.cpp src/corelib/core/msystemdirectories.cpp
sed -i '1i #include <unistd.h>' src/corelib/core/mdebug.cpp src/corelib/core/msyslogclient.cpp src/corelib/core/mapplicationservice_p.cpp src/corelib/scene/mscene.cpp src/extensions/mashup/appletcommunication/mappletclient.cpp
sed -i 's|-Werror|-Wno-error|' mkspecs/common.pri
sed -i 's|return false|return NULL|' src/extensions/applicationextension/mapplicationextensionloader.cpp

%build
export QTDIR=%{_libdir}/qt4
./configure \
   -prefix %{_prefix} \
   -libdir %{_libdir} \
   -release \
   -testable

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make install INSTALL="install -p" INSTALL_ROOT=%{buildroot}

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/libmeegotouch.sh
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/xdg/autostart/mthemedaemon.desktop

# Avoid mmoc confusion: ship binary on IA32
rm -f %{buildroot}%{_bindir}/mmoc.pl

mkdir -p %{buildroot}%{_localstatedir}/cache/meegotouch

%find_lang %{name} --with-qt --without-mo
%find_lang widgetsgallery --with-qt --without-mo

rm -rf %{buildroot}%{_datadir}/meegotouch-demos-widgetsgallery-tests

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig
mkdir -p %{_localstatedir}/cache/meegotouch

%postun
/sbin/ldconfig
if [ -d /var/cache/meegotouch ]; then
rm -rf /var/cache/meegotouch
fi

%files -f %{name}.lang
%doc README LICENSE.LGPL
%dir %{_sysconfdir}/meegotouch
%config(noreplace) %{_sysconfdir}/meegotouch/themedaemonpriorities.conf
%config(noreplace) %{_sysconfdir}/profile.d/libmeegotouch.sh
%config(noreplace) %{_sysconfdir}/xdg/autostart/mthemedaemon.desktop
%{_bindir}/mservicemapper
%{_bindir}/mthemedaemon
%{_libdir}/libmeegotouchcore.so.*
%{_libdir}/libmeegotouchextensions.so.*
%{_libdir}/libmeegotouchsettings.so.*
%{_libdir}/libmeegotouchviews.so.*
%{_libdir}/libmeegotouchpreloader.so.*
%dir %{_libdir}/meegotouch
%dir %{_libdir}/meegotouch/applets
%{_libdir}/meegotouch/applets/mappletrunner
%dir %{_libdir}/meegotouch/applicationextensions
%{_libdir}/meegotouch/applicationextensions/mapplicationextensionrunner
%{_datadir}/meegotouch/
%dir %{_qt4_translationdir}/meegotouch
%{_qt4_translationdir}/meegotouch/libmeegotouch.qm
%dir %{_localstatedir}/cache/meegotouch

%{_datadir}/dbus-1/services/com.nokia.mservicefw.service
%{_datadir}/dbus-1/services/com.nokia.widgetsgallery.service

%files devel
%{_bindir}/applicationextensiondemo
%{_bindir}/imgcachegen
%{_bindir}/dui-rename-files
%{_bindir}/dui-rename-symbols
%{_bindir}/m-servicefwgen
%{_bindir}/mapplettester
%{_bindir}/mapplicationextensiontester
%{_bindir}/mgen
%{_bindir}/mmoc
%{_bindir}/mnotificationstresstest
%{_bindir}/mnotificationtool
%{_bindir}/mcssvalidator
%{_includedir}/meegotouch
%{_libdir}/libmeegotouchcore.prl
%{_libdir}/libmeegotouchcore.so
%{_libdir}/libmeegotouchextensions.prl
%{_libdir}/libmeegotouchextensions.so
%{_libdir}/libmeegotouchsettings.prl
%{_libdir}/libmeegotouchsettings.so
%{_libdir}/libmeegotouchviews.prl
%{_libdir}/libmeegotouchviews.so
%{_libdir}/libmeegotouchpreloader.prl
%{_libdir}/libmeegotouchpreloader.so
%{_libdir}/pkgconfig/meegotouch-boostable.pc
%{_libdir}/pkgconfig/meegotouch.pc
%{_libdir}/pkgconfig/meegotouchcore.pc
%{_libdir}/pkgconfig/meegotouchsettings.pc
%{_libdir}/qt4/mkspecs/features/*.prf
%{_datadir}/themes/base/meegotouch/mapplettester/

%files -n meegotouch-demos -f widgetsgallery.lang
%{_bindir}/widgetsgallery
%{_libdir}/meegotouch/applicationextensions/libappletinventory-fakeinstallationsource.so
%{_libdir}/meegotouch/applicationextensions/libapplicationextensiondemo-demoextension.so
%{_libdir}/meegotouch/applicationextensions/libapplicationextensiondemo-demoextension2.so
%{_datadir}/applications/widgetsgallery.desktop
%{_datadir}/applications/widgetsgallery-boosted.desktop
%{_datadir}/meegotouch/applicationextensions/appletinstallationsource.desktop
%{_datadir}/meegotouch/applicationextensions/applicationextensiondemo-demoextension.desktop
%{_datadir}/meegotouch/applicationextensions/applicationextensiondemo-demoextension2.desktop
%{_datadir}/widgetsgallery/
%{_datadir}/themes/base/meegotouch/icons/icon-l-widgetsgallery.png
%{_datadir}/themes/base/meegotouch/widgetsgallery/
%{_qt4_translationdir}/meegotouch/widgetsgallery.qm

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.21.17
- Rebuild for Fedora
* Wed Sep 07 2011 Jon Nordby <jonn@openismus.com> - 0.21.17-2
- Remove contextkit dep on Fedora
* Sun May 29 2011 Jon Nordby <jonn@openismus.com> - 0.21.17-1
- Update to 0.21.17
* Wed May 25 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.21.17-0
- Update to 0.21.17
* Thu Apr  7 2011 Miroslav Safr <miroslav.safr@tieto.com.com> - 0.21.4
- BMC#15199 - Update libmeegotouch to 0.21.4 to make theme working
- added Boot_sequence_is_broken_after_erase-user-data_flashing_MR_1709.patch
  Only time out when not receiving any data from the themedaemon for more than
  15 seconds, then print out a warning and retry
- added Requires meegotouch-demos-l10n to meegotouch-demos
* Tue Apr  5 2011 Miroslav Safr <miroslav.safr@tieto.com.com> - 0.21.1
- disabled explicitely meegographicssystem: the feature is autodetected since
  latest update and causes segfaults on ARM
* Fri Apr  1 2011 Miroslav Safr <miroslav.safr@tieto.com.com> - 0.21.1
- BMC#15199 - Update libmeegotouch to 0.21.1-1
- added Requires meegotouch-demos to meegotouch-demos-tests
- added disable_ut_mlabel_test.patch
- removed patches:
  rely_on_QT_ARCH_for_mmoc.patch - merged upstream
  BMC_12753_temp_solve_statusbar_height.patch - merged upstream
  BMC_12929_meegographicssystem.patch - merged upstream
- removed patches backported from 0.20.95-1 previously:
  BMC13246_0001-New-MDeviceProfile-orientationFromAngle.patch
  BMC13246_0002-Changes-Code-cosmetics.-Removing-trailing-whitespace.patch
  BMC13246_0003-Changes-MWindow-Remove-assumption-that-Angle0-is-Lan.patch
  BMC13246_0004-Changed-MTheme-remove-assumption-that-default-orient.patch
  BMC13246_0005-Changed-MStyleSheetAttribute-consider-device-s-nativ.patch
  BMC13246_0006-Changed-MSceneManager-remove-assumption-that-native-.patch
  BMC13246_0007-Changed-MOrientationTrackerPrivate-remove-assumption.patch
  BMC13246_0008-New-Adding-a-default-portrait-device-configuration.patch
  BMC13246_0009-Revert-Changes-Do-not-rotate-the-dim-layer-effect-wi.patch
* Mon Mar 21 2011 Shane Bryan <shane.bryan@linux.intel.com> - 0.20.89
- BMC#13246 - Assumes all displays start in Landscape orientation
  added patches backported from fixes merged upstream (as of 0.20.95-1):
  - BMC13246_0001-New-MDeviceProfile-orientationFromAngle.patch
  - BMC13246_0002-Changes-Code-cosmetics.-Removing-trailing-whitespace.patch
  - BMC13246_0003-Changes-MWindow-Remove-assumption-that-Angle0-is-Lan.patch
  - BMC13246_0004-Changed-MTheme-remove-assumption-that-default-orient.patch
  - BMC13246_0005-Changed-MStyleSheetAttribute-consider-device-s-nativ.patch
  - BMC13246_0006-Changed-MSceneManager-remove-assumption-that-native-.patch
  - BMC13246_0007-Changed-MOrientationTrackerPrivate-remove-assumption.patch
  - BMC13246_0008-New-Adding-a-default-portrait-device-configuration.patch
  - BMC13246_0009-Revert-Changes-Do-not-rotate-the-dim-layer-effect-wi.patch
  added new DefaultPortrait.conf to .spec file
* Mon Mar 21 2011 Fathi Boudra <fathi.boudra@nokia.com> - 0.20.89
- removed BMC14407_MTextEdit_prompt_only_visible_when_text_edit_not_focused.patch
  as it has been rejected upstream. The current behavior is intentional
* Wed Mar 16 2011 Fathi Boudra <fathi.boudra@nokia.com> 0.20.89
- added BMC14407_MTextEdit_prompt_only_visible_when_text_edit_not_focused.patch
  Thanks to Robin Burchell
* Tue Mar 15 2011 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.89
- updated BMC_12753_temp_solve_statusbar_height.patch so it solves the same
  problem in 2nd place where the scene is resized
* Fri Mar 11 2011 Fathi Boudra <fathi.boudra@nokia.com> - 0.20.89
- added BMC_12929_meegographicssystem.patch to define M_USE_OPENGL when
  OpenGL ES 2 support is availble in QT_CONFIG
* Wed Mar  2 2011 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.89
- updated to 0.20.89-1
- removed  integrated add_iCDK_config_target.patch
- BMC#10384 - meego-im-uiserver does not register to qttas-server
  added TDriver support by  ./configure -testable
- BMC#8510 - libmeegotouchviews behaves both a plugin and a library
  moved .so files to devel and marked obsoletes with older versions
- BMC#8268 - added BMC_8268_show_statusbar_on_n900.patch
- merged arm_ftbfs_egl.patch to arm_egl_visibility.patch
* Thu Feb 24 2011 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.87
- Update meegotouch components to week 8 (BMC#13802)
- removed obsolete patch incorrect_libmeegotouch_version.patch
- rebased rely_on_QT_ARCH_for_mmoc.patch
- removing  meegotouch-config-default package - not needed anymore
* Tue Feb 22 2011 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.84
- BMC#13632 - Update libmeegotouch 0.20.84-1
- BMC#12975 - libmeegotouch Requires gtk2 (generated from spectacle)
* Fri Feb 18 2011 Brad Peters <brad.t.peters@intel.com> 0.20.83
- BMC#10383 - Added an iCDK.conf to targets directory
* Thu Feb 10 2011 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.83
- BMC#13441 - Update meegotouch components to week 6
  - updated to 0.20.83-1
* Sat Feb  5 2011 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.81
- BMC#13257 - Update meegotouch components to week 5
  - updated to 0.20.81-1 (depends on meegotouch-theme 0.20.72)
* Thu Feb  3 2011 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.80
- updated libmeegotouch to latest tag 0.20.80-1 (depends on meegotouch-theme 0.20.71)
- removed fixed patch incorrect_libmeegotouch_version.patch
* Thu Feb  3 2011 Fathi Boudra <fathi.boudra@nokia.com> - 0.20.77
- removed QtServiceFramework build requires to avoid OBS extra build cycles
* Tue Feb  1 2011 Fathi Boudra <fathi.boudra@nokia.com> - 0.20.77
- added QtServiceFramework and xcomposite build requires
- replaced contextprovider-1.0 by contextsubscriber-1.0 >= 0.5.25
- used UseAsNeeded: no
- avoided mmoc confusion: ship script on ARM and binary on IA32
- added rely_on_QT_ARCH_for_mmoc.patch to select mmoc executable based on
  QT_ARCH (BMC#13202)
- added incorrect_libmeegotouch_version.patch, it should be 0.20.77 instead of
  0.20.76
* Mon Jan 31 2011 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.77
- updated libmeegotouch to 0.20.77
- cleaning temporary widgetsgallery_number.patch
- changed obsoletes for all lower versions than current
- added benchmark dependency on meegotouch-demos
- cleaned duplicated files and cleaned previous fix (BMC#8109) widgetsgallery,mthemedaemon,mservicemapper
* Tue Jan 25 2011 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.76
- BMC#8109 - libmeegotouch package does not mark file conflicts with older libmeegotouch-devel
  - added confilcts for devel package
- updated libmeegotouch to latest tag 0.20.76-1 (depends on meegotouch-theme 0.20.68)
* Wed Jan 19 2011 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.74
- updated libmeegotouch to latest tag 0.20.74-1 (depends on meegotouch-theme 0.20.68)
- BMC#12150 - touch failed to work sometimes (as a part of the fix)
* Fri Jan  7 2011 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.73
- updated libmeegotouch to latest tag 0.20.73 (depends on meegotouch-theme 0.20.67)
* Fri Jan  7 2011 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.72~1
- BMC#12171 - Update libmeegotouch to latest tag 0.20.71 or newer (0.20.72+git201001101555)
- removed integrated patch 1142.patch
- added patch to show version in widgetsgallery caption
- added libmeegotouch-tests dependency on fi translation because in ut_mcalendar we are testing swithcing beteen en and fi
* Tue Jan  4 2011 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.70-1
- dependent on meegotouch-theme 0.20.66
- BMC#7117:Default configuration causes unwanted gconf warnings. - fixed
* Tue Dec 21 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.66-2
- removed  dbus-1 dependency
- update to 0.20.66-2 - additional changes needed for BMC#8164
- added temporary_enable_qdbus_link.patch to fix QDBus dependency
* Wed Dec 15 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.66
- BMC#10742: updated to release 0.20.66-1
- dependent on meegotouch-theme 0.20.63
- BMC#8807 - We should integrate icu 4.6
  - properly handled icu data directory path (so the build does not have to be broken always when icu is updated)
- #8164 - [FEA] User Interface elements agnostic of display resolution
  - nCDK config uses autodetect for X,Y screen resolution
* Wed Dec 15 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.63
- BMC#10742: updated to release 0.20.63-1 - needed by libmeegotouch
* Wed Dec 15 2010 Wang Quanxian <quanxian.wang@intel.com> 0.20.64
- icu has been upgraded to 4.6 and libmeegotouch will change to icu 4.6 dependency. BMC#8807
* Thu Dec  9 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.64
- BMC#10717: updated to release 0.20.64-1
- updated headers list
* Mon Nov 29 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.60
- BMC#10520 - Orientation from accelerometer not working
- BMC#10109 - [REG]When the user's press combination key or orientation rotate,the Application ui is unable to rotated.
- updated to release 0.20.60-1
- removed integrated patches: unit-tests-init.patch,allow_rotation_for_nCDK_configuration.patch
- removed non-existing header files from .spec file
* Tue Nov 23 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.54
  BMC#9191 - Screen orientation is wrong on nCDK hardware
- added unit-tests-init.patch to fix arm build
* Thu Nov 18 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.54
- updating to release tag 0.20.54-1
- removed ncdk_device_configuration.patc - cherry-picked upstream
- removed patch arm_read_write.patch - merged upstream
- removed unneccesary file fixes from spec files (fixed upstream)
- removed animatedlayout example
- BMC#8938: Linker error when trying to compile MTF application with i586
  sysroot/toolchain. changed libmeegotouch linking from LFLAGS_RPATH to
  LIBS += -L$${M_LIB_DIR}
- meegotouch-demos-tests package separated so eat-self test does not run
  the timedemo when only demos package is installed
* Thu Nov 11 2010 Fathi Boudra <fathi.boudra@nokia.com> 0.20.51
- Add nCDK configuration file (BMC#9955)
* Thu Nov 11 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.51
- BMC#8807 - Too old ICU package
- fix build
* Thu Nov 11 2010 Wang Quanxian <quanxian.wang@intel.com> 0.20.51
- Since icu is upgrade to 4.5.2, the pc mechanism is changed
- Change to adapt icu 4.5.2
* Tue Nov  9 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.51
- BMC#9902:Spec file post errors for libmeegotouch-tests
  - fdupes order in spectacle
  - disabled /usr/sbin/locale-gen in %%post because it has to generated different way
- version numbers corrention in changes file
- temporary meegotouch-theme dependency change restored
* Mon Nov  8 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.51
- cleaning unpackaged files
- moved fdupes post install before post for test package
* Fri Nov  5 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.51
- added correction patch for arm build arm_read_write.patch
  * Thu Nov 04 2010 Kaitlin Rupert <kaitlin.rupert at intel.com> 0.20.51
- Temporarily change the meegotouch-theme version dependency to enable build
* Thu Nov  4 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.51
- updated to release 0.20.51-1
* Mon Nov  1 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.50
- updated to release 0.20.50-1
* Tue Oct 26 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.49
- updated to release 0.20.49-1
* Wed Oct 20 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.48
- added gst-plugins-good and gst-plugins-base to tests
- commented out dependency on locales, gstreamer0.10-plugins-good because the package is not available yet
* Tue Oct 19 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.48
- Added Requires: locales, gstreamer0.10-plugins-good to libmeegotouch-tests so
  more unit tests will pass
- Clean up changelog formatting
* Thu Oct 14 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.48
- BMC#4812 - Mthemedaemon is missing in startup session
- removed OnlyShowIn=X-MEEGO-HS so it will execute everywhere
- updated include files list in spec file
- updated to release 0.20.48-1
* Fri Oct  8 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.46
- BMC#8109 -  libmeegotouch package does not mark file conflicts with older
  libmeegotouch-devel
  addded Conflicts: libmeegotouch-devel < 0.20.46-1
* Fri Oct  8 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.46
- cleaning removed integrated patches: unit_tests_init.patch,
  gconf_default_config.patch
- BMC#3462 - All meegotouch apps need LD_AS_NEEDED unset
- BMC#5126 - Missing version less sonames for libraries in the package
  added libmeegotouch-rpmlintrc to handle the .so files in non devel pacakage
  libmeegotouchviews.so moved from devel package to library package
  views are loaded in runtime so the .so file should be in library package
* Wed Oct  6 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.46
- updated to release 0.20.46-1
- removed integrated patches: unit_tests_init.patch, gconf_default_config.patch
- removed ut_mimagedirectory-dir dummy files from spec
* Fri Oct  1 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.45
- BMC#6423 - libmeegotouch new upstream release 0.20.45~1
- removed patches which were integrated to master or rejected:
  include_order.patch,change_minor_version.patch, fix_russelville_conf.patch
- removed plainqt and plainqt files
- removed duplicated files
- BMC#7812 -  Build break if HAVE_GCONF is not defined
- BMC#6871 - libmeegotouch: revise profile for russellville in devices.conf
- mcssparser tool added
- new unit tests added
- added %%postun
* Thu Sep 30 2010 Fathi Boudra <fathi.boudra@nokia.com> 0.20.42
- Split libmeegotouch-l10n package (BMC#6068)
- Remove libmeegotouch-docs package, it's empty
- Clean up %%files tag and be more verbose
- Remove ts files installation - not needed
  * Thu Sep 30 2010 Kaitlin Rupert <kaitlin.rupert at intel.com> 0.20.42
- Fix meegotouch version: make sure minor version im prf file reflects actual
  version
* Thu Sep 30 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.42
- Update to 0.20.42 (BMC#6423)
- Add gconf_default_config.patch which allows to run libmeegotouch without any
  configuration in gconf
- BMC#4812 - Mthemedaemon is missing in start up session
- BMC#6679 - Missing default gconf schemas for handset installs of libmeegotouch
- BMC#6594 - themedaemon crashes if target name gconf value is missing
- BMC#6595 - Themedaemon fails to parse meegotouch-theme default theme on host
  builds
- Separate meegotouch-config-default package which should be added to all images
- Reformat unit_tests_init.patch
* Thu Sep 30 2010 Miroslav Safr <miroslav.safr@tieto.com.com> 0.20.38
- Update to 0.20.38
- Add unit_tests_init.patch: fix 2 unit tests build for armv7
- Removed Requires libmeegotouch dependency between meegotouch-config packages
- Add patch for ARM visibility EGL issue: disable
  KHRONOS_APICALL __attribute__((visibility("default"))) option
- Re-add meegotouch-config-default package but without any relationship to
  libmeegotouch (schemas files in  installed and rpm requires to package it)
- Clean up gconf settings after uninstalation
- Requires meegotouch-config relation removed so the configuration
  (schemas file) is optional
- Fix EGL visibility compilation problem for armv7 build
- Move mthemedaemon.desktop from theme to libmeegotouch
- Change packages deployment and introduce meegotouch-config packages
  libmeegotouch
  libmeegotouch-benchmarks
  libmeegotouch-debuginfo
  libmeegotouch-devel
  libmeegotouch-docs
  libmeegotouch-l10n
  libmeegotouch-qtstyle
  libmeegotouch-tests
  meegotouch-config-default
  meegotouch-demos
  meegotouch-demos-l10n
* Mon Sep 27 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.25
- BMC#6871 - fix Russelville device settings to properly align with screen res
* Thu Sep 16 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.25
- BMC#3921 - fix battery and settings icons, also fix decorator icons
* Fri Aug 27 2010 Fathi Boudra <fathi.boudra@nokia.com> 0.20.25
- Add include_order.patch to fix build failure with Qt
- Add arm_ftbfs_egl.patch to fix buidl failure on ARM when using EGL
  Thanks to Carsten Valdemar Munk
- Various cleanup in the yaml files
* Wed Aug 11 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.25
- Remove QtMultimedia BuildRequires, as it is not needed
- Change mkspecs install location due to qt update
* Tue Jul 13 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.25
- Add re-enable_code_to_set_orientation.patch to allow for orientation changes
* Fri Jul  9 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.25
- Update to release tag 0.20.25-2
- Remove obsolete patches:
  Remove-QtStyle-icons-from-desktop.patch
- This update fixes BMC #2185, BMC #3564, BMC #3482
* Fri Jul  9 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.15
- Fix compile issues with updated version of gcc.
* Sun Jun 20 2010 Carsten Munk <carsten@maemo.org> 0.20.15
- Fix ARM build stalls within OBS builds.
* Wed Jun 16 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.15
- Add a patch to revert commit c90025d6bde5184346d8bbe148effd47aef354af
  This commit causes a white screen to appear when trying to switch apps
- Move WidgetsGallery and other example related files into devel package
- Clean up some rpmlint errors (marking files as config files, adding provides)
- Consolidate device config patches into one patch:
  Add libmeegotouch-0.20.1-Add-various-devices-to-device-conf.patch
  Remove Adding-various-Moorestown-and-Menlow-devices-to-the.patch
  Remove libmeegotouch-0.20.1-Add-russelville-slate-conf.patch
- Add showStatusBar=true to Aava device config
* Thu Jun  3 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.15
- Update to release tag 0.20.15-1
* Thu May 27 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.12.1
- Update to release tag 0.20.12.1-1 - resolves BMC#545
- Remove doxygen from BuildRequires list
- Remove Fix-Calculate-rotation-and-position-per-device-prof.patch
- Remove Add-new-icon-property-on-MButton.patch
- Remove cell-in-the-last-visible-row-but-not-the-first-colum.patch
- Remove Fix-locateVisibleRowAt-calculation-error.patch
* Tue May 25 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.10
- Add an Obsoletes to ensure libdui is not also installed
- Remove "unset LD_AS_NEEDED" from spec file
* Wed May 19 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.10
- Update to release 0.20.10
- Patch: libmeegotouch-0.20.10-Workaround-icu-config-bug.patch
- Patch: libmeegotouch-0.20.10-missing-Epoch-function.patch
* Mon May 17 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.8
- Update spec to create /var/cache/meegotouch
* Tue May 11 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.8
- Update Add-new-icon-property-on-MButton.patch
- Move libmeegotouchqtstyleplugin.so to its own package
- Don't show QtStyle related icons on the desktop
- Add two patches to fix BMC 545:
-  cell-in-the-last-visible-row-but-not-the-first-colum.patch
-  Fix-locateVisibleRowAt-calculation-error.patch
* Mon May 10 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.8
- Update to release 0.20.8
- Also check /usr/share/pixmap for icons
* Thu May  6 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.7
- Update to release 0.20.7
- Add patch to use icons in the XFreeDesktop standard location
* Thu Apr 29 2010 Carsten Munk <carsten@maemo.org> 0.20.2
- ARM build fixes:
- Patch: ARMv5 build failure due to VFP assumption
- Removed pkgconfig(gl) as dependancy, pkgconfig(QtOpenGL) will pull either GLES1/2 or GL headers+libraries in.
- Removed pkgconfig(mesa-libEGL-devel) as dependancy for same reason.
* Thu Apr 29 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.2
- Patch:  Update device config for Russelville, add device config for slate
- Remove -plainqt plugin from configure due to rendering issues
* Tue Apr 27 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.2
- Patch:  Add device config for Russelville
- Update to release 0.20.2-1
- Convert file to spectacle
- Remove duitheme requires
- Remove epoch
* Wed Apr 21 2010 Kaitlin Rupert <kaitlin.rupert@intel.com> 0.20.1
- Initial import of libmeegotouch - package based on libdui release 0.20.1
- Renamed to match namespace change
