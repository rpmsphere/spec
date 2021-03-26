%define	oname	FreeFileSync
%define __unzip	%{_bindir}/unzip -o

Name:		freefilesync
Version:	9.6
Release:	1
Summary:	A free file sync tool
Group:		File tools
License:	GPLv3
URL:		http://sourceforge.net/projects/freefilesync/
Source0:	https://www.freefilesync.org/download/FreeFileSync_%{version}_Source.zip
Source2:	FreeFileSync.desktop
Source3:	RealTimeSync.desktop
Source4:	FreeFileSync.png
Patch0:		missing-includes.patch
BuildRequires:	ImageMagick
BuildRequires:	wxGTK3-devel
BuildRequires:	boost-devel

%description
FreeFileSync is an Open-Source folder comparison and synchronization tool.
It is optimized for highest performance and usability without restricted
or overloaded UI interfaces.

%prep
%setup -q -c
%autopatch -p1

sed -i 's_../wx+_wx+_' FreeFileSync/Source/ui/gui_generated.cpp
sed -i '/^CXXFLAGS/s|-O3|%{optflags} -Wno-unused-local-typedefs -Wno-deprecated-declarations -Wno-literal-suffix|' FreeFileSync/Source/Makefile FreeFileSync/Source/RealTimeSync/Makefile
sed -i -e '/^LINKFLAGS/s|-s|%{build_ldflags}|' -e 's|wx-config|wx-config-3.0|' FreeFileSync/Source/Makefile FreeFileSync/Source/RealTimeSync/Makefile

sed -i 's/m_listBoxHistory->GetTopItem()/0/g' FreeFileSync/Source/ui/main_dlg.cpp
sed -i 's!static_assert!//static_assert!' zen/scope_guard.h
sed -i 's!inline!!g' FreeFileSync/Source/ui/version_check_impl.h
sed -i -e 's|gtk+-2.0|gtk+-3.0|' -e 's|-Wfatal-errors||' -e 's|$RPM_LD_FLAGS|$(RPM_LD_FLAGS)|' FreeFileSync/Source/Makefile FreeFileSync/Source/RealTimeSync/Makefile

# Fix install
install -Dpm644 Changelog.txt FreeFileSync/Build/

%build
# FFS
make -C \
	FreeFileSync/Source \
	launchpad

# RTS
make -C \
	FreeFileSync/Source/RealTimeSync \
	launchpad

%install
#FFS
%make_install -C FreeFileSync/Source

#RTS
%make_install -C FreeFileSync/Source/RealTimeSync

install -Dm644 %{_sourcedir}/%{oname}.desktop \
	%{buildroot}%{_datadir}/applications/%{oname}.desktop

install -Dm644 %{_sourcedir}/RealTimeSync.desktop \
        %{buildroot}%{_datadir}/applications/RealTimeSync.desktop

rm -rf %{buildroot}%{_docdir}/%{oname}

# (daviddavid) Fix missing icons (mga#14750)
# icons
for png in 256x256 128x128 64x64 32x32 22x22 16x16; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${png}/apps/
  convert -geometry $png %{_sourcedir}/%{oname}.png \
	%{buildroot}%{_datadir}/icons/hicolor/${png}/apps/%{oname}.png
done

