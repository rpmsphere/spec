%global debug_package %{nil}
%global kversion %(uname -r)

Name:    mos7840
Version: 3.7.0
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
URL:     https://www.asix.com.tw/
Source0: https://www.asix.com.tw/FrootAttach/driver/AX781x0_MCS78x0_Linux_Driver_v%{version}_Source.tar.bz2
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel

%description
Linux kernel driver for ASIX AX78140/AX78120/MCS7840/MCS7820/MCS7810.

%package kmod
Summary: Kernel module for ASIX USB Serial devices.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is a kernel driver for ASIX USB Serial devices.
Supports AX78140/AX78120/MCS7840/MCS7820/MCS7810.

%prep
%setup -q -n AX781x0_MCS78x0_Linux_Driver_v%{version}_Source
#sed -i 's|//MODULE_DEVICE_TABLE (usb, id_table_combined);|MODULE_DEVICE_TABLE (usb, moschip_port_id_table);|' mos7840.h
echo 'ACTION=="add", SUBSYSTEM=="usb", ATTRS{idVendor}=="9710", ATTRS{idProduct}=="7841", RUN+="/sbin/modprobe mos7840"' > 80-usb-serial.rules
sed -i 's|EXTRA_CFLAGS += |EXTRA_CFLAGS += -Wno-incompatible-pointer-types |' Makefile

%build
make

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/updates
install -p -m644 *.ko %{buildroot}/lib/modules/%{kversion}/updates
install -Dm644 80-usb-serial.rules %{buildroot}/lib/udev/rules.d/80-usb-serial.rules

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
%{__rm} -rf %{buildroot}

%files kmod
%doc README ioctl
/lib/modules/%{kversion}/updates/*.ko
/lib/udev/rules.d/80-usb-serial.rules

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.7.0
- Rebuilt for Fedora
