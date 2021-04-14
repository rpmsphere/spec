Name:           nimuh-data
Url:            http://www.nimuh.com/
License:        CC-by-nc-sa 2.5 Spain
Group:          Amusements/Games/Logic
Version:        1.02
Release:        1
Summary:        Data needed by nimuh
Source:         http://downloads.sourceforge.net/nimuh/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Nimuh is a game under Creative Commons license and ambiented in Andalusia. A
game based in "Theseus and the Minotaur Mazes" that will go through different
andalusian locations.

This package includes the data files needed by the game.

%prep
%setup -q

%build
cp /usr/share/automake-*/config.guess .
./configure --prefix=%{_prefix}
%{__make}

%install
%{__make} DESTDIR="${RPM_BUILD_ROOT}" install

%clean
%{__rm} -rf "${RPM_BUILD_ROOT}"

%files
%{_datadir}/nimuh

%changelog
* Wed Mar 14 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.02
- Rebuilt for Fedora
* Mon Feb 25 2008 - cmorve69@yahoo.es
- updated data file (mantains 1.02 version)
* Tue Jan 29 2008 - cmorve69@yahoo.es
- updated to version 1.02
  * solve problem with joystick
  * solve error in the third level (english version)
* Sun Jan 27 2008 - cmorve69@yahoo.es
- initial package