%files
%{_bindir}/FreeFileSync
%{_bindir}/RealTimeSync
%{_datadir}/FreeFileSync/
%{_datadir}/applications/FreeFileSync.desktop
%{_datadir}/applications/RealTimeSync.desktop
%{_datadir}/icons/hicolor/*/apps/%{oname}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 9.6
- Rebuild for Fedora
* Tue Jan 09 2018 wally <wally> 9.6-1.mga7
+ Revision: 1191918
- new version 9.6
- add build fixes from AUR
- add patch to fix missing includes
- rebuild for new boost
* Sat Jun 03 2017 akien <akien> 6.2-12.mga6
+ Revision: 1106094
- Rebuild for wxgtk 3.0.3.1
* Thu Jun 02 2016 daviddavid <daviddavid> 6.2-11.mga6
+ Revision: 1019876
- rebuild for wxgtk3.0 built with GTK2
* Sat Dec 26 2015 daviddavid <daviddavid> 6.2-10.mga6
+ Revision: 915175
- rebuild for new boost 1.60.0
* Fri Sep 25 2015 daviddavid <daviddavid> 6.2-9.mga6
+ Revision: 883700
- rebuild for new boost 1.59.0
* Fri Aug 14 2015 daviddavid <daviddavid> 6.2-8.mga6
+ Revision: 864766
- fix missing icon for desktop file (mga#14750)
- add BuildRequires on imagemagick
  + ycantin <ycantin>
    - rebuild for new wxgtk built with wxRE_ADVANCED
* Fri Jul 31 2015 daviddavid <daviddavid> 6.2-6.mga6
+ Revision: 859997
- rebuild for new boost-1.58.0
* Thu Jul 23 2015 philippem <philippem> 6.2-5.mga6
+ Revision: 856572
- fix rebuild for new wxgtk built with gtk3
  + daviddavid <daviddavid>
    - rebuild for new wxgtk built with gtk3
* Wed Oct 15 2014 umeabot <umeabot> 6.2-4.mga5
+ Revision: 744369
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 6.2-3.mga5
+ Revision: 679336
- Mageia 5 Mass Rebuild
* Fri Feb 21 2014 wally <wally> 6.2-2.mga5
+ Revision: 595247
- drop P0 and handle setting build time flags with sed magic
* Fri Feb 21 2014 wally <wally> 6.2-1.mga5
+ Revision: 595240
- add build fixes from AUR
- bundle latest zenXml with sources and build with it
- clean .spec a bit
  + fwang <fwang>
    - new version  6.2
* Sat Oct 19 2013 umeabot <umeabot> 5.10-5.mga4
+ Revision: 529411
- Mageia 4 Mass Rebuild
* Tue Jul 09 2013 fwang <fwang> 5.10-4.mga4
+ Revision: 451793
- rebuild for new boost
* Thu Apr 11 2013 barjac <barjac> 5.10-3.mga3
+ Revision: 409674
- rebuild for boost-1.53
* Fri Jan 11 2013 umeabot <umeabot> 5.10-2.mga3
+ Revision: 350851
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu Dec 20 2012 fwang <fwang> 5.10-1.mga3
+ Revision: 333044
- new version 5.10
* Thu Dec 20 2012 fwang <fwang> 5.9-2.mga3
+ Revision: 333034
- rebuild for new boost
* Mon Nov 05 2012 juancho <juancho> 5.9-1.mga3
+ Revision: 314485
- imported package freefilesync
* Mon Nov 05 2012 Joaquín Moreno <joaquinmandriva@gmail.com> 5.9-3.bdk.mga2
- new version 5.9
* Mon Jun 04 2012 Joaquín Moreno <joaquinmandriva@gmail.com> 5.4-1.bdk.mga2
- new version 5.4
* Sun May 27 2012 Joaquín Moreno <joaquinmandriva@gmail.com> 5.3-1.bdk.mga2
- Packaged to Mageia 2 (Blogdrake Repository)
* Tue Feb 28 2012 Andrey Bondrov <abondrov@mandriva.org> 5.0-1mdv2012.0
+ Revision: 781312
- imported package freefilesync
* Tue Feb 03 2012 Joaquín Moreno <joaquinmandriva@gmail.com> 5.0-6.bdk.mga
- new version 5.0
* Mon Nov 28 2011 Joaquín Moreno <joaquinmandriva@gmail.com> 4.5-5.bdk.mga
- new version 4.5
* Mon Oct 10 2011 Joaquín Moreno <joaquinmandriva@gmail.com> 4.1-4.bdk.mga
- new version 4.1
* Mon Sep 26 2011 Joaquín Moreno <joaquinmandriva@gmail.com> 4.0-3.bdk.mga
- new version 4.0
* Wed Sep 21 2011 Joaquín Moreno <joaquinmandriva@gmail.com> 3.21-2.bdk.mga
- new version 3.21
* Fri Jul 15 2011 Joaquín Moreno <joaquinmandriva@gmail.com> 3.11-1.bdk.mga
- Packaged to Mageia (Blogdrake Repository)
