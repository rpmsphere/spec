%undefine _debugsource_packages

Summary: An X Window System version of the Sokoban puzzle game
Name: xsok
Version: 1.02
Release: 16.1
License: GPL
Group: Amusements/Games
Source0: ftp://tsx-11.mit.edu/pub/linux/sources/usr.bin.X11/%{name}-%{version}-src.tar.gz
Source1: xsok.desktop
Patch0: xsok-%{version}.patch
BuildRequires: imake libX11-devel libXt-devel libXaw-devel

%description
XSokoban is an X Window System version of the Sokoban puzzle game.
The object of the game is to push all the round objects into the score
area of each level using the mouse or the arrow keys. The arrow keys
move the player in the corresponding direction, pushing an object if
it is in the way and there is a clear space on the other side.

%prep
%setup -q
%patch0 -p1 -b .mike
sed -i -e 's|/X11R6||' -e 's|man/man6|share/man/man6|' src/Imakefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
gzip -d $RPM_BUILD_ROOT/usr/lib/X11/xsok/*.gz
install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/xsok.desktop
rm -r $RPM_BUILD_ROOT/usr/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc etc/* doc/xsok.tex README doc/cyberbox.doc
%config /usr/lib/X11/app-defaults
%if %{fedora}<21
%config /etc/X11/app-defaults/XSok
%else
%config %{_datadir}/X11/app-defaults/XSok
%endif
%{_datadir}/applications/xsok.desktop
%{_bindir}/xsok
%{_datadir}/man/man6/xsok.6x*
/usr/lib/X11/xsok
%attr(777, root, root) %dir /var/lib/games/xsok
%attr(666, root, root) /var/lib/games/xsok/*.score

%changelog
* Sat Sep 29 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.02
- Rebuilt for Fedora
* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt
* Mon Jul 24 2000 Than Ngo <than@redhat.de>
- rebuilt
* Thu Jul 13 2000 Than Ngo <than@redhat.de>
- don't strip binaries in specfile
* Thu Jun 01 2000 Than Ngo <than@redhat.de>
- rebuild for 7.0
- gzip man page
* Tue Jul 27 1999 Tim Powers <timp@redhat.com>
- updated ftp location
- rebuilt for 6.1
* Mon Apr 12 1999 Michael Maher <mike@redhat.com>
- cleaned up spec file, added desktop entry. 
* Sun Jan 03 1999 Karl-Martin Skontorp <karl-ms@online.no>
- Maintainer for RHCN: Karl-Martin Skontorp
* Wed Jun 24 1998 Peter Soos <sp@osb.hu>
- Using %attr to build the package as an ordinary user.
* Sun Dec 28 1997 Peter Soos <sp@osb.hu>
- Added wmconfig support
* Tue Dec 13 1997 Peter Soos <sp@osb.hu>
- Recompiled under RedHat Linux 5.0
- Now we use BuildRoot
