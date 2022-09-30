%undefine _debugsource_packages

Name:		bloboats
Summary:	Boat Racing Game
Version:	1.0.2
Release:	11
Source:		http://mirror.kapsi.fi/bloboats.dy.fi/%{name}-%{version}.tar.gz
Patch1:		bloboats-1.0.2-gcc7.patch
License:	GPL
Group:		Games/Arcade
URL:		http://bloboats.dy.fi/
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_net)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(glu)
BuildRequires:	ImageMagick

%description
Bloboats is a boat racing game in which the objective is to reach the
goal as fast as possible, at least faster than your friend does.

%prep
%autosetup -p1
sed -i '1570s|modes > 0|modes != 0|' src/menu.cpp

%build
%make_build DATADIR=%{_datadir}/%{name}/data

%install
%make_install PREFIX=%{buildroot} \
    BINARYDIR=%{buildroot}%{_bindir} \
    DATADIR=%{buildroot}%{_datadir}/%{name}/data

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Boat Racing Game
Exec=%{name}
Icon=%{name}
Terminal=false
StartupNotify=false
Type=Application
Categories=Game;ArcadeGame;
EOF

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp data/images/icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
chmod -R 644 %{buildroot}%{_datadir}

%files
%doc copying.txt readme.txt
%{_bindir}/%{name}
%{_sysconfdir}/%{name}.dirs
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Dec 08 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuilt for Fedora
* Thu Apr 23 2020 danf <danf> 1.0.2-11.mga8
+ Revision: 1571480
- Fix Comment= in .desktop file
* Wed Feb 12 2020 umeabot <umeabot> 1.0.2-10.mga8
+ Revision: 1510736
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%makeinstall_std
* Fri Sep 21 2018 umeabot <umeabot> 1.0.2-9.mga7
+ Revision: 1295509
- Mageia 7 Mass Rebuild
* Sun Sep 24 2017 cjw <cjw> 1.0.2-8.mga7
+ Revision: 1158716
- patch1: fix build with gcc7
* Wed Feb 10 2016 umeabot <umeabot> 1.0.2-7.mga6
+ Revision: 953254
- Mageia 6 Mass Rebuild
* Thu Sep 10 2015 daviddavid <daviddavid> 1.0.2-6.mga6
+ Revision: 875507
- Fix build with new rpm ( empty debuginfo)
* Wed Oct 15 2014 umeabot <umeabot> 1.0.2-5.mga5
+ Revision: 742295
- Second Mageia 5 Mass Rebuild
- Mageia 5 Mass Rebuild
* Fri Oct 18 2013 umeabot <umeabot> 1.0.2-3.mga4
+ Revision: 503112
- Mageia 4 Mass Rebuild
* Fri Jan 11 2013 umeabot <umeabot> 1.0.2-2.mga3
+ Revision: 346919
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu Nov 24 2011 zezinho <zezinho> 1.0.2-1.mga2
+ Revision: 171710
- new version
* Wed May 11 2011 dmorgan <dmorgan> 1.0.1-2.mga1
+ Revision: 97162
- imported package bloboats
