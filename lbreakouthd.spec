Summary: A ball-and-paddle game with nice graphics
Name: lbreakouthd
Version: 1.0.5
Release: 1
License: GPL
Group: Amusements/Games
URL: http://lgames.sourceforge.net/
Source: http://dl.sf.net/lgames/%{name}-%{version}.tar.gz
BuildRequires: SDL2-devel, SDL2_image-devel, SDL2_mixer-devel, SDL2_ttf-devel

%description
First and foremost to make things clear: LBreakoutHD is an HD remake 
of LBreakout2 (all levelsets and themes will work). The game itself is
completely unchanged. A new SDL2/C++11 view has been added to support 
16:9 wide screens of any resolution. Why not adding this to the existing
LBreakout2 package if the game basically remains the same? Because 
second: I wanted to clean up the code (the not really well working 
network stuff bothered me) and not mix SDL2 with SDL for dependencies.

So LBreakoutHD is a clean cut with the old core engine (still in C) and
a brand new fully scalable 16:9 view.

%prep
%setup -q

%build
%configure
sed -i 's|-Werror=format-security||' Makefile */Makefile
%{make_build}

%install
%{make_install}
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%doc COPYING README TODO Changelog
%{_bindir}/lbreakouthd
%{_datadir}/lbreakouthd
%config(noreplace) /var/lbreakouthd.hscr
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/lbreakouthd256.gif

%changelog
* Wed Nov 27 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.5
- Rebuild for Fedora
