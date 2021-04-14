Name:           tux_aqfh
BuildRequires:  freeglut-devel gcc-c++ 
BuildRequires:	plib-devel
License:        GNU General Public License (GPL)
Group:          Amusements/Games/3D/Shoot
Version:        1.0.14
Release:        1
URL:            http://tuxaqfh.sourceforge.net/
Summary:        Tuxedo T. Penguin
Source0:        %{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch:          %{name}-%{version}.patch

%description
A Quest for Herring: OpenSource 3D game starring your Favorite Hero
-- Tux, the Linux Penguin.

Authors:
--------
    Steve Baker <sjbaker1@airmail.net>

%prep
%setup -q
%patch
sed -i 's|/games/|/|g' configure* */Makefile*
sed -i 's|local/share/games|share|g' src/tux.cxx
sed -i 's|/games|/bin|' src/Makefile.am

%build
autoreconf -f -i
%configure
make
make check

%install
make DESTDIR=$RPM_BUILD_ROOT install

# Desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS CHANGES LICENSE README doc/*.html doc/*.png
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.14
- Rebuilt for Fedora
* Tue Oct 21 2008 Feather Mountain <john@ossii.com.tw>
- Rebuild for M6(OSSII)
* Mon May 28 2007 pgajdos@suse.cz
- fixed BuildRequires; plib-devel is needed for all distros in
  the BS project games:arcade, removed unneeded libdrm-devel
* Thu May 24 2007 ro@suse.de
- added plib-devel to buildreq
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Aug 16 2004 ro@suse.de
- added libplibjs to link sequence
* Tue Feb 24 2004 mcihar@suse.cz
- cleaned up specfile
* Sat Jan 10 2004 adrian@suse.de
- build as user
* Mon Oct 13 2003 ro@suse.de
- remove explicit requires for mesa
* Mon May 26 2003 mcihar@suse.cz
- fixed documentation installation
* Thu May 15 2003 mcihar@suse.cz
- use defattr
* Thu Feb 13 2003 mcihar@suse.cz
- updated to 1.0.14
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Wed Apr  3 2002 tcrhak@suse.cz
- added aclocal, autoconf and automake to
  build with new automake/autoconf
* Thu Nov  8 2001 ro@suse.de
- use mesa-devel-packages in neededforbuild
* Mon Jul 16 2001 rvasice@suse.cz
- upgrade to 1.0.13
* Mon Jun  4 2001 rvasice@suse.cz
- spec file cleanup
* Tue May  8 2001 mfabian@suse.de
- bzip2 sources
* Thu Mar 15 2001 ro@suse.de
- changed neededforbuild <mesaglu> to <xf86glu>
- changed neededforbuild <mesaglu-devel> to <xf86glu-devel>
* Wed Mar  7 2001 ro@suse.de
- changed neededforbuild <mesadev> to <mesa-devel>
* Mon Feb 19 2001 uli@suse.de
- fixed for new glibc
* Fri Dec 15 2000 smid@suse.cz
- plib removed from requires
* Wed May 24 2000 smid@suse.cz
- mesadev added to neededforbuild
* Fri Apr 28 2000 smid@suse.cz
- buidroot added
- upgrade to 1.0.10
* Wed Feb  9 2000 sndirsch@suse.de
- changed group tag
* Sat Jan 29 2000 sndirsch@suse.de
- fixed a compile error ...
* Wed Dec 29 1999 sndirsch@suse.de
- update to version 1.0.8
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Thu Aug 19 1999 sndirsch@suse.de
- update to version 1.0.7
* Mon Jul 19 1999 sndirsch@suse.de
- required fonts are now included
- additional doc directory now also included
* Thu Jul  8 1999 sndirsch@suse.de
- tux_aqfh is now compiled with existing plib package
* Tue Jun 15 1999 ro@suse.de
- added mesasoft to neededforbuild
* Fri Jun 11 1999 sndirsch@suse.de
- updated tux_aqfh to version 1.0.4
- updated plib to version 1.0.12
* Thu May  6 1999 sndirsch@suse.de
- SPEC file created for "Tuxedo T. Penguin: A Quest for Herring"
