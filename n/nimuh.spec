Name:           nimuh
Url:            https://www.nimuh.com/
License:        CC-by-nc-sa 2.5 Spain
Group:          Amusements/Games/Logic
Version:        1.02
Release:        1
Summary:        Puzzle game destined to improve the knowledge of Andalusia
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Source2:        %{name}.desktop
Patch0:         %{name}-%{version}-glu.patch
Requires:       %{name}-data = %{version}
BuildRequires:  SDL-devel SDL_mixer-devel SDL_image-devel gcc-c++ make mesa-libGL
BuildRequires:  expat-devel desktop-file-utils

%description
Nimuh is a game under Creative Commons license and ambiented in Andalusia. A
game based in "Theseus and the Minotaur Mazes" that will go through different
ansalusian locations.

%prep
%setup -q
%patch0

%build
sed -i 's/ GL\/glu.h//' configure.ac
sed -i 's/ -lGLU//' configure.ac
autoreconf -ifv
%configure
%{__make} %{?_smp_mflags} CXXFLAGS+=-Wno-format-security

%install
%{__make} DESTDIR="${RPM_BUILD_ROOT}" install
%{__install} -p -D -m 0644 "%{SOURCE1}" "${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png"
%{__install} -p -D -m 0644 "%{SOURCE2}" "${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop"

%clean
%{__rm} -rf "${RPM_BUILD_ROOT}"

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Mar 14 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.02
- Rebuilt for Fedora
* Sun Apr 20 2008 - cmorve69@yahoo.es
- removed bogus libGLU dependency
* Tue Jan 29 2008 - cmorve69@yahoo.es
- updated to version 1.02
  * solve problem with joystick
  * solve error in the third level (english version)
* Sun Jan 27 2008 - cmorve69@yahoo.es
- initial package
