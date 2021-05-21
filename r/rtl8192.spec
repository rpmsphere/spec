%define kmod_name rtl8192
%define kver %(uname -r)

Summary: Linux driver for RTL8192ce/se/de Wireless LAN NICs
Name: %{kmod_name}
Version: 0005.1230.2011
Release: 1
Group: System Environment/Kernel
License: freeware
URL: http://www.realtek.com.tw
Source0: 92ce_se_de_linux_mac80211_%{version}.tar.gz
BuildRequires: gcc, kernel-devel

%description
This is the Linux device driver released for RealTek RTL8192 Wireless LAN NICs.

%package kmod
Summary: Kernel module for RealTek RTL8191/8192 Wireless LAN NICs
Requires: kernel = %kver
Requires: %{kmod_name}-firmware
##Release: %(echo %{kver} | tr - _).1

%description kmod
Realtek Linux mac80211 based kernel module supports follwing RealTek PCIE Wireless LAN NICs:
 RTL8188CE/RTL8192CE
 RTL8191SE/RTL8192SE
 RTL8192DE

%package firmware
Summary: Firmware for RealTek RTL8191/8192 Wireless LAN NICs
BuildArch: noarch

%description firmware
Realtek Linux mac80211 based firmware supports follwing RealTek PCIE Wireless LAN NICs:
 RTL8188CE/RTL8192CE
 RTL8191SE/RTL8192SE
 RTL8192DE

%prep
%setup -q -n rtl_92ce_92se_92de_linux_mac80211_%{version}

%build
make

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}/lib/modules/%{kver}/kernel/drivers/net/wireless/rtlwifi/%{kmod_name}{se,ce,de}
install -p -m 744 rtlwifi.ko %{buildroot}/lib/modules/%{kver}/kernel/drivers/net/wireless/rtlwifi	
install -p -m 744 %{kmod_name}se/%{kmod_name}se.ko %{buildroot}/lib/modules/%{kver}/kernel/drivers/net/wireless/rtlwifi/%{kmod_name}se
install -p -m 744 %{kmod_name}ce/%{kmod_name}ce.ko %{buildroot}/lib/modules/%{kver}/kernel/drivers/net/wireless/rtlwifi/%{kmod_name}ce
install -p -m 744 %{kmod_name}de/%{kmod_name}de.ko %{buildroot}/lib/modules/%{kver}/kernel/drivers/net/wireless/rtlwifi/%{kmod_name}de
mkdir -p %{buildroot}/lib/firmware
cp -a firmware/rtlwifi %{buildroot}/lib/firmware

%post kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%postun kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%clean
%{__rm} -rf %{buildroot}

%files kmod
/lib/modules/%{kver}/kernel/drivers/net/wireless/rtlwifi/*
%doc readme

%files firmware
/lib/firmware/rtlwifi/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Thu Jan 05 2012 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
