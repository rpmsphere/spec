%undefine _debugsource_packages
%define qt5version 5.2

Name:           qwx
Summary:        WeChat for linux
Version:        0.6
Release:        1
License:        GPL-3.0
Url:            https://github.com/xiangzhai/qwx
Group:          Productivity/Networking/Instant Messenger
Source:        %{name}-%{version}.tar.gz
%if 0%{?fedora}
BuildRequires:  qt5-qtbase-devel >= %{qt5version}
%endif
%if 0%{?suse_version}
BuildRequires:  libqt5-qtbase-common-devel >= %{qt5version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  pkgconfig(Qt5Xml) >= %{qt5version}
BuildRequires:  pkgconfig(Qt5Network) >= %{qt5version}
#BuildRequires:  pkgconfig(Qt5QuickParticles) >= %{qt5version}
BuildRequires:  qt5-qtdeclarative-devel >= %{qt5version}
%if 0%{?suse_version}
Requires:       libqt5-qtquickcontrols >= %{qt5version}
%endif
%if 0%{?fedora}
Requires:       qt5-qtquickcontrols >= %{qt5version}
%endif

%description
WeChat for linux, base with QT5.

%prep
%setup -q 
chmod 644 AUTHORS.md LICENSE README.md
sed -i 's|endl|Qt::endl|' src/cookie.cpp
sed -i 's|delete obj;|{delete obj;}|' src/init.cpp
sed -i '4i #include <QPainterPath>' src/circleimage.cpp

%build
qmake-qt5 QWX_DEBUG=ON PREFIX=%{buildroot}%{_prefix}
make

%install
make install
%if 0%{?suse_version}
%suse_update_desktop_file -r %{name} InstantMessaging
%endif

%files 
%doc AUTHORS.md LICENSE README.md
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/
%{_bindir}/%{name}

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
