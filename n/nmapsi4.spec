Name:          nmapsi4
Version:       0.4.1
Release:       4.1
Summary:       Qt4 nmap interface
Group:         Graphical Desktop/Applications/Networking
URL:           https://www.nmapsi4.org/
Source:        https://nmapsi4.googlecode.com/files/nmapsi4-%{version}.tar.bz2
License:       GPL
BuildRequires: libpng-devel
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: qt-webkit-devel
Requires:      nmap
Requires:      bind-utils

%description
NmapSi4 is a complete Qt4-based Gui with the design goals to provide
a complete nmap interface for users, in order to management all options
of this powerful security net scanner.

%prep
%setup -q
#sed -i '1i #include <unistd.h>' nmapsi4/mainwin.cpp nmapsi4/core/toolsUI.cpp nmapsi4/preference/profilemain.cpp nmapsi4/core/profileSession.cpp
sed -i '42,43d' CMakeLists.txt

%build
%cmake .
%cmake_build

%install
rm -rf $RPM_BUILD_ROOT
%cmake_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/nmapsi4*
%{_datadir}/applications/kde4/nmapsi4*.desktop
%{_datadir}/icons/hicolor/*/apps/nmapsi4.png
%{_datadir}/nmapsi4
%{_datadir}/dbus-1/interfaces/org.nmapsi4.Nmapsi4.xml
%doc AUTHORS COPYING NEWS README TODO

%changelog
* Thu Jul 09 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuilt for Fedora
* Mon Nov 29 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 0.2-1mamba
- package created by autospec
