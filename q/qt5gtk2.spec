Name: qt5gtk2
Version: 0.8
Release: 1
Summary: GTK+2.0 integration plugins for Qt5
License: GPLv2
Group: System/Configuration/Other
URL: https://bitbucket.org/trialuser02/qt5gtk2
Source: %name-%version.tar.bz2
BuildRequires: GConf2-devel gtk2-devel libinput-devel mtdev-devel libxkbcommon-devel
BuildRequires: qt5-qtbase-static qt5-qtbase-private-devel

%description
This package provides GKT+2.0 style and platform plugins for Qt 5.7 or higher.

%prep
%setup -q
echo "export QT_QPA_PLATFORMTHEME='%name'" > %name.sh
echo "setenv QT_QPA_PLATFORMTHEME '%name'" > %name.csh

%build
#export PLUGINDIR=.
%qmake_qt5 
%make_build

%install
INSTALL_ROOT=%buildroot %make_install

install -Dm 0644 %name.sh %buildroot%_sysconfdir/profile.d/%name.sh
install -Dm 0644 %name.csh %buildroot%_sysconfdir/profile.d/%name.csh

%files
%doc AUTHORS ChangeLog README
%config %_sysconfdir/profile.d/%name.*sh
%_libdir/qt5/plugins/platformthemes/lib%name.so
%_libdir/qt5/plugins/styles/lib%name-style.so

%changelog
* Sun Jun 5 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuilt for Fedora
* Sun Aug 14 2016 Hihin Ruslan <ruslandh@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
