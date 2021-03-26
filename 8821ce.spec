%global debug_package %{nil}
%global kversion %(uname -r)

Name:    8821ce
Version: 1.0.0git
Release: 1
Group:   System Environment/Kernel
License: GPLv2
URL: https://github.com/tomaspinho/rtl8821ce
Summary: RTL8821CE kernel module
Source0: rtl8821ce-master.zip
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel

%description
Linux kernel driver for 801.11ac Wireless Combo PCIe Adapter:

%package kmod
Summary: Kernel module for Realtek 8821ce chips.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is the Realtek 802.11ac (rtl8821ce) driver.

%prep
%setup -q -n rtl8821ce-master
sed -i 's|i.86/i386|aarch64/arm64|' Makefile

%build
PATH=$PATH:/usr/lib/dkms make

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless
install -p -m 644 8821ce.ko %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
rm -rf %{buildroot}

%files kmod
%doc README.md
/lib/modules/%{kversion}/kernel/drivers/net/wireless/8821ce.ko

%changelog
* Thu Jan 07 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0git
- Rebuild for Fedora
