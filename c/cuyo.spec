Summary:		A tetris like game
Summary(zh_TW):	類似俄羅斯方塊的遊戲
Name:			cuyo
URL:			https://www.karimmi.de/cuyo/
Version:		1.8.5
Release:		1
Source0:		%{name}-%{version}.tar.bz2
Source1:		%{name}-16x16.png
Source2:		%{name}-32x32.png
Source3:		%{name}-48x48.png
License:		GPL
Group:			Amusements/Games
BuildRequires:	qt3-devel bison flex

%description
Cuyo is a Tetris like game, There is many different level,
with different rules. We can play it with two players.


%description -l zh_TW
Cuyo 是一款類似俄羅斯方塊的遊戲。
具有許多不同關卡及規則。
可以兩個人同時玩。

%prep
%setup -q

%build
export MOC=%{_libdir}/qt-3.3/bin/moc
export UIC=%{_libdir}/qt-3.3/bin/uic
./configure	--prefix=%{_prefix} \
		--bindir=%{_bindir} \
		--datadir=%{_datadir} \
		--with-qt-dir=%{_libdir}/qt-3.3
# Fix the error of installation path
sed -i 's/$(prefix)\/games/$(prefix)\/bin/g' src/Makefile
sed -i 's/$(prefix)\/games/$(prefix)\/bin/g' src/Makefile.in
sed -i 's/$(prefix)\/games/$(prefix)\/bin/g' src/Makefile.am
%__make %{?_smp_mflags}

%install
%__rm -rf $RPM_BUILD_ROOT
%makeinstall	bindir=$RPM_BUILD_ROOT%{_bindir} \
		datadir=$RPM_BUILD_ROOT%{_datadir}

# .desktop
%__install -d $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Cuyo
Name[zh_TW]=Cuyo
Comment=%{Summary}
Comment[zh_TW]=類似俄羅斯方塊的遊戲
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

# png
%__install %{SOURCE1} -D $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
%__install %{SOURCE2} -D $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}-32x32.png
%__install %{SOURCE3} -D $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}-48x48.png

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/cu*.6*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}-32x32.png
%{_datadir}/pixmaps/%{name}-48x48.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.5
- Rebuilt for Fedora
* Thu Aug 26 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 1.8.5-3
- add %%dist
- delete Packager
- fix Exec within .desktop file
* Thu Aug 12 2010 Huan-Ting Luo <kylix.lo@ossii.com.tw> 1.8.5-2
- 1.8.5
* Fri Jan 14 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.8.5-1mdk
- 1.8.5
* Sun Jul 11 2004 Michael Scherer <misc@mandrake.org> 1.8.3-2mdk 
- rebuild for new gcc
* Tue Oct 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.8.3-1mdk
- 1.8.3
- moved stuff to %%{_gamesbindir} and %%{_gamesdatadir}
- compile with $RPM_OPT_FLAGs
- added menu item
- added icons
- cleanups
- buildrequires
* Mon Aug 18 2003 Antoine Ginies <aginies@bi.mandrakesoft.com> 1.7.0-1mdk
- new release
* Tue Feb 11 2003 Antoine Ginies <aginies@mandrakesoft.com> 1.6.1-2mdk
- add description and correct Group
* Tue Feb 11 2003 Antoine Ginies <aginies@bi.mandrakesoft.com> 1.6.1-1mdk
- first release for mandrakesoft.
