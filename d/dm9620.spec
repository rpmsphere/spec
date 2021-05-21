%define module_name dm9620
%global kversion %(uname -r)

Name:		%{module_name}
Version:	1.4
Release:	8.1
Summary:	A Davicom DM9620 USB Fast Ethernet driver
License:	GPL
URL:		http://www.davicom.com.tw
Source:		Linux_DM962x_3.2.tgz
Group:		System/Kernel and hardware
BuildRequires:	kernel, kernel-devel
BuildRequires:	elfutils-libelf-devel

%description
A Davicom DM9620 USB Fast Ethernet driver for Linux by Sten Wang.

%package kmod
Summary:        Kernel Driver for DM9620
Requires:       kernel = %(uname -r|sed 's/-.*//')

%description kmod
Kernel Driver for DM9620 from DAVICOM Semiconductor Inc.

%prep
%setup -q -n Linux_DM962x_3.2
sed -i -e '/usbnet_get_settings/d' -e '/usbnet_set_settings/d' dm9620.c

%build
make -C /lib/modules/%{kversion}/build M=$PWD

%install
install -Dpm744 %{name}.ko %{buildroot}/lib/modules/%{kversion}/kernel/drivers/net/usb/%{name}.ko

%post kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%postun kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files kmod
%doc *.txt
/lib/modules/*/kernel/drivers/net/usb/dm9620.ko

%changelog
* Mon Jul 21 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
