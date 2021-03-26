%global _firmwarepath   /usr/lib/firmware
%global debug_package %{nil}
%define _binaries_in_noarch_packages_terminate_build 0

Name:		wcn36xx-firmware
Version:	1032.1.1
Release:	1
Summary:	Firmware for the Qualcomm wcn36xx devices
License:	Redistributable, no modification permitted
URL:		https://www.96boards.org/
Source0:	http://builds.96boards.org/releases/dragonboard410c/qualcomm/firmware/linux-board-support-package-r1032.1.1.zip
BuildArch:      noarch
BuildRequires:	mtools

%description
Firmware for the Qualcomm wcn36xx devices including WiFi,
Bluetooth and GPS.

%prep
%setup -q -n linux-board-support-package-r%{version}

%build
MTOOLS_SKIP_CHECK=1 mcopy -i bootloaders-linux/NON-HLOS.bin ::image/modem.* ::image/mba.mbn ::image/wcnss.* proprietary-linux/

%install
mkdir -p $RPM_BUILD_ROOT/%{_firmwarepath}
install -p proprietary-linux/mba.mbn $RPM_BUILD_ROOT/%{_firmwarepath}
install -p proprietary-linux/modem.* $RPM_BUILD_ROOT/%{_firmwarepath}
install -p proprietary-linux/wcnss.* $RPM_BUILD_ROOT/%{_firmwarepath}
cp -rp proprietary-linux/wlan $RPM_BUILD_ROOT/%{_firmwarepath}

%files
%license LICENSE
%{_firmwarepath}/mba.mbn
%{_firmwarepath}/modem.*
%{_firmwarepath}/wcnss.*
%{_firmwarepath}/wlan/

%changelog
* Thu Nov 23 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1032.1.1-1
- Initial package
