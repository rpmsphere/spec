Name:           battleship
Version:        0.2
Release:        1
Summary:        Battleship game
License:        GNU General Public License
URL:            https://chefche.space4free.net/#battleship
Source0:        https://chefche.space4free.net/battleship-%{version}.tar.gz
Source1:        %{name}-0.2.zh_TW.po
BuildRequires:  libtool, intltool >= 0.35.0, perl >= 5.8.1, atk-devel, cairo-devel, freetype-devel, gtk2-devel, pango-devel

%description
Instead of firing blindly you get informations about the enemy ships' positions.

%prep
%setup -q
sed -i 's|doc/battleship|share/doc/battleship-%{version}|' Makefile*
echo Name[zh_TW]=海戰棋 >> battleship.desktop
echo Comment[zh_TW]=現在你可以獲得船艦位置的線索，不再盲目攻擊了。  >> battleship.desktop
echo zh_TW >> po/LINGUAS
cp %{SOURCE1} po/zh_TW.po

%build
%configure
make CFLAGS+=-lm %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/doc/%{name}-%{version}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Thu Nov 15 2012 Robert Wei <robert.wei@ossii.com.tw> - 0.2-3
- L10N of Traditional Chinese (zh_TW)
* Mon May 21 2012 Chih-Jen Nung <cj.nung@ossii.com.tw> - 0.2-2
- Initial package for OSSII 
