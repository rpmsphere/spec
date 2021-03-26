Summary: An easy to use, modeless text editor
Name: joe
Version: 3.7
Release: 5%{?dist}
License: GPLv2+
Group: Applications/Editors
Source: http://prdownloads.sourceforge.net/joe-editor/joe-%{version}.tar.gz
Source1: joe-3.5.zh_TW.po
Source2: joerc.zh_TW
URL: http://joe-editor.sourceforge.net/index.html
Requires: ncurses
BuildRequires: ncurses-devel libselinux-devel
Patch0: joe-3.5-joerc.patch
Patch2: joe-3.4-selinux.patch
Patch3: joe-3.5-time.patch
Patch4: joe-3.5-documentation.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Joe is a powerful, easy to use, modeless text editor.
It uses the same WordStar keybindings used in Borland's development
environment.

%prep
%setup -q
##%patch0 -p1 -b .joerc
%patch2 -p1 -b .selinux
%patch3 -p1 -b .time
##%patch4 -p1 -b .doc
iconv -f koi8-r -t utf-8 ./man/ru/joe.1.in >./man/ru/joe.1.in.aux
mv ./man/ru/joe.1.in.aux ./man/ru/joe.1.in

%build
%configure
make  %{?_smp_mflags}

%install
rm -fr $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# This is automatically compressed afterwards...
pushd $RPM_BUILD_ROOT%{_mandir}/man1
ln -s joe.1 jmacs.1 
ln -s joe.1 jpico.1 
ln -s joe.1 jstar.1 
ln -s joe.1 rjoe.1 
popd

install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/joe/lang/zh_TW.po
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/joe/joerc.zh_TW
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/joe

