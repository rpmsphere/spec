Name: pccts
Version: 1.33mr33
Release: 16.1
Source: pccts133mr33.tar.gz
Patch0: pccts-syntax.patch
URL: http://www.polhode.com/pccts.html
License: Public domain
Group: Development/Tools
Summary: The Purdue Compiler-Compiler Tool Set

%description
The Purdue Compiler-Compiler Tool Set (PCCTS) is a set of public
domain software tools designed to facilitate the implementation of
compilers and other translation systems.  These tools currently
include antlr, dlg and support code.  In many ways, PCCTS is similar
to a highly integrated version of YACC and LEX; where antlr (ANother
Tool for Language Recognition) corresponds to YACC and dlg (DFA-based
Lexical analyzer Generator) functions like LEX.  However, PCCTS has
many additional features which make it easier to use for a wider range
of translation problems.

%prep
%setup -q -n pccts
%patch0 -p1 -b .dj

%build
mkdir -p $RPM_BUILD_DIR/pccts/man/man1
make COPT="$RPM_OPT_FLAGS -DPCCTS_USE_STDARG=1 -Wno-format-security" MANDIR=man %{?_smp_mflags} pccts manpages

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,share/man/man1,include/pccts}

install -m755 bin/antlr		$RPM_BUILD_ROOT%{_bindir}
install -m644 man/man1/antlr.1	$RPM_BUILD_ROOT%{_mandir}/man1
install -m755 bin/dlg		$RPM_BUILD_ROOT%{_bindir}
install -m644 man/man1/dlg.1		$RPM_BUILD_ROOT%{_mandir}/man1
install -m755 bin/genmk		$RPM_BUILD_ROOT%{_bindir}
install -m755 bin/sor		$RPM_BUILD_ROOT%{_bindir}

cp -a h/* $RPM_BUILD_ROOT%{_includedir}/pccts
cp -a sorcerer/h/*.h $RPM_BUILD_ROOT%{_includedir}/pccts

cp sorcerer/README README-sorcerer
cp sorcerer/UPDATES UPDATES-sorcerer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGES_FROM_131.txt CHANGES_FROM_133.txt KNOWN_PROBLEMS.txt
%doc NOTES.OS2 NOTES.bcc NOTES.msvc NOTES.watcom README RIGHTS
%doc history.ps history.txt README-sorcerer UPDATES-sorcerer
%{_bindir}/antlr
%{_bindir}/dlg
%{_bindir}/genmk
%{_bindir}/sor
%{_includedir}/pccts
%{_mandir}/*/*

%changelog
* Sun Oct 28 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.33mr33
- Rebuilt for Fedora
* Mon Jun 21 2004 Karsten Hopp <karsten@redhat.de> 1.33mr33-11
- update syntax patch for gcc-3.4
* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Thu Apr 22 2004 Karsten Hopp <karsten@redhat.de> 1.33mr33-9
- fix syntax (#115960)
* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Thu Jan 08 2004 Karsten Hopp <karsten@redhat.de> 1.33mr33-7
- add fix from Dave Jones
* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Thu May 22 2003 Jeremy Katz <katzj@redhat.com> 1.33mr33-5
- use stdarg.h instead of varargs.h
* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt
* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches
* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild
* Fri Jun 21 2002 Karsten Hopp <karsten@redhat.de> 1.33mr33-1
- update to bugfix release 1.33mr33
* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild
* Tue May 21 2002 Mike A. Harris <mharris@redhat.com> 1.33mr31-3
- Rebuilt in new environment to be able to build cdrdao
* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild
* Thu Jan 03 2002 Elliot Lee <sopwith@redhat.com>
- Update to MR31
* Mon May 21 2001 Tim Powers <timp@redhat.com>
- rebuilt for the .distro
* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt
* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt
* Wed Jun 21 2000 Tim Powers <timp@redhat.com>
- fixed man page location to be FHS comliant
* Mon May 8 2000 Tim Powers <timp@redhat.com>
- updated to MR22
* Tue Nov 2 1999 Tim Powers <timp@redhat.com>
- updated to MR20
* Sat Jul 10 1999 Tim Powers <timp@redhat.com>
- updated version to mr19
- updated URL
* Wed Jan 6 1999 Michael Maher <mike@redhat.com>
- built package for powertools
- fixed broken includes dir
* Mon Jan  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [pccts-1.33mr17-1]
- #212. (Changed in MR17)  Mac related changes by Kenji Tanaka
* Wed Dec 16 1998 Ryan Weaver <ryanw@infohwy.com>
- Updated to 1.33 Maintainance Release 16a
- Including sor and sorcerer header files.
- #211. (Changed in MR16a)  C++ style comment in dlg
- #210. (Changed in MR16a)  Sor accepts \r\n, \r, or \n for end-of-line
* Fri Dec 11 1998 Ryan Weaver <ryanw@infohwy.com>
- Updated to 1.33 Maintainance Release 16
- #209. (Changed in MR16) Name of files changed.
- #208. (Changed in MR16) Change in use of pccts #include files
- #207. (Changed in MR16) dlg reports an invalid range for: [\0x00-\0xff]
- #206. (Changed in MR16) Free zzFAILtext in ANTLRParser destructor
- #205. (Changed in MR16) DLGStringReset argument now const
* Mon Mar 23 1998 Elliot Lee <sopwith@cuc.edu> 1.33-4
- Include header files
* Mon Mar 23 1998 Elliot Lee <sopwith@cuc.edu> 1.33-3
- Repackage for glibc
