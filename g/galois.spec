Name:           galois
Version:        0.6
Release:        4.1
Summary:        Extended falling blocks game with many different geometries
Group:          Games/Arcade
License:        GPLv3+
URL:            http://www.nongnu.org/galois/
Source0:        http://download.savannah.gnu.org/releases/galois/source/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libxml++-2.6)

%description
Galois is a computer game of the "falling blocks" type, but with unique
features. Unlike most other games of that type, it is not limited to blocks
made of four two-dimensional, square bricks: you can choose among several
different brick shapes, blocks composed of more or less bricks, and even
between two- and three-dimensional games.

%prep
%setup -q
sed -i 's|/games|/bin|' src/makefile.in

%build
autoreconf -vfi
CXXFLAGS="%{optflags} -std=gnu++11" \
%configure
%make_build

%install
%make_install

%find_lang %{name} --with-gnome --with-man

%files -f %{name}.lang
%doc NEWS
%{_datadir}/applications/%{name}.desktop
%lang(C) %{_datadir}/omf/%{name}/%{name}-C.omf
%lang(it) %{_datadir}/omf/%{name}/%{name}-it.omf
%{_datadir}/pixmaps/%{name}.png
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6.*

%changelog
* Mon Jul 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuild for Fedora
* Thu Feb 08 2018 akien <akien> 0.5-1.mga7
+ Revision: 1199724
- Version 0.5
* Thu Oct 20 2016 akien <akien> 0.4-1.mga6
+ Revision: 1062585
- Version 0.4
* Thu Feb 11 2016 umeabot <umeabot> 0.3-5.mga6
+ Revision: 953971
- Mageia 6 Mass Rebuild
* Mon Aug 31 2015 cjw <cjw> 0.3-4.mga6
+ Revision: 871461
- add -std=gnu++11 to CXXFLAGS to fix build with latest libsigc++/gtkmm
* Wed Oct 15 2014 umeabot <umeabot> 0.3-3.mga5
+ Revision: 749389
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 0.3-2.mga5
+ Revision: 679401
- Mageia 5 Mass Rebuild
* Fri Mar 28 2014 akien <akien> 0.3-1.mga5
+ Revision: 609089
- imported package galois
