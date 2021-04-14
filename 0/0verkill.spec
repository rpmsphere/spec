Name:           0verkill
Version:        0.17rc
Release:        1
License:        GPLv2
BuildRequires:  libXpm-devel
Group:          Amusements/Games/Action/Shoot
URL:		http://artax.karlin.mff.cuni.cz/~brain/0verkill
Summary:        Bloody hell in ASCII art
Source:         %{name}-0.16.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         %{name}-%{version}-git.patch.bz2
Patch1:         %{name}-%{version}-install.patch  

%description
2D ASCII art deathmatch jump'n'kill'n'smile_insane.

You were born to DIE - you will enjoy your death!
Your eyes gonna BULGE with horror...
IT is the game you always wanted to die playing !!!
This game will be your worst NIGHTMARE you ever had!

%prep
%setup -q -n %{name}-0.16
%patch0 -p1
%patch1 -p2
%{__cp} %{SOURCE1} .
%{__cp} %{SOURCE2} .
autoreconf

%build
sed -i 's|-Wall|-Wall -Wno-format-security|' Makefile*
export LDFLAGS=-Wl,--allow-multiple-definition
%configure --with-x --datadir=%{_datadir} --bindir=%{_bindir}
make

%install
make DESTDIR="$RPM_BUILD_ROOT" install
%__mkdir_p %{buildroot}%{_datadir}/applications/
%__mkdir_p %{buildroot}%{_datadir}/pixmaps/
%__cp %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
%__cp %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
%__rm -rf $RPM_BUILD_ROOT

%post
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%postun
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%files
%doc doc/AUTHORS doc/CHANGELOG doc/COPYING doc/FILES doc/README.html doc/VERSION
%doc doc/3d.txt doc/adding_a_level.txt doc/avi.txt doc/bot.txt doc/doc.html doc/editor.txt doc/level-changing.txt
%{_bindir}/0verkill*
%{_datadir}/0verkill
%{_bindir}/x0verkill*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.17rc
- Rebuilt for Fedora
* Mon Oct 20 2009 Wind <yc.yan@ossii.com.tw>
- Rebuild for OSSII.
- Add desktop and icon file.
- combine -xwindow packge into original package.