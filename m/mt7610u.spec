%define kversion %(uname -r)

Name:    mt7610u
Version: 20180326
Release: 1
Group:   System Environment/Kernel
License: GPLv2
Summary: %{name} kernel module(s)
URL:     https://github.com/ulli-kroll/mt7610u
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel
BuildRequires:  elfutils-libelf-devel
Source0:  mt7610u-master.zip

%description
Kernel module for RaLink wireless USB series network adapters.

%package kmod
Summary: Kernel module for RaLink wireless USB series network adapters
Requires: kernel = %(uname -r|sed 's/-.*//')
Obsoletes: mt7650u-kmod

%description kmod
This package provides the %{name} kernel module(s) for the
RaLink mt7610/mt7630/mt7650 wireless USB series network adapters.
It is built to depend upon the specific ABI provided by a range of releases
of the same variant of the Linux kernel and not on any one specific build.
Only STA/Monitor Mode is supported, no AP.

%prep
%setup -q -n mt7610u-master
sed -i '5722,5737d' include/rtmp.h

%build
make

%install
install -d %{buildroot}/lib/firmware/
install firmware/* %{buildroot}/lib/firmware/
install -d %{buildroot}/lib/modules/%{kversion}/extra/%{name}/
install mt7610u.ko %{buildroot}/lib/modules/%{kversion}/extra/%{name}/
install -d %{buildroot}%{_sysconfdir}/Wireless/RT2870STA/
install *.dat %{buildroot}%{_sysconfdir}/Wireless/RT2870STA/

%post kmod
depmod -a > /dev/null 2> /dev/null

%postun kmod
depmod -a > /dev/null 2> /dev/null

%clean
%{__rm} -rf %{buildroot}

%files kmod
%doc *.txt README* COPYING
/lib/firmware/*
/lib/modules/%{kversion}/extra/%{name}
%{_sysconfdir}/Wireless/RT2870STA

%changelog
* Mon Oct 08 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20180326
- Rebuilt for Fedora
