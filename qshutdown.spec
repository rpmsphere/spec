%global debug_package %{nil}

Name:           qshutdown
Version:        1.7.3.git
Release:        4.1
Summary:        Timebased shutdown/reboot/suspend/hibernate
License:        GPL-3.0
Group:          System/X11/Utilities
Url:            https://github.com/hakaishi/shutdown-qapps
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  desktop-file-utils

%description
Qt program to shutdown/reboot/suspend/hibernate the system
qshutdown is a Qt program to shutdown/reboot/suspend/hibernate the
computer at a given time or after a certain number of minutes. It shows
the time until the corresponding request is send to either the Gnome- or
KDE-session-manager, to HAL or to DeviceKit and if none of these works
the command 'sudo shutdown -P now' is used. This program may be useful
for people who want to work with the computer only for a certain time.

%package -n qprogram-starter
Summary:        Starting commands and programs on a certain time
Group:          System/X11/Utilities

%description -n qprogram-starter
Qt program to start programs or commands
qprogram-starter is a Qt program to start programs or commands. You can
set a time or date when the processes should start, log error output
and normal output each in a file. After the processes are finished
qprogram-starter shows a "finished" message box, or if you want it can
quit or shutdown the system.

%prep
%setup -q

%build
lrelease-qt5 %{name}/%{name}.pro
lrelease-qt5 qprogram-starter/qprogram-starter.pro
qmake-qt5
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}
install -Dm 0644 debian/%{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
install -Dm 0644 debian/qprogram-starter.1 %{buildroot}/%{_mandir}/man1/qprogram-starter.1

%files
%doc %{name}/{COPYING,NEWS,README}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/red_glasses*
%{_mandir}/man1/%{name}.1.*

%files -n qprogram-starter
%doc qprogram-starter/{COPYING,NEWS,README}
%{_bindir}/qprogram-starter
%{_datadir}/pixmaps/qprogram-starter.xpm
%{_datadir}/applications/qprogram-starter.desktop
%{_mandir}/man1/qprogram-starter.1.*
%{_datadir}/qprogram-starter

%changelog
* Thu Apr 27 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7.3.git
- Rebuild for Fedora
* Sat Feb  4 2017 and.november@opensuse.org
- initial package (version 1.7.3) for openSUSE
