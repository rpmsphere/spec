%global debug_package %{nil}
%global kversion %(uname -r)

Name:    8852be
Version: 1.15.6.0.2
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
Source0: rtl8852BE_WiFi_linux_v1.15.6.0.2-0-gac110bf5.20211029_SparkLAN_V1.tar.gz
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel

%description
Linux kernel driver for 801.11ax Wireless Combo PCIe Adapter:
Sparklan WNFT-238AX(BT) v2

%package kmod
Summary: Kernel module for Realtek 8852be chips.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is the Realtek 802.11ax (rtl8852be) driver.

%prep
%setup -q -n rtl8852BE_WiFi_linux_v1.15.6.0.2-0-gac110bf5.20211029_SparkLAN_V1

%build
make

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless
install -p -m644 8852be.ko %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
rm -rf %{buildroot}

%files kmod
/lib/modules/%{kversion}/kernel/drivers/net/wireless/8852be.ko

%changelog
* Sun Apr 24 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.15.6.0.2
- Initial package
