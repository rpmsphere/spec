%undefine _debugsource_packages
%bcond_without ncurses
# build with support for allegro - disabled by default
%bcond_with allegro

Name:           vitetris
Version:        0.58.0
Release:        lp150.6.5
Summary:        Terminal-based Tetris clone
License:        BSD-2-Clause
Group:          Amusements/Games/Action/Arcade
URL:            http://victornils.net/tetris/
#Git-Clone:     https://github.com/vicgeralds/vitetris.git
Source:         https://github.com/vicgeralds/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vitetris.6
Patch5:         vitetris-no-need-for-root-to-install.patch
Patch6:         vitetris-fix-font-path.patch
%if 0%{with allegro}
BuildRequires:  liballeg-devel
%endif
%if 0%{with ncurses}
BuildRequires:  ncurses-devel
%endif

%description
Vitetris is a terminal-based Tetris game. It can be played by one or
two players, over the network or on the same keyboard.

Vitetris comes with customizable appearance and netplay where both
players can choose difficulty (level and height). (No sound, though.)

Rotation, scoring, levels and speed resembles the early Tetris
games by Nintendo, with the addition of a short lock delay which
makes it possible to play at higher levels. (It does not make it
possible to prevent the piece from ever locking by abusing lock delay
resets.)


%prep
%setup -q
%patch5 -p1
%patch6 -p1
sed -i 's|Exec=tetris|Exec=vitetris|' vitetris.desktop

%build
./configure \
    --prefix=%{_prefix} \
    --datarootdir=%{_datadir} \
%if 0%{with allegro}
    --with-allegro \
%else
    --without-allegro \
%endif
%if 0%{with ncurses}
    --with-ncurses \
%else
    --without-ncurses \
%endif
    --with-2player \
    --with-network \
    --with-term_resizing \
    --with-menu \
    --with-blockstyles \
    --with-pctimer

make CFLAGS='%{optflags} -Wno-return-type' %{?_smp_mflags}

%install
%make_install
install -Dm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man6/vitetris.6
mv %{buildroot}%{_bindir}/tetris %{buildroot}%{_bindir}/vitetris
rm -fR %{buildroot}%{_datadir}/doc/vitetris/

%files
%doc README changes.txt
%license licence.txt
%{_bindir}/vitetris
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%if 0%{with allegro}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/pc8x16.fnt
%endif

%changelog
* Tue Jun 18 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.58.0
- Rebuilt for Fedora
* Sun Mar 10 2019 Martin Hauke <mardnh@gmx.de>
- Update to version 0.58
  * bugfix release - no functional changes
- Remove patches (included upstream):
  * 0001-fix-extraneous-licence.patch
  * 0002-fix-insecure-printf.patch
  * 0003-rename-program-to-vitetris.patch
  * 0004-add-comment-desktop.patch
  * 0005-fix-implicit-declaration.patch
* Thu Jan 17 2019 Jan Engelhardt <jengelh@inai.de>
- Trim filler wording from description.
* Sun Jan 13 2019 mardnh@gmx.de
- Initial package, version 0.57.2
