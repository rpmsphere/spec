%undefine _debugsource_packages

Name:       stroller
Summary:    A GPS Tracker
Version:    0.0.2
Release:    10.4
Group:      Applications/Productivity
License:    GPLv2+
URL:        https://github.com/berndhs/stroller
Source0:    stroller-%{version}.tar.bz2
Source100:  stroller.yaml
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++ qt4-devel qt-mobility-devel
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtDeclarative)
BuildRequires:  desktop-file-utils

%description
A simple GPS tracker showing where the user/device has been.

%prep
%setup -q

%build
qmake-qt4
make

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=$RPM_BUILD_ROOT install

desktop-file-install --delete-original       \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
   $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
/opt/stroller/bin/stroller
/usr/share/icons/hicolor/64x64/apps/stroller.png
/usr/share/applications/stroller.desktop

%changelog
* Mon Apr 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.2
- Rebuilt for Fedora
* Fri Aug 19 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.2 
 - start making some packaging stuff
 - tell deb packing about version
 - command line options for testing, desktop (not-phone), help, version
 - more map and some unrealistic test data
* Wed Aug 17 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.0.1
- start
