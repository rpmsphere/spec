%undefine _debugsource_packages

Name:      slimevolley
Version:   2.4.1
Release:   1
Summary:   A volley ball game
Group:     Amusements/Games
License:   GPL
URL:       http://slime.tuxfamily.org/
Source0:   slimevolley_2.4.1.tar.gz
Source1:   slimevolley.desktop
Source2:   slimevolley.png
BuildRequires: SDL-devel

%description
Slime Volley is a game inspired by the Java games of the same name
(in the style of Blobby Volley). It is a volleyball simulation :
You control a semi-circular blob on which the ball bounces.
A this time, the stable 2.4 version allows from 2 to 6 players,
with any combination of local, remote and AI players.

%prep
%setup -q
sed -i -e 's|share/games|share|' -e 's|games|bin|' -e '42i m' CMakeLists.txt

%build
export LDFLAGS=-Wl,--allow-multiple-definition
cmake . -DCMAKE_INSTALL_PREFIX=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
echo -e "Name[zh_TW]=黏土排球\nComment[zh_TW]=平面排球模擬遊戲" >> %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*
%{_datadir}/locale/*/LC_MESSAGES/slimevolley.mo
%{_mandir}/man6/slimevolley.6.gz

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.1
- Rebuilt for Fedora
* Thu Aug 27 2009 Harry Chen <harry@server1.ossii.com.tw> - 2.4.1-1.ossii
- Initial package for ossii
