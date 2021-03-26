%define kmod_name r8187
%define kver %(uname -r)

Summary: Realtek RTL8187/8187B Wireless LAN NIC.
Name: %{kmod_name}
Version: 1.24
Release: 3
Vendor: Realtek
URL: http://rtl-wifi.sourceforge.net/
License: GPL
Group: System/Kernel and hardware
Source0: http://www.datanorth.net/~cuervo/rtl8187b/rtl8187b-unmodified-realtek.tar.gz
Patch0: rtl8187b-fixes.patch
Patch1: rtl8187b-8197.patch
BuildRequires: gcc, kernel-devel
Requires: kernel = %kver

%description
This is the Linux device driver released for RealTek RTL8187/8187B Wireless LAN NIC.

%package kmod
Summary: Realtek RTL8187/8187B Wireless LAN NIC.
##Release: %(echo %{kver} | tr - _).3

%description kmod
This is the Linux device driver released for RealTek RTL8187/8187B Wireless LAN NIC.

%prep
%setup -q -n rtl8187B_linux_24.6.1024.0822.2007
%patch0 -p1 -b .fixes
%patch1 -p1 -b .8197
sed -i 's|asm/semaphore.h|linux/semaphore.h|' rtl8187/r8187.h

%build
cd rtl8187
%__make modules

%install
install -Dm 744 rtl8187/r8187.ko %{buildroot}/lib/modules/%{kver}/kernel/drivers/net/r8187.ko

%post kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%postun kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%clean
rm -rf %{buildroot} 

%files kmod
/lib/modules/%{kver}/kernel/drivers/net/r8187.ko
%doc rtl8187/{readme,license,changes,install,copying,authors}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri May 30 2008 Wei-Lun Chao <bluebat@member.fsf.org> 1.24-3.ossii
- Build for M6(CentOS5)

* Sat Mar  1 2008 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.
