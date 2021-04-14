%undefine _debugsource_packages

Name:           pam_dbus_launch
BuildRequires:  gcc-c++ pam-devel libselinux-devel cmake glib2-devel
License:        GPLv3
Group:          System/Libraries
Summary:        PAM module to launch dbus on login
Version:        0.1
Release:        1264178.1
Source:         %{name}.tar.bz2
URL:            http://code.confuego.org/index.php/p/pamdbuslaunch/

%description
This PAM module launches D-Bus on session start.
Required by pam_kwallet.

%prep
%setup -q -n %{name}

%build
cmake .
make

%install
install -D pam_dbus_launch.so $RPM_BUILD_ROOT/%{_lib}/security/pam_dbus_launch.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
/%{_lib}/security/pam_dbus_launch.so

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Mon Nov 14 2011 admin@eregion.de
-  0.1: initial package
