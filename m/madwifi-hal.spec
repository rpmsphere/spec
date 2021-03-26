%define kmod_name madwifi-hal
%define kver %(uname -r)
%define kmdl_moduledir /lib/modules/%{kver}/kernel/drivers

Summary: A linux device driver for Atheros chipsets (ar5210, ar5211, ar5212)
Name: %{kmod_name}
Version: 0.10.5.6
Release: 1.r4126
Group: System Environment/Kernel
URL: http://madwifi-project.org/
Source0: http://snapshots.madwifi-project.org/%{kmod_name}-%{version}/%{kmod_name}-%{version}-r4126-20100324.tar.gz
BuildRequires: gcc, kernel-devel
Obsoletes: madwifi-old, madwifi-ng <= %{evr}
Requires: %{kmod_name}-kmod = %{version}
License: BSD 3-Clause

%description
This package contains the Multiband Atheros Driver for WiFi, A linux
device driver for 802.11a/b/g universal NIC cards - either Cardbus,
PCI or MiniPCI - that use Atheros chipsets (ar5210, ar5211, ar5212).

%package kmod
Summary: Kernel module for madwifi
##Release: %(echo %{kver} | tr - _).39_r2756
BuildRequires: gcc, kernel-devel
License: GPL/BSD

%description kmod
This package contains kernel drivers for madwifi


%prep
%setup -q -n %{kmod_name}-%{version}-r4126-20100324
##find . -name Makefile\* | xargs perl -pi -e's,/sbin/depmod,: /sbin/depmod,'
sed -i 's|\[4-9\]|[0-9]*|' Makefile

%build
export TOOLPREFIX=`which gcc|sed -e's,gcc$,,'`

make -C tools KERNELPATH=%{kmdl_moduledir} KERNELRELEASE=%{kver}
make modules
#make modules KERNELPATH=%{kmdl_moduledir} KERNELRELEASE=%{kver}

%install
rm -rf %{buildroot}

export TOOLPREFIX=`which gcc|sed -e's,gcc$,,'`
export KERNELPATH=%{kmdl_moduledir}
export KERNELRELEASE=%{kver}

mkdir -p %{buildroot}%{_bindir}
make -C tools install DESTDIR=%{buildroot} \
     BINDIR=%{_bindir} MANDIR=%{_mandir} \
     KERNELPATH=/lib/modules/%{kver}/build \
     KERNELRELEASE=%{kver}
##mv hal/COPYRIGHT hal/COPYRIGHT.hal
##mv hal/README hal/README.hal

mkdir -p %{buildroot}%{kmdl_moduledir}/net
make KERNELPATH=/lib/modules/%{kver}/build \
     KERNELRELEASE=%{kver} \
     DESTDIR=%{buildroot} \
     KMODPATH=%{kmdl_moduledir}/net \
     install-modules

%post kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%postun kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYRIGHT README
%{_bindir}/*
%{_mandir}/man8/*.8*

%files kmod
%defattr(744,root,root,-)
%{kmdl_moduledir}/net/*.*o


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Mon Dec 06 2010 Wei-Lun Chao <bluebat@member.fsf.org> 0.10.5.6_r4126.ossii
- Use madwifi-hal-0.10.5.6-r4126-20100324.tar.gz

* Wed Jan 2 2008 Wei-Lun Chao <bluebat@member.fsf.org> 1:0.9.3.3-39_r2756.ossii
- Use madwifi-ng-r2756-20071018.tar.gz
- Add madwifi-ng-0933.ar2425.20071130.i386.patch

* Tue Oct 30 2007 Wei-Lun Chao <bluebat@member.fsf.org> 1:0.9.3.3-39.ossii
- Build for M6(CentOS5)

* Sun Oct 21 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.9.3.3-39
- Update to 0.9.3.3.

* Sun Jun 24 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.9.4-38_r2512
- Update to r2512.

* Thu Jun  7 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.9.4-37_r2431
- Update to r2431 (security fix).

* Sun May 13 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.9.4-36_r2321
- Update to r2321.

* Mon Mar 19 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.9.3-34
- Update to 0.9.3 final.

* Wed Feb  7 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.9.3-33_r2088
- Update to r2088.
- rhel4hack no longer needed.

* Fri Feb  2 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.9.3-32_r2068
- Update to r2068.
- Apply patch for vmware from #753.

* Fri Dec 22 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.9.3-31_r1865
- Update to r1865.

* Tue Oct 17 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.9.3-29_r1754
- Update to 0.9.3svn (r1754).

* Sun Aug 27 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.9.2-28
- Add devel subpackage.

* Sun Jul 30 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1:0.9.2-24
- Update to 0.9.2.

* Mon Jun 26 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.9.1.

* Tue May 30 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Upgrade to first madwifi release! :)
- Introduce epoch since we were over 0.9.0 already. :/

* Tue Feb 21 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Split off non-GPL modules into their own subpackage
  to make GPL compliance unambiguous.

* Sat Feb 18 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to today's svn.

* Sun Oct  2 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to today's cvs (0.9.6.0).

* Thu Apr 14 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to today's cvs.

* Sat Jan 22 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to today's cvs.

* Tue Jan  4 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs (0.9.4.12).

* Wed Dec 22 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs.

* Tue Nov  2 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs (0.9.4.11).

* Wed Aug 18 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs (0.9.3.1).

* Mon Jul 26 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to WPA cvs (0.9.2.2-WPA).

* Sun May 30 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to cvs (0.8.5.5).

* Wed Mar 24 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 0.8.5.4.

* Tue Feb  3 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.
