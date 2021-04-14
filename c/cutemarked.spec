%undefine _debugsource_packages

Name:                   cutemarked
Summary:                Qt-based Markdown editor
Group:                  Productivity/Text/Editors
Version:                0.11.3
Release:                6.1
License:                GPL-2.0+
URL:                    http://github.com/cloose/CuteMarkEd
Source0:                CuteMarkEd-%{version}.tar.gz
Requires:               cutemarked-plugin-fontawesome
BuildRequires:          libstdc++-devel 
BuildRequires:          gcc-c++ 
BuildRequires:          make
BuildRequires:          pkgconfig
BuildRequires:          pkgconfig(Qt5Core)
BuildRequires:          pkgconfig(Qt5Gui)
BuildRequires:          pkgconfig(Qt5Network)
BuildRequires:          pkgconfig(Qt5WebKitWidgets)
BuildRequires:          qt5-qttools-devel
BuildRequires:          libmarkdown-devel
BuildRequires:          pkgconfig(hunspell)
BuildRequires:          desktop-file-utils
BuildRequires:          pkgconfig(gstreamer-0.10) pkgconfig(gstreamer-app-0.10)
BuildRequires:          pkgconfig(sqlite3)

%description
A Qt-based Markdown editor with live HTML preview and syntax highlighting of
markdown document.

%package plugin-fontawesome
Summary:                Qt Iconengine - Fontawesome plugin
Group:                  Qt/Qt
License:                BSD-3-Clause

%description plugin-fontawesome
This package provides the fontawesome iconengine plugin.
 
%prep
%setup -q -n CuteMarkEd-%{version}
sed -i '27i #include <QAction>' app/optionsdialog.cpp

%build
qmake-qt5
make

%install
make INSTALL_ROOT="%buildroot" install

%files 
%_bindir/cutemarked
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%files plugin-fontawesome
%{_libdir}/qt5/plugins/iconengines/libfontawesomeicon.so

%changelog
* Tue Mar 29 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11.3
- Rebuilt for Fedora
* Mon Apr 07 2014 Christian Loose <christian.loose@hamburg.de> 0.9.2-1
- New patch version 0.9.2 released
* Fri Jan 31 2014 Christian Loose <christian.loose@hamburg.de> 0.9.1-1
- New patch version 0.9.1 released
* Sat Jan 25 2014 Christian Loose <christian.loose@hamburg.de> 0.9.0-1
- New minor version 0.9.0 released
* Tue Nov 19 2013 Christian Loose <christian.loose@hamburg.de> 0.8.1-1
- New patch version 0.8.1 released
* Fri Nov 08 2013 Christian Loose <christian.loose@hamburg.de> 0.8.0-1
- New minor version 0.8.0 released
* Thu Jul 04 2013 Christian Loose <christian.loose@hamburg.de> 0.6.1-1
- New patch version 0.6.1 released
* Tue Jun 25 2013 Christian Loose <christian.loose@hamburg.de> 0.6.0-1
- New minor version 0.6.0 released
* Fri Jun 14 2013 Christian Loose <christian.loose@hamburg.de> 0.5.0-1
- New minor version 0.5.0 released
* Fri Jun 07 2013 Christian Loose <christian.loose@hamburg.de> 0.4.1-2
- New patch version 0.4.1 released
* Thu May 30 2013 Christian Loose <christian.loose@hamburg.de> 0.4.1-1
- First Linux packages
* Tue Apr 30 2013 Christian Loose <christian.loose@hamburg.de> 0.1.0-1
- Initial release
