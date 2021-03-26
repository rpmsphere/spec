%define kmod_name r8101
%define kver %(uname -r)

Name:           %{kmod_name}
Url:            http://www.realtek.com.tw
Summary:        Realtek kernel module for RTL8100E/RTL8101E/RTL8102E-GR PCI Express cards
Version:        1.007.00
Release:        1
Group:          System/Kernel and hardware
License:        GPL
Source:         %{kmod_name}-%{version}.tar.bz2
Patch:		r8101-1.007.00.diff
BuildRequires: gcc, kernel-devel
Requires: kernel = %kver

%description
Realtek kernel module for RTL8100E/RTL8101E/RTL8102E-GR PCI Express cards

%package kmod
Summary: Realtek kernel module for RTL8100E/RTL8101E/RTL8102E-GR PCI Express cards
##Release: %(echo %{kver} | tr - _).1

%description kmod
Realtek kernel module for RTL8100E/RTL8101E/RTL8102E-GR PCI Express cards

%prep
%setup -q -n %{kmod_name}-%{version}
%if "%kver" != "2.6.18-53.1.21.el5"
%patch
%endif

%build
%__make modules

%install
install -Dm 744 src/r8101.ko %{buildroot}/lib/modules/%{kver}/kernel/drivers/net/r8101.ko

%post kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%postun kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%clean
rm -rf %{buildroot} 

%files kmod
%doc readme release_note.txt
/lib/modules/%{kver}/kernel/drivers/net/r8101.ko

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri Jun 13 2008 Wei-Lun Chao <bluebat@member.fsf.org> 1.007.00-1.ossii
- Rebuild for M6(CentOS5)

* Mon Oct 23 2007 - Rain_Maker <rain_maker@root-forum.org>
- initial build (version 1.003.00)
