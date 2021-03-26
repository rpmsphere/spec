Name:       ksmoothdock
Summary:    KDE Applications Docker
Version:    6.2
Release:    1
Group:      Graphical desktop/KDE5
License:    GPLv2
URL:        https://dangvd.github.io/ksmoothdock/
Source0:    %name-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: kf5-kactivities-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kjobwidgets-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-sonnet-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kwallet-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kio-devel
BuildRequires: qt5-devel
BuildRequires: taglib-devel
BuildRequires: phonon-devel
BuildRequires: pkgconfig

%description
KSmoothDock is a cool desktop panel with parabolic zooming effect for KDE
Plasma  5. While visually it is inspired by Mac OS X's Dock, it aims to
follow the traditional Linux model of desktop panel with the application
menu, launchers, the pager, the taskbar and the system tray. Currently
KSmoothDock only supports the application menu, launchers and the pager,
and is meant to use in conjunction with a Plasma 5 panel that provides
the taskbar and the system tray.

KSmoothDock is written in C++ and depends on Qt 5 and KDE Frameworks 5

%files
%doc README
%{_bindir}/ksmoothdock
%{_datadir}/applications/ksd.ksmoothdock.desktop
%{_libdir}/libksmoothdock_lib.so

%prep
%setup -q

%build
cd src
%cmake_kf5 .
%make_build

%install
rm -rf %buildroot
cd src
%make_install

mkdir -p %buildroot/%{_libdir}
install -m 0755 libksmoothdock_lib.so %buildroot/%{_libdir}/libksmoothdock_lib.so

desktop-file-install --vendor="" \
 --remove-category='Utility' \
 --add-category='Monitor' \
 %{buildroot}%{_datadir}/applications/*.desktop

%changelog
* Fri Jan 17 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 6.2
- Rebuild for Fedora
* Tue Jul 02 2019 tex - 5.12-1pclos2019
- new version
