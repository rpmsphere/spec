Name:		test-config
Version:	2015.08
Release:	1
Summary:	Configuration files in Test System
License:	Public Domain
Group:		System
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
# for intel-linux-graphics-installer
Requires:	libproxy-mozjs PackageKit
# for hwqv
Requires:       lshw inxi hdparm lcdtest monitor-edid setserial lm_sensors
Requires:       alsa-utils pulseaudio-utils glx-utils pcsc-tools
# for wakethemup
Requires:       wol iputils

%description
Configuration for various models and scripts for quality control.

%prep
%setup -q

%build

%install
%make_install

%files
%doc README.*
%{_bindir}/*
%{_datadir}/%{name}
%{_sysconfdir}/udev/rules.d/90-usbhid-wakeup.rules
%{_sysconfdir}/X11/xinit/xinitrc.d/xset.sh

%changelog
* Tue Aug 04 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2015.08
- Inital package
