%global module_name nwfermi
%global kversion %(uname -r)


Name:		%{module_name}
Version:	0.4.2
Release:	24.1
Summary:	Kernel Driver for the NextWindow Touch Screen
License:	GPL
URL:		http://www.fusionnetwork.us/index.php/articles/linux-tutorials/hp-touchsmart-300-touchscreen-linux-nextwindow-working/
Source:		%module_name-%{version}.tar.bz2
Group:		System/Kernel and hardware
BuildRequires:	kernel, kernel-devel
BuildRequires:  elfutils-libelf-devel

%description
Kernel Driver for USB touchscreen chipset, Nextwindow Fermi touchscreen driver.

%package kmod
Summary:        Driver for the NextWindow Touch Screen
Requires:       kernel = %(uname -r|sed 's/-.*//')

%description kmod
Kernel Driver for USB touchscreen chipset, Nextwindow Fermi touchscreen driver.

%prep
%setup -q
sed -i -e '21i #include <linux/sched.h>' -e '246,247d' -e '/err(/d' nw-fermi.c
sed -i 's|copy_to_user|raw_copy_to_user|' nw-fermi.c

%build
make -C /lib/modules/%{kversion}/build M=$PWD modules

%install
install -Dpm744 nw-fermi.ko $RPM_BUILD_ROOT/lib/modules/%{kversion}/kernel/drivers/input/touchscreen/nw-fermi.ko
install -Dm755 40-nw-fermi.rules $RPM_BUILD_ROOT/etc/udev/rules.d/40-nw-fermi.rules

%post kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%postun kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%clean
rm -rf $RPM_BUILD_ROOT

%files kmod
/lib/modules/%{kversion}/kernel/drivers/input/touchscreen/nw-fermi.ko
/etc/udev/rules.d/40-nw-fermi.rules

%changelog
* Sun Oct 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuilt for Fedora
* Fri Jan 07 2011 Antoine Ginies <aginies@mandriva.com> 0.4.2-1mdv2011.0
+ Revision: 629590
- import dkms-nwfermi
