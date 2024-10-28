Name:           tuxcards 
Version:        2.2
Release:        33.1
Source:         tuxcards-2.2.tar.bz2
Source1:        %{name}.desktop
Source2:        %{name}.png
License:        GPL2
Group:          Productivity/Office/Organizers
Summary:        Manage Notes within a Hierarchical Tree
URL:            https://www.tuxcards.de/
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++ expat-devel qt4-devel

%description
Tuxcards provides a hierarchical notebook similar to the "CueCards"
program. With it, all kinds of notes and ideas can be managed and
sorted within a tree structure.

Authors:
--------------
    Alexander Theel <alex.theel@gmx.net>

%prep
%setup -q -n tuxcards
cp %{S:1} .
cp %{S:2} .
sed -i '46s|0 <|NULL !=|' src/information/CInformationElementHistory.cpp

%build
qmake-qt4 %{name}.pro
%{__make} -f Makefile 

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/usr/bin
%{__mkdir} -p $RPM_BUILD_ROOT/usr/share/tuxcards
%{__install} -m 755 tuxcards $RPM_BUILD_ROOT/usr/bin
%{__install} -m 644 src/gui/cactusbar/flowers/*.gif $RPM_BUILD_ROOT/usr/share/tuxcards
%{__install} -m 644 src/gui/cactusbar/flowers/cactus.egg $RPM_BUILD_ROOT/usr/share/tuxcards
%{__install} -D -m 644 %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%{__install} -D -m 644 %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%doc AUTHORS README COPYING INSTALL
%{_bindir}/tuxcards
%{_datadir}/tuxcards
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Feb 13 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuilt for Fedora
* Mon May 17 2010 - mweckbecker@suse.de
- suse_update_desktop_file added
* Fri Jun 19 2009 - mweckbecker@suse.de
- .desktop/.png file added
* Thu Jun 18 2009 - mweckbecker@suse.de
- initial package with version 2.2 and a few patches
