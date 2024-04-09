%define kver %(uname -r)

Name:		    8812au
Version:	    6.1
Release:	    1
Summary:	    Realtek 8812AU/8821AU USB WiFi driver
Group:		    System Environment/Kernel
License:	    GPLv2
URL:		    https://github.com/lwfinger/rtl8812au
#Source0:	    https://github.com/abperiasamy/rtl8812AU_8821AU_linux/archive/rtl8812AU_8821AU_linux-master.zip
Source0:            rtl8812au-master.zip
#Source11:           rtl8812au-kmod-kmodtool-excludekernel-filterfile
BuildRequires:      gcc, kernel-devel

%description
for AC1200 (801.11ac) Wireless Dual-Band USB Adapter
This code is base on version 4.3.14 from https://github.com/diederikdehaas/rtl8812AU

%package kmod
Summary: Kernel module for Realtek 8812AU/8821AU
Requires: kernel = %kver

%description kmod
Realtek 8812AU/8821AU USB WiFi driver.
Known Supported Devices:
* COMFAST 1200Mbps USB Wireless Adapter(Model: CF-912AC)
* TP-LINK AC1200 Wireless Dual Band USB Adapter(Model: Archer-T4U)
* TP-LINK AC600 Wireless Dual Band USB Adapter(Model: Archer-T2U Nano)

%prep
#setup -q -n rtl8812AU_8821AU_linux-master
%setup -q -n rtl8812au-master
#sed -i '236,240d' include/rtw_security.h

%build
make -C /usr/src/kernels/%{kver} M=`pwd` modules

%install
rm -rf ${RPM_BUILD_ROOT}
install -Dm 744 %{name}.ko %{buildroot}/lib/modules/%{kver}/updates/%{name}/%{name}.ko

%post kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%postun kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%clean
rm -rf $RPM_BUILD_ROOT

%files kmod
%doc LICENSE *.md
/lib/modules/%{kver}/updates/%{name}/%{name}.ko

%changelog
* Sun Mar 24 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 6.1
- Rebuilt for Fedora
* Tue May 30 2017 Alexei Panov <me AT elemc DOT name> 4.3.14-2
-  Fixed obsolete-name parameter
* Tue May 30 2017 Alexei Panov <me AT elemc DOT name> 4.3.14-1
-  Initial build
