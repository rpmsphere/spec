Summary:        X11 browser interface to Archie
Name:           xarchie
Version:        2.0.10
Release:        7
Source:         ftp://ftp.x.org/contrib/applications/xarchie-2.0.10.tar.gz
Source1:        %{name}.png
Patch0:         Xarchie2.0.10.patch
License:        Free
Group:          Networking/Other
BuildRequires:  imake
BuildRequires:  libXaw-devel
BuildRequires:  Xaw3d-devel
BuildRequires:  xorg-x11-xbitmaps

%description
This is release 2.0 of xarchie, an X browser interface to the Archie
Internet information system.

%prep
%setup -q -n xarchie-2.0.10
%patch 0
sed -i 's|char \*pmatch|static char *pmatch|' regex.c
sed -i 's|struct restrict|struct restriction|' pfs.h
sed -i -e 's|regexp\.h|regex.h|' -e '48i #define NO_REGEXP' FWF/Dir/RegExp.c
sed -i 's|clq|cq|' */*/Makefile*

%build
xmkmf
make "CDEBUGFLAGS=%optflags" "XAWLIB=-lXaw3d"

%install
make install DESTDIR=%buildroot
make install.man DESTDIR=%buildroot MANPATH=%_mandir

install -d %buildroot%_datadir/applications
cat << EOF > %buildroot%_datadir/applications/%name.desktop
[Desktop Entry]
Name=Xarchie
Comment=X11 browser interface to Archie
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Network;
EOF

install -Dm644 %{SOURCE1} %buildroot%_datadir/pixmaps/%{name}.png

%files
%doc README PROBLEMS
%{_mandir}/man1/*
%{_bindir}/%{name}
%_prefix/lib/X11/app-defaults
%_datadir/applications/%{name}.desktop
%_datadir/pixmaps/%{name}.png
%_datadir/X11/app-defaults/Xarchie

%changelog
* Sun Jan 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.10
- Rebuilt for Fedora
* Sat Jan 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 2.0.10-7mdk
- Fix menu entry
- Add missing file
* Tue Aug 21 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.10-6mdk
- Fix menu entry
* Thu Jun 21 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.0.10-5mdk
- rebuild
* Fri Jan 05 2001 David BAUDENS <baudens@mandrakesoft.com> 2.0.10-4mdk
- BuildRequires: Xaw3d-devel
- Add missing man pages
- Spec clean up
* Tue Aug 01 2000  Lenny Cartier <lenny@mandrakesoft.com> 2.0.10-3mdk
- macros
- bm
- menu
* Wed Apr 19 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.0.10-2mdk
- fix group
- bz2 patch
- fix file list
* Tue Jan 25 2000 Lenny Cartier <lenny@mandrakesoft.com>
- build for mandrake
