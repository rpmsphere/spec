%undefine _debugsource_packages

Name: gsoko
Version: 0.4.2
Release: 1
Summary: Clone of the Sokoban game
License: GPL
Group: Amusements/Games
URL: http://people.via.ecp.fr/~jm/gsoko.html
Source: %{name}-%version-src.tar.gz
Source1: %{name}.desktop
Source2: %{name}.xpm
BuildRequires: glib2-devel, gtk2-devel

%description
gSoko is a gtk+ clone of the famous Sokoban game.  The goal of the
game is to push all the boxes on the squares with a red pattern.

%prep
%setup -q -n %{name}
sed -i -e 's/gtk-config/pkg-config gtk+-2.0/' -e 's/-Wall/-Wall -Wl,--allow-multiple-definition/' makefile
#sed -i -e 's|/_File|/檔案(_F)|' -e 's|/File|/檔案(F)|' -e 's|/_Restart|/重新開始(_R)|' -e 's|/_New Game|/新遊戲(_N)|' -e 's|/_Undo move|/回復移動(_U)|' -e 's|/Quit|/離開(_Q)|' -e 's|/_Help|/求助(_H)|' -e 's|/Help|/求助(H)|' -e 's|/_About|/關於(_A)|' -e 's|level %i - moves %i - boxes %i|關卡 %i - 移動 %i - 箱子 %i|' interface.c

%build
make DATADIR='"%{_datadir}/%{name}"'

%install
rm -rf $RPM_BUILD_ROOT

%__install -D -m755 %{name} %{buildroot}%{_bindir}/%{name}
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp -a img levels %{buildroot}%{_datadir}/%{name}
%__install -pD -m644 %SOURCE1 %{buildroot}%{_datadir}/applications/%{name}.desktop
%__install -pD -m644 %SOURCE2 %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGES README
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuilt for Fedora
* Wed Jun 4 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.4.2-alt1
- 0.4.2
* Sun May 25 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.4-alt1
- First version of RPM package.
