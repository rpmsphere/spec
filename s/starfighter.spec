%undefine _debugsource_packages

Summary: A space arcade game
Name: starfighter
Version: 2.4
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.parallelrealities.co.uk/starfighter.php
# No absolute URL since the home page tunnels it through a PHP script
Source0: starfighter-%{version}-src.tar.gz
Source1: starfighter.png
Patch0: starfighter-1.1-makefile.patch
BuildRequires: SDL2-devel SDL2_mixer-devel SDL2_image-devel SDL2_ttf-devel desktop-file-utils

%description
After decades of war one company, who had gained powerful supplying both sides
with weaponary, steps forwards and crushes both warring factions in one swift
movement. Using far superior weaponary and AI craft, the company was completely
unstoppable and now no one can stand in their way. Thousands began to perish
under the iron fist of the company. The people cried out for a saviour, for
someone to light this dark hour... and someone did.

This game features 26 missions over 4 star systems and boss battles.

%prep
%setup -q -n %{name}-%{version}-src
#patch0 -p1 -b .makefile
# No files need to be executable, yet quite a few are, so fix that
find . -type f -exec %{__chmod} -x {} \;
chmod +x configure

%build
%configure
%{__make} %{?_smp_mflags} PREFIX="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__make} install PREFIX="%{_prefix}" DESTDIR="%{buildroot}"

# Install menu icon
%{__install} -D -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/pixmaps/starfighter.png

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Starfighter
Comment=Space Arcade Game
Icon=starfighter
Exec=starfighter
Terminal=false
Type=Application
Categories=Application;Game;ArcadeGame;
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor fedora \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%doc COPYING LICENSES README.txt
%{_bindir}/starfighter
%{_datadir}/starfighter/
%{_datadir}/pixmaps/starfighter.png
%{_datadir}/applications/*%{name}.desktop
%{_mandir}/man6/starfighter.6*

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4
- Rebuilt for Fedora
* Thu Jun 14 2007 Matthias Saou <http://freshrpms.net/> 1.1-9
- Move binary and data to "proper" locations by updating patch (#229197).
* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.1-8
- FC6 rebuild.
* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.1-7
- FC5 rebuild.
* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 1.1-6
- Rebuild for new gcc/glibc.
- Clean up spec file a little (desktop file conditional).
* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.1-5
- rebuild on all arches
* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt
* Wed Jan  5 2005 Matthias Saou <http://freshrpms.net/> 1.1-3
- Fix desktop_vendor in the desktop file name (#143285).
* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 1.1-2
- Bump release to provide Extras upgrade path.
* Tue Jun  8 2004 Matthias Saou <http://freshrpms.net/> 1.1-1
- Initial RPM release.
