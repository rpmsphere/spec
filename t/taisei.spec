Name:           taisei
Version:        1.3.1
Release:        2
Summary:        Taisei is a fan-made, Open Source clone of the Touhou series
License:        MIT and CC0
Group:          Games/Shooter
URL:            https://taisei-project.org
Source0:        https://github.com/taisei-project/taisei/releases/download/v%{version}/%{name}-v%{version}.tar.xz
BuildRequires:  glslc
BuildRequires:  meson
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3
BuildRequires:  python3-docutils

%description
Taisei is an open clone of the Touhou series. Touhou is a one-man project
of shoot-em-up games set in an isolated world full of Japanese folklore.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson --buildtype=plain -Dstrip=false
%meson_build

%install
%meson_install

%files
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-replay-viewer.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/mimetypes/%{name}-replay.png

%changelog
* Sun Jan 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.1
- Rebuilt for Fedora
* Sat Oct 02 2021 wally <wally> 1.3.1-2.mga9
+ Revision: 1747940
- rebuild for openssl 3.0.0
* Fri Jan 15 2021 akien <akien> 1.3.1-1.mga8
+ Revision: 1671975
- Version 1.3.1, using Meson and new deps
* Fri Feb 14 2020 daviddavid <daviddavid> 1.1.2-3.mga8
+ Revision: 1517758
- use new cmake macros
+ umeabot <umeabot>
- Mageia 8 Mass Rebuild
* Sun Sep 23 2018 umeabot <umeabot> 1.1.2-2.mga7
+ Revision: 1301309
- Mageia 7 Mass Rebuild
* Sat Dec 30 2017 akien <akien> 1.1.2-1.mga7
+ Revision: 1187907
- Version 1.1.2
- Switch to SDL2
* Fri Sep 22 2017 cjw <cjw> v1.0a_116-10.mga7
+ Revision: 1156954
- fix debug packages
* Mon Feb 08 2016 umeabot <umeabot> v1.0a_116-9.mga6
+ Revision: 943435
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> v1.0a_116-8.mga5
+ Revision: 745994
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> v1.0a_116-7.mga5
+ Revision: 689683
- Mageia 5 Mass Rebuild
* Sat Oct 19 2013 umeabot <umeabot> v1.0a_116-6.mga4
+ Revision: 526465
- Mageia 4 Mass Rebuild
* Tue Jun 04 2013 fwang <fwang> v1.0a_116-5.mga4
+ Revision: 436961
- rebuild for new libpng
* Mon Jan 14 2013 umeabot <umeabot> v1.0a_116-4.mga3
+ Revision: 384032
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Fri Sep 28 2012 blue_prawn <blue_prawn> v1.0a_116-3.mga3
+ Revision: 299155
- moved to new rpm group Games/Shooter
* Fri Sep 07 2012 blue_prawn <blue_prawn> v1.0a_116-2.mga3
+ Revision: 289081
- libpng dependency
- libfreealut dependency
- openal dependency
- removed optipng, some images don't support the conversion
- build requires cmake
- imported package taisei
