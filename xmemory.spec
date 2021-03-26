%global debug_package %{nil}
Name:           xmemory
URL:            ftp://ftp.x.org/contrib/games/multiplayer/
BuildRequires:  gcc-c++ 
BuildRequires:	imake
License:        Any permissive
Group:          Amusements/Games/Board/Other
AutoReqProv:    on
Version:        3.7
Release:        1
Summary:        Memory Game
Source:         xmemory-%{version}.tar.bz2
Patch:          xmemory-%{version}.dif
Patch1:         %{name}-%{version}_default-font.patch
%define _xorg7libs %_lib
%define _xorg7libs32 lib
%define _xorg7bin bin
%define _xorg7_mandir %_mandir
%define _xorg7pixmaps include
%define _xorg7libshare share
%define _xorg7_xkb /usr/share/X11/xkb
%define _xorg7_termcap /usr/lib/X11/etc
%define _xorg7_serverincl /usr/include/xorg
%define _xorg7_fonts /usr/share/fonts
#%define _xorg7_config /usr/share/X11/config #use libshare macro
%define _xorg7_prefix /usr

%description
This memory game is playable by many users on different X11 displays
simultaneously.

Authors:
--------
    Helmut Hoenig <Helmut.Hoenig@hub.de>

%prep
%setup -q
%patch
%patch1
sed -i 's|const char|char|g' gif_image.C gif_image.H mem_image.C mem_image.H

%build
xmkmf -a
make %{?jobs:-j%jobs} CXXOPTIONS=-Wno-narrowing xmemory

%install
make DESTDIR="$RPM_BUILD_ROOT" install
make DESTDIR="$RPM_BUILD_ROOT" MANDIR=%{_xorg7_mandir}/man6/ MANSUFFIX=6 install.man 
install -m 755 -d $RPM_BUILD_ROOT/usr/share/games/xmemory
cp -a *.mem $RPM_BUILD_ROOT/usr/share/games/xmemory
install -D -m 0644 %{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{name}
Name[zh_TW]=翻牌記憶遊戲
Comment=
Comment=[zh_TW]=記憶的休閒遊戲
Exec=xmemory
Terminal=false
StartupNotify=true
Type=Application
Categories=Application;Game
Icon=%{name}.png

EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYRIGHT
%{_bindir}/%{name}
#/usr/%{_xorg7bin}/*
/usr/share/games/xmemory/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%doc %{_xorg7_mandir}/man6/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.7
- Rebuild for Fedora
* Wed Jun  5 2011 - chris.lin@ossii.com.tw
- Fix types
* Wed Oct 22 2008 - john@ossii.com.tw
- Rebuild for M6(OSSII)
* Mon Jun 11 2007 - pgajdos@suse.cz
- changed default font to working one
  * default-font.patch
* Fri Jul 28 2006 - lmichnovic@suse.cz
- builds also with new X.org 7.x, detecting prefix in X.org
- building with icecream
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Oct 13 2004 - ro@suse.de
- updated requires
* Sun Jan 11 2004 - adrian@suse.de
- add %%defattr
* Tue Sep 17 2002 - ro@suse.de
- removed bogus self-provides
* Tue Oct 30 2001 - ro@suse.de
- use g++ to compile
- bzip source
* Wed Feb 07 2001 - uli@suse.de
- fixed for glibc 2.2.1
* Thu May 25 2000 - vinil@suse.cz
- sorted in group
- shareable files relocated to /usr/share/games/xmemory
* Fri Mar 24 2000 - vinil@suse.cz
- BuildRoot added
* Fri Jan 28 2000 - fehr@suse.de
- fix for new gcc 2.95
* Wed Jan 12 2000 - fehr@suse.de
- changed to new version 3.7
* Mon Sep 13 1999 - bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
