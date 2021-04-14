%undefine _debugsource_packages
Name:           xye
Version:        0.12.1
Release:        1
URL:            http://xye.sourceforge.net/
Summary:        Puzzle game where the goal is to collect all the gems in the room
License:        Zlib
Group:          Amusements/Games/Action/Arcade
# Downloaded from sourceforge at http://downloads.sourceforge.net/xye/xye-0.9.3.tar.gz, repacked as bzip2
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
# PATCH-FIX-UPSTREAM xye-external-tinyxml.patch -- xye bundles tinyxml because not available in all distros, this patch makes it use the libtinyxml shared library
Patch0:         %{name}-external-tinyxml.patch
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  tinyxml-devel

%description
Xye is a puzzle game in which the objective is to help a character that looks like a green circle to get all the gems in the room. This is, of course, not as easy as it sounds, Xye must solve all sorts of puzzles while at the same time avoiding all sorts of traps and beasts.

Xye is similar to other puzzle games like sokoban or boulderdash, yet it also includes some arcade elements.

Xye is a derivative of a classic windows game called Kye, which is the base of the gameplay experience and visual elements. Xye is able to play level files that were made for Kye and Sokoban. It is also able to play custom .xye files, a richer level format that allows the new objects and features, you can make these levels by hand or by using the built-in editor that comes with the game.

Authors:
--------
	Víctor Hugo Solíz Kuncar (Vexorian) <vexorian@gmail.com>

%prep
%setup -q

# Convert to unix line end to be able to properly apply the patch
find src -name "*.h" -exec dos2unix "{}" "+"
find src -name "*.cpp" -exec dos2unix "{}" "+"
%patch -P 0 -p1

# Fix docdir
sed -i -e "s|^docedir =.*|docedir = %{_docdir}/%{name}|" Makefile.in
sed -i '1i #include <unistd.h>' src/gen.cpp
sed -i 's|int i,j;|int j;|' src/editorsave.cpp

%build
%configure --docdir=%{_docdir}/%{name}

# Some docs have the DOS line ends
dos2unix COPYING AUTHORS NEWS ChangeLog
sed -i 's|-Wall|-Wall -Wno-narrowing|' Makefile
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install-strip

install -D %{S:1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -d -D %{buildroot}%{_datadir}/pixmaps/
ln -s %{_docdir}/%{name}/%{name}.svg %{buildroot}%{_datadir}/pixmaps/

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.12.1
- Rebuilt for Fedora
* Fri May 04 2012 chris@ossii.com.tw
- Rebuild make to OX2 version
* Mon Mar 26 2012 PVince81@opensuse.org
- Updated to version 0.12.1
- Added _service file
* Sun Feb 19 2012 jengelh@medozas.de
- Remove redundant tags/sections from specfile
- Parallel build with %%_smp_mflags
- Actually do use the system's tinyxml library
* Thu Oct 13 2011 PVince81@opensuse.org
- Updated to version 0.11.2
* Sun Oct  2 2011 PVince81@opensuse.org
- Updated to version 0.11.1
* Sun Jul 31 2011 PVince81@opensuse.org
- Updated to version 0.10.0
* Sun Jan 16 2011 PVince81@opensuse.org
- Updated to version 0.9.3
* Mon Jan  4 2010 PVince81@yahoo.fr
- Changed SDL dependencies to SDL instead of libSDL
- Updated summary
* Wed Sep  2 2009 PVince81@yahoo.fr
- Updated to version 0.9.1
* Fri Jul 31 2009 PVince81@yahoo.fr
- Initial package
