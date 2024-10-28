%undefine _debugsource_packages
Name:           sabacc
Version:        1.0beta1
Release:        1
Summary:        Card game for two or more players that is similar to Blackjack
Group:          Amusements/Games
License:        GPL
URL:            https://sabacc.sourceforge.net/
Source0:        https://downloads.sourceforge.net/sabacc/sabacc-1.0-beta1.tar.gz
BuildArch:      noarch

%description
Sabacc is a game originally found in the Star Wars universe. 
It is similar in many ways to the game of Blackjack/Twenty-one
/Pontoon, with a number of differences:
    * It is played with a special deck of 76 cards, some of which
      are negative.
    * The aim of the game is to score as close as possible to 
      positive or negative 23 without exceeding it.
    * At any point during the game, a number of cards can change 
      values, meaning that a winning hand can instantly transform 
      into a losing hand or vice-versa.

Although these are the main differences, Sabacc actually has a 
complicated set of rules which differ in many ways to those of 
Blackjack. It is recommended that you familiarise yourself with 
them before starting to play Sabacc.
Copyright © 2007-2008 Joel Cross and the Sabacc Project 

%prep
%setup -q -n sabacc-1.0-beta1

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --root=$RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/doc/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%{_mandir}/man6/%{name}.6.gz
%{python2_sitelib}/%{name}*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0beta1
- Rebuilt for Fedora
* Tue Sep 1 2009 Harry Chen <harry@server1.ossii.com.tw> - 1.0-beta1.ossii
- Initial package for ossii
