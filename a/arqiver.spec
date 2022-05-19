Name:           arqiver
Version:        0.9.0
Release:        1
Summary:        A simple Qt5 archive manager
Group:          Archiving/Other
License:        GPLv3
URL:            https://github.com/tsujan/Arqiver
Source:         https://github.com/tsujan/Arqiver/releases/download/V%{version}/Arqiver-%{version}.tar.xz
BuildRequires:  qt5-qttools
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
Requires:       bsdtar
Requires:       gzip
Requires:       p7zip

%description
A simple and desktop-agnostic Qt file archiver
LXQt Archiver is derived from the following programs:
* Engrampa of MATE desktop
* File Roller of Gnome desktop

%prep
%setup -q -n Arqiver-%{version}

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md ChangeLog
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/

%changelog
* Sun Apr 24 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.0
- Built for Fedora
* Mon Apr 04 2022 umeabot <umeabot> 0.7.0-2.mga9
+ Revision: 1843678
- Mageia 9 Mass Rebuild
* Thu Jun 03 2021 dglent <dglent> 0.7.0-1.mga9
+ Revision: 1729426
- imported package arqiver
