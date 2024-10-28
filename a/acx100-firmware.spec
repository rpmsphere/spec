Summary: Firmware for Texas Instruments ACX100 network adaptors
Name: acx100-firmware
Version: 1.9.8.b
Release: 1
License: freeware
Group: System Environment/Kernel
URL: https://acx100.sourceforge.net/wiki/Firmware
Source0: https://acx100.erley.org/acx_fw/acx100_dlink_dwl520+/fw1/WLANGEN.BIN_%{version}
Source1: https://acx100.erley.org/acx_fw/acx100usb_dlink_dwl120+/fw1/ACX100_USB.bin
BuildArch: noarch

%description
Firmware files for Texas Instruments ACX100 based wireless network adaptors,
required by the acx Linux kernel module. You might need to add some card
specific radio firmware files in addition to this packages. Please see :
https://acx100.erley.org/acx_fw/acx1xx.htm


%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/lib/firmware
%{__install} -p -m 0644 %{SOURCE0} %{buildroot}/lib/firmware/tiacx100
%{__install} -p -m 0644 %{SOURCE1} %{buildroot}/lib/firmware/tiacx100usb



%files
/lib/firmware/tiacx100
/lib/firmware/tiacx100usb

%changelog
* Mon Feb 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.1.34
- Rebuilt for Fedora
* Fri Mar 31 2006 Matthias Saou <https://freshrpms.net> 1.2.1.34-1
- Initial RPM release, based on the ipw2200-firmware spec file.
