%define kversion %(uname -r)

Name:    rt5572
Version: 2.6.1.3
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
URL:     http://www.mediatek.com/en/downloads/
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel
Source0:  DPO_RT5572_LinuxSTA_2.6.1.3_SparkLAN.tar.bz2
Source1:  GPL-v2.0.txt
Patch0:   rt5572sta_fix_64bit.patch

%description
Kernel module for RaLink wireless USB series network adapters.

%package kmod
Summary: Kernel module for RaLink wireless USB series network adapters
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This package provides the %{name} kernel module(s) for the
RaLink RT8070/RT3070/RT3370/RT3572/RT5370/RT5372/RT5572 wireless USB series network adapters.
It is built to depend upon the specific ABI provided by a range of releases
of the same variant of the Linux kernel and not on any one specific build.

%prep
%setup -q -n DPO_RT5572_LinuxSTA_2.6.1.3_SparkLAN
%patch0 -p1
cp %{SOURCE1} .
sed -i -e 's|(.*tftpboot$)|#$1|g' Makefile
sed -i -e 's|HAS_WPA_SUPPLICANT=n|HAS_WPA_SUPPLICANT=y|g' \
       -e 's|HAS_NATIVE_WPA_SUPPLICANT_SUPPORT=n|HAS_NATIVE_WPA_SUPPLICANT_SUPPORT=y|g' \
       os/linux/config.mk
sed -i 's|-Wno-trigraphs|-Wno-trigraphs -Wno-incompatible-pointer-types|' os/linux/config.mk
sed -i -e 's|VERIFY_WRITE, wrqin->u.data.pointer|wrqin->u.data.pointer|' -e 's|VERIFY_READ, wrqin->u.data.pointer|wrqin->u.data.pointer|' os/linux/sta_ioctl.c
sed -i 's|memcpy(extra, &addr|memcpy(extra, addr|' os/linux/sta_ioctl.c
sed -i -e '130,132d' -e '133i timer_setup(pTimer,function,(unsigned long)data);' os/linux/rt_linux.c

%build
make LINUX_SRC=%{_usrsrc}/kernels/%{kversion}

%install
install -d %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless/
install os/linux/rt5572sta.ko %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/wireless/
install -d %{buildroot}%{_sysconfdir}/Wireless/RT2870STA/
install RT2870STA.dat %{buildroot}%{_sysconfdir}/Wireless/RT2870STA/
install RT2870STACard.dat %{buildroot}%{_sysconfdir}/Wireless/RT2870STA/
install -d %{buildroot}%{_sysconfdir}/modprobe.d/
echo blacklist rt2800usb > %{buildroot}%{_sysconfdir}/modprobe.d/blacklist-%{name}.conf

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
%{__rm} -rf %{buildroot}

%files kmod
%doc *.txt README_STA_usb
/lib/modules/%{kversion}/kernel/drivers/net/wireless/
%{_sysconfdir}/Wireless/RT2870STA
%{_sysconfdir}/modprobe.d/blacklist-%{name}.conf

%changelog
* Wed Jan 27 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.1.3-1
- Rebuild

* Tue Mar 25 2014 Philip J Perry <phil@elrepo.org> - 2.6.1.3-1
- Port to el6.

* Mon Mar 24 2014 Maksim Gefke <ds_shadof@quickpay.ru> - 2.6.1.3-1
- Initial build of the kmod package.
