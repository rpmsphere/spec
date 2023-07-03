Summary: Some cartoon themes for xpenguins
Name: xpenguins-themes
Version: 1.0
Release: 8.1
Source0: https://xpenguins.seul.org/xpenguins_themes-%{version}.tar.gz
Group: Amusements/Graphics
Requires: xpenguins >= 1.9
License: various
URL: https://xpenguins.seul.org/
BuildArch: noarch
Provides: xsimpsons

%description
Themes for xpenguins: "The Simpsons", "Sonic the Hedgehog", "Winnie
the Pooh", "Lemmings" and "Worms". These are distributed separately
from the basic xpenguins package because they were created from
animated gifs found on the web so the licensing/copyright situation is
unclear, or, in the case of Lemmings, imitate copyrighted
artwork. Type "xpenguins -l" to see a list of available themes.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT 
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xpenguins/themes
cp -a themes $RPM_BUILD_ROOT/%{_datadir}/xpenguins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/xpenguins/themes/Sonic_the_Hedgehog
%{_datadir}/xpenguins/themes/The_Simpsons
%{_datadir}/xpenguins/themes/Winnie_the_Pooh
%{_datadir}/xpenguins/themes/Lemmings
%{_datadir}/xpenguins/themes/Worms

%changelog
* Sun Aug 26 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Sun Sep 15 2002  <R.J.Hogan@reading.ac.uk> 1.0-1
- Added Worms theme
* Mon Sep 24 2001  <R.J.Hogan@reading.ac.uk> 0.9-1
- Added Lemmings theme
* Sun May  6 2001  <R.J.Hogan@reading.ac.uk> 0.2-1mdk
- First rpm
