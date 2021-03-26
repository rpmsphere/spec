%define         upstream_name Stacer

Name:           stacer
Version:        1.1.0
Release:        1
Summary:        Linux System Optimizer and Monitoring
Group:          Monitoring
License:        MIT
URL:            https://github.com/oguzhaninan/Stacer/
Source0:        https://github.com/oguzhaninan/Stacer/archive/v%{version}.tar.gz#/%{upstream_name}-%{version}.tar.gz
Patch0:         stacer-1.0.9-fix-build-against-qt-5.11.0.patch
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  cmake

%description
Linux System Optimizer and Monitoring.

%prep
%setup -q -n %{upstream_name}-%{version}
#autosetup -n %{upstream_name}-%{version} -p1

%build
%cmake .
make

%install
make install
install -Dm755 output/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
cp -a icons %{buildroot}%{_datadir}

%files
%doc README.md LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Thu Dec 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuild for Fedora
* Sun Sep 23 2018 umeabot <umeabot> 1.0.9-3.mga7
  (not released yet)
+ Revision: 1301182
- Mageia 7 Mass Rebuild
* Mon Jun 04 2018 daviddavid <daviddavid> 1.0.9-2.mga7
+ Revision: 1234393
- add patch to fix build with new Qt5 >= 5.11.0
* Tue Apr 10 2018 kekepower <kekepower> 1.0.9-1.mga7
+ Revision: 1217314
- imported package stacer