%files
%defattr(-,root,root,-)
%doc README TODO HINTS NEWS LIST COPYING
%{_bindir}/*
%dir /etc/joe
%config(noreplace) /etc/joe/*
%{_datadir}/joe
%{_mandir}/man1/*
%{_mandir}/ru/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Mar 11 2010 Wei-Lun Chao <bluebat@member.fsf.org> - 3.7-5.ossii
- Add zh_TW locale
- Rebuild for OSSII

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.5-5
- Autorebuild for GCC 4.3

* Tue Jan 22 2008 Ivana Varekova <varekova@redhat.com> 3.5-4
- rebuilt

* Fri Feb 23 2007 Ivana Varekova <varekova@redhat.com> 3.5-3
- incorporate the package review feedback

* Wed Feb  7 2007 Ivana Varekova <varekova@redhat.com> 3.5-2
- fix 227487 - joe wakes up spuriously once per ...
  patch by Arjan van de Ven
- spec file cleanup

* Mon Oct 23 2006 Ivana Varekova <varekova@redhat.com> 3.5-1
- update to 3.5

* Fri Jul 14 2006 Ivana Varekova <varekova@redhat.com> 3.4-3
- remove uncessary patches

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.4-2.1
- rebuild

* Fri Jun 09 2006 Martin Bacovsky <mbacovsk@redhat.com> 3.4-2
- fix nonworking PgUp - bug 194213

* Wed May 31 2006 Ivana Varekova <varekova@redhat.com> 3.4-1
- update to 3.4

* Mon Apr 10 2006 Ivana Varekova <varekova@redhat.com> 3.3-3
- fix problem with Polish characters - bug 188235

* Wed Mar  1 2006 Ivana Varekova <varekova@redhat.com> 3.3-2
- add forgotten header files - bug 183455

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.3-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.3-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Jun  6 2005 Ivana Varekova <varekova@redhat.com> 3.3-1
- new upstream version

* Fri Mar  4 2005 Ivana Varekova <varekova@redhat.com> 3.1-8
- rebuilt

* Mon Jan 24 2005 Ivana Varekova <varekova@redhat.com> 3.1-7
- Fix bug #137025 - missing return statement

* Tue Oct 05 2004 Lon Hohberger <lhh@redhat.com> 3.1-6
- Pass 2 at fixing UTF-8 decoding in help display (#134197)

* Fri Oct 01 2004 Lon Hohberger <lhh@redhat.com> 3.1-5
- Fix UTF-8 decoding in help display (#134197)

* Sat Sep 25 2004 Bill Nottingham <notting@redhat.com> 3.1-4
- fix SELinux support (#133602)
- clean up %%prep (#133601)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 08 2004 Lon Hohberger <lhh@redhat.com> 3.1-2
- Rebuild

* Tue Jun 01 2004 Lon Hohberger <lhh@redhat.com> 3.1-1.2
- Rebuild

* Tue Jun 01 2004 Lon Hohberger <lhh@redhat.com> 3.1-1
- Import 3.1 from upstream
- Include mktemp behavior from #124462

* Thu May 27 2004 Lon Hohberger <lhh@redhat.com> 3.0-2.3
- Include HINTS NEWS LIST in doc line (#124464)

* Mon May 03 2004 Lon Hohberger <lhh@redhat.com> 3.0-2.1
- Fix /etc/joe/joe/* sysconf dirs; the new Makefile.am handles this for us.
- Ensure we reference correct directories in manpages and joe-configs.

* Wed Apr 28 2004 Lon Hohberger <lhh@redhat.com> 3.0-2
- Rebuild.

* Wed Apr 28 2004 Lon Hohberger <lhh@redhat.com> 3.0-1.1
- Kill ancient configure scripts in tarball to cause it to build on 
ppc64.

* Wed Apr 28 2004 Lon Hohberger <lhh@redhat.com> 3.0-1
- Import of 3.0 upstream.
- Removed zero-rc patch for now; it doesn't correctly fix the
  problem.
- Merge new SELinux patch from Dan Walsh.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 29 2004 Dan Walsh <lhh@redhat.com> 2.9.8-8
- Modify SELinux patch to only attempt change if the context is different
- Change is_selinux_enabled to >0 check.

* Mon Dec 15 2003 Lon Hohberger <lhh@redhat.com> 2.9.8-7
- SELinux patch to keep context on backup files when saving.

* Tue Jun 17 2003 Lon Hohberger <lhh@redhat.com> 2.9.8-6
- Rebuild for FC2 tree

* Tue Jun 17 2003 Lon Hohberger <lhh@redhat.com> 2.9.8-5
- Rebuilt 

* Tue Jun 17 2003 Lon Hohberger <lhh@redhat.com> 2.9.8-4
- Fixed incomplete patch for #80657

* Mon Jun 16 2003 Lon Hohberger <lhh@redhat.com> 2.9.8-3
- Rebuilt 

* Mon Jun 16 2003 Lon Hohberger <lhh@redhat.com> 2.9.8-2
- Import from 2.9.8 upstream.  This eliminates most of the patches
we maintained.  Added patch from #80657 from Hans de Goede.

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 2.9.7-13
- fix build with gcc 3.3

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan 2 2003 Lon Hohberger <lhh@redhat.com> 2.9.7-11
- Added fix for #80673 - 'restrict' (C99 keyword) used as variable.
- Fixed build bugs on i386.

* Tue Nov 11 2002 Lon Hohberger <lhh@redhat.com> 2.9.7-9
- Fixed zero-byte rc file hang.

* Tue Nov 06 2002 Lon Hohberger <lhh@redhat.com> 2.9.7-8
- Cleaned up warnings on ppc/ia32/ia64.
- Fixed help message.
- Fixed bugs on ia64 and ppc architectures.
- Fixed build bugs on ia64.

* Mon Jul 22 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.9.7-7
- Make it build again (auto*... sigh. #69409)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Feb 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.9.7-4
- Rebuild

* Mon Feb  4 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.9.7-3
- The joe.1 man-page was called <autoconf-arch-string>-joe.1 

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Nov  8 2001 Trond Eivind Glomsrød <teg@redhat.com> 2.9.7-1
- 2.9.7

* Mon Jul 30 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Patch for wordwrap problem (#50321)

* Mon Jun  4 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 2.9.6 - someone's developing it again, on sourceforge
- all patches absorbed or unnecesarry
- add doc files and URL
- use %%configure and %%makeinstall

* Wed Feb 28 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Don't try to read .joerc from CWD (#30031)
- make sure the docs say /etc/joe everywhere

* Fri Nov 17 2000 Trond Eivind Glomsrød <teg@redhat.com>
- clean up the patch file from yesterday  

* Thu Nov 16 2000 Trond Eivind Glomsrød <teg@redhat.com>
- security fix - don't blindly write to DEADJOE, unlink it
  and create it safely first

* Mon Oct 09 2000 Trond Eivind Glomsrød <teg@redhat.com>
- added patch so it will build on Red Hat 6.x (#18639)

* Wed Jul 19 2000 Jakub Jelinek <jakub@redhat.com>
- fix the vfile patch

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jun 30 2000 Trond Eivind Glomsrød <teg@redhat.com>
- added new patch for supporting big files (15+ MB). 
- obsoleted one of our which is contained within the
  above patch
 
* Tue Jun 27 2000 Trond Eivind Glomsrød <teg@redhat.com>
- move config files to /etc/joe

* Tue Jun 27 2000 Trond Eivind Glomsrød <teg@redhat.com>
- added new patch for resizing, by Seth Vidal
- removed an old patch which did almost the same thing, 
  but not as well

* Tue Jun 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- disabled a patch which no longer works

* Mon Jun 19 2000 Trond Eivind Glomsrød <teg@redhat.com>
- and yet another

* Mon Jun 19 2000 Trond Eivind Glomsrød <teg@redhat.com>
- once more

* Mon Jun 19 2000 Trond Eivind Glomsrød <teg@redhat.com>
- rebuild

* Wed Jun 07 2000 Trond Eivind Glomsrød <teg@redhat.com>
- use symlinked man pages
- use %%{_mandir}

* Wed May  3 2000 Bill Nottingham <notting@redhat.com>
- fix for ia64 (sizeof(int) != sizeof(time_t))

* Wed Apr 26 2000 Trond Eivind Glomsrød <teg@redhat.com>
- fixed a problem loading .joerc. Thanks to Jeff Peters
  for the patch (#11049)

* Wed Apr 26 2000 Trond Eivind Glomsrød <teg@redhat.com>
- patched it to restore the tty after exiting

* Thu Apr 20 2000 Trond Eivind Glomsrød <teg@redhat.com>
- gzip man page
- hardlink the joe man page to jmacs, jpico, jstar, rjoe


* Fri Mar 31 2000 Bill Nottingham <notting@redhat.com>
- add patch to fix coredumps on quit for large files
  (b4506055@csie,ntu.edu.tw, #5372)

* Mon Feb  7 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages

* Tue Jan 18 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Add patch from Hans de Goede <hans@highrise.nl> to fix the End key

* Tue Sep 07 1999 Cristian Gafton <gafton@redhat.com>
- patch for closing on some buffer overflow problems (not that is really
  critical...)

* Thu Sep  2 1999 Jeff Johnson <jbj@redhat.com>
- DEADJOE files shouldn't be world readable (#4219).

* Thu Aug 12 1999 Cristian Gafton <gafton@redhat.com>
- add patch from Giuseppe Ghibo' <ghibo@caesar.polito.it> to fix resizing
  problems

* Sun May 16 1999 Jeff Johnson <jbj@redhat.com>
- don't rely on (broken!) rpm patch (#2735)

* Fri Apr 09 1999 Cristian Gafton <gafton@redhat.com>
- added locale patch from  Petr Kolar <PETR.KOLAR@vslib.cz>
  (yeah, finally!)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 17)

* Wed Jan 20 1999 Alex deVries <puffin@redhat.com>
- added mipseb support

* Fri Dec 18 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Tue Sep 15 1998 Cristian Gafton <gafton@redhat.com>
- built with Alan's -port patch

* Fri May 08 1998 Cristian Gafton <gafton@redhat.com>
- enable -asis in the config files so international keyboards will be better
  supported

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- /usr/lib/joe/* are config files

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- manhattan build

* Thu Dec 11 1997 Cristian Gafton <gafton@redhat.com>
- fixed termcap problems for terms other than 80x25
- added support for buildroot and BuildRoot

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc

