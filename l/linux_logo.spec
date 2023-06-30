Summary: Show a logo with some system info on the console
Name: linux_logo
Version: 6.0
Release: 1
License: GPLv2
Group: Applications/System
URL: https://www.deater.net/weave/vmwprod/linux_logo/
Source: https://www.deater.net/weave/vmwprod/linux_logo/linux_logo-%{version}.tar.gz
Patch0: linux_logo-5.11-add-ppc64le.patch
Patch1: linux_logo-5.11-default-logo.patch
Patch2: 0001-initial-aarch64-support.patch
Patch3: linux_logo-5.11-kvm-cpus.patch
BuildRequires: gettext
BuildRequires: which

%description
Linux logo shows a logo, a colorful penguin by default, with some optional
system info on the console. It's typically used to generate issue and motd
files or executed upon login.

%prep
%setup -q
#patch0 -p1
#patch1 -p1
#patch2 -p1
#patch3 -p1

%build
# We still need to override CFLAGS later on, configure can't set them
%configure --prefix=%{_prefix}
make logos-all %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make install PREFIX=%{buildroot}%{_prefix}
%find_lang %{name}

%files -f %{name}.lang
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc CHANGES* LINUX_LOGO.FAQ README* TODO USAGE
%{_bindir}/linux_logo
%{_mandir}/man1/linux_logo.1*

%changelog
* Wed May 13 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 6.0
- Rebuilt for Fedora
* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.11-20
- Escape macros in %%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Thu Nov  3 2016 Matthias Saou <matthias@saou.eu> 5.11-15
- Add support for (some) KVM Intel CPUs.
* Tue Aug 16 2016 Peter Robinson <pbrobinson@fedoraproject.org> 5.11-14
- Add initial aarch64 support
- Cleanup spec
- Use %%license
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Tue Oct  6 2015 Matthias Saou <matthias@saou.eu> 5.11-12
- Include patch to have a consistent default logo, the banner logo (#1268065).
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sun May 25 2014 Brent Baude <baude@us.ibm.com> - 5.11-8
- Added ppc64le arch support; changed configure to use macro
* Tue Apr 29 2014 Matthias Saou <matthias@saou.eu> 5.11-7
- Very minor spec file cleanup. Keep it legacy for RHEL6 rebuilding as-is.
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sat Dec  4 2010 Matthias Saou <https://freshrpms.net/> 5.11-1
- Update to 5.11.
- Use the make target to enable all logos instead of a custom way.
- Update summary and description.
* Mon Apr 26 2010 Matthias Saou <https://freshrpms.net/> 5.10-1
- Update to 5.10.
* Fri Oct 2 2009 Matthias Saou <https://freshrpms.net/> 5.06-1
- Update to 5.06.
* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Fri Feb  6 2009 Matthias Saou <https://freshrpms.net/> 5.04-1
- Update to 5.04.
* Sun Feb  3 2008 Matthias Saou <https://freshrpms.net/> 5.03-1
- Update to 5.03.
* Mon Oct 22 2007 Matthias Saou <https://freshrpms.net/> 5.02-1
- Update to 5.02.
* Wed Aug 22 2007 Matthias Saou <https://freshrpms.net/> 5.01-3
- Rebuild for new BuildID feature.
* Sun Aug  5 2007 Matthias Saou <https://freshrpms.net/> 5.01-2
- Update License field.
* Tue Jul 24 2007 Matthias Saou <https://freshrpms.net/> 5.01-1
- Update to 5.01.
- Remove no longer needed strip patch.
- Clean up build/install based on the upstream improvements.
- Add "which" build requirement, the custom configure script uses it.
* Thu Mar 15 2007 Matthias Saou <https://freshrpms.net/> 4.16-1
- Update to 4.16.
* Mon Aug 28 2006 Matthias Saou <https://freshrpms.net/> 4.14-1
- Update to 4.14.
- FC6 rebuild.
* Tue May 23 2006 Matthias Saou <https://freshrpms.net/> 4.13-3
- Update the debug patch to remove stripping of the binaries (Ville, #192442).
* Mon Mar  6 2006 Matthias Saou <https://freshrpms.net/> 4.13-2
- FC5 rebuild.
* Thu Feb  9 2006 Matthias Saou <https://freshrpms.net/> 4.13-1
- Update to 4.13.
* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 4.12-2
- rebuild on all arches
* Mon May  2 2005 Matthias Saou <https://freshrpms.net/> 4.12-1
- Update to 4.12.
- Add trivial patch to remove stripping upon install, to get useful debuginfo.
* Sat Apr 30 2005 Matthias Saou <https://freshrpms.net/> 4.11-1
- Update to 4.11.
* Sat Apr  2 2005 Matthias Saou <https://freshrpms.net/> 4.10-1
- Update to 4.10.
- Remove no longer needed gcc4 patch.
- Get optflags also used during the compilation of libsysinfo.
* Wed Mar 30 2005 Adrian Reber <adrian@lisas.de> 4.09-3
- Added gcc4 patch
- Fixed a warning
* Tue Nov 16 2004 Matthias Saou <https://freshrpms.net/> 4.09-2
- Bump release to provide Extras upgrade path.
* Mon May 17 2004 Matthias Saou <https://freshrpms.net/> 4.09-1
- Update to 4.09.
- Re-enabled all logos, they build fine again.
* Fri Dec 12 2003 Matthias Saou <https://freshrpms.net/> 4.07-3
- Disabled many of the logos as they prevent building :-(
- Rebuilt for Fedora Core 1.
* Mon Mar 31 2003 Matthias Saou <https://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
* Wed Jan 29 2003 Matthias Saou <https://freshrpms.net/>
- Update to 4.07.
* Sat Sep 28 2002 Matthias Saou <https://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
* Thu Sep 26 2002 Matthias Saou <https://freshrpms.net/>
- Update to 4.05.
* Thu May  2 2002 Matthias Saou <https://freshrpms.net/>
- Update to 4.02.
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.
* Thu Feb 21 2002 Matthias Saou <https://freshrpms.net/>
- Update to 4.0.
- Included all the existing logos, it's more fun :-)
* Wed Jan  9 2002 Matthias Saou <https://freshrpms.net/>
- Update to 3.9b5.
- Added the Red Hat banner (yes, this is an rpm ;-)).
* Thu Apr 26 2001 Matthias Saou <https://freshrpms.net/>
- Update to 3.9b3 and rebuilt for Red Hat 7.1.
* Mon Nov 20 2000 Tim Powers <timp@redhat.com>
- rebuilt to fix bad dir perms
* Fri Nov 10 2000 Than Ngo <than@redhat.com>
- update to 3.9b1
* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt
* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- use RPM macros
* Mon Jul 03 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild
* Sat May 27 2000 Ngo Than <than@redhat.de>
- update to 3.05 for 7.0
- cleanup specfile
- use RPM_OPT_FLAGS
* Thu Nov 18 1999 Ngo Than <than@redhat.de>
- initial RPM
