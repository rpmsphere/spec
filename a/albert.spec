%global __python %{__python3}

Name:           albert
Version:        0.23.0
Release:        1
Summary:        Desktop agnostic launcher
License:        GPL-3.0+
Group:          System/GUI/Other
URL:            https://albertlauncher.github.io/
Source0:        %{name}-%{version}.tar.gz
Source1:        QHotkey.zip
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.2
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5DBus) >= 5.2
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2
BuildRequires:  pkgconfig(Qt5Network) >= 5.2
BuildRequires:  pkgconfig(Qt5Sql) >= 5.2
BuildRequires:  pkgconfig(Qt5Svg) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.2
BuildRequires:  pkgconfig(Qt5Xml) >= 5.2
BuildRequires:  pkgconfig(muparser)
BuildRequires:  qt5-qtdeclarative-devel

%description
Access everything with virtually zero effort. Run applications,
open files or their paths, open bookmarks in your browser, search
the web, calculate things and a lot more.

%prep
%setup -q
#sed -i '32i #include <functional>' src/lib/albert/src/albert/albert.cpp
#sed -i '31i #include <QAction>' src/lib/albert/src/albert/mainwindow/mainwindow.cpp
#sed -i '26i #include <QRegularExpression>' src/plugins/ssh/src/main.cpp
#sed -i '/plugins/d' CMakeLists.txt
unzip %{SOURCE1} -d lib/QHotkey

%build
%cmake \
  -DCMAKE_SHARED_LINKER_FLAGS="" \
  -DCMAKE_SKIP_RPATH=OFF
%cmake_build

%install
%cmake_install

%files
%doc *.md
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Sun Dec 08 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 0.23.0
- Rebuilt for Fedora
* Tue May  9 2017 sor.alexei@meowr.ru
- Update to version 0.11.1:
  * No changelog available.
- Rebase albert-fix-libdir.patch.
* Mon Feb  6 2017 sor.alexei@meowr.ru
- Update to version 0.9.3:
  * No changelog available.
- Add albert-fix-libdir.patch: Install libraries into a correct
  directory.
* Sat Jul 23 2016 sor.alexei@meowr.ru
- Update to version 0.8.10:
  * No changelog available.
* Sat May 28 2016 sor.alexei@meowr.ru
- Update to version 0.8.9:
  * No changelog available.
* Wed May  4 2016 sor.alexei@meowr.ru
- Update to version 0.8.8.
* Mon Apr 25 2016 p.drouand@gmail.com
- Update to version 0.8.7.2
  * No changelog available
- Add pkgconfig(Qt5Svg) requirement; new upstream dependency
* Mon Nov 23 2015 sor.alexei@meowr.ru
- Initial package.
