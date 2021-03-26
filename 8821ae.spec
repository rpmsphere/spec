%global debug_package %{nil}
%global kversion %(uname -r)

Name:    8821ae
Version: 4.3.14
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
Source0: rtl8821AE_linux_v4.3.14_15494.20151026_BTCOEX20150128-51.tar.gz
Source1: 8821ae-readme.txt
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel
Patch0: rtl8821ae-timer.patch

%description
Linux kernel driver for 801.11ac Wireless Combo PCIe Adapter:
ZQ802XRACB.

%package kmod
Summary: Kernel module for Realtek 8821ae chips.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is the Realtek 802.11ac (rtl8821ae) driver.

%prep
%setup -q -n rtl8821AE_linux_v4.3.14_15494.20151026_BTCOEX20150128-51
%patch0 -p1
cp %{SOURCE1} readme.txt
sed -i '16i EXTRA_CFLAGS += -Wno-date-time -Wno-implicit-function-declaration -Wno-incompatible-pointer-types' Makefile
#sed -i 's|strnicmp|strncasecmp|' os_dep/linux/rtw_android.c
sed -i 's|if(_seqdump(sel, fmt, ##arg))|_seqdump(sel, fmt, ##arg)|' include/rtw_debug.h
sed -i 's|\([^_]\)file_path|\1rtl_file_path|' include/hal_com.h hal/hal_com.c
sed -i 's|\([^_]\)file_path|\1rtl_file_path|' hal/hal_btcoex.c hal/hal_com_phycfg.c
sed -i 's|padapter->pnetdev->trans_start = jiffies;|netif_trans_update(padapter->pnetdev);|' hal/rtl8812a/pci/pci_ops_linux.c
sed -i 's|get_ds()|KERNEL_DS|' os_dep/osdep_service.c
sed -i 's|VERIFY_READ, priv_cmd.buf, priv_cmd.total_len|priv_cmd.buf, priv_cmd.total_len|' os_dep/linux/rtw_android.c
sed -i 's|i.86/i386|aarch64/arm64|' Makefile

%build
make

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless
install -p -m 644 8821ae.ko %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless
mkdir -p %{buildroot}/etc/modprobe.d
echo blacklist rtl8821ae > %{buildroot}/etc/modprobe.d/blacklist-8821ae.conf

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
rm -rf %{buildroot}

%files kmod
%doc readme.txt
/lib/modules/%{kversion}/kernel/drivers/net/wireless/8821ae.ko
/etc/modprobe.d/blacklist-8821ae.conf

%changelog
* Thu May 26 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 4.3.14
- Initial package
