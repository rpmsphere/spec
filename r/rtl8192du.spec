%global debug_package %{nil}
%global kversion %(uname -r)

Name:    rtl8192du
Version: 4.13
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
URL:     https://github.com/lwfinger/rtl8192du
Source0: rtl8192du-master.zip
Source1: rtl8192du-readme.txt
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel-uname-r

%description
Linux kernel driver for 802.11n Wireless Dual-Band USB Adapter:
TOTOLINK N500UM.

%package kmod
Summary: Kernel module for Realtek 8192du chips.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is the Realtek 802.11n (rtl8192du) driver.

%prep
%setup -q -n rtl8192du-master
cp %{SOURCE1} readme.txt
sed -i -e '/depmod -a/d' -e 's|ARCH=$(ARCH) CROSS_COMPILE=$(CROSS_COMPILE)||' Makefile
#sed -i 's|0, GFP_ATOMIC|0, true, GFP_ATOMIC|' os_dep/ioctl_cfg80211.c
#sed -i 's|IEEE80211_BAND_|NL80211_BAND_|g' os_dep/ioctl_cfg80211.c

%build
make

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless
install -p -m 644 *.ko %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless
mkdir -p %{buildroot}/lib/firmware/rtlwifi
install -p -m 644 *.bin %{buildroot}/lib/firmware/rtlwifi
#make_install

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
%{__rm} -rf %{buildroot}

%files kmod
%doc readme.txt
/lib/modules/%{kversion}/kernel/drivers/net/wireless/*.ko
/lib/firmware/rtlwifi/*

%changelog
* Mon Aug 26 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 5.2
- Initial package
