%undefine _debugsource_packages

Name:           flashlauncher
Version:        0.3
Release:        25.1
Summary:        Flash Game and Application Database/Launcher
Group:          Amusements/Games
License:        LGPL
URL:            https://maemo.org/packages/view/flashlauncher/
Source0:        flashlauncher-0.3.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  qt-devel
BuildRequires:  qtwebkit-devel
BuildRequires:  desktop-file-utils

%description
Flashlauncher is a flash game^H^H^H^H application database
and launcher that facilitates the easy use of Maemo device
friendly flash content.

%prep
%setup -q
sed -i '1i #include <unistd.h>' flashlauncher/launcher.cpp
sed -i 's|/usr/lib/browser/plugins|%{_libdir}/flash-plugin|' flashlauncher/launcher.cpp
sed -i 's|/hildon||' flashlauncher/flashlauncher.pro

%build
qmake-qt4
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}
echo 'Categories=Game;Emulator;' >> %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}

%changelog
* Sun Jan 06 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
