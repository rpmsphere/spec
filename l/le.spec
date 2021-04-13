Summary: This is terminal text editor
Name: le
Version: 1.16.8
Release: 1
License: GPL
Group: Applications/Editors
Source: ftp://ftp.yar.ru/pub/source/le/%{name}-%{version}.tar.gz
URL: http://lav.yar.ru/programs.html
BuildRequires: gcc-c++

%description
LE has many block operations with stream and rectangular blocks, can edit
both unix and dos style files (LF/CRLF), is binary clean, has hex mode,
tunable syntax highlighting, tunable color scheme, tunable key map and some
more useful features. It is slightly similar to Norton Editor from DOS.

%prep
%setup -q
sed -i 's|-lsupc++|-lstdc++ -lsupc++|' configure

%build
#define __libtoolize :
export CC=gcc CXX=g++
%configure
make

%install
%makeinstall

%files
%doc FEATURES HISTORY NEWS README doc/README.keymap.ru
%{_bindir}/le
%{_mandir}/man1/le.1.*
%{_datadir}/le
%{_datadir}/applications/le.desktop
%{_datadir}/icons/hicolor/48x48/apps/le-icon.png

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.16.8
- Rebuild for Fedora
* Fri Feb 27 2004 Peter Soos <sp@osb.hu>
- Moved to  Fedora Core 1
* Mon Apr 28 2003 Peter Soos <sp@osb.hu>
- Moved to RedHat Linux 9
- Moved to version 1.9.2
* Fri Aug 23 2002 Peter Soos <sp@osb.hu>
- Moved to Red Hat Linux 7.3
- Moved to version 1.9.1
* Sun Jun 02 2002 Peter Soos <sp@osb.hu>
- Moved to Red Hat Linux 7.2
* Mon Oct 01 2001 Peter Soos <sp@osb.hu>
- Moved to Red Hat Linux 7.2 beta
- Moved to version 1.9.0
* Thu May 03 2001 Peter Soos <sp@osb.hu>
- Moved to Red Hat Linux 7.1
* Wed Apr 18 2001 Peter Soos <sp@osb.hu>
- Moved to Red Hat Linux 7.0
* Sun Feb 11 2001 Peter Soos <sp@osb.hu>
- Moved to version 1.6.3
* Thu Nov 02 2000 Peter Soos <sp@osb.hu>
- Moved to version 1.6.0
* Mon Nov 08 1999 Peter Soos <sp@osb.hu>
- Moved to version 1.5.5
* Thu Jul 01 1999 Peter Soos <sp@osb.hu>
- Moved to version 1.5.2
* Thu May 13 1999 Peter Soos <sp@osb.hu>
- Moved to version 1.5.1
- Corrected the file and directory attributes to rebuild the package
  under RedHat Linux 6.0
* Tue Feb 23 1999 Peter Soos <sp@osb.hu>
- Moved to version 1.5.0
* Fri Dec 25 1998 Peter Soos <sp@osb.hu>
- Corrected the file and directory attributes
- Recompiled under RedHat Linux 5.2
* Mon Jun 22 1998 Peter Soos <sp@osb.hu>
- Using %%attr
* Thu Mar 18 1998 Peter Soos <sp@osb.hu>
- moved to 1.4.2
* Fri Dec 12 1997 Peter Soos <sp@osb.hu>
- moved to 1.4.1 from 1.4.0
* Sun Dec 7 1997 Peter Soos <sp@osb.hu>
- Recompiled under RedHat Linux 5.0
- Added BuildRoot
