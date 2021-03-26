%global debug_package %{nil}
%global kversion %(uname -r)

Name:    udlfb
Version: 0.4
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
URL:     http://plugable.com/category/project/udlfb
Source0: %{name}.tar.bz2
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel

%description
Linux kernel driver for Displaylink USB Framebuffer.

%package kmod
Summary: Kernel module for DisplayLink USB devices.
Requires: kernel = %(uname -r|sed 's/-.*//')

%description kmod
This is a kernel framebuffer driver for DisplayLink USB devices.
Supports fbdev clients like xf86-video-fbdev, kdrive, fbi, and
mplayer -vo fbdev. Supports all USB 2.0 era DisplayLink devices.

%prep
%setup -q -n %{name}
sed -i '18i #define VM_RESERVED (VM_DONTEXPAND | VM_DONTDUMP)' udlfb.c
sed -i 's|\berr(|pr_err(|' udlfb.c
echo "blacklist udl" > blacklist-%{name}.conf

%build
make

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/extra
install -p -m 644 *.ko %{buildroot}/lib/modules/%{kversion}/extra
#make_install
install -Dm644 blacklist-%{name}.conf %{buildroot}%{_prefix}/lib/modprobe.d/blacklist-%{name}.conf

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
%{__rm} -rf %{buildroot}

%files kmod
%doc description
/lib/modules/%{kversion}/extra/*.ko
/usr/lib/modprobe.d/blacklist-%{name}.conf

%changelog
* Thu May 21 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Initial package
