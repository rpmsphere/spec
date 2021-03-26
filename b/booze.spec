Name:		booze
Version:	0.9b
Release:	1
Summary:	Chess like game
Group:		Amusements/Games
License:	GPL
URL:		http://drunksoft.com/booze/
Source:		http://booze.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	wxGTK-devel

%description
Booze is a game engine that can play a number of Chess like games.
It is totally free and works on all major operating systems.
The game features 3D graphics and a simplified interface.
Just right click on any piece if you can't remember what it is.
The built in AI has difficulty levels appropriate for a wide range of
players and is under heavy development to increase the playing strength
on the higher settings. 

%prep
%setup -q -n %{name}-%{version}
sed -i 's|usr/local|usr|' configure* Makefile*
sed -i -e 's|usr/local|usr|' -e 's|Game;|Game;BoardGame;|' build/%{name}.desktop
echo -e 'Name[zh_TW]=棋宴\nComment[zh_TW]=日本將棋遊戲' >> build/%{name}.desktop

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri Jun 26 2009 Kami <kami@ossii.com.tw> 0.9b-1.ossii
- Build for OSSII
