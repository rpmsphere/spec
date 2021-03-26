Name:		xletters
Version:	2.0.4
Release:	1
Summary:	A multi-lingual xletters version
Group:		X11/Games
License:	GPL
URL:		http://www.pmmh.espci.fr/~daerr/progs/%{name}
Source0:	http://www.msc.univ-paris7.fr/~daerr/progs/xletters/%{name}-%{version}.tgz
Source1:	%{name}.png
BuildRequires:	libXaw-devel

%description
Typing toy, help kids learn typing and spelling, they must type the words
that fall on the screen before they reach the ground.

Catch falling words by typing them before they reach the bottom of the screen.
This cousin of Space Invaders helps you practice your typing skill.

%prep
%setup -q
sed -i 's|define FONTNAME .*|define FONTNAME "-arphic technology co.-ar pl new sung-medium-r-normal--0-0-0-0-c-0-iso10646-1"|' xletters.h
sed -i 's|usr/local|usr|' *

%build
./configure --prefix=/usr --mandir=/usr/share/man
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mv $RPM_BUILD_ROOT%{_bindir}/xletters2 $RPM_BUILD_ROOT%{_bindir}/xletters

install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/xletters.png
%__mkdir_p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Xletters
Name[zh_TW]=極限字母
Comment=A multi-lingual xletters version 
Comment[zh_TW]=Xletters 的多國語言版本
Exec=xletters
Terminal=false
Type=Application
Categories=Application;Education;
Icon=xletters.png
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
/var/local/games/lib/xletters/scores_jp-en
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/man/man6/%{name}*
%{_bindir}/%{name}*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.4
- Rebuild for Fedora
* Thu Jun 25 2009 Kami <kami@ossii.com.tw> 2.0.4-1.ossii
- Build for OSSII
* Tue Jan 6 2004 Adrian Daerr <adrian.daerr@gmx.de>
- copied and modified Felipe's spec file
* Mon Jan 13 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1.0-2mdk
- from Maxim Heijndijk <cchq@wanadoo.nl> :
	- Added Requires: words.
* Mon Nov 18 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1.0-1mdk
- from Maxim Heijndijk <cchq@wanadoo.nl> :
	- Fixed menu-item section.
	- Fixed License, Group.
* Tue Oct 23 2001 Maxim Heijndijk <cchq@wanadoo.nl> 1.1.0-1
- Initial Wrap.
* Thu May 10 2001 Felipe Bergo <bergo@seul.org>
- created spec file based on gPS spec file.
