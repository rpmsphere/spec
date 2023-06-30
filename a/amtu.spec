Summary: Abstract Machine Test Utility
Name: amtu 
Version: 1.0.8
Release: 19.1
License: CPL
Group: System Environment/Base
URL: https://sourceforge.net/projects/amtueal/
Source0: %{name}-%{version}.tar.gz
Patch1: amtu-1.0.8-doc.patch
Patch2: amtu-1.0.8-init.patch
Patch3: amtu-1.0.8-memsep.patch
Patch4: amtu-1.0.8-net-device.patch
Patch5: amtu-1.0.8-net-device_name.patch
BuildRequires: audit-libs-devel
BuildRequires: automake
Requires: chkconfig

%description
Abstract Machine Test Utility (AMTU) is an administrative utility to check
whether the underlying protection mechanism of the hardware are still being
enforced. This is a requirement of the Controlled Access Protection Profile
FPT_AMT.1, see 
https://www.radium.ncsc.mil/tpep/library/protection_profiles/CAPP-1.d.pdf

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
LDFLAGS=-Wl,--allow-multiple-definition
touch ChangeLog
touch NEWS
touch AUTHORS
autoreconf -fv --install
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make "DESTDIR=${RPM_BUILD_ROOT}" "bindir=%{_sbindir}" install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add amtu

%preun
if [ $1 -eq 0 ]; then
   /sbin/service amtu stop > /dev/null 2>&1
   /sbin/chkconfig --del amtu
fi

%files
%doc doc/AMTUHowTo.txt LICENSE
%attr(755,root,root) /etc/rc.d/init.d/amtu
%config(noreplace) %attr(640,root,root) /etc/sysconfig/amtu
%attr(0750,root,root) %{_sbindir}/amtu
%attr(0644,root,root) %{_mandir}/man8/*

%changelog
* Mon Apr 18 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.8
- Rebuilt for Fedora
* Fri May 30 2014 Paul Moore <pmoore@redhat.com> - 1.0.8-11
- Added amtu-1.0.8-net-device_name.patch
  Resolves #1098076
* Thu Mar 13 2014 Paul Moore <pmoore@redhat.com> - 1.0.8-10
- Rebuild for RHEL-6.6-fastrack
  Resolves #689823 #723049
* Tue Dec 10 2013 Paul Moore <pmoore@redhat.com> - 1.0.8-9
- Added amtu-1.0.8-net-device.patch
  Resolves #689823 #723049
* Tue Feb 16 2010 Steve Grubb <sgrubb@redhat.com> - 1.0.8-8
- Move amtu to /usr/sbin
* Tue Jan 19 2010 Steve Grubb <sgrubb@redhat.com> - 1.0.8-7
resolves: #556852 - amtu memory separation test can fail randomly
* Mon Jan 11 2010 Steve Grubb <sgrubb@redhat.com> 1.0.8-6
- rebuild for new audit-libs
* Fri Sep 11 2009 Steve Grubb <sgrubb@redhat.com> - 1.0.8-5
- Corrected config file test (#522708)
- Made init script more LSB compatible (#522789)
* Fri Aug 28 2009 Steve Grubb <sgrubb@redhat.com> - 1.0.8-4
- Add ExclusiveArch for platforms having memory separation tests
* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.0.8-3
- rebuilt with new audit
* Wed Aug 19 2009 Steve Grubb <sgrubb@redhat.com> 1.0.8-2
- rebuild for new audit-libs
* Sun Jul 26 2009 Steve Grubb <sgrubb@redhat.com> 1.0.8-1
- new upstream version
- Add init script for bootup system check
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Wed Jul 01 2009 Steve Grubb <sgrubb@redhat.com> 1.0.7-1
- new upstream version
* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0.6-3
- fix license tag
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.6-2
- Autorebuild for GCC 4.3
* Sat Dec 08 2007 Steve Grubb <sgrubb@redhat.com> 1.0.6-1
- new upstream version
* Thu Mar 08 2007 Steve Grubb <sgrubb@redhat.com> 1.0.5-1
- new upstream version
* Fri Feb 16 2007 Steve Grubb <sgrubb@redhat.com> 1.0.4-6
- change buildroot
* Thu Feb 8 2007 Steve Grubb <sgrubb@redhat.com> 1.0.4-5
- specfile updates
* Tue Jan 9 2007 Steve Grubb <sgrubb@redhat.com> 1.0.4-4
- patch fixing network and disk tests
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.4-3.1
- rebuild
* Mon Jun 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.4-3
- Fix missing BR on automake
* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.4-2.2
- bump again for double-long bug on ppc(64)
* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.4-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes
* Tue Jan  3 2006 Jesse Keating <jkeating@redhat.com> 1.0.4-2
- rebuilt
* Fri Dec 9 2005 Steve Grubb <sgrubb@redhat.com> 1.0.4-1
- New upstream version updated for new audit messages
* Mon Dec 5 2005 Steve Grubb <sgrubb@redhat.com> 1.0.2-2
- Fix "clean" section of spec file (bz 172942)
- Add memsep-random patch (bz 174767)
* Thu Jul 14 2005 Steve Grubb <sgrubb@redhat.com> 1.0.2-1
- New upstream version.
* Tue Jul 12 2005 Steve Grubb <sgrubb@redhat.com> 1.0.1-1
- New version fixes bug where audit system was disable at end of test.
* Wed Jun  8 2005 Steve Grubb <sgrubb@redhat.com> 1.0-2
- add a few more include "config.h"
* Fri May  27 2005 Steve Grubb <sgrubb@redhat.com> 1.0-1
- New upstream version from IBM
- Drop memsep patch
- Rework specfile
* Thu Sep  2 2004 root <ccb@redhat.com> 0.1-7RHEL
- integrate memsep patch from Matt Anderson at HP
* Mon Aug 16 2004 root <ccb@redhat.com> 0.1-6RHEL
- Integrate ia64 patches from HP's Matt Anderson, enabling use on ia64
* Tue Jun 29 2004 root <ccb@redhat.com> 0.1-4RHEL
- fix /usr/bin/amtu modes for real this time
* Tue Jun 29 2004 root <ccb@redhat.com> 0.1-4RHEL
- set execute bits on /usr/bin/amtu
* Fri May 28 2004 ccb <ccb@redhat.com> 0.1-3RHEL
- fixed owners and permissions in "files"
* Wed May 26 2004 ccb <ccb@redhat.com> 0.1-2RHEL
- move docs to a version-qualified directory name
* Sat May  1 2004 root <chavezt@cs679156-153.austin.rr.com> 
- Initial build.
