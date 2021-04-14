Name: xsoldier
Version: 1.8
Release: 14.1
Source0: %{name}-%{version}.tar.gz
Source1: %{name}.png
Source2: %{name}.desktop
Patch0:	%{name}-1.5-fix-str-fmt.patch
License: GNU General Public License
Group: Amusements/Games/Action/Arcade
URL: http://www.interq.or.jp/libra/oohara/xsoldier/
Summary: A X11 shoot-em up game for Linux
BuildRequires:  SDL_image-devel, libXpm-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
xsoldier is a X11 shoot-em up game for Linux.
It was created by Yuusuke HASHIMOTO <hachi@surfline.ne.jp>.
The webpage of the original author is [http://www.surfline.ne.jp/hachi/xsoldier.html].
Oohara Yuuma <oohara@libra.interq.or.jp> took over the development of xsoldier. 

%prep
%setup -q
%patch0 -p1 -b .strfmt

%build
%configure --with-sdl
make

%install
make DESTDIR=${RPM_BUILD_ROOT} mandir=%{_mandir} install
install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -Dm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%dir %{_datadir}/games/%{name}
%{_datadir}/games/%{name}/*
%{_datadir}/applications/xsoldier.desktop
%{_datadir}/pixmaps/xsoldier.png
%{_mandir}/man6/xsoldier.6.gz
%attr(0775,games,games) %dir %{_localstatedir}/games/%{name}
%attr(0664,games,games) %{_localstatedir}/games/%{name}/xsoldier.scores

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8
- Rebuilt for Fedora
* Wed May 18 2011 kobayashi
- rebuild for openSUSE, update 1.5
* Sat Sep 06 2008 Shu KONNO <owa@bg.wakwak.com> 1.4-1vl5
- applied new versioning policy, spec in utf-8
- updated man-path to %%{_mandir}
* Sun Jun 3 2007 Munehiro Yamamoto <myamamoto@g.math.s.chiba-u.ac.jp> 1.4-0vl2
- rebuild for VineSeed
* Wed Mar 21 2007 Munehiro Yamamoto <myamamoto@g.math.s.chiba-u.ac.jp> 1.4-0vl1
- initial build for Vine Linux
