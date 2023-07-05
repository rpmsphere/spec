Name:           cervi 
BuildRequires:  esound-devel gcc-c++ timidity++
BuildRequires:  gtk+-devel
Summary:        Multiplayer Game
Version:        0.4.0
Release:        1
License:        GPL
Group:          Amusements/Games/Arcade
URL:            https://www.nomi.cz
Source:         %{name}-svn-%{version}.tar.bz2
Source1:        %{name}.png
Patch1:         %{name}-svn-%{version}-makefile.patch
Patch2:         %{name}-svn-%{version}-intptr.patch
Patch3:         %{name}-svn-%{version}-declaration.patch
Requires:       esound

%description
GTK Cervi is clone of Cervi.  I'm not really sure if Cervi is original name
of it but I know this game as Cervi so it will be named GTK Cervi.  It is 
a multiplayer game (for 2-8 players) where players drive their worms.  Worms
are getting longer and players mustn't collide with any worm.  Winner is the
last surviving worm.  For more information see `Gameplay internals' section.

Authors:
--------
Tomáš Janoušek <tomi@nomi.cz>, ICQ #161807083, Brno, Czech Republic
 * author and maintainer of this project
 * programming

Vladimír Chvátil, Brno, Czech Republic
 * made original Cervi, (C) 1993 
 * Cervi music, (C) 1993

%prep
%setup -q -n cervi-svn-0.4.0
%patch1
%patch2
%patch3

%build
#no configure in package
# use of RPM_OPT_FLAGS are implemented in patch1
make 

%install
make DESTDIR=$RPM_BUILD_ROOT install
%__mkdir_p $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
install -m 644 %{S:1} $RPM_BUILD_ROOT/%{_datadir}/pixmaps/
%__mkdir_p $RPM_BUILD_ROOT/%{_datadir}/applications/
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{name}
Comment=GTK Cervi is clone of Cervi
Exec=%{name}
Terminal=false
StartupNotify=true
Categories=Applications;Game
Icon=%{name}.png
Name[zh_TW]=線蟲大作戰
Comment[zh_TW]=Cervi, GTK Cervi is clone of Cervi.
EOF

%files
%{_bindir}/%{name}
%{_datadir}/cervi
%doc changelog README COPYRIGHT COPYING AUTHORS INSTALL
%{_datadir}/pixmaps/*
%{_datadir}/applications/%name.desktop

%clean
%__rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
* Tue Oct 21 2008 Wind Win <yc.yan@ossii.com.tw>
- Rebuild for OSSII.
* Fri Jul  4 2008 lmichnovic@suse.cz
- fixed missing declaration of rand (*-declaration.patch)
