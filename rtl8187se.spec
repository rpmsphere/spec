%define kmod_name rtl8187se
%define kver %(uname -r)

Name:		%{kmod_name}
Summary:	Driver for Realtek RTL8187SE mini PCI WLAN-Cards
Version:	2.6.36
Release:	2.1
Group:		System/Kernel
License:	GPL
Source0:        %{name}-%{version}.tar.bz2
Source1:        preamble
Source100:	%{name}.changes
Patch0:		%{name}-Makefile.diff
Patch1:		%{name}-2.6.31-backport.patch
BuildRequires:	gcc, kernel-devel
Requires:	kernel = %kver

%description 
This package contains a kernel module for Realtek RTL8187SE mini PCI WLAN-Cards
(PCI-ID 10ec:8199), which can be found in MSI Wind laptops.

%package kmod
Summary: Driver for Realtek RTL8187SE mini PCI WLAN-Cards
##Release: %(echo %{kver} | tr - _).1

%description kmod
This package contains a kernel module for Realtek RTL8187SE mini PCI WLAN-Cards.

%prep
%setup -q 
%patch0 -p0
%patch1 -p0

%build
export EXTRA_CFLAGS='-DVERSION=\"%version\"'
%__make -C /usr/src/kernels/%{kver} modules M=$PWD

%install
install -Dm 744 rtl8187se.ko %{buildroot}/lib/modules/%{kver}/updates/rtl8187se/rtl8187se.ko

%post kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%postun kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%clean
rm -rf %{buildroot} 

%files kmod
/lib/modules/%{kver}/updates/rtl8187se/rtl8187se.ko

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Mon Nov 29 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Sun Oct 24 2010 AxelKoellhofer@web.de - 2.6.36
- updated sources from linux 2.6.36 for openSUSE >= 11.2
- patches refreshed
- merged with package for openSUSE <= 11.1
- removed patches for discontinued openSUSE versions
- enabled build for openSUSE 11.3
- spec cleanup
* Wed May 12 2010 AxelKoellhofer@web.de - 2.6.34
- initial package for openSUSE = 11.2, sources from linux 2.6.34 (rc7)
* Sat Jul 25 2009 AxelKoellhofer@web.de
- disabled new "ec2"-flavor (breaks build)
* Sat May 16 2009 AxelKoellhofer@web.de
- updated to latest GIT from linux-next
- removed old sources
- added patch 3 and 4 for build of git-sources with  openSUSE 11.0 and 10.3
- spec cleanup
* Mon May 11 2009 AxelKoellhofer@web.de
- updated to latest GIT from linux-next
* Thu Apr 23 2009 AxelKoellhofer@web.de
- updated to latest GIT from linux-next
* Sat Apr  4 2009 AxelKoellhofer@web.de
- added Source1 (from original project at  http://code.google.com/p/msi-wind-linux/)
- enabled build for openSUSE 10.3 with Source1
* Thu Apr  2 2009 AxelKoellhofer@web.de
- updated to latest GIT from linux-next
* Sat Mar 14 2009 AxelKoellhofer@web.de
- updated to latest GIT from linux-next
* Sat Feb 28 2009 AxelKoellhofer@web.de
- updated to newest GIT from linux-staging tree
* Thu Feb 19 2009 AxelKoellhofer@web.de
- updated to newest GIT from linux-staging tree
- spec cleanup
* Tue Jan  6 2009 AxelKoellhofer@web.de
- Initial package, version 04
