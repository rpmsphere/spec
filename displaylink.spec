%global debug_package %{nil}
%global kversion %(uname -r)

Name:    displaylink
Version: 0.3
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
URL:     http://libdlo.freedesktop.org/wiki/%{name}-mod
Source0: http://projects.unbit.it/downloads/%{name}-mod-%{version}.tar.gz
Source1: %{name}-txt.zip
Patch0:  kernel-2.6.18-use-vmalloc-instead-of-kzalloc.patch
BuildRequires: kernel-headers
BuildRequires: kernel-devel

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
%setup -q -n %{name} -a 1
#patch0 -p1
sed -i '2i #define VM_RESERVED (VM_DONTEXPAND | VM_DONTDUMP)' displaylink-fb.c
sed -i 's|<drm/drm_edid.h>|"drm_edid.h"|' displaylink.h
sed -i 's|\berr(|pr_err(|' displaylink-main.c
echo "blacklist udl" > blacklist-%{name}.conf

%build
make

%install
mkdir -p %{buildroot}/lib/modules/%{kversion}/extra
install -m 644 *.ko %{buildroot}/lib/modules/%{kversion}/extra
#make_install
install -Dm644 blacklist-%{name}.conf %{buildroot}%{_prefix}/lib/modprobe.d/blacklist-%{name}.conf

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
%{__rm} -rf %{buildroot}

%files kmod
%doc COPYING README
/lib/modules/%{kversion}/extra/*.ko
/usr/lib/modprobe.d/blacklist-%{name}.conf

%changelog
* Tue May 26 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Initial package

* Thu Sep 09 2010 Alexander Todorov <atodorov@NO_SPAM.otb.bg> - 2.2.0.3-2
- define the dist macro if not previously defined (workaround for rhbz #481023)

* Wed Jul 21 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 2.2.0.3-1
- remove PRODUCT_VERSION from Makefile
- add test target to Makefile

* Mon Jul 19 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 2.1.0.3-2
- build for kernel-PAE as well

* Tue Mar 30 2010 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 2.1.0.3-1
- rebuild for SUMU 2.1 release

* Sun Dec 06 2009 Alexander Todorov <atodorov@NO-SPAM.otb.bg> - 0.3-1
- Initial Build
