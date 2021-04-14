%undefine _debugsource_packages

Name:               qomodoro
Version:            0.0.99+0.1rc1
%define pkg_version 0.1-rc1
Release:            7.4
Summary:            Cross-Platform Pomodoro Timer
Source:             http://prdownloads.sourceforge.net/qomodoro/qomodoro-%{pkg_version}-src.tar.bz2
Source1:            qomodoro.desktop
Source2:            qomodoro.png
URL:                http://sourceforge.net/p/qomodoro/home/
Group:              Productivity/Office/Organizers
License:            BSD3c
BuildRequires:      libpng-devel
BuildRequires:      qt4-devel
BuildRequires:      phonon-devel
BuildRequires:      gcc-c++
BuildRequires:      gcc make glibc-devel pkgconfig
BuildRequires:      autoconf automake libtool

%description
qomodoro is cross-platform pomodoro timer written in C++ using Qt4. To learn
more about the Pomodoro technique: http://www.pomodorotechnique.com/

Easy to use:
* Left click to show/hide the timer.
* Middle click to quickly start/stop pomodoro.
* Right click to show context menu.

Features:
* Collects statistics on started and completed pomodoros.
* Export statistics to csv.
* Change Skype status to 'Do Not Disturb' on pomodoro start and back to
* "Online'. (Unix only)

%prep
%setup -q -n "qomodoro-%{pkg_version}"

%build
qmake-qt4 QT_CXXFLAGS="%{optflags}"
%__make %{?jobs:-j%{jobs}} STRIP=/bin/true

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m0755 qomodoro "$RPM_BUILD_ROOT%{_bindir}/qomodoro"
%__install -D -m0644 "%{SOURCE1}" "$RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop"
%__install -D -m0644 "%{SOURCE2}" "$RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc LICENSE
%{_bindir}/qomodoro
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.99+0.1rc1
- Rebuilt for Fedora
* Fri Dec 17 2010 pascal.bleser@opensuse.org
- update to 1.0rc1:
  * introduceds basic configurable options and improved the look of the timer
* Mon Nov 29 2010 pascal.bleser@opensuse.org
- initial package (0.0.99+0.1beta1 / 0.1-beta1)
