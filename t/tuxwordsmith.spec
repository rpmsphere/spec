%global debug_package %{nil}
%define pkg_name TuxWordSmith

Name:		tuxwordsmith
Summary:        Scrabble like game for young children 
Version:        0.7.12
Release:        1
Group:          Educations/Games
License:        GPL
URL:            http://www.asymptopia.org/index.php?topic=TWS
Source0:        %{name}-%{version}.zip
Source1:        %{pkg_name}.desktop
Source2:        %{pkg_name}.png
Requires:	pygame
Requires:	wxGTK
BuildRequires:  python2
BuildArch:	noarch
%define         mp_group  games
%define         mp_user   games

%description
TuxWordSmith is similar to the classic word game "Scrabble", but with unicode
support for multiple languages and character sets. The game is currently
distributed with forty-two (42) dictionary resources for playing
Language[i]-Language[j] "Scrabble". 

For example, if configured to use the French-German dictionary, then the
distribution of available tiles will be computed based on frequency of
occurance of each character of Language[i] (French), and for each submission
the corresponding definition will be given in Language[j] (German). 

The latest release includes support for the Greek and Cyrillic (Russian,
Ukranian) character sets, thus making it possible to play Scrabble in Greek,
Russian and Ukranian, as well as a host of other languages which use latin
characters.

Author:
-------
	Charles B. Cosse


%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp tuxwordsmith.py %{buildroot}%{_bindir}/tuxwordsmith
chmod 755 %{buildroot}%{_bindir}/tuxwordsmith

mkdir -p %{buildroot}/var/games/TuxWordSmith
cp -a .tws_config_master Font xdxf %{buildroot}/var/games/TuxWordSmith
chmod -R 755 %{buildroot}/var/games/TuxWordSmith

mkdir -p %{buildroot}%{python2_sitelib}
cp -a TuxWordSmith %{buildroot}%{python2_sitelib}
chmod -R 755 %{buildroot}%{python2_sitelib}/TuxWordSmith

install -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

sed -i 's|/usr/bin/python|/usr/bin/python2|' %{buildroot}%{python2_sitelib}/TuxWordSmith/*.py %{buildroot}/var/games/TuxWordSmith/xdxf/*/*.py
sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf %buildroot

%files
%doc README INSTALL CHANGES LICENSE VERSION
%{_bindir}/%{name}*
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
/var/games/%{pkg_name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.12
- Rebuild for Fedora
* Mon Dec 08 2008 Feather Mountain <john@ossii.com.tw>
- Rebuild for M6(OSSII)
* Wed Nov  5 2008 lars@linux-schulserver.de
- enable post-build-checks again as suid-check is now in rpmlint
* Thu Oct 30 2008 lars@linux-schulserver.de
- disable post-build-checks
* Thu Sep 25 2008 lars@linux-schulserver.de
- moved to Education base repository
* Mon Apr 21 2008 lars@linux-schulserver.de
- initial version 0.5.3
