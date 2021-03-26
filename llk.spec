Name: llk
Summary: A Shisen-Sho style board game
Version: 0.1
Release: 7.1
Group: Amusements/Games
License: GPLv2
Source0: %{name}_%{version}-1.tar.gz
BuildRequires: SDL-devel
BuildRequires: qt3-devel

%description
Lian Lian Kan is a puzzle game written in Qt.

%prep
%setup -q

%build
export QTDIR=%{_libdir}/qt-3.3
$QTDIR/bin/qmake
make

%install
make install INSTALL_ROOT=%{buildroot}

%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/apps/%{name}
%{_datadir}/applications/kde/%{name}.desktop
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png

%changelog
* Wed Jan 15 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuild for Fedora
