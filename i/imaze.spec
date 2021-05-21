%undefine _debugsource_packages

Name:         imaze
Release:      15.1
License:      GPL-2.0
Group:        Amusements/Games/Action/Arcade
Version:      2.0
Summary:      Multi-Player 3D Game
URL:          http://home.tu-clausthal.de/student/iMaze/
Source:       %{name}-%{version}.tar.bz2
BuildRequires: motif-devel alsa-lib-devel

%description
A 3D TCP/IP-network-game under X11/OpenMotif. There are clients (imaze, ininja)
working together with one server (imazesrv).

To start the game, you have to fire up the server first:
  imazesrv /usr/lib/imaze/labs/demolab.lab &
Then you can start the clients with:
  ininja <Server> &
  imaze &

Authors:
--------
    Hans-Ulrich Kiel <Kiel@rz.tu-clausthal.de>
    Joerg Czeranski <Czeranski@informatik.tu-clausthal.de>

%prep
%setup -q
sed -i '1i #include <sys/types.h>' src/grafik.h
sed -i -e 's/|| errno >= sys_nerr//' -e 's|sys_errlist\[errno\]|strerror(errno)|' src/system.c

%build
./configure --prefix=/usr
make %{?_smp_mflags} CPPFLAGS='-DDEFAULT_SERVER=\"localhost\" -DDEFAULT_SOUND_DIR=\"%{_datadir}/imaze/sounds\"' CFLAGS=-Wno-error

%install
%makeinstall
rm -f $RPM_BUILD_ROOT%{_libdir}/lib*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/packages
mv $RPM_BUILD_ROOT%{_bindir}/ninja $RPM_BUILD_ROOT%{_bindir}/ininja

%files
%doc README AUTHORS COPYING Copyright
%doc doc/imazedoc.pdf
%doc /usr/share/man/man6/*
%{_bindir}/*
%{_libdir}/libimaze.so*
%{_datadir}/imaze
%{_datadir}/applications/imaze.desktop
%{_datadir}/pixmaps/imaze.png

%changelog
* Sun Mar 24 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1
- Rebuilt for Fedora
* Thu Mar 07 2013 - rfno@fietze-home.de
- update to openSUSE 11.3
- using g++ and C++0x
* Sun Jul 13 2008 - rfno@fietze-home.de
- add desktop file for imaze and imazesrv
* Sat Jan 26 2002 - oliver.teuber@teuber.com
- update to 1.4 and OpenMotif
