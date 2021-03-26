Name:           etoys
Version:        5.0.2408
Release:        15
Summary:        A media-rich model, game, and simulation construction kit and authoring tool
Vendor:         Viewpoints Research
Group:          Development/Languages
License:        ASL 2.0 and MIT
URL:            http://squeakland.org/
BuildArch:      noarch
Source0:        http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.gz
Source2:        etoys.desktop
Source3:        etoys.png
# Fall back on ALSA backend when pulse is not available
Patch0:         launcher-alsa.patch
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
Requires:       squeak-vm >= 3.10
Requires:       shared-mime-info
Source10:       etoys-langpack-zh_TW.zip
Source11:       http://etoys.squeak.org/svn/trunk/Etoys/fonts/FontSimplifiedChineseEnvironment.sar

%description
Squeak Etoys was inspired by LOGO, PARC-Smalltalk, Hypercard, and starLOGO. It 
is a media-rich authoring environment with a simple powerful scripted object 
model for many kinds of objects created by end-users that runs on many 
platforms, and is free and open source. It includes 2D and 3D graphics, images, 
text, particles, pres-entations, web-pages, videos, sound and MIDI, etc. It 
includes the ability to share desktops with other Etoy users in real-time, so 
many forms of immersive mentoring and play can be done over the Internet.

%package       sugar
Summary:       Sugar activity wrapper for Etoys
Group:         Sugar/Activities
Requires:      sugar
Requires:      sugar-presence-service
Requires:      %{name} = %{version}-%{release}

%description   sugar
A Sugar activity that launches Etoys within the Sugar environment.

%prep
%setup -q
%patch0 -p1

mkdir zh_TW
unzip %{SOURCE10} -d zh_TW

%build
./autogen.sh --prefix=%{_prefix}
make %{?_smp_mflags} V=1

cd zh_TW
for i in *.po ; do
msgfmt $i -o `basename $i .po`.mo
done

