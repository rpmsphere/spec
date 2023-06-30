Summary:	GNOME 3D Tetris game
Name:		gno3dtet
Version:	1.96.1
Release:	1
License:	GPL
Vendor:		Sebastien Nicoud <snicoud@home.com>
Group:		X11/Applications/Games
Group(de):	X11/Aplikacje/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	ftp://webdat.com/pub/seb/gno3dtet/%{name}-%{version}.tgz
#Patch0:		%{name}-DESTDIR.patch
#Patch1:		%{name}-desktop.patch
URL:		https://gno3dtet.eseb.net/3dtetris.php
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgnome-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool

%description
gno3dtet is a 3D Tetris-like game for GNOME.

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1
sed -i 's/gnome-games/gno3dtet/' configure*
sed -i '800s/index/transfo/' src/cgame.cc

%build
%__rm -rf $RPM_BUILD_ROOT
#libtoolize --copy --force
#aclocal -I %{_aclocaldir}/gnome
#autoconf
#%__rm -f missing
#automake -a -c
#./runme
./autogen.sh --prefix=/usr --localstatedir=%{_localstatedir}

#configure
%__make

%install
%__rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT
#	Gamesdir=%{_bindir}

%clean
%__rm -rf $RPM_BUILD_ROOT

%post
touch %{_localstatedir}/games/gno3dtet.hof
chmod 664 %{_localstatedir}/games/gno3dtet.hof
chown games.root %{_localstatedir}/games/gno3dtet.hof

%files
%attr(755,root,root) %{_bindir}/gno3dtet
%{_datadir}/sounds/gno3dtet
%{_datadir}/pixmaps/gno3dtet.png
%{_datadir}/applications/gno3dtet.desktop
%{_datadir}/gnome/help/gno3dtet/C/gno3dtet.xml
%{_datadir}/gnome/help/gno3dtet/C/legal.xml
%{_datadir}/locale/fr/LC_MESSAGES/gno3dtet.mo
%{_datadir}/omf/gno3dtet/gno3dtet-C.omf
%attr(664,root,games) %{_localstatedir}/games/gno3dtet.hof

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.96.1
- Rebuilt for Fedora
* Wed Jun  8 2011 Chris Lin <chris.lin@ossii.com.tw>
- Fix cgame.cc
* Tue Nov 25 2008 Wind <yc.yan@ossii.com.tw>
- Initial for OSSII.
