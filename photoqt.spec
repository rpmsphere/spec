Name:           photoqt
Version:        1.3
Release:        4.1
Summary:        A fast Qt image viewer
License:        GPLv3
Group:          Graphics/Viewers
URL:            http://photoqt.org/
Source0:        http://photoqt.org/pkgs/%{name}-%{version}.tar.gz
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-tds
BuildRequires:  qt5-qtbase-odbc
BuildRequires:  qt5-qtbase-mysql
BuildRequires:  qt5-qtbase-postgresql
BuildRequires:  qt5-qtbase-ibase
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  cmake
BuildRequires:  phonon-qt5-devel
BuildRequires:  pkgconfig(GraphicsMagick++)

%description
PhotoQt is a simple, yet powerful and good looking image viewer,
written in Qt, published as open-source, and completely free.

%prep
%setup -q

%build
%cmake

%install
%make_install

%files
%doc CHANGELOG COPYING README
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sun Nov 29 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuild for Fedora
* Sat Nov 16 2013 dglent <dglent> 1.0-1.mga4
+ Revision: 551499
- imported package photoqt
