%global debug_package %{nil}
%global kversion %(uname -r)

Name:    88x2bu
Version: 5.13.1.30
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
URL:     https://github.com/RinCat/RTL88x2BU-Linux-Driver
Source0: RTL88x2BU-Linux-Driver-master.zip
#URL:     https://github.com/cilynx/rtl88x2bu
#Source0: rtl88x2bu-5.6.1_30362.20181109_COEX20180928-6a6a.zip
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel

%description
Linux kernel driver for 801.11ac Wireless Dual-Band USB Adapter:
DWA-182 Rev D.

%package kmod
Summary: Kernel module for Realtek 8812bu, 8822b chips.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is the Realtek 802.11ac (rtl8812bu) driver.

%prep
#setup -q -n rtl88x2bu-5.6.1_30362.20181109_COEX20180928-6a6a   
%setup -q -n RTL88x2BU-Linux-Driver-master
sed -i 's|strlcpy|strncpy|' os_dep/linux/os_intfs.c
sed -i 's|usbdrv.drvwrap.driver.shutdown|usbdrv.driver.shutdown|' os_dep/linux/usb_intf.c

%build
make

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless/
install -p -m 644 %{name}.ko %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless/

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
%{__rm} -rf %{buildroot}

%files kmod
%doc README.md
/lib/modules/%{kversion}/kernel/drivers/net/wireless/%{name}.ko

%changelog
* Sun Dec 08 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 5.13.1.30
- Rebuilt for Fedora
