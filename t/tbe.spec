Name:           tbe
Version:        0.9.3.1
Release:        7.1
Summary:        Physics Game like "The Incredible Machine" 
Group:          Games/Puzzles
License:        GPLv2
URL:            https://github.com/the-butterfly-effect/tbe
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-linguist
BuildRequires:  gettext
Provides:       thebutterflyeffect

%description
The Butterfly Effect uses realistic physics simulations to combine
lots of simple mechanical elements to achieve a simple goal in the
most complex way possible.

%prep
%setup -q
sed -i -e 's|share/games|share|' -e 's|games)|bin)|' CMakeLists.txt

%build
#pushd i18n
#./%{name}_levels_i18n.sh
#popd
%cmake -DWITH_DOCS=OFF \
       -DBUILD_SHARED_LIBS=OFF \
       -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS DESCRIPTION README.md installer/License imagery/README.*
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Mon May 08 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.3.1
- Rebuilt for Fedora
* Wed Oct 28 2015 alexl <alexl> 0.9.2.1-1.mga6
+ Revision: 896053
- version 0.9.2.1
- new spec file
- del upstreamed patches
  + akien <akien>
    - imported package tbe
