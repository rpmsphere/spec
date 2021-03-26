%define kmod_name r8180
%define kver %(uname -r)

Summary: Realtek RTL8180/8185/8187 Ethernet Controller Driver module
Name: %{kmod_name}
Version: 1023
Release: 1
Vendor: Realtek
URL: http://www.realtek.com.tw/downloads
License: GPL
Group: System/Kernel and hardware
Source: rtl8187se_linux_26-1023.1118.2008.tar.bz2
BuildRequires: gcc, kernel-devel
Requires: kernel = %kver

%description
This is the Linux device driver released for RealTek RTL8180/8185/8187,
Gigabit Ethernet controllers with PCI-Express interface.

%package kmod
Summary: Realtek RTL8180/8185/8187 Ethernet Controller Driver module
##Release: %(echo %{kver} | tr - _).1

%description kmod
This is the Linux device driver released for RealTek RTL8180/8185/8187,
Gigabit Ethernet controllers with PCI-Express interface.

%prep
%setup -q -n rtl8187se_linux_26-1023.1118.2008
#sed -i 's/^CFLAGS/EXTRA_CFLAGS/g' rtl8185/Makefile
#sed -i -e 's/proc_net/init_net.proc_net/' -e 's/SA_SHIRQ/IRQF_SHARED/' -e '/SET_MODULE_OWNER/d' rtl8185/r8180_core.c

%build
cd rtl8185
%__make modules

%install
#make install
install -Dm 744 rtl8185/r8180.ko %{buildroot}/lib/modules/%{kver}/kernel/drivers/net/r8180.ko

%post kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%postun kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%clean
rm -rf %{buildroot} 

%files kmod
/lib/modules/%{kver}/kernel/drivers/net/r8180.ko
%doc rtl8185/{readme,license,changes,install,copying,authors}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri Feb 20 2009 Wei-Lun Chao <bluebat@member.fsf.org> 1023-1.ossii
- Update to 1023

* Fri May 30 2008 Wei-Lun Chao <bluebat@member.fsf.org> 1012-1.ossii
- Build for M6(CentOS5)
