%undefine _debugsource_packages

Name: spacewar-sdl
Version: 0.3
Release: 7.1
Source0: https://sourceforge.net/projects/%{name}/files/%{name}/spacewar-%{version}/spacewar-%{version}.tar.gz
Source1: %{name}.png
Source2: %{name}.desktop
License: GNU General Public License
Group: Amusements/Arcade
URL: https://sourceforge.net/projects/spacewar-sdl/
Summary: A SpaceWar-like game in SDL
BuildRequires:  gcc-c++, SDL-devel

%description
Spacewar is an arcade game in wich two players have to destroy each-others
space ship by hitting them with their lasers. It is written in SDL and
currently runs on both the Windows and Linux operating system, but it should
compile on more platforms.

%prep
%setup -q -n spacewar-%{version}
sed -i -e 's| -march=pentium||' -e 's| -L/usr/X11R6/lib||' src/Makefile
sed -i -e 's|iostream\.h|iostream|' -e 's|cout|std::cout|' -e 's|endl|std::endl|' src/util.cpp
sed -i 's|images|/usr/share/spacewar-sdl|' src/gfx_sdl.cpp

%build
make -C src

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 755 bin/spacewar $RPM_BUILD_ROOT%{_bindir}/%{name}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 bin/images/* $RPM_BUILD_ROOT%{_datadir}/%{name}
install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -Dm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Dec 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
