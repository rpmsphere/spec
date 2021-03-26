%define kversion %(uname -r)

Name:    mt7662u
Version: 20170426
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
#URL:     https://github.com/jurobystricky/Netgear-A6210
URL:     https://github.com/genodeftest/Netgear-A6210/tree/port-to-4.14
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel
Source0:  Netgear-A6210-master.zip
Patch0:   Netgear-A6210.timer.patch

%description
Kernel module for RaLink wireless USB series network adapters:
SparkLAN WUBM-273ACN, Netgear A6210, Netgear AC1200,
ASUS USB-AC55, ASUS USB-N53, EDUP EP-AC1601.

%package kmod
Summary: Kernel module for RaLink wireless USB series network adapters
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This package provides the %{name} kernel module(s) for the
RaLink mt7662u/mt7632u/mt7612u wireless USB series network adapters.
It is built to depend upon the specific ABI provided by a range of releases
of the same variant of the Linux kernel and not on any one specific build.

%prep
%setup -q -n Netgear-A6210-master
%patch0 -p1
sed -i 's|VERIFY_READ, wrqin->u.data.pointer, wrqin->u.data.length|wrqin->u.data.pointer, wrqin->u.data.length|' os/linux/sta_ioctl.c
sed -i 's|get_ds()|KERNEL_DS|' os/linux/rt_linux.c

%build
make

%install
install -d %{buildroot}/lib/modules/%{kversion}/extra/%{name}/
install os/linux/mt7662u_sta.ko %{buildroot}/lib/modules/%{kversion}/extra/%{name}/
install -d %{buildroot}%{_sysconfdir}/Wireless/RT2870STA/
install RT2870STA.dat %{buildroot}%{_sysconfdir}/Wireless/RT2870STA/

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
%{__rm} -rf %{buildroot}

%files kmod
%doc *.txt README_STA_usb
/lib/modules/%{kversion}/extra/%{name}
%{_sysconfdir}/Wireless/RT2870STA

%changelog
* Wed Mar 14 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20170426
- Rebuild for Fedora
