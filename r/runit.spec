%global debug_package %{nil}

Summary:	An UN*X init scheme with service supervision
Name:		runit
Version:	2.1.1
Release:	6.1
License:	BSD
Group:		System/Base
URL:		http://smarden.org/runit/
Source0:	http://smarden.org/runit/%{name}-%{version}.tar.gz
BuildRequires:	dietlibc-devel >= 0.32

%description
runit is a daemontools alike replacement for SysV-init and other init schemes.
It currently runs on GNU/Linux, OpenBSD, FreeBSD, and can easily be adapted to
other Unix operating systems. runit implements a simple three-stage concept.
Stage 1 performs the system's one-time initialization tasks. Stage 2 starts the
system's uptime services (via the runsvdir program). Stage 3 handles the tasks
necessary to shutdown and halt or reboot.

%prep
%setup -q -n admin

%build
pushd %{name}-%{version}/src
    echo "diet gcc -Os -pipe" > conf-cc
    echo "diet gcc -Os -static -s" > conf-ld
    make
popd
 
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/sbin/
install -d $RPM_BUILD_ROOT%{_mandir}/man8
pushd %{name}-%{version}
    for i in `cat package/commands`; do
	install -m0755 src/$i $RPM_BUILD_ROOT/sbin/
    done
popd
install -m0644 %{name}-%{version}/man/*.8 $RPM_BUILD_ROOT%{_mandir}/man8/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc %{name}-%{version}/package/CHANGES
%doc %{name}-%{version}/package/README
%doc %{name}-%{version}/package/THANKS
%doc %{name}-%{version}/doc/*.html
%doc %{name}-%{version}/etc/2
%doc %{name}-%{version}/etc/debian
%attr(0755,root,root) /sbin/chpst
%attr(0755,root,root) /sbin/runit
%attr(0755,root,root) /sbin/runit-init
%attr(0755,root,root) /sbin/runsv
%attr(0755,root,root) /sbin/runsvchdir
%attr(0755,root,root) /sbin/runsvdir
%attr(0755,root,root) /sbin/sv
%attr(0755,root,root) /sbin/svlogd
%attr(0755,root,root) /sbin/utmpset
%attr(0644,root,root) %{_mandir}/man8/chpst.8*
%attr(0644,root,root) %{_mandir}/man8/runit-init.8*
%attr(0644,root,root) %{_mandir}/man8/runit.8*
%attr(0644,root,root) %{_mandir}/man8/runsv.8*
%attr(0644,root,root) %{_mandir}/man8/runsvchdir.8*
%attr(0644,root,root) %{_mandir}/man8/runsvdir.8*
%attr(0644,root,root) %{_mandir}/man8/sv.8*
%attr(0644,root,root) %{_mandir}/man8/svlogd.8*
%attr(0644,root,root) %{_mandir}/man8/utmpset.8*

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.1
- Rebuild for Fedora
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-3mdv2011.0
+ Revision: 614798
- the mass rebuild of 2010.1 packages
* Tue Feb 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-2mdv2010.1
+ Revision: 499592
- rebuild
* Wed Oct 07 2009 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-1mdv2010.0
+ Revision: 455668
- 2.1.1
* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 2.1.0-1mdv2010.0
+ Revision: 451705
- 2.1.0
* Sun Aug 23 2009 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-2mdv2010.0
+ Revision: 419985
- rebuild
* Wed Jun 25 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-1mdv2009.0
+ Revision: 229040
- 2.0.0
* Tue Jun 10 2008 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-3mdv2009.0
+ Revision: 217532
- rebuild
- re-introduce the dietlibc build (requires dietlibc-0.32)
* Tue May 13 2008 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-1mdv2009.0
+ Revision: 206799
- fix deps (thanks anssi)
- 1.9.0
- don't build it against broken dietlibc
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %$RPM_BUILD_ROOT on Pixel's request
* Tue Dec 12 2006 Oden Eriksson <oeriksson@mandriva.com> 1.7.2-1mdv2007.0
+ Revision: 95958
- Import runit
* Tue Dec 12 2006 Oden Eriksson <oeriksson@mandriva.com> 1.7.2-1mdv2007.1
- 1.7.2
* Mon Dec 19 2005 Lenny Cartier <lenny@mandriva.com> 1.3.2-1mdk
- 1.3.2
* Thu Oct 20 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.3.1-1mdk
- 1.3.1
* Fri Apr 15 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.2.2-1mdk
- 1.2.2
* Tue Jan 18 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2.1-4mdk
- enable dietlibc build on x86_64 as dietlibc-devel-0.27-9mdk knows
  about "nice" now (Gwenole Beauchesne)
* Tue Jan 18 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2.1-3mdk
- rebuilt to match changelogs
* Tue Jan 18 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2.1-2mdk
- disable dietlibc build on x86_64 until it can handle "nice"
* Tue Jan 18 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.2.1-1mdk
- 1.2.1
* Mon Dec 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.0-1mdk
- 1.2.0
* Mon Nov 08 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.1.0-1mdk
- 1.1.0
* Fri Sep 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.5-1mdk
- 1.0.5
* Wed Aug 04 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.0.4-1mdk
- 1.0.4
