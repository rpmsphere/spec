Summary: 3D first-person shooter game
Name: AlephOne
Version: 20080913
Release: 1
License: GPL
Group: Amusements/Games
Source: %{name}-%{version}.tar.gz
URL: https://alephone.cebix.net
# not relocatable because the data file packages depend upon the location
# of the data files in this package

Requires: SDL >= 1.2.0 SDL_image >= 1.2.0 SDL_net 
Requires: smpeg-devel libmad-devel libsndfile-devel
BuildRequires: SDL-devel SDL_image-devel SDL_net-devel boost-devel 
BuildRequires: speex-devel >= 1.0

%description
Aleph One is an Open Source 3D first-person shooter game, based on the game
Marathon 2 by Bungie Software. It is set in a Sci-Fi universe dominated by
deviant computer AIs and features a well thought-out plot. Aleph One
supports, but doesn't require, OpenGL for rendering.

Aleph One requires additional data -- shape, sound, and map
information -- in order to run. The easiest way to get this is to go
to https://source.bungie.org/get/, and download one of the scenario zip
files there. Unzip it, and pass the resulting directory as an argument
to alephone. For example:

alephone "~/Marathon Infinity"

%prep
%setup -q

%build
%configure --disable-speex
sed -i 's|-fexceptions|-fexceptions -fpermissive -std=gnu++14|' Makefile */Makefile */*/Makefile */*/*/Makefile
make

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall

%files
%doc AUTHORS COPYING INSTALL.Unix README docs/MML.html docs/Lua.html
%{_bindir}/alephone
%{_datadir}/AlephOne/Fonts
%{_datadir}/AlephOne/MML
%{_datadir}/AlephOne/Themes/Default
%{_mandir}/man6/alephone.6.gz

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20080913
- Rebuilt for Fedora
* Wed Oct 15 2008 Feather Mountain <john@ossii.com.tw> 
- Rebuild for M6(OSSII)
* Sat Jun 21 2008 Gregory Smith <wolfy@treellama.org>
- removed the dependence on AlephOne-core-data (users can use unimap zip files)
- removed deprecated cheats docs
- updated required libraries (there are many)
* Sun Nov 20 2005 Christian Bauer <www.cebix.net>
- modernized the spec file a bit
* Thu Oct  5 2000 Christian Bauer <Christian.Bauer@uni-mainz.de>
- Added docs and theme data files
- Package name and version are set by configure script
* Fri Sep 30 2000 Tom Moertel <tom-rpms-alephone@moertel.com>
- Added a requirement to the base package for AlephOne-core-data
- Split out the Marathon Infinity Demo data into its own package
* Thu Sep 29 2000 Tom Moertel <tom-rpms-alephone@moertel.com>
- Added patch for SDL 1.1.5 SDL_SetClipping incompatability.
* Sat Sep 23 2000 Tom Moertel <tom-rpms-alephone@moertel.com>
- Added Marathon Infinity Demo data to package.
