%global debug_package %{nil}
%global kversion %(uname -r)

Name:    8192eu
Version: 4.4.x
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
Source0: rtl8192eu-linux-driver-realtek-4.4.x.zip
URL: https://github.com/Mange/rtl8192eu-linux-driver
BuildRequires:  gcc make
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel

%description
Linux kernel driver for the rtl%{name} chipset for wireless adapter:
D-Link DWA-131 rev E1, Rosewill RNX-N180UBE v2 N300, StarTech USB300WN2X2C,
TP-Link TL-WN823N.

%package kmod
Summary: Kernel module for Realtek %{name} chips.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is the Realtek 802.11bgn (rtl%{name}) driver.

%prep
%setup -q -n rtl%{name}-linux-driver-realtek-%{version}
#sed -i 's|VERIFY_READ, priv_cmd.buf, priv_cmd.total_len|priv_cmd.buf, priv_cmd.total_len|' os_dep/linux/rtw_android.c
sed -i 's|i.86/i386|aarch64/arm64|' Makefile
#sed -i 's|cfg80211_ch_switch_started_notify(adapter->pnetdev, &chdef, 0);|cfg80211_ch_switch_started_notify(adapter->pnetdev, \&chdef, 0, 0);|' os_dep/linux/ioctl_cfg80211.c

%build
make

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless
install -p -m 644 %{name}.ko %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless
mkdir -p %{buildroot}/etc/modprobe.d
echo blacklist rtl8xxxu > %{buildroot}/etc/modprobe.d/blacklist-%{name}.conf

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
rm -rf %{buildroot}

%files kmod
%doc README.md
/lib/modules/%{kversion}/kernel/drivers/net/wireless/%{name}.ko
/etc/modprobe.d/blacklist-%{name}.conf

%changelog
* Sun Sep 4 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 4.4.x
- Rebuild for Fedora
