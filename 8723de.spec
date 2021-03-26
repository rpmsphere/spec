%global debug_package %{nil}
%global kversion %(uname -r)

Name:    8723de
Version: 5.1.1.8
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
Source0: %{version}_21285.20171026_COEX20170111-1414.tar.gz
URL: https://github.com/smlinux/rtl%{name}
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel

%description
Linux kernel driver for the rtl%{name} chipset for wireless adapter:

%package kmod
Summary: Kernel module for Realtek %{name} chips.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is the Realtek rtl%{name} driver.

%prep
%setup -q -n rtl%{name}
#sed -i 's|VERIFY_READ, priv_cmd.buf, priv_cmd.total_len|priv_cmd.buf, priv_cmd.total_len|' os_dep/linux/rtw_android.c
sed -i 's|i.86/i386|aarch64/arm64|' Makefile

%build
make

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless
install -p -m 644 %{name}.ko %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
rm -rf %{buildroot}

%files kmod
%doc README.md
/lib/modules/%{kversion}/kernel/drivers/net/wireless/%{name}.ko

%changelog
* Thu Jul 11 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 5.1.1.8
- Initial package
