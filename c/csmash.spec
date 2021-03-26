Name:		csmash
Summary:	A 3D table tennis game
Version:	0.6.6
Release:	12.1
Source0:	http://belnet.dl.sourceforge.net/sourceforge/cannonsmash/%{name}-%{version}.tar.bz2
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
Patch0:		csmash-0.6.6-64bit-fixes.patch
Patch1:		csmash-0.6.6-gcc4.patch
Patch2:		csmash-0.6.6-extraqualif.patch
Patch3:		csmash-0.6.6-cflags.patch
Patch4:		csmash-0.6.6-format.patch
Patch5:         csmash-0.6.6-datadir.patch
URL:		http://CannonSmash.sourceforge.net/
License:	GPLv2
Group:		Games/Sports
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	gtk2-devel
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libjpeg)
#BuildRequires:	texinfo
BuildRequires:	pkgconfig(zlib)
BuildRequires:	gettext
BuildRequires:	bison

%description
CannonSmash is a 3D tabletennis game. The goal of this project is to represent
various strategies of tabletennis on computer game.

%prep
%setup -q
%autopatch -p1

%build
autoreconf -fi
%configure
make

%install
%makeinstall
rm -rf %{buildroot}%{_datadir}/%{name}/win32

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Cannon Smash
Comment=3D table-tennis game
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;SportsGame;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README README.en
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Tue May 15 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.6
- Rebuild for Fedora
* Tue Sep 12 2017 cjw <cjw> 0.6.6-25.mga7
+ Revision: 1153112
- fix debug packages
* Thu Feb 04 2016 umeabot <umeabot> 0.6.6-24.mga6
+ Revision: 934219
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 0.6.6-23.mga5
+ Revision: 739359
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.6.6-22.mga5
+ Revision: 678603
- Mageia 5 Mass Rebuild
* Fri Oct 18 2013 umeabot <umeabot> 0.6.6-21.mga4
+ Revision: 503604
- Mageia 4 Mass Rebuild
* Fri Jan 11 2013 umeabot <umeabot> 0.6.6-20.mga3
+ Revision: 348363
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Tue Jun 12 2012 dams <dams> 0.6.6-19.mga3
+ Revision: 260059
- fix configure option
* Sun Jun 10 2012 dams <dams> 0.6.6-18.mga3
+ Revision: 259203
- fix path for binary
- clean specfile
- update specfile to use 'gamesbindir' and 'gamesdatadir'
* Wed Sep 14 2011 fwang <fwang> 0.6.6-18.mga2
+ Revision: 143363
- bunzip the patches
* Mon May 09 2011 ahmad <ahmad> 0.6.6-18.mga1
+ Revision: 96654
- Drop BR esound-devel, phasing out esound from the distro
* Sun Mar 13 2011 stormi <stormi> 0.6.6-17.mga1
+ Revision: 70692
- clean spec
- fix license
- imported package csmash
