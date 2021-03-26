%global debug_package %{nil}

Name:			5ball
Version:		0.43
Release:		19.1
Summary:		A simple logic game
Group:			Amusements/Games/Board/Other
License:		GPL
URL:			http://www.pcbypaul.com/software/5ball.html
Source0:		http://www.pcbypaul.com/software/dl/%{name}-%{version}.tar.gz
Source1: %{name}.desktop
Source2: %{name}.png
BuildRequires:	atk-devel
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk2-devel
BuildRequires:	pango-devel
BuildRequires:	cairo-devel
BuildRequires:	pkgconfig
BuildRequires:	desktop-file-utils

%description
5ball is a simple logic game. The goal of the game is to make the
maximum number of lines with balls of the same color. A line is
made of five balls. Each time you don't do a line, extra balls
appear on the grid. You loose when the grid is full.

This is a logic game, lining up 5 balls of like color to get them
off a grid, to keep the grid from filling up. Requires 1024x768
or better screen resolution.

It looks a lot like klines, but with bigger balls. 5ball is
actually a modification of gtkBalls (a game similar to klines but
with several features giving it loads of potential -- but somewhat
lacking in the UI department.) All the other 'Lines' games I have
tried were too small on a decent screen. This one is big and the
chicks think it's sexy. Yeah.

%prep
%setup -q
%__sed -i -e 's|/var/lib/games/5ball-scores|/var/games/5ball-scores|g' \
	src/child.c
%__sed -i -e 's|/var/lib/games/5ball-scores|/var/games/5ball-scores|g' \
	src/scoreboard.c

%build
export CFLAGS="-Wno-error -fPIC"
autoreconf -ivf
%configure \
	--localstatedir=/var/games
%__make %{?jobs:-j%{jobs}}

%install
%__rm -rf %{buildroot}
%__sed -i -e 's|/var/lib|%{buildroot}/var/games|g' Makefile
%makeinstall
%__install -D -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
%__install -D -m 644 %{SOURCE2} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png
%__rm %{buildroot}/var/games/games/5ball-scores

%post
if [ ! -f /var/games/5ball-scores ]; then
	touch /var/games/5ball-scores
fi
%__chgrp games /var/games/5ball-scores
%__chmod 0664  /var/games/5ball-scores

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog NEWS README TODO
%doc %{_mandir}/man6/*
%{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Jul 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.43
- Rebuild for Fedora
- modify the spec file in 0.43-0.pm.1.src.rpm
* Wed May 06 2009 Toni Graffy <toni@links2linux.de> - 0.43-0.pm.1
- update to 0.43
* Thu Sep 27 2007 oc2pus <oc2pus@arcor.de> 0.41-0.pm.2
- openSUSE-10.3 build
* Fri Feb 23 2007 oc2pus <oc2pus@arcor.de> 0.41-0.pm.1
- build for packman
* Tue Mar 22 2005 oc2pus <oc2pus@arcor.de> 0.41-0.oc2pus.1
- update to 0.41
* Tue Nov 16 2004 oc2pus <oc2pus@arcor.de> 0.3-0.oc2pus.1
- Initial rpm build
