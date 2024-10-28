%undefine _debugsource_packages

Name:           tuxomania
BuildRequires:  gcc-c++ SDL-devel SDL_image-devel SDL_ttf-devel mesa-libGL-devel xerces-c-devel cmake dos2unix fdupes bitstream-vera-sans-fonts
Summary:        You control Tux the penguin and must collect all the pearls in each level
Version:        0.0.3
Release:        12.1
License:        GPLv3; CC-BY-SA
Group:          Amusements/Games/Action/Arcade
Source:         %{name}-%{version}-src.tar.bz2
Patch0:         %{name}-fix-compile-error.patch
Patch1:         tuxomania-0.0.3-no_freetype_dependency.patch
URL:            https://sourceforge.net/projects/tuxomania/
Requires:       bitstream-vera-sans-fonts

%description
Tuxomania is a platform game in isometric 3d. The player controls Tux
the penguin and must collect all the pearls in each level, which includes
solving puzzles and avoiding monsters. The game is in an early stage.
The current version contains only three test levels and can't be completed.

Authors:
--------
    Vincent Petry <PVince81@users.sourceforge.net>

%prep
%setup -q -n %{name}-%{version}-src
%patch 0 -p1
%patch 1
dos2unix doc/README-SDL*.txt

%build
make PREFIX="%{_prefix}" DATA_PATH="%{_datadir}/%{name}"

%install
make PREFIX="%{_prefix}" DESTDIR="%{buildroot}" install
# Use shared Vera font instead of the bundled one
ln -sf %{_datadir}/fonts/bitstream-vera/Vera.ttf %{buildroot}/%{_datadir}/%{name}/fonts/
mv %{buildroot}/%{_datadir}/doc/packages/%{name} %{buildroot}/%{_datadir}/doc/%{name}-%{version}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_docdir}/%{name}-%{version}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Mar 24 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.3
- Rebuilt for Fedora
* Thu Apr 28 2011 PVince81@opensuse.org
- Fixed compile error
* Sat Mar 13 2010 PVince81@yahoo.fr
- Updated to version 0.0.3
* Mon Feb  1 2010 PVince81@yahoo.fr
- Initial package
