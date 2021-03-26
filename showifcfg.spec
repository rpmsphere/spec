%global debug_package %{nil}

Name:       showifcfg
Summary:    Show Ifconfig Utility
Version:    0.2.0
Release:    6.1
Group:      System/GUI/Other
License:    GPLv2
URL:        http://moui.sourceforge.net
Source0:    %{name}-%{version}.tar.bz2
Source100:  showifcfg.yaml
#Requires:   geuzen-qml-utils
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig(QtCore) >= 4.7.0
BuildRequires:  pkgconfig(QtDeclarative) >= 4.7.0
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils

%description
Utility to show network configuration.

%prep
%setup -q

%build
qmake-qt4
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 0644 images/%{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -m 0644 %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications

desktop-file-install --delete-original       \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
   $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files
/usr/bin/showifcfg
/usr/share/applications/showifcfg.desktop
/usr/share/pixmaps/showifcfg.png

%changelog
* Mon Apr 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuild for Fedora
* Wed Aug 10 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.2.0
- use geuzen-qml-utils plugin instead of static .cpp
* Tue Aug  9 2011 Bernd Stramm <bernd.stramm@gmail.com> - 0.1.2
- allow editing so that copy works
- different colors, button borders
