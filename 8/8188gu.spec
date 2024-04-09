%global debug_package %{nil}
%global kversion %(uname -r)

Name:    8188gu
Version: 2023.01.12
Release: 1
Group:   System Environment/Kernel
License: GPLv2
URL: https://github.com/McMCCRU/rtl8188gu
Summary: RTL8188GU kernel module
Source0: rtl8188gu-master.zip
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel

%description
Linux kernel driver for 801.11ac USB Wireless Adapter:

%package kmod
Summary: Kernel module for Realtek 8188gu chips.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is the Realtek 802.11ac (rtl8188gu) driver.

%prep
%setup -q -n rtl8188gu-master
#sed -i 's|if (rtw_napi_gro_receive(&padapter->napi, pskb) != GRO_DROP)|rtw_napi_gro_receive(\&padapter->napi, pskb);|' os_dep/linux/recv_linux.c
sed -i '398s|, 0|, 0, false|' os_dep/linux/ioctl_cfg80211.c

%build
make

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless
install -p -m 644 8188gu.ko %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
rm -rf %{buildroot}

%files kmod
%doc README.md
/lib/modules/%{kversion}/kernel/drivers/net/wireless/8188gu.ko

%changelog
* Thu Nov 30 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2023.01.12
- Rebuilt for Fedora
