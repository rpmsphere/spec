%global debug_package %{nil}
%global kversion %(uname -r)

Name:    88x2bu
Version: 5.8.7.1
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
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 5.8.7.1
- Rebuild for Fedora
