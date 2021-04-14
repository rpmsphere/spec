Name:           lierolibre
Version:        0.5
Release:        16
Summary:        Old-school duel shooter in wormholes based on the classic Liero game
Group:          Games/Shooter
License:        BSD and WTFPL
URL:            https://launchpad.net/lierolibre
Source0:        https://launchpad.net/lierolibre/trunk/%{version}/+download/%{name}-%{version}.tar.xz
Patch0:         lierolibre-0.5-mga-cfg-utf8.patch
Patch1:         adapt-to-new-libconfig.patch
### for arm build (patch2,3,4)
Patch2:         0001-Use-unaligned-access-define-over-checking-arch.patch
Patch3:         0002-At-least-try-building-for-other-archs-than-x86.patch
Patch4:         0003-Remove-unknown-arch-warning.patch
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(libconfig++)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  ImageMagick
BuildRequires:  sox

%description
Liero is a simple game. Pick your five weapons, and unleash your inner fury.
The game is always played one versus one on a map of your choice, and yes,
you have to play with someone who is right next to you.

To shoot is of course easy enough to figure out, but if you want to step up
your game, you need to figure out things like how to swing yourself to safety
with the ninja rope, to use timed weapons for area denial, to hunt without
being hunted, to ambush, hit and run, and control that darn guided missile.

Lierolibre is a 100% free fork of Liero, and stays true to the original
gameplay.

%prep
%setup -q
%autopatch -p1
sed -i -e 's/Name=lierolibre/Name=Lierolibre/g' data/lierolibre.desktop

%build
%configure \
        --bindir=%{_bindir} \
        --datadir=%{_datadir}
%make_build

%install
%make_install

%files
%doc ChangeLog README NEWS AUTHORS
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_libexecdir}/%{name}
%{_mandir}/man6/*

%changelog
* Tue Mar 19 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
* Tue Oct 16 2018 wally <wally> 0.5-16.mga7
+ Revision: 1321061
- rebuild for new boost 1.68.0
* Sun Sep 23 2018 umeabot <umeabot> 0.5-15.mga7
+ Revision: 1299297
- Mageia 7 Mass Rebuild
* Fri Apr 06 2018 kekepower <kekepower> 0.5-14.mga7
+ Revision: 1215612
- Rebuild for new libconfig
* Mon Dec 25 2017 wally <wally> 0.5-13.mga7
+ Revision: 1184758
- rebuild for new boost
* Tue Nov 21 2017 tv <tv> 0.5-12.mga7
+ Revision: 1178333
- rebuild for boost 1.65
* Sun Sep 17 2017 tv <tv> 0.5-11.mga7
+ Revision: 1154975
- rebuild with latest boost
* Tue Jan 19 2016 daviddavid <daviddavid> 0.5-10.mga6
+ Revision: 925850
- add 3 patches from debian to try building for other archs than x86 and x86_64
* Tue Jan 19 2016 daviddavid <daviddavid> 0.5-9.mga6
+ Revision: 925846
- add patch1 from debian to adapt to new libconfig++9
* Sat Dec 26 2015 daviddavid <daviddavid> 0.5-8.mga6
+ Revision: 915371
- rebuild for new boost 1.60.0
* Sun Sep 27 2015 daviddavid <daviddavid> 0.5-7.mga6
+ Revision: 884293
- rebuild for new boost 1.59.0
* Sat Aug 29 2015 cjw <cjw> 0.5-6.mga6
+ Revision: 871005
- rebuild with gcc 5
* Sun Aug 02 2015 daviddavid <daviddavid> 0.5-5.mga6
+ Revision: 860572
- rebuild for new boost-1.58.0
* Wed Oct 15 2014 umeabot <umeabot> 0.5-4.mga5
+ Revision: 746405
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.5-3.mga5
+ Revision: 681923
- Mageia 5 Mass Rebuild
* Thu May 22 2014 akien <akien> 0.5-2.mga5
+ Revision: 625059
- Fix capitalization in desktop file
* Tue Feb 25 2014 akien <akien> 0.5-1.mga5
+ Revision: 597218
- imported package lierolibre
