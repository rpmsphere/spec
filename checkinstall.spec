%global debug_package %{nil}
Name:           checkinstall
Summary:        "make install" Installation Tracker
Version:        1.6.2
Release:        1
License:        GPLv2+
Group:          Development/Tools
URL:            http://asic-linux.com.mx/~izto/checkinstall/
Source:         checkinstall-%{version}.tar.bz2
Source1:        checkinstall.in
Source2:        checkinstallrc-dist.in
Source3:	%{name}-1.6.1.zh_TW.po
Patch0:         checkinstall-glibc_bug.patch
Patch2:         checkinstall-destdir.patch
Patch3:         checkinstall-makefile_cleanup.patch
Patch6:         checkinstall-no_fortify_source.patch
Patch14:        checkinstall-translations.patch.bz2
Patch15:        checkinstall-install_paths.patch
Patch19:        checkinstall-scandir.patch
Patch10:        installwatch-glibc_minor.patch
Patch20:	checkinstall-ldflags.diff
Provides:       installwatch
Vendor:		Felipe Eduardo Sánchez Díaz Durán

%description
Uses installwatch to keep track of all files created or modified during
the run of an installation script like "make install". The information
is used to create a rpm package that holds all files installed by the
tracked installation. This makes it possible, for example, to remove
all files later with rpm -e package or to install the package on
another system.

