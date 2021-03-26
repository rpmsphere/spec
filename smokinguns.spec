Name:           smokinguns
Summary:        A semi-realistic simulation of the "Old West's" great atmosphere FPS game
Version:        1.1
Release:        1
Group:          Games/Shooter
License:        GPLv2+
URL:            http://www.smokin-guns.org
Source0:        %{name}.sh
Source1:        %{name}.autodlrc
Source2:        %{name}.desktop
Source3:        %{name}.png
BuildRequires:  desktop-file-utils
Requires:       ioquake3
Requires:       opengl-games-utils
BuildArch:      noarch

%description
Smokin' Guns is intended to be a semi-realistic simulation of the "Old West's"
great atmosphere & was developed on Id Software's Quake III Arena Engine.

This total conversion includes completely new weapons created with historically
correct information about damage, rate of fire, reload time, etc. It also
includes new gametypes and maps inspired mostly by movies. And to increase the
feeling of a "gunslingers atmosphere" we also created music tracks and sounds
adapted to this time period.

Smokin' Guns uses the GPL licensed ioquake3 engine, however the Smokin' Guns
data files are not freely redistributable. This package will install an Smokin'
Guns menu entry, which will automatically download the necessary data files
(350 MB!) the first time you start Smokin' Guns.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ioquake3

install -p -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/ioquake3

# below is the desktop file and icon stuff.
desktop-file-install --vendor ""            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE3} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

%files
%{_bindir}/%{name}
%{_datadir}/ioquake3/%{name}.autodlrc
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%changelog
* Wed Mar 10 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuild for Fedora
* Wed Sep 19 2018 umeabot <umeabot> 1.0-10.mga7
  (not released yet)
+ Revision: 1275441
- Mageia 7 Mass Rebuild
* Fri Feb 05 2016 umeabot <umeabot> 1.0-9.mga6
+ Revision: 937634
- Mageia 6 Mass Rebuild
* Fri Feb 05 2016 umeabot <umeabot> 1.0-8.mga6
+ Revision: 937181
- Mageia 6 Mass Rebuild
+ akien <akien>
- Fix URL
* Wed Oct 15 2014 umeabot <umeabot> 1.0-7.mga5
+ Revision: 745271
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 1.0-6.mga5
+ Revision: 689214
- Mageia 5 Mass Rebuild
* Fri Oct 18 2013 umeabot <umeabot> 1.0-5.mga4
+ Revision: 518421
- Mageia 4 Mass Rebuild
* Mon Jan 14 2013 umeabot <umeabot> 1.0-4.mga3
+ Revision: 382212
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Fri Nov 16 2012 juancho <juancho> 1.0-3.mga3
+ Revision: 318424
- Change group to Shooter
* Tue Feb 14 2012 juancho <juancho> 1.0-2.mga2
+ Revision: 208599
- Updated autodownloader window title
* Thu Dec 08 2011 juancho <juancho> 1.0-1.mga2
+ Revision: 178842
- Fix file permissions and shortened Summary
- imported package smokinguns
