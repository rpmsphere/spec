Summary: Tools for managing a frame buffer's video mode properties
Name: fbset
Version: 2.1
Release: 47
License: GPL+
Group: Applications/System
URL: http://users.telenet.be/geertu/Linux/fbdev/
Source: http://users.telenet.be/geertu/Linux/fbdev/fbset-2.1.tar.gz
BuildRequires: gcc bison flex
BuildRequires: perl-interpreter perl-generators
Suggests: modeline2fb
Patch0: fbset-2.1-makefile.patch
Patch1: fbset-2.1-fixmode.patch
Patch2: fbset-2.1-manfix.patch
# See: s390 (#484843), s390x (#484843)
ExcludeArch: s390 s390x

%description
Fbset is a utility for maintaining frame buffer resolutions.  Fbset
can change the video mode properties of a frame buffer device, and is
usually used to change the current video mode.

Install fbset if you need to manage frame buffer resolutions.

%package -n modeline2fb
Summary: A simple modeline-to-fb-modes translator
License: GPL+
Requires: fbset
Requires: perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

%description -n modeline2fb
%{summary}.

%prep
%setup -q
%patch0 -p1 -b .makefile
%patch1 -p1 -b .fixmode
%patch2 -p1 -b .man

%build
%set_build_flags
# Parallel build is not supported.
make

%install
%makeinstall

%files
%{_sbindir}/fbset
%{_mandir}/man[58]/*
%config(noreplace) %{_sysconfdir}/fb.modes

%files -n modeline2fb
%{_sbindir}/modeline2fb

%changelog
* Thu Nov 28 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuilt for Fedora

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.1-46
- Perl 5.28 rebuild

* Fri Feb 23 2018 Florian Weimer <fweimer@redhat.com> - 2.1-45
- Use LDFLAGS from redhat-rpm-config (via %%set_build_flags)
- Remove "rm -rf ${RPM_BUILD_ROOT}"
- Remove "%%defattr(-,root,root)"
- Add gcc build requirement

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.1-41
- Perl 5.26 rebuild

* Tue Apr 18 2017 Petr Šabata <contyk@redhat.com> - 2.1-40
- Subpackaging modeline2fb to avoid the needless perl dependency in
  minimal environments
- Add correct perl build time and run time dependencies

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Zdenek Prikryl <zprikryl@redhat.com> 2.1-27
- Spec review (#225744)

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1-26
- fix license tag

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.1-25
- Autorebuild for GCC 4.3

* Thu Jan 18 2007 Jindrich Novy <jnovy@redhat.com> - 2.1-24
- add dist tag, minor rpmlint fix

* Thu Jan  2 2007 David Woodhouse <dwmw2@redhat.com> - 2.1-23
- Fix man page syntax error

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.1-22
- rebuild
- Add missing br flex

* Mon May 29 2006 Jindrich Novy <jnovy@redhat.com> 2.1-21
- add BuildRequires: bison (#193362)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.1-20.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.1-20.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Mar  4 2005 Jidnrich Novy <jnovy@redhat.com> 2.1-20
- rebuilt with gcc4

* Thu Feb 10 2005 Jindrich Novy <jnovy@redhat.com> 2.1-19
- remove -D_FORTIFY_SOURCE=2 from CFLAGS, present in RPM_OPT_FLAGS

* Wed Feb  9 2005 Jindrich Novy <jnovy@redhat.com> 2.1-18
- Copyright -> License conversion
- rebuilt with -D_FORTIFY_SOURCE=2

* Mon Oct 11 2004 Bill Nottingham <notting@redhat.com> 2.1-17
- add URL (#122128)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Dec 12 2002 Tim Powers <timp@redhat.com> 2.1-12
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 19 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add ExcludeArch: s390 s390x

* Fri Feb 23 2001 Preston Brown <pbrown@redhat.com>
- fix 1024x768 72 Hz mode (#29024)

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jun 15 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Tue Feb 15 2000 Bill Nottingham <notting@redhat.com>
- ship fb.modes everywhere

* Fri Feb  4 2000 Bill Nottingham <notting@redhat.com>
- fix man page permissions

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix summary

* Thu Oct  7 1999 Bill Nottingham <notting@redhat.com>
- update to 2.1
- don't include fb devs.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- include fb devs too (#1515)
- update to 19990118 version.

* Thu Nov  5 1998 Jeff Johnson <jbj@redhat.com>
- import from ultrapenguin 1.1.
- upgrade to 19981104.

* Thu Oct 29 1998 Jakub Jelinek <jj@ultra.linux.cz>
- new package
