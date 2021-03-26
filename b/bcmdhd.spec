%global debug_package %{nil}
%global kversion %(uname -r)

Name:    bcmdhd
Version: 1.363.59.144
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
Source0: bcmdhd.1.363.59.144.x.cn.tgz
Source1: AP12356_4.2.tgz
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel
BuildRequires:  elfutils-libelf-devel

%description
Linux kernel for Broadcom FullMAC Wireless Adapter:
Ampak AP12356.

%package kmod
Summary: Kernel module for Broadcom FullMAC chipset.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is the Broadcom Dongle Host Driver.

%prep
%setup -q -n bcmdhd.1.363.59.144.x.cn -a 1
sed -i -e 's|#CONFIG_BCMDHD |CONFIG_BCMDHD |' -e 's|#CONFIG_BCMDHD_PCIE |CONFIG_BCMDHD_PCIE |' Makefile
sed -i 's|drivers/net/wireless/bcmdhd|$(M)|g' Makefile

%build
make -C /lib/modules/%{kversion}/build M=$PWD

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless/
install -p -m 644 *.ko %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless/
mkdir -p %{buildroot}/lib/firmware/brcm
cp AP12356_4.2/Wi-Fi/* %{buildroot}/lib/firmware/brcm
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d
cat > %{buildroot}%{_sysconfdir}/modprobe.d/%{name}.conf <<EOF
blacklist brcmfmac
options bcmdhd firmware_path=/lib/firmware/brcm/fw_bcm4356a2_pcie_ag.bin
options bcmdhd nvram_path=/lib/firmware/brcm/nvram_ap12356.txt
EOF

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
%{__rm} -rf %{buildroot}

%files kmod
/lib/modules/%{kversion}/kernel/drivers/net/wireless/*.ko
/lib/firmware/brcm/*
%{_sysconfdir}/modprobe.d/%{name}.conf

%changelog
* Tue Dec 26 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.363.59.144
- Initial package
