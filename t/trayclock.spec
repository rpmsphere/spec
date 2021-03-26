Name: trayclock
Summary: An analog clock for the sys-tray
Version: 0.3.7
Release: 1
License: GPL
Group: User Interface/Desktops
Source0: https://launchpad.net/trayclock/0.5/0.3.7/+download/%{name}-%{version}.tar.gz
URL: http://www.jezra.net/projects/trayclock
BuildRequires: intltool
BuildRequires: vala

%description
Trayclock is an application written in Vala that will display an analog clock
in the system tray.

%prep
%setup -q

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc AUTHORS README COPYING ChangeLog
%{_bindir}/%{name}

%changelog
* Wed Apr 26 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.7
- Rebuild for Fedora
