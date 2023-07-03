Name:           tuxmathscrabble
Version:        2.9r1
Release:        1
Summary:        An educational, math version of scrabble
Group:          Educations/Games
License:        GPL
URL:            https://www.asymptopia.org/index.php?topic=tuxmathscrabble
Source0:        https://easynews.dl.sourceforge.net/sourceforge/tuxmathscrabble/TuxMathScrabble-2.9-r1.tgz
Source1:	%{name}.png
BuildRequires:  python2-devel, SDL-devel, SDL_image-devel, SDL_mixer-devel, SDL_ttf-devel
Requires:	python2-pygame
Requires:       python2-wxpython
BuildArch:	noarch

%description
TuxMathScrabble encourages kids to construct compound equations and
to consider multiple abstract possibilities. The movements are by
drag-and-drop.  Upon valid submission, little penguins emerge from 
tiles like a cuckoo-clock. 

%prep
%setup -q -n TuxMathScrabble-2.9-r1
# remove junk files
rm -rf ./tuxmathscrabble/old/themes/default/images/.xvpics
rm -rf ./tuxmathscrabble/old/themes/default/anim_images/.xvpics
#find . -name "CVS" -exec  rm -rf "{}" ";"
#find . -name ".xvpics" -exec  rm -rf "{}" ";"

%install
rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/games/tuxmathscrabble
cp -a {User,Cast,Scoring,Theme} $RPM_BUILD_ROOT/var/games/tuxmathscrabble
#chmod -R 0777  $RPM_BUILD_ROOT/var/games/tuxmathscrabble
mkdir -p $RPM_BUILD_ROOT/%{python2_sitelib}
cp -a tuxmathscrabble $RPM_BUILD_ROOT/%{python2_sitelib}
chmod -R 0755 $RPM_BUILD_ROOT/%{python2_sitelib}
install -D -p app.py $RPM_BUILD_ROOT/%{_bindir}/tuxmathscrabble
chmod +x $RPM_BUILD_ROOT/usr/bin/tuxmathscrabble
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/tuxmathscrabble/
install -p AUTHOR CHANGES COPYING INSTALL LICENSE README VERSION $RPM_BUILD_ROOT/%{_defaultdocdir}/tuxmathscrabble/
chmod a-x $RPM_BUILD_ROOT/%{_defaultdocdir}/tuxmathscrabble/*

# Freedesktop menu entries
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT/usr/share/applications/%name.desktop <<EOF
[Desktop Entry]
Name=Tux Math Scrabble
Name[zh_TW]=企鵝填字數學
Exec=tuxmathscrabble 
Type=Application
Terminal=false
Categories=Education;
Encoding=UTF-8
Icon=%{name}
EOF

sed -i -e 's|/usr/bin/python$|/usr/bin/python2|' -e 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name} %{buildroot}%{python2_sitelib}/%{name}/*.py %{buildroot}%{python2_sitelib}/%{name}/*/*.py %{buildroot}%{python2_sitelib}/%{name}/*/*/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc %{_defaultdocdir}/*
%{_bindir}/tuxmathscrabble
%{_datadir}/applications/tuxmathscrabble.desktop
%{_datadir}/pixmaps/%{name}.png
/var/games/tuxmathscrabble/*
%{python2_sitelib}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.9r1
- Rebuilt for Fedora
* Mon Dec 08 2008 Feather Mountain <john@ossii.com.tw> 2.9r1-1.ossii
- Rebuild for M6(OSSII)
* Tue Feb 08 2006 Andrew Ziem <andrewz@springsrescuemission.org>  2.9r1-1fc4
- initial RPM
- some copy and paste from jean-sebastien HUBERT's .spec
