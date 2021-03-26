%define snapshot 20080210
%define kmod_name acx
%define kver %(uname -r)

Summary: Kernel module for Texas Instruments ACX100/ACX111 based network adapters
Name: %{kmod_name}
Version: 0.3.38
Release: 1
Group: System Environment/Kernel
License: GPL
URL: http://acx100.sourceforge.net/
Source0: http://downloads.sourceforge.net/acx100/acx-%{snapshot}.tar.bz2
BuildRequires: gcc, kernel-devel
Requires: kernel = %kver
Patch0: acx_karmic.patch

%description
This RPM contains a binary Linux kernel module.
It provides a driver for Texas Instruments ACX100/ACX111
based wireless network adapters.

%package kmod
Summary: Kernel module for Texas Instruments ACX100/ACX111 based network adapters
##Release: %(echo %{kver} | tr - _).1

%description kmod
This RPM contains a binary Linux kernel module.
It provides a driver for Texas Instruments ACX100/ACX111
based wireless network adapters.

%prep
%setup -q -n %{kmod_name}-%{snapshot}
%patch0 -p1
chmod -Rf a+rX,u+w,g-w,o-w .

%build
make


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0755 %{kmod_name}.ko %{buildroot}/lib/modules/%{kver}/kernel/drivers/net/%{kmod_name}.ko

%post kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%postun kmod
depmod -a > /dev/null 2> /dev/null
exit 0


%clean
%{__rm} -rf %{buildroot}

%files kmod
%defattr(-,root,root)
/lib/modules/%{kver}/kernel/drivers/net/%{kmod_name}.ko
%doc Changelog README


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Wed Jun 4 2008 Wei-Lun Chao <bluebat@member.fsf.org> 0.3.38-1.ossii
- Rebuild for M6(CentOS5)

* Mon Jun 19 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-1.20060521
- Enable i586 SMP since the kernel is available.

* Wed May 31 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-1.20060521
- Update to 20060521.
- Update kmodtool to 0.10.10.

* Fri Mar 31 2006 Matthias Saou <http://freshrpms.net/> 0.0.0-1.20060215
- Initial RPM release, based on the new Extras kernel module template.
