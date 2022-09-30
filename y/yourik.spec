Name:          yourik
Version:       2.1.2
Release:       8
Summary:       The animal rights themed arcade shooter
Group:         Games/Arcade
License:       Public Domain
URL:           https://github.com/psemiletov/yourik-qt5
Source0:       https://github.com/psemiletov/yourik-qt5/archive/%{version}/%{name}-qt5-%{version}.tar.gz
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5OpenGL)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(SDL2_mixer)

%description
Yourik The Intergalactic Rabbit is the animal
rights-themed arcade game. Fight your way from the
 vivisection laboratory and save the animals. 
You are the genetically modified rabbit, Yourik,
the Intergalactic One.

%prep
%setup -q -n %{name}-qt5-%{version}

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot} 

%files
%{_bindir}/yourik
%{_datadir}/applications/yourik.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/64x64/apps/yourik.png

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.2
- Rebuilt for Fedora
* Sun Apr 03 2022 umeabot <umeabot> 2.1.2-8.mga9
+ Revision: 1842279
- Mageia 9 Mass Rebuild
* Thu Dec 17 2020 umeabot <umeabot> 2.1.2-7.mga8
+ Revision: 1660335
- Rebuild for new Qt5
* Sat Feb 15 2020 umeabot <umeabot> 2.1.2-6.mga8
+ Revision: 1525187
- Mageia 8 Mass Rebuild
* Tue Apr 02 2019 umeabot <umeabot> 2.1.2-5.mga7
+ Revision: 1385332
- Qt5 Rebuild
* Sun Sep 23 2018 umeabot <umeabot> 2.1.2-4.mga7
+ Revision: 1302026
- Mageia 7 Mass Rebuild
* Sat Feb 10 2018 daviddavid <daviddavid> 2.1.2-3.mga7
+ Revision: 1199998
- use a named-versioned tarball from github
- fix owner of data dir
* Mon Feb 05 2018 semiletov <semiletov> 2.1.2-2.mga7
+ Revision: 1199104
- imported package yourik
