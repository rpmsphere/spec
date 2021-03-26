%global debug_package %{nil}
%global kversion %(uname -r)

Name:    it87_wdt
Version: 4.20
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
URL:     https://github.com/torvalds/linux/blob/master/drivers/watchdog
Source0: %{name}.tar.bz2
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel

%description
Linux kernel driver for watchdog on IT87XX SIO chips.

%package kmod
Summary: Kernel module for IT87XX Watchdog Timer.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is the driver for the hardware watchdog on the ITE IT8607,
IT8620, IT8622, IT8625, IT8628, IT8655, IT8665, IT8686, IT8702,
IT8712, IT8716, IT8718, IT8720, IT8721, IT8726, IT8728, IT8783
and IT8786 Super I/O chips.

This watchdog simply watches your kernel to make sure it doesn't
freeze, and if it does, it reboots your computer after a certain
amount of time.

%prep
%setup -q -n %{name}

%build
make

%install
mkdir -p %{buildroot}/usr/lib/modules/%{kversion}/updates
install -p -m 644 *.ko %{buildroot}/usr/lib/modules/%{kversion}/updates
mkdir -p %{buildroot}/usr/lib/modules-load.d
echo %{name} > %{buildroot}/usr/lib/modules-load.d/%{name}.conf

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
rm -rf %{buildroot}

%files kmod
%doc description
/usr/lib/modules/%{kversion}/updates/%{name}.ko
/usr/lib/modules-load.d/%{name}.conf

%changelog
* Fri Jan 18 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.20
- Initial package
