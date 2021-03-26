%global debug_package %{nil}
%global kversion %(uname -r)

Name:    smscufx
Version: 4.18
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
URL:     https://github.com/torvalds/linux/blob/master/drivers/video/fbdev
Source0: %{name}.tar.bz2
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel

%description
Linux kernel driver for SMSC UFX USB Framebuffer.

%package kmod
Summary: Kernel module for DisplayLink USB devices.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is a kernel framebuffer driver for SMSC UFX USB devices.
Supports fbdev clients like xf86-video-fbdev, kdrive, fbi, and
mplayer -vo fbdev. Supports all USB 2.0 era SMSC UFX devices.

%prep
%setup -q -n %{name}

%build
make

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/extra
install -p -m 644 *.ko %{buildroot}/lib/modules/%{kversion}/extra

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
%{__rm} -rf %{buildroot}

%files kmod
%doc description
/lib/modules/%{kversion}/extra/*.ko

%changelog
* Fri Sep 14 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 4.18
- Initial package
