Name:           squaroid
BuildRequires:  gtk2-devel
BuildRequires:  imlib-devel 
BuildRequires:  ncurses-devel 
%define         gfx_version 0.2
%define         sfx_version 0.1
License:        GPL v2 or later
Group:          Amusements/Games/Strategy/Other
Summary:        A Strategy Game
Version:        0.60.3
Release:        1
URL:            https://www.squaroid.org/
Source0:        squaroid-%{version}.tar.bz2
Source1:        squaroid-gfx-%{gfx_version}.tar.bz2
Source2:        squaroid-sfx-%{sfx_version}.tar.bz2
Source3:        squaroid.desktop
Source4:        squaroid.png
Patch0:         %{name}-%{version}-ia64.diff
Patch1:         %{name}-%{version}-config-sound.diff
Patch2:         %{name}-%{version}-strings.diff
Patch3:         %{name}-%{version}-libtool.diff
Patch4:         %{name}-%{version}-gcc4.diff
Patch5:         %{name}-%{version}-overflow.diff
Patch6:         %{name}-%{version}-aliasing.diff
Patch7:         %{name}-%{version}-userstruct.diff
Patch8:         %{name}-%{version}-undefined_operation.diff
Patch9:         %{name}-%{version}-return.diff
Patch10:        %{name}-%{version}-cflags.diff
Patch11:        %{name}-%{version}-implicit.diff

%description
A strategy game.

Authors:
--------
    Lukas Schröder <lukas@azzit.de>
    Yair Chuchem <yair@gimby.save-net.co.il>
    Danny Sung <dannys@mail.com>
    Rob Speer <rob@twcny.rr.com>

%prep
%setup -q -a1 -a2
%patch 0
%patch 1
%patch 2
%patch 3
%patch 4
%patch 5
%patch 6
%patch 7
%patch 8
%patch 9
%patch 10
%patch 11

%build
autoreconf --force --install
export CFLAGS="$RPM_OPT_FLAGS -Wall -Wno-format-security -Wl,--allow-multiple-definition"
./configure --enable-force_sound --prefix=%{_prefix} --datadir=%{_datadir}
make
#build squaroid-sfx
cd squaroid-sfx-%{sfx_version}
autoreconf --force --install
./configure --prefix=%{_prefix} --datadir=%{_datadir}
make
#build squaroid-gfx
cd ../squaroid-gfx-%{gfx_version}
autoreconf --force --install
./configure --prefix=%{_prefix} --datadir=%{_datadir}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
install -d -m 755 $RPM_BUILD_ROOT/usr/share/squaroid/
#install squaroid-sfx
cd squaroid-sfx-%{sfx_version}
make DESTDIR=$RPM_BUILD_ROOT install
mkdir ../sfx
install -m 644 AUTHORS COPYING ChangeLog README NEWS ../sfx
#install squaroid-gfx
cd ../squaroid-gfx-%{gfx_version}
make DESTDIR=$RPM_BUILD_ROOT install
mkdir ../gfx
install -m 644 AUTHORS COPYING ChangeLog README NEWS ../gfx
cd ..
#%suse_update_desktop_file -i %name Game StrategyGame
# Desktop
mkdir $RPM_BUILD_ROOT%{_datadir}/applications
install -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Icon
mkdir $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%doc AUTHORS COPYING ChangeLog README NEWS TODO HACKING* sfx gfx
%{_bindir}/*
%{_datadir}/squaroid/
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.60.3
- Rebuilt for Fedora
* Tue Oct 21 2008 Feather Mountain <john@ossii.com.tw> - 0.60.3.ossii
- Rebuild for M6(OSSII)
* Thu Jun 07 2007 - pgajdos@suse.cz
- add --datadir option to configure
* Thu Mar 29 2007 - rguenther@suse.de
- add ncurses-devel BuildRequires
* Tue Jan 30 2007 - anicka@suse.cz
- build all files with RPM_OPT_FLAGS
- fix implicit definitions
- fix overflow in sqirc.c
* Fri Jul 07 2006 - anicka@suse.cz
- fix missing return statement in libqdwav [#187246]
* Fri Mar 24 2006 - anicka@suse.cz
- fix undefined operation [#160440]
* Fri Mar 24 2006 - ro@suse.de
- rename struct user to sq_user
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Oct 12 2005 - anicka@suse.cz
- fix aliasing
* Fri May 13 2005 - mcihar@suse.cz
- fix buffer overflows
* Wed Apr 13 2005 - mcihar@suse.cz
- fix for gcc 4
* Sat Jan 10 2004 - adrian@suse.de
- build as user
* Fri Aug 15 2003 - adrian@suse.de
- add desktop file
* Wed May 14 2003 - ro@suse.de
- run autoreconf
* Wed Nov 13 2002 - mcihar@suse.cz
- fixed multiline string literals
* Mon Aug 05 2002 - mcihar@suse.de
- removed dependencies on squaroid-sfx and squaroid-gfx packages
* Thu Jul 18 2002 - mcihar@suse.cz
- fix building on machines without /dev/dsp
* Tue Jun 11 2002 - prehak@suse.cz
- merged with squaroid-sfx and squaroid-gfx packages  [#16416]
* Mon Aug 13 2001 - cihlar@suse.cz
- disable sound on s390
* Tue Jun 12 2001 - cihlar@suse.cz
- added libtoolize --force and aclocal to fix
  to compile
* Tue May 22 2001 - cihlar@suse.cz
- fixed cast warnings on ia64
* Fri Dec 01 2000 - cihlar@suse.cz
- package created