%install
make install-etoys install-activity ROOT=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/etoys/locale/zh_TW/LC_MESSAGES
cp zh_TW/*.mo %{buildroot}%{_datadir}/etoys/locale/zh_TW/LC_MESSAGES
mkdir -p %{buildroot}%{_datadir}/etoys/fonts
cp %{SOURCE11} %{buildroot}%{_datadir}/etoys/fonts

# FIXME:
#  according to my reading of the sugar activity doc, this shouldn't
#  be necessary.  The bin/ directory of the activity should be added to 
#  the PATH.  But it doesn't seem to be for F-10.
cp %{buildroot}%{_datadir}/sugar/activities/Etoys.activity/bin/etoys-activity %{buildroot}%{_bindir}/
# these files will be put in std RPM doc location
rm -rf %{buildroot}%{_datadir}/doc/etoys
install -Dm 644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/etoys.png 
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/sugar/activities/Etoys.activity/setup.py

%post
update-desktop-database &> /dev/null ||:
touch --no-create %{_datadir}/mime/packages &>/dev/null || :

%postun
update-desktop-database &> /dev/null ||:
if [ $1 -eq 0 ] ; then
  update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :

%files
%doc ChangeLog LICENSE NOTICE README
%{_datadir}/etoys
%{_bindir}/etoys
%{_bindir}/etoys-activity
%{_datadir}/mime/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%files sugar
%{_datadir}/sugar/activities/*

%changelog
* Thu Mar 21 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0.2408
- Rebuild for Fedora

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.2408-14
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2408-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2408-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2408-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2408-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.2408-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 09 2014 Rex Dieter <rdieter@fedoraproject.org> 5.0.2408-8
- update mime scriptlet

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.2408-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.2408-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 26 2013 Daniel Drake <dsd@laptop.org> - 5.0.2408-5
- Add patch to enable ALSA sound backend when Pulse is not available
- Needed for OLPC XO-4

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.2408-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 21 2012 Daniel Drake <dsd@laptop.org> - 5.0.2408-3
- Rebuild for fixed gzip package

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.2408-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 5.0.2408-1
- eToys build 5.0.2408

* Thu Apr 12 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 5.0.2406-1
- eToys build 5.0.2406

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2390-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Apr  5 2011 Peter Robinson <pbrobinson@gmail.com> - 4.1.2390-4
- Require sugar-presence-service

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.2390-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@gmail.com> - 4.1.2390-2
- Bump build

* Thu Oct 14 2010 Peter Robinson <pbrobinson@gmail.com> - 4.1.2390-1
- eToys build 4.1.2390

* Wed Sep 29 2010 Peter Robinson <pbrobinson@gmail.com> - 4.1.2388-1
- eToys 4.1 final release - build 4.1.2388

* Wed Sep 22 2010 Peter Robinson <pbrobinson@gmail.com> - 4.1.2387-1
- New upstream stable 4.1.2387 release

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 4.0.2340-2
- recompiling .py files against Python 2.7 (rhbz#623293)

* Tue Mar 20 2010 Peter Robinson <pbrobinson@gmail.com> - 4.0.2340-1
- New upstream stable 4.0.2340 release

* Sun Jan 10 2010 Peter Robinson <pbrobinson@gmail.com> - 4.0.2339-2
- cleanup spec and update to various package guidelines

* Tue Dec  1 2009 Daniel Drake <dsd@laptop.org> - 4.0.2339-1
- new upstream release

* Mon Nov 23 2009 Daniel Drake <dsd@laptop.org> - 4.0.2332-2
- don't own /usr/share/sugar/activities and move sugar activity to subpackage

* Sun Oct 11 2009 Steven M. Parrish <smparrish@gmail.com> - 4.0.2332-1
- lastest upstream release 4.0.2332

* Thu Oct 1 2009 Steven M. Parrish <smparrish@gmail.com> - 4.0.2319-1
- lastest upstream release 4.0.2319

* Sat Sep 12 2009 Steven M. Parrish <smparrish@gmail.com> - 4.0.2279-1
- lastest upstream release 4.0.2279

* Fri Sep  4 2009 Gavin Romig-Koch <gavin@redhat.com> - 4.0.2258-1
- pulled in latest upstream release 4.0.2258

* Sat Aug 29 2009 Gavin Romig-Koch <gavin@redhat.com> - 4.0.2247-1
- pulled in latest upstream release 4.0.2247

* Tue Aug 11 2009 Gavin Romig-Koch <gavin@redhat.com> - 4.0.2229-1
- pulled in latest upstream release 4.0.2229

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2212-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun  2 2009 Gavin Romig-Koch <gavin@redhat.com> - 4.0.2212-1
- pulled in latest upstream release 4.0.2212

* Thu Mar  6 2009 Gavin Romig-Koch <gavin@redhat.com> - 4.0.2206-3
- added files necessary for EToys to work as a Sugar activity.
- pulled in latest upstream release 4.0.2206 

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2201-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Gavin Romig-Koch <gavin@redhat.com> - 4.0.2201-1
- Switch to using the full color icon for Etoys.
- correct the name to Etoys in places where the letter case was non-standard.
- corrections needed by rpmlint
- add the localebug macro

* Sat Jan 17 2009 Gavin Romig-Koch <gavin@redhat.com> - 4.0.2201-1
- upgrade to upstream 4.0.2201
- switch from srpm to tarball as upstream source

* Fri Nov 25 2008 Gavin Romig-Koch <gavin@redhat.com> - 3.0.2159-2
- Fixes for rpmlint
  - replace tabs with spaces
  - use -q (quiet) on setup
  - remove wrong and unnecessary ROOT=buildroot from primary make
  - use explicit file modes when installing files
  - etoys.desktop: correct Icon, delete obsolete Encoding 
  - add needed lang macros

* Fri Nov 14 2008 Gavin Romig-Koch <gavin@redhat.com> - 3.0.2159-1
- added %%{?dist} to release
- altered the License field to use cononical License short names
- remove the Prefix (relocatable) field
- added .desktop file and etoys icon.

* Wed Oct 29 2008 Bert Freudenberg <bert@freudenbergs.de>
- 3.0.2160-1
- make Makefile work on Fedora 9
- use bundle_id instead of service_name
- adjust to recent bundlebuilder changes
- Content v. 179:
- update translation: tr
- fixed scripting command tiles in FishAndPlankton project
- 2160newDatastore-bf: Cope with Datastore using ByteArrays for Strings

* Thu Sep 25 2008 Bert Freudenberg <bert@freudenbergs.de>
- 3.0.2159-1
- update translation: tr
- Content v. 176:
- 2159putSourceFix-yo: Guard putSource:fromParseNode:... with a nil check
- 2158bkwdCompatFixes-sw: Fixes two backward-compatibility problems
- 2157WsReleasesInput-yo: fix WorldStethoscope analog input (#8608)
- 2156composeTitle-bf: Compose title of Journal object (#8351)
- 2155buddyFix-bf: Compose buddy nick name. Protect against bad colors
- 2154dissociateWSWorld-yo: Complete 2152rmSingletonFromWs-yo (#8541)

* Thu Sep 18 2008 Bert Freudenberg <bert@freudenbergs.de>
- 3.0.2153-1
- Content v. 174:
- set LC_ALL to fix composite character input (#8531)
- 2153metaData-bf: Preserve meta data set in Journal (#8550)
- 2152rmSingletonFromWs-yo: WorldStethoscope releases sound device (#8541)
- 2151releaseResourceThumb-yo: fix icon builder not releasing camera (#8540)
- 2150condenseSources2-yo: Fix the added comment to not include stamp:
- 2149localeAndPangoCheck-yo: Enable pango when the locale is unknown (#8530)
- 2148condenseSources-yo: Make condense sources work after EtoysV3

* Tue Sep 16 2008 Bert Freudenberg <bert@freudenbergs.de>
- 3.0.2147-1
- add license info to xo bundle
- Content v. 173:
- update translations: ja
- 2147sqLandNavBarHeight-yo: set navbar height to 75 when emulating XO
- 2146dropHandler-bf: Fix drop handler garbage collection
- 2145tempFile-bf: Do not delete temp files too soon (#8402)
- 2144TextLocaleChng-yo: Fix project loading from different locale (#8495)
- 2143macEnc-bf: Use utf8 filenames on Mac even in browser
- 2142sqRelBuilderInit-yo: Change the start up screen.

* Mon Sep 08 2008 Bert Freudenberg <bert@freudenbergs.de>
- 3.0.2141-1
- Content v. 171:
- 2141chooser-bf: Enable Find button in Sugar
- 2140dbusObjects7-bf: add argument matching on DBusProxy

* Mon Sep 08 2008 Bert Freudenberg <bert@freudenbergs.de>
- 3.0.2139-1
- Content v. 170:
- update de translation
- 2139buddyLayout-bf: make buddy flap resizable (#7749)
  add new buddies below older buddies (#8082)
- 2138enterWelcome-bf: Skip welcome if DnD events are queued
- 2137vd2-yo: Allow slight lax of screen size difference
- 2136activeHand-sw: Fix error in #hide script during event replay.
- 2135vd-yo: enable screen scaling when loading project in browser
- 2134fixDnD-bf: Do not flush drag-and-drop events
- 2133answerFlushed-bf: answer flushed elements in queue
- 2132datastoreEnc-bf: utf8-encode file names in datastore (#8212)
- 2131dbusCore45-bf: utf8-encode WideStrings sent on DBus
- 2130revertSugarClip-bf: Revert workaround for Sugar bug (#6262/#8287)
- 2129pangoJump-yo: do not use Pango for these jumping guys
- 2128unhibExtensArrow-sw: Fix extension arrows on open scripts
- 2127pangoBeforeFixLayout-yo: Fixes layout problem with Pango

* Wed Sep 03 2008 Bert Freudenberg <bert@freudenbergs.de>
- 3.0.2126-1
- Content v. 167:
- updated QuickGuides for center-of-rotationn again
- updated translations: de, ja
- 2126fixLayoutSep2-yo: Fix the layout of tiles upon loading
- 2125sugarClip-bf: Make open from clipboard work (#6262)
- 2124noSaveDefault-bf: Do not save default project (#8046)
- 2123invites-bf: Fix invitations (#5280)
- 2122slowLangMenu-bf: Show feedback while assembling the language menu

* Fri Aug 29 2008 Bert Freudenberg <bert@freudenbergs.de>
- 3.0.2121-1
- add update_url for XO bundle
- Content v. 164:
- updated QuickGuides for center-of-rotation and forward-direction
- updated translations: de, mn
- updated StartOfDTPDocument and ParticlesDyeInWater projects
- 2121RussianConveters-yo: Fix #8193
- 2120zeroClipboardWrkarnd-yo: fix NUL chars in clipboard 
- 2119dbusObjects6-bf: Fix evaluation of dbus handlers (#8210)
- 2118stderrAppend-bf: Append to the end of stderr and stdout
- 2117prjTitle-bf: Convert project title to UTF-8 only once (#8199)
- 2116errlog-bf: The error logged to the console was cut off occasionally
- 2115robustStdStreams2-bf: reopen std streams if closed (#
- 2114robustStdStreams-bf: Protect std streams against file open failure
- 2113pangoWidth2-yo: Fix the width of menu.
- 2112pangoWidth-yo: UpdatingString overwrote #fitContents wrongly.
- 2111rotationHandlesAgain-sw: Put up balloon help, require shift
- 2110GetTextRandom2-yo: Bullet proofing
- 2109screenModeMenuAug28-yo: Add full screen to the  screen mode choice
- 2108pangoInitInHaloName-yo: fix usePango for NameStringInHalo
- 2107journalUTC-bf: put proper Unix timestamps in Journal (#8176)
- 2106chronologyUnix-bf: Add asUnixTime to Kernel-Chronology (#8176)
- 2105idSlotNameChange-yo: Fix canceling renaming
- 2104pangoPrefAug27-yo: No font autoload under Sugar. Autoenable Pango
- 2103MenuItemPango-yo: Fix menu rendering with with Pango
- 2102NatLangExtraInfo2-yo: Fix a typo
- 2101NatLangExtraInfo-yo: put extra rendering info into .pot (#7610)

* Tue Aug 26 2008 Bert Freudenberg <bert@freudenbergs.de>
- 3.0.2100-1
- exclude raw pootle po files from rpm
- add SQUEAK_FAKEBIGCURSOR (#8008)
- Content v. 159:
- Added translations:  ar, bg, fa_AF, ht, mn, mr, nl, ro, si, te, tr
- Updated: bn, el, en, es, fr, it, ko, ne, ps, pt, pt_BR, ru, sv, zh_TW 
- 2100notUCQuit-sw: Remove an infelicitous capitalization.
- 2099textNil-bf: Protect against text being nil (#7737)
- 2098typo-bf: Fix a typo introduced in last update (#8129)
- 2097buddiesFix2-bf: Fix another occurrence of #8129
- 2096buddiesFix-bf: Protect against buddies being nil (#8129)
- 2095dbusObjects5-bf: use copy of blocks when handling messages(#8129)
- 2094dbusCore44-bf: default to int64 for LargeIntegers (#8152)
- 2093journalTime-bf: Add 'timestamp' property (#8152)
- 2092LocalePluginAddins-tpr: fix time zone / UTC support (#8152)
- 2091flipFix-bf: fix flip left-right rotation style
- 2090trnProxyEdit-KR: translate HTTPProxyEditor 
- 2089MiniEditorFixAug25-yo: Fix the behavior of MiniEditor (#7737)
- 2088etoysNotSqueak-sw: Change 'Squeak' to 'Etoys' in Quit dialogs.
- 2087projectName2-bf: Prevent unwanted suffix in project name (#8087)
- 2086projectName-bf: Preserve project name set in Journal (#8087)
- 2085shareHelp-bf: Update share-button help message (#8119)
- 2084retreatOnDirArrow-sw: Do not (for the moment) require shift key
- 2083msgHarmonize-sw: Harmonizes two recently-added informers
- 2082centerOfRot-sw: Always show center+direction handles on halos
  of Sketches, but require shift to be pressed
- 2081obtrudesFix-sw: fix 'obtrudes' (#7931)
- 2080macCase-bf: Mac file system is case-insensitive
- 2079noAudioNebraska-bf: Remove AudioChat and ScreenSharing (#7745,#7446) 
- 2078SuppliesContentAug6-yo: Fix the supplies bin contents.
- 2077TextWidthAug6-yo: Prevent text from supplies to shrink

* Wed Aug 06 2008 Takashi Yamamiya <takashi@vpri.org>
- 3.0.2076-1
- Content v. 156:
- Updated translations: ne, fr, ur, de, el
- 2076stickTo16bit2-yo: Complete the fix by 2074stickTo16-bit-yo.
- 2075pangoForRelease-yo: For this summer release, pango is off by default.
- 2074stickTo16bit-yo: Keep the screen depth at 16 bit upon the transition of virtual display and non-virtual.
- 2073pangoFixesAug5-yo: Some fixes for the pango rendering binding.
- 2072MorphInFile2-tk: In cases where the structures in a SmartRefStream happen to miss a class,
- 2071MorphInFile-tk: Fixes a bug in 'save Morph on file'.
- 2070keystroke-sw: TRAC #7779:  lastKeystroke malfunction in player moved to different project.
- 2069buddiesFlap-bf.cs: Use translated name to find buddies flap, do not translate holder morph name

* Wed Jul 30 2008 Takashi Yamamiya <takashi@vpri.org>
- 3.0.2068-1
- Content v. 154:
- Updated translations: es
- 2068FireFoxOnVista-yo: SugarLauncher looks to see if it has the src parameter from Squeak plugin on FF.
- 2067nilContents2-yo: The right fix for it after 2059pangoSpeedup.
- 2066nilContents-yo: Add a guard to StringMorph when contents is nil.
- 2065WSRework-yo: Fix analog/direct input mode. 
- 2064polyStep-sw: Give PolygonMorphs the same stepTime as other Morphs when they have players attached.
- 2063GStreamer-UI: Initial import of GStreamer code base from squeaksource.com/GStreamer
- 2062GStreamer-Base: Initial import of GStreamer code base from squeaksource.com/GStreamer
- 2061welcome-bf: Do not enter welcome project if SRC parameter given
- 2060squeakletDir-bf: Allow to configure Squeaklet directory location by VM parameter (trac #7624)

* Mon Jul 21 2008 Takashi Yamamiya <takashi@vpri.org>
- 3.0.2059-1
- Content v. 149:
- Updated translations: it, de, ja
- 2059pangoSpeed-bfyo: Reuse plugin canvas for a considerable speedup.
- 2058tubes-bf: use telepathy tubes, put buddies in a flap
- 2057telepathy-bf: update Presence Service bindings
- 2055DBus-Tools-bf-3: add manual proxy class selection when compiling methods
- 2054DBus-Objects-bf-4: fix mainloop, add signals.
- 2053buddies-bf: Cache joined buddies in inst var
- 2052projNameAgain-yo: 
- 2051strMorphComposition2-yo: Adds the fall back case when it is run on an older VM.

* Mon Jul 07 2008 Bert Freudenberg <bert@freudenbergs.de>
- 3.0.2050-1
- Updated translations: de, ja
- Content v. 146:
- 2050nebraskaPorts-bf: Make Nebraska work on multiple ports
- 2049etoyPorts-bf: Make Etoys peer-to-peer networking use multiple ports.
- 2048connQPorts-bf: Make ConnectionQueue work with a collection of ports
- 2047sqLandPangoFlag-yo: For Squeakland OLPC 2008, we don't use Pango.
- 2046strMorphComposition-yo: Fix measuring Strings.
- 2045ResetProgressBar-yo: Clear the UniqueInstance of SystemProgressBar.
- 2044sugarService-bf: Properly register our activity service
- 2043pangoJun23-yo: language attribute is created in a primitive.
- 2042renameDndOutMethods-tak: methods are renamed to 'dndOut'
- 2041fixPointerJumpDnD-tak: Move HandMorph before a drop event occurs.
- 2040functionTileInTest-sw: allows a function tile in TEST area
- 2039StarMorphScripting-kfr: Adds two scripting access points to StarMorphs.
- 2038atCursorRefresh-sw: fix valueAtCursor and firstElement updates
- 2037pangoRecompose-yo: Call composeToBounds upon use pango flag change
- 2036occlusionsProb-sw: remove broken avoid-occlusions from UI
- 2035numberAtCursorFix-sw: fix 'number at cursor' if text is rotated
- 2034menuTileFixes-sw: dismiss arrows when menu pops up
- 2033releaseKbd-kfr: release keyboard focus when hiding a morph
- 2032abandonUnsituated-sw: add 'abandon unsituated players' cleanup option
- 2031tabAmongFields-sw: fix tabbing
- 2030pangozeroTextFix-yo: protect against text size zero

* Tue Jun 19 2008 Bert Freudenberg <bert@freudenbergs.de>
- 3.0.2029-1
- Content v. 141:
- updated QuickGuides
- 2029dbusExplorer-bf: available from world menu
- 2028dbusStartup-bf: Fix DBus startup
- 2027enablePango-bf: Enable Pango
- 2026Nepalese1-yo: 
- 2025languageAttrPrims-yo
- 2024DBus-EtoysScripting-bf: Etoys scripting from outside
- 2023dbusSugar-bf: switch to new DBus bindings
- 2022DBus-Objects-bf-2: new high-level bindings
- 2021DBus-Core-bf-42: fix sending ByteArrays, coerce types
- 2020projectWriteError-bf: Log error while storing project
- 2019informDuring-bf: Ensure informer is removed after inform:during:
- 2018dropFix-sw: no invisible detritus after duplicating a tile phrase
- 2017psEncode-bf: Fix writing Integers in PostScript
- 2016ImageSeg-fix-tk: record uniclass metaclass organization in roots
- 2015PangoCharBoxFix-yo: remove workaround
- 2014trnDefName-KR: translate default Name of SketchMorph
- 2013trn18May2008-KR: translate border style values
- 2012fontInProjView-yo: 
- 2011keepVersionSqland-yo: fix update number for Squeakland.
- 2010fixSharedQueueAgain-bf: fix nextOrNil to signal correctly
- 2009fixSharedQueue-bf: make nextOrNilSuchThat: not throw away elements
- 2008PlayersToolFixJun5-yo: inspecting a player raised an error

* Tue Jun 06 2008 Bert Freudenberg <bert@freudenbergs.de>
- 3.0.2007-1
- Content v. 139:
- 2007hidePopArrows-sw: Remove arrows on watchers when watcher is moved
- 2006worldScriptingCat-sw: Offer scripting category in world's viewer.
- 2005timesRepeatFixes-sw: makes Times/Repeat tiles translatable
- 2004goldBoxFix-sw: A tile from golden box was duplicated
- 2003pointTypeArrows-sw: Remove Up/Down button for location in viewer.
- 2002ForceTileHeight-kfr: fix tile layout
- 2001trnMisc11May08-KR: fix for many missing translations
- 2000trnFlapHelp-KR: translate help text for Flap
- 1999evtRollHelp-sw: fix event-roll help-string

* Tue Apr 22 2008 Bert Freudenberg <bert@freudenbergs.de>
- 3.0.1998-1
- requires new DBusPlugin (in squeak-vm 3.10)
- Content v. 137:
- fixed EtoysActivity.pr to 16 bpp
- updated de and es translations
- move directory name for MO files from 'lang' to 'locale'
- condensed sources to EtoysV3.sources, empty changes
- new QuickGuides format
- fixed Welcome, DemonCastle, and Gallery projects
- 1998NotificationForOld-yo: notifies of projects loaded into old image
- 1997nilSelectionFix-sw: Paste with yellow menu in FillInTheBlank
- 1996DBus-Core-bf-41: fix reading empty ByteArrays
- 1995transTriggers2-KR: translate helpStrings
- 1994transPgCtrl-KR: translate page controls
- 1993transMisc1May08-KR:
- 1992transWinColor-KR: translate Windows Colors panel 
- 1991transMisc30Apr08-KR: translate captions for requests etc.
- 1990transProjDetail-KR: translate captions on EtoyProjectDetailsMorph
- 1989ButtonInSupplies-yo: Add button to the Supplies flap
- 1988VideoPropertiesFix-kfr: make brightness and contrast sliders 10 px
- 1987locChgPatchTile-KR: fix switching language causes DNU in Kedama
- 1986OLPCVirtual16-yo: Default depth for the virtual screen is now 16
- 1985transTriggers-KR-2: translate ScriptStatus chooser
- 1984transTransition-KR: translate page transition for BookMorph
- 1983transSymbolList-KR: translate Layout menu and borderStyle menu
- 1982transSvcLabel-KR: translate service entries for FileList
- 1981transStarSq-KR-2: translate StarSqueak
- 1980transPrefPanel-KR-1: translate preference panel
- 1979transNebraska-KR: translate several strings in Nebraska
- 1978transMisc2-KR: translated misc missing translations
- 1977transMisc1-KR: fix miscellaneous translations
- 1976transMisc08APR15-KR: fix translations reported by Gerhard Steiner
- 1975transGame-KR: translate Games
- 1974transEmphAlign-KR: translate Emphasis and Alignment of TextMorph
- 1973transAdhereEdge-KR-1: translate adhere-to-edge menu
- 1972noAltV-sw: Unhook cmd-shift-V / alt-V from 'paste author initials'
- 1971authorInitialsIssues-sw: USe default initial when dialog canceled
- 1970lessFuzzyGoldBox-sw: Makes the icons in the gold box less fuzzy.
- 1969gridOnDrop-sw: Picks up on Karl Ramberg's effort to restore some of 
  the lost functionality of pasteUpMorph 'gridding'.
- 1968translatedOperator-sw: un-camel-case and translate operator tiles
- 1967RemoveProgress-cjs: Replace uptoEndWithProgressBar with upToEnd.
- 1966activeSubMenu-kfr: make sub menus stay up
- 1965textMorphHalo-sw: halo on a TextMorph indicates bounds as well.
- 1964functionNames-sw: add sign() and truncate(), clean up function names
- 1963savePasteUp-sw: saving a pasteup morph creates a .morph file, not .pr
- 1962goldBoxIconSize-sw: Tiles in golden 'treasure box' were too small
- 1961squeaklandClouds-yo: Add clouds to Squeakland OLPC initial screen.
- 1960QGuide-web2-tk: Enhance writeing QuickGuides out as web pages
- 1959HideUpdateServer-yo
- 1958addLocalPrefs-yo: Add ServerDirectory to ExternalSettings
- 1957narrowForgetDoIts-yo: forgetDoIt only in classes touched
- 1956phraseExpandFix-sw: Honor auto-phrase-expansion flag
- 1955anchorTransl-bf: Fix one missing translate send.
- 1954MoveMODir2-bf: One more place to change 'lang' to 'locale'
- 1953MoveMODir-tak: Move MO files from 'lang' to 'locale'.
- 1952ProjectLoadingMar28-yo: Some optimizations on ProjectLoading.
- 1951SISSChangeSets-yo: Simplify a bit to avoid recursion.
- 1949SISSPrefObj-yo: Preference object follows the one in the environment.
- 1948SISSFlapTab-yo: 
- 1947PopUpArrowsFix-yo: guard against ActiveHand being nil
- 1946sugarProxies-bf: add proxies for datastore, journal, and presence
- 1945DBus-Core-bf-40: default to int32 when sending integers
- 1944xoBundle3-bf: Include lang dir when bundling, add MO_PATH in script
- 1943DBus-Tools-bf-1: DBusExplorer supports proxy class compiling
- 1942DBus-Objects-bf-1: high-level DBus bindings with proxy support
- 1941DBus-Core-bf-39: optimize ByteArrays
- 1940DBus-Core-bf-38: rename bool to boolean
- 1939viewerMenuHelp-sw: Fix wording of viewer menu help message.
- 1938polyFill-sw: Avoid errors in halo menu for open polygons.
- 1937FD-oldFileOrNoneNamed: 
- 1936polygonFillStyle-sw: fix viewer for "open" PolygonMorphs
- 1935unicodeFallback-bf: Fall back to MacRoman if UTF32 charcode is 0
- 1934romepango2-yo: The image-side Pango support rev. 2.
- 1933romepango-yo: The image-side Pango support.
- 1932romepango-base: The code borrowed from the Rome package.
- 1931WhiteMenuHandle-tak: It makes menu handle be white 
- 1930ScrptEditFeedback-kfr: feedback for tile dragged from a TestTile
- 1929evtTheatreTransl-sw: translate event theater
- 1928collapseFixes-sw: Make the sugar-navigator-bar immune to collapsing.
- 1927helpFlapScroll-sw: take Sugar nav-bar into account for pane-size.
- 1926SISSNoSortDict-yo: Ignore key order when writing out SISS.
- 1925unixLatin1Input-yo: Simply use UTF32InputInterpreter on unix.
- 1924lingeringPlayers-sw: remove stale entries from projects on save
- 1923KedamaTilesRefac-yo: Clean up a bit around Kedama tiles.
- 1922SISSAvoidNameCrash-yo: add suffix if there is a project with same name.
- 1921SISSProjVerAndCS-yo: Save project version and changeset
- 1920SISSUniclassHier-yo: better handling of uniclasses in a hierarchy
- 1919SISSPlayerAndWspace-yo: write out an uniclass without its instance.
- 1918UTF8InputFix-ar: Raise an error for malformed utf8 input
- 1917bearingToFix-sw: report bearingTo: in the range -180 to 180.
- 1916sugarDBus-bf.cs: adapt to new DBus-Core
- 1915DBus-Core-bf-37: changes for DBus-Plugin-bf.31 (requires new plugin)
- 1914fixSharedQ2-bf: Nil out unused slots in shared queue.
- 1913compareToClipFix-sw: Fix the compare-to-clipboard feature
- 1912sketchName-sw: fix name of duplicated newly-created Sketch
- 1911sketchPolygonUndo-nice: Fix undo in painting tool's polygon mode.
- 1910revealFix-sw: Fix reveal-player whose costume is the World.
- 1909stderrLog-bf: Log errors to stderr
- 1908stdStreams2-bf: use standard streams only on unix
- 1907crlfFix-bf: fix ignored lineEndConversion settings
- 1906stdStreams-bf: Add support for stdin, stdout, stderr.
- 1905changesFix-bf: fix changes file in a non-default directory.
- 1904dbusExplorer-bf: Add a graphical DBusExplorer.
- 1903idParams-bf: Refactor activity id and bundle id parameters
- 1902suspendUI-bf: Suspend the UI process while not active (#2939)
- 1901rehashMDs-lg: Speed up project loading by faster rehashing of
  method dictionaries
- 1900htmlColor-bf: Fix asHTMLColor, also speeds up 10x.

* Thu Mar 13 2008 Bert Freudenberg <bert@freudenbergs.de>
- 2.3.1896-1
- Content v. 121:
- update QuickGuides
- 1896jumpTo3dot0-bf: offer jump to version 3.0
- 1895fixCondensing-yo: Fix condensing changes and sources.

* Fri Feb 22 2008 Bert Freudenberg <bert@freudenbergs.de>
- 2.3.1894-2
- Content v. 117:
- rebuilt etoys.image

* Wed Feb 13 2008 Bert Freudenberg <bert@freudenbergs.de>
- 2.3.1894-1
- Content v. 116:
- Added translations: ru, ps 
- updated bn, de, el, es, fr, it, ja, pt, pt_BR, ur
- 1894setSqLandFont-yo
- 1893toggleFullScrn3and13: toggle fullscreen on alt-enter
- 1892manifestFixHack-yo: A workaround of multi-line value in manifest.
- 1891FixDismissViaSel-yo: Clean up block in NewHandleMorph

* Fri Feb 01 2008 Bert Freudenberg <bert@freudenbergs.de>
- 2.3.1890-1
- Content v. 114:
- Updated translations: es, de
- Updated QuickGuides
- 1890scaleSugar-bf: enable screen scaling on startup (#5507)

* Thu Jan 31 2008 Bert Freudenberg <bert@freudenbergs.de>
- 2.3.1889-1
- Content v. 111:
- 1889TextFixJan30Again-yo: Revert and fix the null text case differently
- 1888initialClipboard-yo: set the initial contents of clipboard
- 1887NarrowTab-tk: The Tabs were all too wide.
- 1886docksFix-sw: hitting tab within scripted world caused error.
- 1885resumeFix2-bf: must not modify the original journal entry (Trac #5348)
- 1884TTObjForStream-yo: True Type font rework broke saving TrueType banner.
- 1883NoDragGuide-tk: No picking up for QuickGuideMorph.

* Mon Jan 28 2008 Bert Freudenberg <bert@freudenbergs.de>
- 2.3.1882-1
- remove audio/mpeg and video/mpeg mimetypes
- add application/x-squeak-archive mimetype
- Content v. 109:
- added bn, pt_BR, sv translations
- updated translations from pootle
- fixed unplayable movie in example project
- 1882parameterTileSuffix-sw: Fix for TRAC 6197
- 1881moPath-KR: activity bundles can provide private translation
- 1880rainbowKey2-bf: re-disable key generation on startup
- 1879GuideUnderPaint-tk: fix painting within quick help
- 1878ResumeMidi-yo: Make resuming a midi file from Journal work.
- 1877NoUpdateInRelease-tak: do not load code updates automatically
- 1876xobundle2-bf: Create bundle compatible with more etoys versions
- 1875xoBundle-bf: support making an OLPC XO bundle
- 1874dropFix-bf
- 1873GuideToWeb-tk: writes out QuickGuides as web pages
- 1872TranslateGuide-tk: translate text in a Guide (not enabled yet)
- 1871spanWorld-tk: fix an error reentering the project

* Fri Jan 04 2008 Bert Freudenberg <bert@freudenbergs.de>
- 2.3.1870-1
- Content v. 104:
- new QuickGuides
- 1870defaultLineHeight-kfr: Fix TextMorph becoming tiny
- 1869latin1PathEncoding-yo: Change the default path encoding to UTF8.
- 1868avoidUnCamel-yo: uncamelcase help hrases for KedamaPatchMorph
- 1867ChatBiggerFont-yo: Use bigger font for text chat.
- 1866TextNumericValue-yo: fix fractions in numeric value of Text
- 1865MOmagicNo-KR: fix typo of magic no of gettext MO file.

* Tue Dec 25 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.3.1864-1
- Content v. 98:
- new QuickGuides
- updated translations
- 1864SugarNav24-yo: Add findButton but make it invisible in Sugar.
- 1863DelayedStopButton-yo:
- 1862TTCFontObjStream-yo: restore the backward compatibility
- 1861RestoreSocketRemoved: For backward compatibility
- 1860ButtonFormDepthFix-yo: fix in form translator for Japanese
- 1859arithErrorTweaks-sw: tweaks to run-time-arithmetic-error handling:
- 1858EtoyNotifier-yo:
- 1857SqueaklandConfig-yo: Use #usePopUpArrows and dark green for navigator
- 1856NoNoHaloMorph-yo: Remove the uses of NoHaloMorph
- 1855ButtonFormDepth-yo: Adjust the depth of pre-made forms for buttons.
- 1854PrefUsePopUpArrows-tak: Added a preference #usePopUpArrows (#5341)
- 1853RecordingCtrlsTrans-kfr: Make the menu translatable.
- 1852RecordCtrlCodecNaming2-yo: Insert #translated to Karl's fix.
- 1851RelBuilderForSqLand3-yo: Setup the update stream for Squeakland
- 1850RelBuilderForSqLand2-yo: Change the preferences for non-OLPC platforms
- 1849stopRecording-KR: SoundRecorder and VideoMorph stop on project
  transition and Squeak's shutdown (#3665)
- 1848RecordCodecNaming-kfr: adds end user wording for compression choices
- 1847WideFindStrngMiniFix-yo: fix the WideString findSubstring issue.
- 1846headingPrecision-yo: Fix the rounding behavior of setHeading:
- 1845AudioChatGUIUI-yo: Minimum facelift for AudioChatGUI. 
- 1844PlayerHueFix-kfr: The hue change was applied to brightness
- 1843UseOriginalName-yo: Use base name of stream for imported graphics
- 1842NoCameraSoundInTrashCan-kfr: fix TrashCan sound
- 1841SugarNav23-yo: Fix next icon.
- 1840NotWelcome-yo: Don't dive into launcher when eToyFriendly is off.
- 1839ScriptingTileSoundBug-kfr: Fix dropping a SoundTile
- 1838ComposeNick-yo: Compose decomposed form of Unicode string.
- 1837GrabAndLassoCursor-yo: Fix cursor for Grab patch and Lasso
- 1836OpTranslation-yo: Fix translating operators (i.e., "/" to ":"
- 1835BookPickable-yo: A book should be pickable at its title bar
- 1834FontRegFix-yo: Wrong test method was called. 
- 1833SavedUpdateEncoding-yo: Treat saved change set as binary.
- 1832TTCFontSetFix-yo: Fix more problems with TTCFontSet.
- 1831AddRussian-yo: Add partial Russian support.
- 1830newLineInGetText-KR: all LFs in MO need to be converted to CR (#5462)
- 1829CP1253Table-yo: CP1253 table specifies wrong direction.
- 1828TTProperReference-yo: Fix multi-level composition in TrueType.
- 1827sketchColor-sw: Don't offer color category for a Sketch (#5437)
- 1826TTCFontSetRework-yo: Clean up TTCFontSet and friends.
- 1825GreekInput2-yo: A return symbol was missing.
- 1824SysVerInPO-KR: Embed SystemVersion in header of exported PO/POT.
- 1823GreekClipboard-yo: A fix for clipboard access for Greek on Windows.
- 1822GreekEnviron-yo: An experimental version of Greek support.
- 1821UnicodeFntLoading-bf-yo: load part of a large font and save it

* Wed Dec 05 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.3.1820-1
- integrate with Pootle
- merged translations from launchpad
- added el, ne, ur, zh_TW
- Content v. 90:
- 1820OrangeSugarBar-yo: Experiment a bar interface for Squeakland-OLPC.
- 1819SugarNav22-yo: Project name follows resizing and recoloring of bar
- 1818ScriptActButtonLabel-kfr: Set the right font for the new label
- 1817autoBadge-bf: Automatically pop up badges as buddies join and leave
  Needs 3.9.12olpc4 VM to work properly
- 1816asyncXdnd-tak: fix  that you can't drag a morph to another window
  which overlaps on Squeak's window. Needs VM from takashi-branch r1793
- 1815latin1Chars-yo: Fix some non-ascii chars in source code
- 1814IncludeChangeSet-yo: Include changeset by default when saving 
- 1813macPasteUTF8-bf: Make pasting unicode strings work on Mac.
  Needs ExtendedClipboardPlugin.bundle
- 1812SugarNav21-yo: replace stop icon.
- 1811CondenseSources-yo: fix condensing sources
- 1797-1810: gap fillers

* Wed Nov 16 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.2.1796-1
- Content v. 87:
- 1796autoBuddy-yo-bf: Create badges when joining activity (#3758)
- 1795PopUpCaretFixLayout-tak: pop up arrow's layout malfunction (#5126, #5148)
- 1794DBus-Core-bf-36: fix signal matching (#3758)

* Fri Nov 16 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.2.1793-1
- Content v. 86:
- 1793joinActivity-yo-bf: when joining, go into shared mode (#3758)
- 1792noNarrowScrollbar-sw: Eliminate narrow scrollbars (#3545)
- 1791PopUpCaretFix2-tak: Fix pop up carets (#2807)
- 1790rainbowKey-bf: Disable sandbox and key generation in rainbow (#4787)
- 1789arrowTile-bf: use tile background color for pop-up carets (#2807)
- 1788PopUpCaretFix-tak: arrow pos follows width of the text (#2807)
- 1787QG-JumpTo-tk: adjust look of page control in the Guides 
- 1786fixPopupArrowUpDown-tak: fix mouse event handler (#2807)
- 1785logEntryOops-sw: Remove leftover debugging printout from 1783

* Fri Nov 16 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.2.1784-1
- make DBus warnings non-fatal
- Content v. 84:
- 1784DBus-Core-bf-35: fix sending DBus struct 
- 1783fullScreenToggle-sw: latest sugar key bindings
- 1782userTextFix-kfr: fix tiny font issue (#4943)
- 1781PopUpCaret-tak: larger pop up arrows (#2807)
- 1780RemoveAnOldComment-yo: Clean up a left over obsoleted comment.
- 1779classicNaviTrans-KR: make navigator buttons translatable
- 1778Paint-World-tk: When painting the background, do not center it.
- 1777FileDialogToCatalog-yo: add file dialog to catalog
- 1776authorName-bf: Set authorName to the XO owner's name
- 1775balloonHelpLocation-yo: Fix balloon help direction (#4807)
- 1774TextFieldFocus-yo: fix rounded text field (#4808)
- 1773DynCheckSecurity-yo: dynamically disable security if on XO
- 1772noKomika-sw: Eliminate remaining uses of Komika font

* Fri Nov 09 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.2.1771-1
- set umask to 0002 to make group-accessible (#4770)
- rename sandbox to MyEtoys (#4787)
- updated guides
- Content rev. 82:
- 1771DisableSandbox-yo: disable sandbox and key generation (#4787, #4788).
- 1770SISSProxy2-yo: do not execute arbitrary method.
- 1769SISSProxy-yo: store objects that are not reachable from the root.
- 1768AllowReadonlyChanges-yo: For view source, support readonly changes

* Thu Nov 08 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.2.1767-1
- exclude QuickGuides/[a-z]*
- make private dir group-writable for rainbow
- Content rev. 80:
- 1767RenameLauncher-yo: Rename the Launcher project to Etoys Activity.
- 1766SugarNav20-yo: The project name field tracks the screen size change.
- 1765BiggerPaintBox2-yo: Add a preference to control the painting box size.
- 1764BigPaintBox-ka: This patch makes a PaintBox big. (1.5X)
- 1763suppliesFlapFixes-sw: Fix all-scripts-tool, re-add book, remove triangle
- 1762showSourceAgain-sw: show-source on ctrl-comma as well as on alt-comma
- 1761userTextObject-sw: grows/shrinks text as the user types
- 1760SugarNav19-yo: Make the rounded field wider when there is enough space.

* Mon Nov 05 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.2.1759-1
- recompress guides with --rsyncable (#4620)
- use "data/" subdirectory of $SUGAR_ACTIVITY_ROOT (#2546)
- Content rev. 78:
- 1759keyLoc-bf: Look for owner.key in the right directory. (#2546)
- 1758screenshot-bf: Handle DBus TakeScreenshot() method
- 1757properShare-bf: Integrate with presence service (#3758)
- 1756newBookRevert-yo: Provides better revert for book pages.
- 1755TryHardToCleanup-yo: Delete World's references recursively.
- 1754Paint-place-tk: Fix object repaint  (#4426)
- 1753roundInput-bf: Fix text quality by not drawing the label twice
- 1752QuickGuide-order-tk: Fix order of guides in the menus in the index.
- 1751QuickGuides5-tk: create QuickGuides index at build time.
- 1750HandleResize-kfr-yo: Adjust the handle size of StarMorph and others.
- 1749StarMorph-wiz: Fix StarMorph.
- 1748narrowCursor2-tak: cursor must have alpha pre-multiplied.(#2813)

* Thu Oct 31 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.2.1747-1
- Content rev. 76:
- new quick guides
- repositioned about flap in projects
- add sources for view source
- 1747narrowCursor-tak: Use Bluecurve large cursor.
- 1746showSource-sw: React to the hitting of the show-source key
- 1745PreventGoingTopProj-yo: don't exit to the top-level project
- 1744SoundMixer-yo
- 1743noHelpDragover-sw: Do not close help flap when dragging out from it.
- 1742SugarNav18-yo: Always adds the project name text field.
- 1741SugarNav17-yo: add project name field, intelligent share button. 
- 1740TransCategory-KR: export all viewer category symbols to POs/POT
- 1739SymListWOCamel-KR: SymbolListTile options and readout as no camel case.
- 1738transSymbols2-tak: export all symbols in vocabulary to POs/POT

* Thu Oct 31 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.2.1737-1
- Content rev. 71
- 1737fastChooseLang-KR: language selection menu speed up
- 1736NewClipboard2-yo: A fix for the previous change.
- 1735NewClipboard-yo: Make simple text clipboard work on new and old VMs
- 1734ConsistentFileName-yo: Set the name instance variable with proper value.
- 1733translucFix-sw: Fix bug that broke setting of translucency (#4512)
- 1732removePipe-bf: Remove old pipe protocol (was used by the Python wrapper)
- 1731UpdBtnFontFix-KR: preserve font for ticking button in scriptor (#4150)
- 1730transDom3-tak: use class instead of class name
- 1729transDom2-KR: translation resolves domain by class, not class category.
- 1728transDom1-KR: registration API for classCategory->domain mapping. 
  Addon application can register its domain by prefix (i.e. package name)
- 1727cleanupMOSupport3-tak: Restore backward compatibility.
- 1726SystemFont2-yo: Change the system font upon release builder.
- 1725SystemFont-yo: Fix the recursive fallbackfont problem.
- 1724soundLibrary-kfr-sw: A tool for browsing and managing the sound library.
- 1723anonymousSound-sw: Handle a drop of an external sound file
- 1722kbdMorphForInput-kfr: Use bigger font for KeyboardMorphForInput
- 1721waveAndGraphFixes-kfr: Use olpc fonts in the WaveEditor.
- 1720support-sw: Four little changes
- 1719cleanupMOSupport2-tak: nicer startup of NaturalLanguageTranslator.
- 1718cleanupMOSupport1-tak: first pass to cleanup NaturalLanguageTranslator
- 1717switchGetTextRT-KR: make EToys to use new translation stuff.
- 1716gettextRT1-KR: new language translation framework 

* Thu Oct 18 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.2.1715-2
- Content rev. 70
- correct directory structure for .mo files

* Thu Oct 18 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.2.1715-1
- make same bundle work in old and new Sugar (bf)
- Content rev. 69:
- add compiled .mo files
- 1715utf8toSqueakFix2-yo: Revert the change for now
- 1714UnicodeInput2-yo: Fix the way it checks the VM version.
- 1713UnicodeInput1-yo: First attempt to enable Unicode composed characters.
- 1712utf8toSqueakFix-yo: add proper language tag.
- 1711UTF8Clipboard-ar: UTF8 clipboard support

* Tue Oct 16 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.2.1710
- changed activity launch to match new Sugar
- switch to UTF-8 encoding
- log to stdout instead of Etoys.log
- merged all po's into single po
- Content rev. 67:
- updated quick guides
- 1710ctrlAlt-bf: Keep swapControlAndAltKeys from mangling non-letters
- 1709playfieldOpt-sw: remove empty playfield options category 
- 1708pageTurnViewer-sw: Remove viewers on page-turn (#3618)
- 1707noNilInit-sw: Remove UndefinedObject>>initialize
- 1706noWorldTransluc-sw: Do not accept translucency in the World's color
- 1705removeLenna-yo: Remove a big literal (#4222)
- 1704QuickIndex4-tk: In Guide file names, allow a dash (-) to mean a space.
- 1703playfieldOptionsCat-sw: Disenfranchise the playfield-options item
- 1702gettextExpCtx-KR: Show correct context for viewer additions in POs
- 1701ObjToolLocChg-KR: Fix object catalogue locale change (#3743)
- 1700QuickIndex3-tk: Enhance the way names of guides are displayed
- 1699worldRecolorHalo-sw: recolor handle for world halo.
- 1698setAsBackgroundFix-sw: Translucent bg image fix (#3888)
- 1697gridVisFix-sw: Corrects a typo i1669playfieldOptions-sw
- 1696gradientWorld-sw: Make relevant items in the fill & border 
  category be visible in the World's viewer.
- 1695unBatchPenTrails-yo: Turn off batch pen trails option.
- 1694QuickIndex2-tk: Allow the index to be read as a .pr file
- 1693FileOpenFixes-kks: Media files are now opened in readonly mode
- 1692ProjectQueryMorphFix-mu: Send encoded query string to SuperSwiki
- 1691noCamels-bf: Consistently use space instead of capitalization 
  to separate words in tiles.
- 1690underlineCommentGT-tak: Replaces white spaces to _ in .po comments
- 1689bookMenu-sw: Adds 'find-again' alongside 'find' in the book menu
  Provides balloon help for book menu items.
- 1688addTranslatedList-sw: translate lists
- 1687scorePlayer-kfr: Use latest etoy fonts in Score Player
- 1686polygonMenu-sw: Cleanup of the halo menu of a PolygonMorph.
- 1685QuickGIndex-tk: 1) Add 'Index' to the Jump to Guide menu, so one
  can get back to the Index page.
  2) Allow .pr files in the QuickGuides folder (for debugging).
  3) Redid the bar at the bottom of the Guide.
- 1684sortedPObyCategory-tak: Sort PO file entries by
  class categories -> class -> methods -> msgid (alphabetical)
- 1683worldHaloMenu-sw: Harmonize and rationalize the eToyFriendly 
  and non-eToyFriendly versions of the world halo menu.
  Remove 'layout' from both versions.
  Some rewording, reordering, refactoring.
- 1682distanceAndBearing: adds distanceTo: and bearingTo: tiles
- 1681sortedPOFile-tak: Sorting in pot files (#3596)
- 1680GTExpByDomain-KR: exports POs based on textdomain for class category
- 1679graphPaperPickers: Use appropriate color pickers for constructing
  graph paper, and position them appropriately (#2870)
- 1678embedDynamic-sw: Make the 'embed' command dynamic
- 1677evtTheatreNav-sw: Brings the pseudo-sugar nav bar in the event
  theatre back more closely into line with current sugar-nav-bar
- 1676playbackCursorPos-sw: Fixes the initial positioning of the
  playback cursor in event-theatre and event-playback-space.
- 1675pasteUpHalo-bf: Respect #wantsHaloFromClick in PasteUpMorphs
- 1674GuideInPrs-tk: Better QuickGuideGenerator
- 1673GetTextNormCR-KR: adjust msgstr for format checking by msgfmt tool
- 1672fixArrayTransNoop-tak: fix and add a test case for ArrayTransNoop-KR
- 1671fixNoErrorSUnit-tak: SUnit fix
- 1670ArrayTransNoop-KR: translate strings in arrays
- 1669playfieldOptions-sw: Spruce up the playfield-options menu
- 1668stringTransl-bf: Make TextMorphs translateable. To try, simply 
  switch a project's language, edit the text, and switch back.
- 1667nonPlayerViewer-sw: A few fixes to breathe a little life back into
  the 'Direct Viewer' -- i.e. a Viewer for a non-player object.
- 1666simpleSwitchMorph-apb: compatibility support for examples in the 
  book 'Squeak by Example' -- see http://www.iam.unibe.ch/~scg/SBE/
- 1665displayFix-bf: Release virtual display on shutdown

* Wed Sep 19 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.1.1664
- Content rev. 59
- corrected help cards (#3574)
- fixed gallery project (#3575)
- fixed wording in launcher and tutorials
- updated spanish translations (#3518, #3540)
- 1664prjLocale-bf: switch project locale on enter (#3598)
- 1663QuickGuide14-yo: One more place to show wait cursor.
- 1662QuickGuide13-yo: Show wait cursor (#3555)
- 1661RelResources-yo:  release microphone and camera (#3547, #3567)

* Mon Sep 17 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.1.1660
- Content rev. 51
- 1660QuickGuide12-yo: and one more
- 1659QuickGuide11-yo: more quick guide fixes
- 1658Repaint-rot3-tk: Fix repainting un-rotated sketches
- 1657QuickGuide10-yo: 
- 1656QuickGuide9-yo: Allow to choose a guide from a menu.
- 1655Paint-bulletproof-tk: One more piece of safety code in case the
  user turns the page of a Guide while painting.
- 1654Repaint-rot2-tk: After repainting, leave the top left of the
  object where is was before.
- 1653thumbAlpha-bf: #3332: Fix alpha in preview
- 1652gettextSorted-tak: Sort keyword entry in gettext files
- 1651helpFlapTab-sw: Make the textual help flaps clear the sugar bar.
  Constrain guides-flap tab movement. React properly to screen-size change.
- 1650QuickGuide8-yo: Fix the layer of help again so that halo shows up.
- 1649RelBldrFix-yo: A fix of typo and initialization of default thumbnail.
- 1648Repaint-close-tk: bullet-proofs the code closing the paintBox 
- 1647QuickGuide7-yo: Fixes the halo problem one more time.

* Fri Sep 14 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.1.1646
- Content rev. 44
- updated example projects
- 1646setActive-bf: DBus method set_active() changed to SetActive()
- 1645prjKeepFix2-bf: Typo in previous fix
- 1644ColoPickerSize-tak: Color picker's buttons become larger.
- 1643QuickGuide6-yo: Follow some intelligent ordering.
- 1642QuickGuide5-yo
- 1641prjKeepFix-bf: We were creating too many journal entries
- 1640Repaint-rot-tk: Fix repainting a rotated and scaled sketchMorph.
- 1639FlapMargin-yo: pad the space around flap referent.
- 1638balloonTransl-bf: Make initial balloons translatable
- 1637gettextSpace-bf: #3452: replace space with underscore in .po filenames
- 1636BalloonsNewProj-tk:
- 1635NewSavingFeedback-tak: Python friendly feedback while saving.

* Tue Sep 11 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.1.1634
- remove B1 128mb memory hack (bf)
- fix icon (display inline)
- Content Rev. 40
- update launcher project
- 1634SugarNav16-yo
- 1633NebraskaTransform-yo: Send float, not fraction over the net.
- 1632ViewerLineFeedback-kfr: The Viewer feedback rectangle was showing
  the wrong height.
- 1631BalloonHelpWording-yo: Second round for balllon help wording.
- 1630FeedbackWhileSaving-yo: Give better feedback while automatically
  saving.
- 1629SugarNav15-yo: Change buttons in the SugarBar.
- 1628startFix2-bf: Only enter launcher if no script given on cmd line.
- 1627startFix-bf: On startup, enter Launcher project if no other project
  supplied.
- 1626FontNameGlitch-yo: Fix a sort of typo in the list of font names.
- 1625HelpInHalo-yo: Allows a morph in help books.
- 1624ClickHaloProperty-yo: Enable customizing wantsHaloFromClick.
- 1623BroomSave2-yo: one more place to restore the filter variable.
- 1622fontFix-sw: Disenfranchise two items from the 'standard system fonts'
  choice menu
- 1621NebraskaFontDecode-yo: Yet another patch to fix the font
  transmission problem in Nebraska.
- 1620NebraskaSep11-yo: Make Nebraska sharing work on non-IPv6
  environment, and fix the color problem.
- 1619TempInTextual-yo: Support saving a textually coded script with
  temporaries into the S-expression format.
- 1618BookColor-tak: It changes the default color of BookMorph and its 
  icon to white as Yoshiki's request.
- 1617initialProjects-yo: Building initial screen with initial projects.
- 1616NewProjWithBalloon2-yo: BalloonMorph can handle arbitrary morph.
- 1615NewProjWithBalloon-yo: A mechanism to put up balloon helps upon
  entering a new project.
- 1614quitFix-bf: Ensure we quit even if project saving fails.
- 1613keepFix-bf: Do auto-save on startup
- 1612QuickGuide4-yo: Compress guide data.
- 1611QuickGuide3-yo: A new version of Quick Guides.
- 1610penTrailGraphic-sw: Makes the graphic of a playfield's pen trails
  accessible for scripting through the viewer, as a slot of PasteUpMorph.
- 1609objCatAdjustments-sw: Some recategorizing and renamings of 
  objects-catalog and supplies-bin entries
- 1608eToyButtonFont-sw: Add separate system-font preferences specifically
  for etoys buttons and for etoys textual code
- 1607constantTileVis-sw: Make the numeric-constant tile in the gold box
  visible again.
- 1606BroomSave-yo: BroomMorphs can be saved in a project now.

* Fri Sep 07 2007 Takashi Yamamiya <tak@metatoys.org>
- 2.1.1605-1
- Content Rev. 36
- 1605trimReleaseBuilder-tak: Remove some projects in the image,
  and trim verbose messages.
- 1604EmptyConditional-yo: Make Sexp form work when testPart is
  empty.
- 1603SISSFuncTiles-yo: Make FunctionTiles work with SISS file
  format.
- 1602keepPrj-bf: Update the current project in journal on close,
  save copy on keep button press.
- 1601initialBalloonHelp-yo: For the initial project, this
  changeset adds explaination on where to start.
- 1600flapFix-bf: Fix a DNU when there is no current SugarNavBar
  instance
- 1599Repaint-size-tk: Bug from Kathleen Harness: If a SketchMorph
  is shrunk down to a small size, and you repaint, the original form
  can be cut off by the painting area.
- 1598helpIcon2-tak: Better color of help icon.
- 1597RelBuilderForSqLand-yo: A release builder setting for a
  non-OLPC release.
- 1596helpIcon-tak: An icon for Etoys Quick Guide.
- 1595nonSugarSuppliesTab2-yo: Make Red old Supplies tab show when
  sugarNavigator is false.
- 1594nonSugarSuppliesTab-yo: Make Red old Supplies tab show when
  sugarNavigator is false.
- 1593tabsClearSugarBar-sw: In lining up flap-tabs along the left
  edge of the screen, start *below* the sugar-nav-bar if the
  sugarNavigator preference is on.
- 1592redSuppliesInEvtTh-sw: Position the supplies tab in non-sugar
  evt theatre properly.  Requires a change to the
  newSuppliesFlapFromQuads:positioning: method from Yoshiki before
  this all comes together...
- 1591jpegExt-bf: Add JPE as supported jpeg extension as workaround
  for issues 3163 and 3164
- 1590noInteractionSaving-yo: Add a way to save a project without
  any interaction.  Also, remove the menu bar from the generated
  thumbnail.
- 1589stickyGuides-sw: Make the Guides cards in the Help flap be
  sticky.
- 1588veraSansForEtoys-tak: Choose BitstreamVeraSans for Etoys.
- 1587flexibleEtoysFont-tak: Makes tile and viewer layout to fit
  with various font sizes.
- 1586moreRotationFixes-sw: Fixes two more bugs arising from morph
  rotation:
- 1585littleOops-sw: Removes a snippet of debugging code
  inadvertently lingering in update 1580sugarSupplies..
- 1584evtTheatreSugarFlaps-sw: Complete the porting of
  sugar-nav-bar and sugar-supplies-bin changes in the outer UI to the
  flaps used on the edge of an event theatre.
- 1583fixDupHelpMsg-sw: Fix the help message for the green
  'duplicate' halo handle so that it doesn't mislead about siblings
  when that's not an option.
- 1582sugarNavsViewer-sw: Make some of the sugar navigator-bar menu
  items available in its viewer.
- 1581noAutoFlap-sw: Stop automatically putting up help-flaps for
  recording-controls, event theatre, and event roll.
- 1580sugarSupplies-sw: Special buttons for controlling the
  supplies flap and the flap accommodating the QuickGuide.
- 1579scriptorHeaderLook-sw: Proposed tweaks to the scriptor
  header:
- 1578variableSpacer-sw: Adds a generic variable transparent spacer
  that is halo-shy.
- 1577chooseGraphicFix-sw: Fixes the bug that a second request for
  'choose new graphic' for a sketchMorph for which a graphical-menu
  was already put up (in place of the original sketch) would generate
  an error.
- 1576sugarBtnBorder-yo: Fix the background color problem
  introduced by the canvas tranclucent change.

* Fri Aug 31 2007 Takashi Yamamiya <tak@metatoys.org>
- 2.1.1575-1
- content rev. 35
- 1575QuickGuide2-yo: Remove player in the IndexPage prototype.
- 1574WindowEvents-JMM-bf: Add WindowEvent handling, based on JMM's
  Ffenestri-b-4-Events-Morphic.1.cs.
- 1573baloonWording-yo: Change the wording in baloon help for the
  supplies tab.
- 1572fixAlphaInThumb-yo: fix alpha channel of thumbnails.
- 1571QuickGuide1-yo: First cut of quick guide index viewer system.
- 1570FixInspectProps-sw-yo: Fixes inspect property in the debug
  menu.
- 1569OLPCDisplayCopy-yo: Copy shouldn't be made for the display.
- 1568player-ref-tk: Fixes bug that prevented the Revert feature of
  bookmorphs from working.
- 1567BookIcon-tak: Better next and previous button for BookMorph.
- 1566safeFailDbus-yo: Ignore error when the VM doesn't have DBus
  plugin.
- 1565transformRestore-sw: Restore the change of 1552TransformFix.
- 1564projectViewIssues-sw: TRAC 2888: Makes project-view icons
  obey the acceptDrops flag governed in the halo menu.
- 1563picker-yo-sw: TRAC 2831: Remove all uses of Sensor in
  color-picking, thus allowing event-replays of modal color picking to
  work.
- 1562noEmptyMenus-sw: TRAC 2808: Don't show a menu icon in a
  viewer for a slot/variable which would have no menu items to offer
  in such a menu.
- 1561fullScreenBook-sw: TRAC 2825: When exiting full-screen mode
  of a BookMorph, restore the original position of the book.
- 1560evtRecorderItems-sw: TRAC 2830: Remove the old EventRecorder
  from the Objects catalog.
- 1559editBalloonText-sw: TRAC 2826 - Move the edit-balloon-text
  command from the debug menu to the extras menu, thus making it
  available to all users.
- 1558bookControls-sw: TRAC 2820: Add an option allowing book
  controls to appear at top *or* bottom of the book
- 1557arrowPointingUp-sw: TRAC 2867 - Make the arrow obtained from
  the objects catalog start out life pointing upward and with a
  heading of 0 to match.
- 1556gettextUtils-tak: Verify and export all gettext files.
- 1555TransWorldMenu-KR: make WorldMenu translatable
- 1554transformRevert-sw: Revert the change in 1552TransformFix, at
  least for the time being.
- 1553TransScriptor-KR: translation stuff for scriptor menu/goldbox
- 1552TransformFix-ar: A small fix for FormCanvas' transform
  methods due to the fact that WarpBlt wants to know its sourceForm
  before setting the cellSize

* Sun Aug 12 2007 Takashi Yamamiya <tak@metatoys.org>
- 2.1.1551-1
- content rev. 33
- 1551useGetTextnoop2-KR: apply #translatedNoop to bunch of classes
  for prototypes in flap
- 1550pickerForRotated-sw: Position the modal color-picker properly
  on rotated objects.
- 1549sugarTheatre-sw: Sugarizing the event theatre flaps.
- 1548pageTurnFont-sw: Use the etoy font for constructing the
  page-turn buttons.
- 1547collapseBelowSugar-sw: Exclude the area of the Sugar bar from
  the space considered suitable for locating collapsed window-tabs
  when the #sugarNavigator preference is true.
- 1546releaseBuilderOLPC-tak: Cleanup configure script.
- 1545unmatchedMouseDown-sw: bracketing mouse-up, to avoid some odd
  consequences of playback ending
- 1544WsFixupAug9-yo: Resolve conflicts from WsRangeFinder-ka.
- 1543WsRangeFinder-ka: Enable to use a range finder (GP2D12) with
  a World-Stethoscope.
- 1542sibsOfNonSketches-sw: Don't offer the 'make all my siblings
  look like me' item in the siblings submenu unless the morph is a
  SkechMorph
- 1541typo-sw: Fixes a typo in the help-text for the
  sound-recorder, and uses the opportunity to flesh out more detail in
  the message.
- 1540getEntireFile-sw: provide a null backstop method for
  RemoteFileStream>>converter:
- 1539SemaphoreCritical-ar: This change set fixes a set of severe
  problems with concurrent use of Delay.
- 1537Translucent-yo: SketchMorphs that have translucency (0 <
  alpha < 255) were not blending with the background in drawOn:.
  Yoshiki found the fix.
- 1536PolygonMorph-kfr:
- 1535varNameFix-sw: Do not allow a system player-slot name to be
  used as a user-defined variable name.
- 1534fontTweak-sw: One button label in the all-scripts tool was
  not being rendered in the standard etoys button font...

* Mon Aug 08 2007 Takashi Yamamiya <tak@metatoys.org>
- 2.1.1533-1
- content rev. 32
- 1533selectionMorphIssues-sw: Assure halo is deleted from an
  object being deleted, taking care in case in the SelectionMorph
  case.
- 1532SugarNav13-yo: Update the buttons in the Sugar bar.
- 1531noOldSoundRecorder-sw: Again expunge the old SoundRecorder
  from the Objects Catalog.  And set the new SoundRecorder up properly
  for translations.
- 1530gettextDirectory-tak: Gettext files are located good structure.
- 1529NebraskaOverMesh-yo: This might be a wrong way to fix it, but
  this changeset makes the Nebraska work over olpc mesh.
- 1528netNameResolverFix-mir:
- 1527useGettextFromArray-tak: Put #gettextNoop keyword in array
  literals for making translation templates.
- 1526gettextFromArray-tak: Aggregate gettext keywords from array
  literals.
- 1525TransExport4-KR: To make context information for tile
  wording/help better
- 1524suffixArrowFix-sw: Don't show suffix arrows on tiles that
  don't do arithmetic.
- 1523notShowUpdateDir-yo: Hide update directory from the project list.
- 1522resumeFix-bf: Cross-published from olpc2.0 update 1469resumeFix-bf.
- 1521enableScrollingText-sw: Make a scrolling-text item be
  available in the basic category of the objects catalog.
- 1520ScrollingField-width-tk: Fixes for ScrollableField
- 1519lastOccurrenceFix-sw: Fixes a bug in
  String>>findLastOccuranceOfString: startingAt:, and corrects the
  spelling of the selector to be #findLastOccurrenceOfString:startingAt:
- 1518animatedImageFix-sw: Fix an update problem with animated
  images; derived from from a fix posted to Mantis by Jerome Peace.
- 1517gettextNoopConflicts-sw: Fixes a few conflicts between update
  1512useGettextNoop and other recent updates:
- 1516ITNPosOption-yo: Add a menu item to set the prefered position
  of navigator.
- 1515fixEmbedInWindow-yo: We decided to take out 'put in a window'
  feature, but it is nice to make it work anyway.
- 1514avoidScreenCtlr-yo: Morphic World menu shouldn't hold onto
  ScreenController instance.
- 1513relBuilderFix-21-yo: Make sure that change set is cleared.
- 1512useGettextNoop-tak: A lot of fix to apply #translatedNoop
- 1511gettextNoopSupport-tak: Detect receiver of #translatedNoop to use 
  keywords.
- 1510soundRecorderViewer-sw: Adds control over record, stop, and
  play buttons of a sound recorder via new tiles in its viewer.
- 1509soundRecorder-sw: A simplified UI for John Maloney's SoundRecorder.
- 1508flapsOnLanguageChg-sw: Let the sugarNavigator preference dominate
  over the eToyFriendly flag.
- 1507magnifiers-sw: Only offer a single magnifier in the objects catalog.
- 1506noStackMorph-sw: As agreed at conference call 19July07,
  disenfranchise the StackMorph.
- 1505uers-sw: Fixes four methods that had the same 'uers' misspelling
  of 'users.
- 1504viewerSearchAgain-sw: Eliminate all non-letters from the string
  processing associated with Viewer Search.
- 1503barePlayerlessPhrase-sw: Treat bare playerless phrases on the
  desktop like all others.
- 1502lessENotation-sw: Improvements for printout of numeric values
  in etoy readouts.
- 1501moribundWatcher-sw: Get rid of problematical watchers.

* Mon Jul 30 2007 Bert Freudenberg <bert@freudenbergs.de> 
- 2.0.2471-1
- removed examples.dir
- content rev. 31:
- 1471SugarNav13-yo: Update the buttons in the Sugar bar.
- 1470notShowUpdateDir-yo: Hide update directory from the project list.
- 1469resumeFix-bf: fix resuming non-projects from Journal

* Thu Jul 24 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1468-1
- provide shared-mime-info magic file
- fixed icon (eben)
- declare mime-types in activity.info
- fix typo in etoys-instance script
- content rev 30:
- 1468datastore-bf: Make resuming a project from datastore 
  work (like after downloading a project). Also allow saving
  to and loading from datastore.
- 1467DBus-Core-bf-34: fix dbus error handling
- 1466SqueakToUtf8-ar: conversion from and to UTF-8
- 1465TransExportUI-tak: Modify Language Editor UI for 
  Korakurider's new gettext exporter.
- 1464TransExport3-KR: package pot by top-category of class
  excluding Morphic-*, export wordings and documentions
- 1463relBuilderBinIcons-yo: Release Builder creates icons.

* Thu Jul 19 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0-1462-1
- content rev 29:
- fix camera not opening (bf)
- 1462networkFix-mir-bf: Fix non-blocking socket connection (mir)
  Fix getting local host address (bf)
- 1461helpTypo-sw: Fixes a typo in the help msg for previous-arrow

* Wed Jul 18 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0-1460-1
- content rev 28:
- 1460journalFix2-bf: Use title from journal for project name,
  and vice versa
- 1459journalFix-bf: Datastore object id must not be retained
  in image or project files

* Tue Jul 17 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0-1458-1
- content rev 27:
- 1458avoidHelpFlap-sw: avoid appearance of an unexpected 
  evt-theatre help flap after a locale change
- 1457journal-bf: Datastore support part one: Create journal
  entries, update on deactivation, retrieve when resuming.
- 1456FasterLocaleChange-yo: Make locale change faster
- 1455SugarNav12-yo: Fix a one-off bug in the use of WarpBlt.
  Also, fix the corrupted bitmaps.
- 1454scriptorParam-sw: Fixes some problems in the headers of
  scriptors that have parameters.
- 1453DBus-Core-bf-33: fix writing of container types
- 1452FixCopyMorph-tak: Fix a problem that you cannot copy a 
  morph on Windows nor Mac.

* Fri Jul 13 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1451-1
- fix spec file clean, add _smp_mflags as requested by fedora (bf)
- fix alternate image logic (yo)
- content rev 26:
- 1451ownerBuddy-bf: Treat owner buddy specially: do not show in 
  peer list, use  its nick as authorName (fixes #2091)
- 1450TransExport2-KR: merge duplicate msgid entry on export, and
  show each occurence as header for msg id
- 1449WanderingLetters-tk
- 1448MouseOverHalosFix-tak: Fixed bug that mouse over halos need
  a double click (#2086)
- 1447supressViewerNotice-yo: In non eToyFriendly mode, building
  viewer progress bar is suppressed.  (Also, #translated is added.)
- 1446disablePutInWindow-yo: In eToyFriendly mode, disable put in 
  a window feature.
- 1445SugarNav11-yo: Replace quit button with stop button.
- 1444CatalogEntriesJul12-yo: Adjust some labels in object catalog.
- 1443RemoveAtomicGame: Remove AtomicGame from the system.
- 1442TransExport1-KR: Collect translated literals and extract them
  to gettext POT (prototype attempt).
- 1441ExClipboardMorphic4-tak: Better behavior in Sugar environment:
  Fixed a bug that it happens to be copied 3 times to Sugar frame.
  Fixed a bug not to work dragging out on Sugar.
- 1440HonorCursorChange-yo: biggerCursor preference change informes
  HandMorph and reinitializes the class var.
- 1439rotatedBareTileOops-sw: Fixes a glitch that caused the jump
  when grabbing a bare tile to appear again.

* Thu Jul 12 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1438-1
- add workaround for ticket 1951 (bf)
- fix SUGAR_BUNDLE_PATH in etoys-factory (bf)
- content rev. 24:
- 1438DndOutMorphic-tak: An immature attempt of dragging out.
- 1437explicitlySetDisplay-yo: Upon release, we set display depth
   to 16 explicitly. 
- 1436VIrtDepthNativeDepth-yo: The current OLPCVirtualDisplay 
  stays in 32-bit mode. With this change, it uses the native display
  depth when saving.
- 1435WSandCatalog-yo:
  SpectrumAnalyzer gets bigger buttons.
  SpectrumAnalyzer shows up in Multimedia category.
  VideoMorph shows up as 'Camera'.
  PhonePad is moved to Multimedia.
  PhonePad gets better buttons.
  WorldStethoscope is moved to Multimedia.
  WorldStethoscope get bigger buttons.

* Tue Jul 10 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1434-1
- use bundlebuilder for packaging .xo (bf)
- include NEWS file in xo bundle, ChangeLog in RPM (bf)
- look for alternative "olpc-dev/etoys.image" in /media instead of /mnt
- content rev. 23:
- 1434releaseForOLPC3-yo: Tweak the release builder code again
- 1433SaveVideo-yo: VideoMorph can be saved into a project, and it
  pauses when the project switches.
- 1432TRscalingOptions-yo: change the wording for English via translation
- 1431scalingChoice-yo: Enable translations for scaling options and helps
- 1430KedamaPatchTiles-yo
- 1429bareTiles-sw: Do not allow editing in tiles on the desktop.  Instead,
  any mouse down on such a tile basically just picks it up.  This is not 
  100% ideal, but better than the previous situation.
- 1428caretIssues-sw: Refactors the logic for adding/deleting/showing/hiding
  carets on tiles.
- 1427kbdFocusInPhrase-sw: Assure release of keyboard focus when user grabs
  a phrase tile
- 1426FixScaledDrop-ar: Fixes a problem with DnD handling when scaling is on.
- 1425simpleErase-sw: Make the 'erase' and 'stamp & erase' tiles do simple
  deletion of the object, *not* putting it in the trash and *not* animating.
- 1424tinyTweaks-sw: Default clock does not show seconds. 'make this the 
  template for new pages' wording change in 'advanced' book-morph submenu.
- 1423scriptorMenu-sw: Remove some redundancy between scriptor menu and 
  gold-box, and harmonize the eToyFriendly and non-eToyFriendly variants of
  the scriptor menu.
- 1422alignProjSorter-yo: Align the sorter. Add scroll bar to the project
  sorter when it is too big.
- 1421viewerTabs-sw: When toggling the implicitSelfInTiles preference, 
  assure that all the viewers represented by viewer-flap-tabs in the 
  projects are fully instantiated.

* Fri Jun 29 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1420-1
- split off activity into .xo bundle
- removed factory-service (now in Sugar as sugar-native-factory)
- cleaned up spec file
- content rev. 22:
- use Ctrl-X/C/V for cut/copy/paste
- copy an etoys object as image to other activity
- fix listen loop

* Tue Jun 26 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1401
- IPv6 image support code (mir, ikp)
- updated projects

* Tue Jun 26 2007 Bert Freudenberg <bert@freudenbergs.de>
- remove python activity wrapper, get rid of automake (bf)
- add factory-service (external activity factory) (bf)
- provide activity protocol on DBus from etoys (bf)
- require squeak-vm-3.9-11 for DBus support and IPv6
- 2.0.1396 from SVN rev.12
- new function tiles, treasure chest in scriptor, various fixes (sw)
- hide screen scaling button if on native 1200x900 (yo) 
- sibling fixes (tk)
- project load fix, viewer feedback (kfr)

* Thu Jun 14 2007 Bert Freudenberg <bert@freudenbergs.de>
- added detailed ChangeLog (generated via mkChangeLog)
- for old Sugar, use nick name sans spaces as key
- 2.0.1361 from SVN rev. 11
- enhanced BookMorph controls (sw)
- dnd supports images and text in addition to files now (tak)
- add DBus bindings (impara)

* Mon May 14 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1349 from SVN rev. 8
- put back screen sharing button

* Thu May 10 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1345 from SVN rev. 7
- minor fixes
- new demo project

* Wed May 09 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1337 from SVN rev. 6
- added presence service support, buddy badges (bf)
- Meta parser, used for expression precedence (yo, alex)
- s-expr serialization (yo)
- simulate 1200x900 on any screen (ar)

* Tue Apr 24 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1283 from SVN rev. 5:
- fix olpc bar to not constantly consume CPU (yo)

* Mon Apr 23 2007 Bert Freudenberg <bert@freudenbergs.de>
- generate activity_version for activity.info from etoys.spec
- 2.0.1276 from SVN rev. 4:
- navigator bar and supplies in olpc look (yo)
- blueprint canvas (sw), optional implicit self in tiles (sw)

* Mon Apr 02 2007 Bert Freudenberg <bert@freudenbergs.de>
- use $HOME as user directory for trial1

* Fri Mar 30 2007 Bert Freudenberg <bert@freudenbergs.de>
- moved Content to SVN (now at rev. 3)
- 2.0.1252
- bigger cursors (bf)
- load rather than generate DSA key (bf)

* Fri Mar 23 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1238, launch project from webbrowser (bf)
- add Ogg support (tak, needs new plugin)
- better camera support (dgd, needs new plugin)
- updated DemonCastle project (ted)

* Tue Feb 27 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1224-2: Fixes to run under new Sugar
- adjust case of file/directory names to match other activities

* Wed Feb 21 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1224, fixes, added XML support, new DAV-based updates

* Mon Feb 12 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1203, fix icon path

* Mon Jan 17 2007 Yoshiki Ohshima <yoshiki@squeakland.org>
- 2.0.1198, Changes from Scott Wallace

* Mon Jan 16 2007 Yoshiki Ohshima <yoshiki@squeakland.org>
- 2.0.1192, initial screens tweak

* Mon Jan 15 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1188, minor fixes

* Fri Jan 12 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1185, new start screen

* Thu Jan 11 2007 Yoshiki Ohshima <yoshiki@squeakland.org>
- 2.0.1183, pre-loaded Welcome and a tutorial projects

* Wed Jan 10 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1179, updated projects

* Tue Jan 09 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1178, more font adjustments

* Fri Jan 05 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1168, use Komika fonts

* Thu Jan 04 2007 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1166, fixed DemonCastle

* Fri Dec 22 2006 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1156, run from /mnt/stick/olpc-dev/etoys.image if existant

* Tue Dec 19 2006 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1145, patched icon because of broken css lib

* Mon Dec 18 2006 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1142, new bundle info, requires latest sugar

* Fri Dec 01 2006 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1134, require squeak-vm >= 3.9-10 for ALSA fix

* Fri Nov 24 2006 Bert Freudenberg <bert@freudenbergs.de>
- 2.0.1130, activity bundle v1, deactivate sound if not focused

* Fri Nov 10 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1118, stop sound when done

* Fri Oct 27 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1108, more example projects

* Thu Oct 26 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1105, example projects

* Wed Oct 25 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1104, DemonCastle1.009.pr, Welcome.023.pr

* Tue Oct 24 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1102, DemonCastle1.007.pr, Welcome.021.pr

* Sat Oct 21 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1098

* Fri Oct 20 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1095 added Welcome and DemonCastle1 projects

* Thu Oct 19 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1093 relicense to APACHE 2.0 / MIT

* Wed Oct 18 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1092

* Tue Oct 17 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1085

* Wed Oct 11 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1045

* Tue Oct 10 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1039

* Mon Oct 09 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1037

* Sat Oct 07 2006 Bert Freudenberg <bert@freudenbergs.de>
- 1.0.1032

* Fri Oct 06 2006 Bert Freudenberg <bert@freudenbergs.de>
- initial RPM for OLPC (1.0.1022)
