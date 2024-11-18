%undefine _debugsource_packages

Name:     arduide
Summary:  Qt-based IDE for Arduino
Version:  1.0
Release:  10.1
Group:    Development/Tools
License:  GPLv2+
URL:      https://www.mupuf.org/project/arduide.html
Source0:  arduide-%version.beta1.tar.bz2
BuildRequires: qt4-devel
BuildRequires: cmake
BuildRequires: qtwebkit-devel
BuildRequires: grantlee-devel
BuildRequires: qscintilla-devel

%description
ArduIDE is a Qt-based IDE for the open-source Arduino
electronics prototyping platform.

%prep
%setup -q -n %name
sed -i -e 119d -e 125,133d gui/FirstTimeWizard.cpp
sed -i '322s|return .*|return true;|' utils/hexview/QHexView.cpp
sed -i '32i #include <cstdint>' gui/Editor.h

%build
%cmake -DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=/usr -DUSE_FHS_PATHS=ON .
%cmake_build

%install
%cmake_install
mv %{buildroot}%{_datadir}/icons %{buildroot}%{_datadir}/pixmaps

%files 
%_bindir/arduino-ide
%_datadir/applications/arduino-ide.desktop
%_datadir/arduino-ide
%_datadir/pixmaps/arduide.png

%changelog
* Sun May 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Fri Jan 11 2013 umeabot <umeabot> 1.0-0.beta1.4.mga3
+ Revision: 346023
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu Jan 03 2013 mikala <mikala> 1.0-0.beta1.3.mga3
+ Revision: 338071
- Rebuild for new grantlee
* Tue Dec 11 2012 matteo <matteo> 1.0-0.beta1.2.mga3
+ Revision: 329759
- rebuilt against new lib qscintilla
* Thu Oct 18 2012 neoclust <neoclust> 1.0-0.beta1.1.mga3
+ Revision: 307908
- imported package arduide
