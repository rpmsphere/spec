%global debug_package %{nil}
%global kversion %(uname -r)

Name:    88XXau
Version: 5.6.4.2
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
URL:     https://github.com/aircrack-ng/rtl8812au/
Source0: https://github.com/aircrack-ng/rtl8812au/archive/v%{version}.zip#/rtl8812au-%{version}.zip
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel

%description
Linux kernel driver for 801.11ac Wireless Dual-Band USB Adapter:
AC1200UBE, EW-7822UAC, WUSB6300, TEW-805UB, DWA-171, DWA-182 Rev C.

%package kmod
Summary: Kernel module for Realtek 8812au, 8811au, 8821au chips.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is the Realtek 802.11ac (rtl8812au) driver.

%prep
%setup -q -n rtl8812au-%{version}
#sed -i '16i EXTRA_CFLAGS += -Wno-date-time -Wno-incompatible-pointer-types' Makefile
#sed -i 's|strnicmp|strncasecmp|' os_dep/linux/rtw_android.c
#sed -i 's|if(_seqdump(sel, fmt, ##arg))|_seqdump(sel, fmt, ##arg)|' include/rtw_debug.h
#sed -i 's|\([^_]\)file_path|\1rtl_file_path|' hal/hal_com_phycfg.c
#sed -i 's|i.86/i386|aarch64/arm64|' Makefile

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
%doc LICENSE README.md ReleaseNotes.pdf
/lib/modules/%{kversion}/kernel/drivers/net/wireless/%{name}.ko

%changelog
* Sun Sep 11 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 5.6.4.2
- Rebuild for Fedora
