%global debug_package %{nil}
%global kversion %(uname -r)

Name:    pl2303
Version: 5.2
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
URL:     https://github.com/torvalds/linux/blob/master/drivers/usb/serial
Source0: %{name}.zip
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel
BuildRequires:  elfutils-libelf-devel

%description
Linux kernel driver for Prolific PL2303 USB to serial adaptor.

%package kmod
Summary: Kernel module for Prolific PL2303 USB to serial adaptor
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
Updated driver for Prolific PL2303 USB to serial adaptor adding
new PID to support PL2303HXN.

%prep
%setup -q -n %{name}

%build
make

%install
mkdir -p %{buildroot}/usr/lib/modules/%{kversion}/updates
install -p -m 644 *.ko %{buildroot}/usr/lib/modules/%{kversion}/updates
#mkdir -p %{buildroot}/usr/lib/modules-load.d
#echo %{name} > %{buildroot}/usr/lib/modules-load.d/%{name}.conf

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
rm -rf %{buildroot}

%files kmod
%doc description
/usr/lib/modules/%{kversion}/updates/%{name}.ko
#/usr/lib/modules-load.d/%{name}.conf

%changelog
* Tue Aug 13 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 5.2
- Initial package
