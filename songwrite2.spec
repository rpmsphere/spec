Name:		songwrite2
Version:	0.4.1
Release:	12.1
Summary:    	Guitar tabulature editor with playing and printing
License:	GPLv2
Group:		Sound/Midi
URL:        	http://home.gna.org/oomadness/en/songwrite
Source0:     	http://download.gna.org/songwrite/Songwrite2-%{version}.tar.gz
BuildRequires:  python2-devel
Requires:	python-editobj2
Requires:       hicolor-icon-theme
BuildArch:	noarch
Obsoletes:	songwrite

%description
Songwrite2 is a tablature (guitar partition) editor. It's the successor of songwrite.
Songwrite2 is coded in Python and uses Tk (Tkinter); it relies on Timidity to
play midi and on GNU Lilypond for printing.

%prep
%setup -q -n Songwrite2-%version

%build

%install
python2 setup.py install --root=%{buildroot}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
mv %{buildroot}%{_datadir}/*.egg-info %{buildroot}%{_datadir}/%{name}

#icons
install -Dm644 data/%{name}_64x64.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Songwrite2
Comment=Guitar TAB editor
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=AudioVideo;Audio;
EOF

%find_lang %name

# remove unpackaged files
rm -f %{buildroot}%{_datadir}/locale/*/*/*.po

mv %{buildroot}%{_datadir}/doc/%{name}/en/doc.pdf en-doc.pdf
mv %{buildroot}%{_datadir}/doc/%{name}/fr/doc.pdf fr-doc.pdf

sed -i 's|/usr/bin/python |/usr/bin/python2 |' %{buildroot}%{_bindir}/%{name}

%files -f %name.lang
%doc README CHANGES AUTHORS *.pdf
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/*

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuild for Fedora
* Mon Jan 14 2013 umeabot <umeabot> 0.4.1-5.mga3
+ Revision: 382326
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sat Dec 29 2012 barjac <barjac> 0.4.1-4.mga3
+ Revision: 336219
- changed group in line with new policy
* Fri Oct 21 2011 obgr_seneca <obgr_seneca> 0.4.1-3.mga2
+ Revision: 157178
- timidity is only a suggest
- require application handler for pdf
* Tue Oct 18 2011 obgr_seneca <obgr_seneca> 0.4.1-2.mga2
+ Revision: 156214
- removed unneeded %%post and %%postun section
- renamed icon files
- Added icons
* Mon Sep 19 2011 obgr_seneca <obgr_seneca> 0.4.1-1.mga2
+ Revision: 145405
- new version 0.4.1
  + kharec <kharec>
    - imported package songwrite2
