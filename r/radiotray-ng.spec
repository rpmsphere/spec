Name:		radiotray-ng
Version:	0.2.7
Release:	7
Summary:	An Internet radio player for Linux
License:	GPLv3+
Group:		Sound/Players
URL:		https://github.com/ebruck/radiotray-ng
Source0:	https://github.com/ebruck/radiotray-ng/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Add-French-radio-stations.patch
Patch1:		0001-Don-t-override-system-CFLAGS-CXXFLAGS.patch
Patch2:		0001-Don-t-treat-warnings-as-errors.patch
Patch3:		0001-Port-to-Ayatana-AppIndicator.patch
BuildRequires:	git-core
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	boost-devel
BuildRequires:	wxgtk-devel
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(libxdg-basedir)
BuildRequires:	pkgconfig(libbsd)
BuildRequires:	pkgconfig(ayatana-appindicator3-0.1)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(glibmm-2.4)
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-plugins-bad
Requires:	gstreamer1.0-plugins-ugly
Requires:	gstreamer1.0-soup
Requires:	python-lxml
Obsoletes:	radiotray < 0.7.3-12
Provides:	radiotray

%description
Radiotray-NG runs in the system tray allowing you to select and play
configured radio stations.

%prep
%autosetup -p1 -Sgit_am

%build
%cmake \
	-DCONFIGURED_ONCE:BOOL=YES
%cmake_build

%install
%cmake_install

# fix .desktop file
desktop-file-edit %{buildroot}%{_datadir}/applications/radiotray-ng.desktop \
	--set-comment="Internet Radio Player" \
	--set-icon=radiotray-ng-on

# another .desktop file with bad icon
desktop-file-edit %{buildroot}%{_datadir}/applications/rtng-bookmark-editor.desktop \
	--set-icon=radiotray-ng-on

# install better app icons from ubuntu-mono-light
rm -rf %{buildroot}%{_iconsdir}/hicolor/*/apps/radiotray-ng-{on,off}.png
install -Dpm644 data/themes/ubuntu-mono-light/apps/24/radiotray-ng-off.svg \
	%{buildroot}%{_iconsdir}/hicolor/scalable/apps/radiotray-ng-off.svg
install -Dpm644 data/themes/ubuntu-mono-light/apps/24/radiotray-ng-on.svg \
        %{buildroot}%{_iconsdir}/hicolor/scalable/apps/radiotray-ng-on.svg

# we don't want these
rm -rf %{buildroot}%{_iconsdir}/ubuntu*

# handle docs in files section
rm -rf %{buildroot}%{_docdir}

%files
%license COPYING
%doc README.md AUTHORS
%{_bindir}/radiotray-ng
%{_bindir}/rt2rtng
%{_bindir}/rtng-bookmark-editor
%{_datadir}/radiotray-ng/
%{_datadir}/applications/radiotray-ng.desktop
%{_datadir}/applications/rtng-bookmark-editor.desktop
%{_sysconfdir}/xdg/autostart/radiotray-ng.desktop
%{_iconsdir}/{hicolor,Yaru}/*/apps/radiotray-ng*.{png,svg}
%{_iconsdir}/breeze/apps/*/radiotray-ng*.{png,svg}
%{_datadir}/metainfo/radiotray-ng.appdata.xml

%changelog
* Sat Apr 3 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.7
- Rebuilt for Fedora
* Sun Aug 16 2020 wally <wally> 0.2.7-7.mga8
+ Revision: 1614366
- rebuild for new wxgtk 3.1.4
* Mon Aug 03 2020 wally <wally> 0.2.7-6.mga8
+ Revision: 1610836
- add patch to port to Ayatana AppIndicator
* Sun May 03 2020 wally <wally> 0.2.7-5.mga8
+ Revision: 1578108
- rebuild for boost 1.73.0
* Wed Feb 19 2020 umeabot <umeabot> 0.2.7-4.mga8
+ Revision: 1544896
- Mageia 8 Mass Rebuild
* Sun Jan 26 2020 wally <wally> 0.2.7-3.mga8
+ Revision: 1483428
- rebuild for boost 1.72.0
- build with new cmake macros
* Tue Nov 12 2019 wally <wally> 0.2.7-2.mga8
+ Revision: 1459488
- rebuild for wxgtk 3.1.3
* Sun Oct 27 2019 wally <wally> 0.2.7-1.mga8
+ Revision: 1456066
- new version 0.2.7
* Wed Jul 10 2019 wally <wally> 0.2.6-1.mga8
+ Revision: 1419909
- new version 0.2.6
* Mon Jul 08 2019 wally <wally> 0.2.5-3.mga8
+ Revision: 1419534
- rebuild for wxgtk 3.1.2 with 2.8 compatibility
* Sun Jun 30 2019 wally <wally> 0.2.5-2.mga8
+ Revision: 1416373
- rebuild with gtk3 enabled wxgtk 3.1.2
* Mon Apr 15 2019 wally <wally> 0.2.5-1.mga7
+ Revision: 1390796
- new version 0.2.5
+ alexl <alexl>
- typo
* Sat Oct 20 2018 wally <wally> 0.2.4-1.mga7
+ Revision: 1322978
- new version 0.2.4
* Tue Oct 16 2018 wally <wally> 0.2.3-3.mga7
+ Revision: 1321092
- rebuild for new boost 1.68.0
* Sun Oct 07 2018 umeabot <umeabot> 0.2.3-2.mga7
+ Revision: 1318465
- Mageia 7 Mass Rebuild
* Sun Jul 29 2018 wally <wally> 0.2.3-1.mga7
+ Revision: 1245750
- new version 0.2.3
* Sun May 06 2018 wally <wally> 0.2.2-1.mga7
+ Revision: 1226839
- new version 0.2.2
* Sat Jan 20 2018 wally <wally> 0.2.0-5.mga7
+ Revision: 1195091
- require gstreamer1.0-plugins-ugly
* Sat Jan 06 2018 wally <wally> 0.2.0-4.mga7
+ Revision: 1190974
- yet another icon fix
- use better app icons
* Sat Jan 06 2018 wally <wally> 0.2.0-2.mga7
+ Revision: 1190969
- fix bookmark editor menu icon
* Sat Jan 06 2018 wally <wally> 0.2.0-1.mga7
+ Revision: 1190958
- new version 0.2.0
* Mon Dec 25 2017 wally <wally> 0.1.8-4.mga7
+ Revision: 1184705
- rebuild for new boost
* Tue Nov 21 2017 tv <tv> 0.1.8-3.mga7
+ Revision: 1178106
- rebuild for boost 1.65
* Sat Nov 04 2017 wally <wally> 0.1.8-2.mga7
+ Revision: 1175938
- install better app menu icon
* Sat Nov 04 2017 wally <wally> 0.1.8-1.mga7
+ Revision: 1175926
- imported package radiotray-ng to replace radiotray
