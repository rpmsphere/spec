Name:           qgo
Version:        2.0.0
#Version:        2.1.0
Release:        1
Summary:        A Go Board and SGF Editor
License:        GPL-2.0+
Group:          Amusements/Games/Board/Other
URL:            https://github.com/pzorin/qgo
Source:         https://github.com/pzorin/qgo/archive/qt4-final.tar.gz
#PATCH-FIX-UPSTREAM fix gcc6 narrowing conversion from int to char inside {}
Patch:          qgo-2.0.0-gcc6.patch
BuildRequires:  qt4-devel
BuildRequires:  alsa-lib-devel

%description
A Go board, sgf editor and client for IGS/NNGS/WINGS based on the Qt
library. Go is an ancient boardgame, very common in Japan, China and
Korea.

%prep
%setup -q -n %{name}-qt4-final
%patch -p1
sed -i 's|$(QTDIR)|%{_libdir}/qt4|' src/src.pro
sed -i 's|msg.contains("\([^0]*\)") > 0|msg.contains("\1") != NULL|g' src/network/igsconnection.cpp

%build
qmake-qt4 -makefile %{name}.pro QMAKE_CFLAGS="%{optflags} -Wno-format-security" QMAKE_CXXFLAGS="%{optflags} -Wno-format-security"
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}
cp src/translations/*.qm %{buildroot}%{_datadir}/qgo/languages/

%files
%doc AUTHORS COPYING README.md
%{_bindir}/qgo
%{_datadir}/pixmaps/qgo*
%{_datadir}/applications/qgo.desktop
%{_datadir}/mime/text/x-sgf.xml
%{_datadir}/mimelnk/text/sgf.desktop
%{_datadir}/qgo

%changelog
* Wed Jul 18 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.0
- Rebuilt for Fedora
* Tue Jun 21 2016 i@marguerite.su
- add patch: qgo-2.0.0-gcc6.patch
  * fix boo#985098
  * fix gcc6 narrowing conversion from int to char inside {}
  * fix gcc6 cannot convert bool to GameData in return
* Sat Mar 14 2015 p.drouand@gmail.com
- Update to version 2.0.0
  * No changelog available
- Remove obsolete patchs
  * qgo-1.5.4-gcc4.3.diff
  * qgo-1.5.4-desktop.diff
- Move to qt4; follow upstream changes
  * Replace qt3-devel require with pkgconfig(QtCore)
  * Remove qt3 require
- Update project Url
- Use download Url as source
- TODO and COPYING don't exit anymore; do not perform %%doc on them
- README has been renamed to README.md
- Copy AUTHORS and COPYING into package doc directory
* Tue Mar 27 2012 jengelh@medozas.de
- Build in parallel with %%_smp_mflags
- Strip redundant sections/tags from specfile
* Fri Mar  5 2010 coolo@novell.com
- fix build with gcc 4.5
* Tue Mar 10 2009 anicka@suse.cz
- install correct desktop file (bnc#483231)
* Fri Nov 16 2007 anicka@suse.cz
- fix deprecated headers
* Mon Jun 18 2007 ltinkl@suse.cz
- update to 1.5.4:
  * fixed : mark issue with teaching games
  * added : blind go
  * added : 2 new translations (latin and simplified chinese)
  * changed : added 'SGF' (uppercase) as file suffix
* Tue Jan 16 2007 meissner@suse.de
- use RPM_OPT_FLAGS
* Thu Jan 11 2007 ltinkl@suse.cz
- update to 1.5.3
  * fixed : 9x9 grid display
  * changed : 'remember last dir' set by default
  * changed : made ugly 2D stones available
  * added : IGS 'nmatch' range now in the preferences
* Mon Oct  9 2006 ltinkl@suse.cz
- update to 1.5.2
* Sat Sep  9 2006 anicka@suse.de
- use proper lib (/usr/lib/qt3/lib64 on biarch)
* Wed Aug 30 2006 ltinkl@suse.cz
- initial release (1.5.1)
