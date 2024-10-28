Name:           gperiodic
Summary:        A graphical application for browsing the periodic table
Version:        3.0.1
Release:        6.1
URL:            https://www.frantz.fi/software/gperiodic.php
Group:          Sciences/Chemistry
License:        GPLv2+
Source0:        https://sourceforge.net/projects/gperiodic/files/%{name}-%{version}.tar.gz
BuildRequires:  gtk2-devel
BuildRequires:  intltool

%description
Gperiodic displays a periodic table of the elements, allowing you to
browse through the elements, and view detailed information about each
element. This program also features a non-graphical interface.

%prep
%setup -q

%build
make

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_bindir}/*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/*.xpm
%{_mandir}/man1/*.1*

%changelog
* Mon Feb 22 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.1
- Rebuilt for Fedora
* Sat Feb 20 2016 umeabot <umeabot> 3.0.1-2.mga6
+ Revision: 972472
- Mageia 6 Mass Rebuild
* Sun Nov 08 2015 alexl <alexl> 3.0.1-1.mga6
+ Revision: 898870
- version 3.0.1
- new url
- s/makeinstall_std/make_install/ 
- del upstreamed genericname.patch
* Wed Jan 07 2015 alexl <alexl> 3.0.0-4.mga5
+ Revision: 808913
- added patch from upstream for addding GenericName in desktop file
* Wed Oct 15 2014 umeabot <umeabot> 3.0.0-3.mga5
+ Revision: 751091
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 3.0.0-2.mga5
+ Revision: 679908
- Mageia 5 Mass Rebuild
* Fri Aug 01 2014 alexl <alexl> 3.0.0-1.mga5
+ Revision: 658946
- imported package gperiodic
