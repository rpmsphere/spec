Name:          xemeraldia
Version:       0.4.3
Release:       1
Summary:       Another tetris-like simple game
Group:         Amusements/Games
URL:           http://www.reloco.com.ar/xemeraldia/
Source:        http://www.reloco.com.ar/xemeraldia/xemeraldia-%{version}.tar.gz
Source1:       xemeraldia-0.4.3.zh_TW.po
License:       BSD
BuildRequires: glibc-devel
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: glib-devel
BuildRequires: gtk+-devel
BuildRequires: pango-devel

%description
Falling blocks game. Yes, another tetris-like simple game.
Although it looks like Tetris, it's not---and figuring out how to make
blocks go away is half the fun.

%prep
%setup -q
sed -i '7a#include <gtk/gtk.h>\n' graphics.c
echo zh_TW >> po/LINGUAS
msgfmt %{SOURCE1} -o po/zh_TW.gmo
sed -i "s|/var/games/xemeraldia.scores|%{_datadir}/games/%{name}/xemeraldia.scores|g" Makefile.in Makefile.am
sed -i "s|Exec=@prefix@/games/xemeraldia|Exec=xemeraldia|" xemeraldia.desktop.in
sed -i "s|TryExec=@prefix@/games/xemeraldia|TryExec=xemeraldia|" xemeraldia.desktop.in
sed -i "s|Categories=Application;Game;BlocksGame;|Categories=Game;ArcadeGame;BlocksGame;|" xemeraldia.desktop.in

%build
%configure
%{__make}

%install
rm -rf "%{buildroot}"
%makeinstall
mkdir -p %{buildroot}%{_datadir}/games/%{name}/bitmaps \
         %{buildroot}%{_bindir}

install -m 644 bitmaps/*.xbm %{buildroot}%{_datadir}/games/%{name}/bitmaps

install %{buildroot}/usr/games/xemeraldia %{buildroot}%{_bindir}

rm -rf %{buildroot}/usr/games/

touch %{buildroot}%{_datadir}/games/%{name}/xemeraldia.scores

%find_lang %{name}

%clean
rm -rf "%{buildroot}"

%files -f %{name}.lang
%attr(2755, root, games) %{_bindir}/xemeraldia
%{_datadir}/applications/xemeraldia.desktop
%{_datadir}/games/%{name}/bitmaps/*.xbm
%{_datadir}/pixmaps/xemeraldia.xpm
%attr(664, root, games) %{_datadir}/games/%{name}/xemeraldia.scores
%doc COPYING ChangeLog NEWS README README.jp TODO

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.3
- Rebuilt for Fedora
* Fri Nov 16 2012 Robert Wei <robert.wei@ossii.com.tw> 0.4.3-3
- L10N of Traditional Chinese (zh_TW)
* Fri May 18 2012 alantom<alan@ossii.com.tw>  0.4.3-2
- rebuild for OX
* Wed Feb 18 2009 gil <puntogil@libero.it> 0.4.3-1mamba
- package created by autospec
