%global __spec_install_post %{nil}
%undefine _debugsource_packages

Summary:	Backend to control your 3D printer
Name:		atcore
Version:	1.0.0
Release:	7.1
License:	GPL, LGPL
Group:		Applications/Engineering
URL:		https://atelier.kde.org/
Source:		https://download.kde.org/stable/atcore/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtcharts-devel
BuildRequires:  qt5-qtserialport-devel

%description
Atelier is an open source program that allows you to control your 3D printer.
Along with the back end, AtCore, you can calibrate, send jobs, or receive
information about the status of your printer.

%package devel
Group: Development/C++
Summary: Development files for %name
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q

%build
%cmake .
%cmake_build

%install
rm -rf $RPM_BUILD_ROOT
%cmake_install
#mkdir -p %{buildroot}%{_libdir}/qt5
#mv %{buildroot}%{_libdir}/plugins %{buildroot}/usr/mkspecs %{buildroot}%{_libdir}/qt5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README* COPYING*
%{_bindir}/AtCoreTest
%{_libdir}/libAtCore.so.*
%{_libdir}/qt5/plugins/AtCore
%{_datadir}/applications/AtCoreTest.desktop
%{_datadir}/locale/*/LC_MESSAGES/atcore_qt.qm
%{_datadir}/pixmaps/AtCoreTest.png

%files devel
%{_includedir}/AtCore
%{_libdir}/libAtCore.so
%{_libdir}/cmake/AtCore
%{_libdir}/qt5/mkspecs/modules/qt_AtCore.pri

%changelog
* Thu Aug 30 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuilt for Fedora