%prep                                                                          
%setup -q
%patch0
%patch2
%patch3
%patch6
%patch14
%patch15
#%patch16
%patch19
%patch10
%patch -P 20 -p1
%__cp %{SOURCE1} %{SOURCE2} .
%__cp %{SOURCE3} locale/checkinstall-zh_TW.po
rm -f checkinstall checkinstallrc-dist
rename no.po nb.po locale/*.po
sed -i '33s|&&|;|' Makefile

%build
# 1. Must pass -m32/-m64 to linker to choose correct output format.
# 2. ld does not accept -mXX, only gcc. (=> LD=gcc)
# 3. Because installwatch uses _init as a symbol, must use -nostdlib
make CFLAGS="%{optflags}" LD="gcc" LDFLAGS="%optflags -nostdlib"

#%check
#cd installwatch
#make CFLAGS="%{optflags}" LD="gcc" LDFLAGS="%optflags -nostdlib" \
#	PREFIX=%{_prefix} LIBDIR=%{_libdir} DESTDIR=%{buildroot} test

%install
make CFLAGS="%{optflags}" LD="gcc" LDFLAGS="%optflags -nostdlib" \
	DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_prefix}/%_lib install
%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%config %attr(644,root,root) %{_sysconfdir}/checkinstallrc
%{_sysconfdir}/checkinstallrc-dist
%{_bindir}/installwatch
%{_libdir}/installwatch.so
%attr(555,root,root) %{_sbindir}/checkinstall
%{_sbindir}/makepak
%docdir /usr/share/doc/packages/checkinstall
##/usr/share/locale/es/LC_MESSAGES/checkinstall.mo
##%doc 

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.2
- Rebuild for Fedora
* Sat Feb  6 2010 jengelh@medozas.de
- Fix linker stage errors on sparc64 due to missing LDFLAGS
* Tue Jan  5 2010 pth@novell.com
- Override buildroot from command line.
* Wed Dec 30 2009 pth@novell.com
- Fix file list
* Mon Dec 28 2009 pth@novell.com
- Update to 1.6.2, the released version that contains support
  for the at-style functions of glibc.
* Wed Dec 16 2009 pth@novell.com
- Fix typo in scandir patch.
* Tue Dec 15 2009 pth@novell.com
- Don't use -t option for cp s older versions don't understand it.
* Mon Dec 14 2009 pth@suse.de
- Fix typo in checkinstall.in
* Mon Dec 14 2009 pth@novell.com
- Fix definition of Glibc minor version in installwatch/create_localedef.
- Fix patch for scandir/scandir64 declaration.
- Prototypes for scandir and scandir64 changed with glibc 2.10
  so modify patch to supply both old and new one depending on
  glibc version.
* Sun Dec 13 2009 pth@novell.com
- Compress tarball and patch with bzip2 to be able to build
  checkinstall on distributions that don't have xz.
* Mon Dec  7 2009 pth@suse.de
- Update to CVS from June to get the support of *at() function (bnc#432497).
- Adapt patches as needed.
- Pass rpmbuild the buildroot to use to override default (bnc#561317).
- Translations now use UTF-8 encoding where not already doing so.
- Change occurances of `` ikn checkinstall to $().
- Compress with xz instead of lzma.
* Wed Aug 26 2009 mls@suse.de
- make patch0 usage consistent
* Mon Jun  8 2009 ro@suse.de
- adapt to changed signature for functions scandir,scandir64
* Mon Apr 27 2009 pth@suse.de
- Catch calls to fchmodat (bnc#432497).
- Remove patch not applied anymore.
* Wed Aug 13 2008 ro@suse.de
- drop needsroot
* Thu Jul  3 2008 pth@suse.de
- Fix tmp race (bnc#404478)
* Fri Sep 14 2007 bk@suse.de
- Trivial: rpm does not allow "-" in version, skip them in proposal
* Thu Mar 29 2007 pth@suse.de
- Update to 1.6.1:
  - Fixed the famous getcwd() bug
  - Added translations for Indonesianj, Italian, Norwegian, German,
    Chinese, Japanese
- Fix installation paths
- Substitute paths in checkinstallrc-dist and checkinstll as
  configured for building.
- Make test work when DESTDIR is used.
* Sun Feb 11 2007 ro@suse.de
- build as root for now
* Wed Apr  5 2006 ro@suse.de
- use ssize_t as return type for readlink as in glibc
* Fri Mar 24 2006 ro@suse.de
- fix build on s390x
* Wed Mar  1 2006 bk@suse.de
- Fix package version proposal when retrieved from config.log
* Fri Feb 10 2006 bk@suse.de
- Fix avoid_buildroot_symlink.patch to set buildroot directory
* Thu Feb  9 2006 pth@suse.de
- Update to 1.6.0.
- Remove now obsolete patches.
* Thu Feb  2 2006 seife@suse.de
- fix the "installed but unpackaged files found" error
* Wed Feb  1 2006 pth@suse.de
- Use tag License instead of Copyright
- Create correct %%files sections
- Omit erroneous leading comma in Requires:
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Nov  7 2005 pth@suse.de
- Fix _all_ cases where /usr/lib was hard-coded.
* Mon Nov  7 2005 pth@suse.de
- Preload library from /usr/lib64 on biarch systems (fixes #132348)
* Wed Oct 19 2005 pth@suse.de
- Installwatch can't be compiled with _FORTIFY_SOURCE, so undefine it
* Fri Jul 29 2005 seife@suse.de
- fix the corrupted display after installation
* Thu Jul 28 2005 seife@suse.de
- fix path /usr/local/bin => /usr/bin
* Tue Jun 28 2005 pth@suse.de
- Update to 1.6.0beta4
- Use buildroot
- Use DESTDIR
- make it possible to pass in compiler flags
* Thu Apr  1 2004 bk@suse.de
- change checkinstallrc to assume a recent rpm-based distribution,
  (if you don't pass -R, the group is not set and rpm build fails)
* Mon Mar 22 2004 uli@suse.de
- installwatch.c: in multithreaded apps _init() seems not to be
  called when a new thread is started -> segfault; worked around
  by checking for sane func ptrs in every function using them
- update -> 1.6.0beta3
* Mon Sep  1 2003 uli@suse.de
- call installwatch with translation off (broken)
- replace /usr/doc with /usr/share/doc/packages as default doc path
* Wed Jul 30 2003 aj@suse.de
- Fix chown usage.
* Tue Jul 29 2003 uli@suse.de
- update -> 1.6.0beta2 (works with RPMv4)
* Wed Dec 11 2002 bk@suse.de
- disable old workarounds for s390/ppc glibc problems in 2.2.4/2.2.5
  (fixed with UL 2.2.5 CVS glibc), set LC_ALL to trigger it in case
  the bug shows up again.
* Fri Aug 30 2002 meissner@suse.de
- make sure the *64 functions are prototyped, or we
  get ftruncate64() creating terabyte files.
* Fri Jun 21 2002 bk@suse.de
- update to checkinstall 1.5.2
* Fri May 31 2002 ro@suse.de
- fix build on lib64 platforms
* Mon Jan 21 2002 bk@suse.de
- update to checkinstall 1.5.1, installwatch 0.6.3
* Fri Dec  7 2001 bk@suse.de
- cure some problems of the release on s390/ppc and enable test suite
* Mon Dec  3 2001 bk@suse.de
- update to version 1.5.0 release - fixes some file descriptor leaks
* Wed Nov  7 2001 bk@suse.de
- update to version 1.5.0beta2 - great updates, e.g. syscall trace
* Tue Oct 30 2001 bk@suse.de
- fix execute permissions of checkinstall script
* Mon Aug  6 2001 bk@suse.de
- update to version 1.4.1
* Sun Apr 15 2001 bk@suse.de
- update to version 1.3.1
* Sun Mar  4 2001 bk@suse.de
- initial package
