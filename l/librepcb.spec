Name:		librepcb
Version:	0.1.5
Release:	1
Summary:	A powerful, innovative and intuitive EDA tool for everyone
License:	GPLv3+
Group:		Sound/Players
URL:		https://librepcb.org
Source0:	https://download.librepcb.org/releases/%{version}/%{name}-%{version}-source.zip
BuildRequires:	qt5-qttools
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5OpenGL)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(gl)
BuildRequires:	SFML-devel
Requires:	qt5-qtbase

%description
LibrePCB is a free EDA software to develop printed circuit boards.

%prep
%autosetup -p1

%build
%qmake_qt5 -r %{name}.pro PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc AUTHORS.md CONTRIBUTING.md README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_metainfodir}/org.%{name}.LibrePCB.appdata.xml
%{_datadir}/mime/packages/org.%{name}.LibrePCB.xml
%{_includedir}/fontobene-qt5

%changelog
* Tue Oct 06 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.5
- Rebuilt for Fedora
* Wed Jul 15 2020 daviddavid <daviddavid> 0.1.4-1.mga8
+ Revision: 1606242
- new version: 0.1.4
* Fri May 01 2020 wally <wally> 0.1.3-4.mga8
+ Revision: 1577616
- use %%make_install
* Fri May 01 2020 ovitters <ovitters> 0.1.3-3.mga8
+ Revision: 1577577
- rebuild to test package builds with cmake_install without a cmake_build
* Tue Feb 18 2020 umeabot <umeabot> 0.1.3-2.mga8
+ Revision: 1539643
- Mageia 8 Mass Rebuild
* Tue Dec 10 2019 daviddavid <daviddavid> 0.1.3-1.mga8
+ Revision: 1465726
- initial package librepcb
