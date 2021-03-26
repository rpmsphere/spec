%global debug_package %{nil}

Name:       fancybrowser
Summary:    Qt Demo - qt fancybrowser
Version:    0.0.1
Release:    8.1
Group:      Development/Tools
License:    LGPLv2.1
URL:        http://qt.nokia.com
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtWebKit)
BuildRequires:  pkgconfig(QtNetwork)
BuildRequires:  desktop-file-utils

%description
Qt Demo fancybrowser.

%prep
%setup -q -n %{name}-%{version}
sed -i '43i #include <QtNetwork>' mainwindow.cpp

%build
qmake-qt4 PREFIX=%{_prefix}
make

%install
rm -rf %{buildroot}
make INSTALL_ROOT=%{buildroot}/usr install
mv %{buildroot}/usr/icons %{buildroot}%{_datadir}/icons

%files
%{_bindir}/fancybrowser
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sun Jan 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1
- Rebuild for Fedora
