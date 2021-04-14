%define _name dvb-usb-af9015

Summary: Firmware for Afatech AF9015 DVB-T USB Devices
Name: %{_name}-firmware
Version: 4.95.0
Release: 1
License: freeware
Group: System Environment/Kernel
URL: http://www.otit.fi/~crope/v4l-dvb/af9015/af9015_firmware_cutter/firmware_files/
Source0: http://www.otit.fi/~crope/v4l-dvb/af9015/af9015_firmware_cutter/firmware_files/%{version}/%{_name}.fw
BuildArch: noarch

%description
* From AFAdriver9015-7.7.4.1.WHQL driver
* Driver release date : 2007/11/08
* Version : v7.7.4.1
* Download: AFAdriver9015-7.7.4.1.WHQL.zip

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/lib/firmware
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}/lib/firmware/%{_name}.fw

%clean
%{__rm} -rf %{buildroot}

%files
/lib/firmware/%{_name}.fw

%changelog
* Mon Feb 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 4.95.0
- Rebuilt for Fedora
