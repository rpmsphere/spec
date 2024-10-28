Name: gtans
Version: 1.99.0
Release: 1
Summary: gTans - a tangram puzzle game
License: GPL
Group: Amusements/Games
URL: https://gtans.sourceforge.net/
Source: https://download.sourceforge.net/gtans/gtans-%version.tar.gz
Source1: gtans-1.99.0.zh_TW.po
Source2: gtanshelpzh.txt
BuildRequires: gtk2-devel

%description
Gtans is a tangram game that runs in X. Tangram is a kind of puzzle game
where the player has to arrange a set of pieces to match a given shape.

%prep
%setup -q
echo -e 'Name[zh_TW]=七巧板\nComment[zh_TW]=gTans 七巧板遊戲' >> %{name}.desktop
echo 'zh_TW' >> po/LINGUAS
cp %{SOURCE1} po/zh_TW.po
sed -i 's/gtanshelp.txt/gtanshelp.txt gtanshelpzh.txt/' data/Makefile.in
cp %{SOURCE2} data/gtanshelpzh.txt

%build
%configure
%__make

%install
%__make DESTDIR=%{buildroot} install
%find_lang %{name}

%post
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor

%postun
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor

%files -f gtans.lang
%doc ChangeLog INSTALL COPYING NEWS README AUTHORS
%{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/*
%{_sysconfdir}/gtansrc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.99.0
- Rebuilt for Fedora
* Tue Apr 24 2007 Victor Forsyuk <force@altlinux.org> 1.2-alt2
- Fix wrong paths in gtans configuration.
- Add URL.
- Refresh build requirements.
- Parallel build.
- Apply optflags.
- Include all localizations.
- Switch to freedesktop-style menu.
* Sun May 25 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.2-alt1
- First version of RPM package.
