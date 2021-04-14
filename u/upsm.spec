Name:          upsm
Version:       2.2.0
Release:       1
Summary:       Qt-based ups monitor (front-end for upsc from Network UPS Tools)
Group:         Monitoring
URL:           https://github.com/psemiletov/upsm
Source0:       https://github.com/psemiletov/upsm/archive/%{name}-%{version}.tar.gz
License:       GPLv3+
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
Requires: nut

%description
upsm is Qt-based ups monitor (front-end for upsc from Network UPS Tools). 
It sits at the tray and polls nut server using upsc, so you need to set 
up NUT first.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -pthread"
%cmake
%make_build

%install
%make_install

%files
%{_bindir}/upsm
%{_datadir}/applications/upsm.desktop
%{_datadir}/icons/hicolor/128x128/apps/upsm.png
%{_datadir}/icons/hicolor/scalable/apps/upsm.svg

%changelog
* Thu Sep 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.0
- Rebuilt for Fedora
* Fri Jul 13 2018 semiletov <semiletov> 2.0.2-1.mga7
  (not released yet)
+ Revision: 1243451
+ rebuild (emptylog)
* Fri Jul 13 2018 semiletov <semiletov> 2.0.1-2.mga7
+ Revision: 1243445
- svg icon added
- patch removed because upstream fixed
- update to upstream 2.0.1
- switch to cmake build system; update to upstream 2.0.0
+ wally <wally>
- add patch to fix CXXFLAGS
* Tue Jan 02 2018 semiletov <semiletov> 1.3.3-2.mga7
+ Revision: 1189320
- spec file fixes and cleanup
* Mon Nov 27 2017 semiletov <semiletov> 1.3.3-1.mga7
+ Revision: 1180110
- desktop file fixes, upstream updated
- imported package upsm
