Name:           pdftohtml
BuildRequires:  gcc-c++
Summary:        PDF to HTML Converter
Version:        0.36
Release:        160.1
# % define version 0_35
Group:          Productivity/Publishing/PDF
#Requires:   xpdf
Obsoletes:      pdf2html
Provides:       pdf2html
License:        LGPL v2.1 or later
URL:            https://pdftohtml.sourceforge.net/
Source0:        %name-%{version}.tar.bz2
Patch0:         pdftohtml-tmpfile.diff
Patch1:         xpdf-CESA-2004-007.diff
Patch2:         %{name}-HtmlLinks.h.patch
# Patch1:       pdf2html-0.35.diff
Patch10:        libgoo-sizet.patch
Patch12:        xpdf2-underflow.patch
Patch13:        xpdf-3.00pl2.patch
Patch14:        xpdf-decrypt.patch
Patch15:        xpdf-JBIG2Stream.patch
Patch16:        xpdf-Stream.patch
Patch17:        xpdf-MOAB-06-01-2007.patch
Patch18:        xpdf-3.00-CVE-2007-3387.patch
Patch19:        xpdf-CVE-2007-5392.patch
Patch20:        xpdf-CVE-2007-5393.patch
Patch21:        xpdf-CVE-2007-4352.patch

%description
pdftohtml is a command-line converter to turn PDF files (Portable
Document Format) into the HTML file format. Fine-tuning is possible
with various command-line switches.

Authors:
--------
    Rainer Dorsch <rainer.dorsch@informatik.uni-stuttgart.de>

%define INSTALL install -m755
%define INSTALL_SCRIPT install -m755
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644

%prep
%setup -q
%patch0 -p1 -b .temp
%patch10 -p 1 -b .goosizet
%patch1
%patch2
cd xpdf
%patch12 -p 2 -b .underflow
%patch13 -p1
%patch14 -p 0 -b .decrypt
cd ..
%patch15 
%patch16
%patch17
%patch18 -p1
%patch19
%patch20
%patch21

%build
#CFLAGS=$RPM_OPT_FLAGS \
#  ./configure --prefix=/usr %{_target_cpu}-suse-linux-gnu
# LDFLAGS=-s
# make CXX=g++ "CFLAGS=$RPM_OPT_FLAGS" prefix=/usr 
make CXX=g++ DEBUG="$RPM_OPT_FLAGS" prefix=/usr 

%install
rm -fr $RPM_BUILD_ROOT
%{INSTALL} -Dm755 pdftohtml $RPM_BUILD_ROOT/usr/bin/pdf2html
# make install prefix=$RPM_BUILD_ROOT/usr
# make install.man

%clean
rm -fr $RPM_BUILD_ROOT

%files
%doc AUTHORS BUGS COPYING CHANGES README
%{_bindir}/*

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.36
- Rebuilt for Fedora
* Mon Nov  5 2007 lrupp@suse.de
- fixes for the following security bugs (see #335637 for details):
  + CVE-2007-4352
  + CVE-2007-5392
  + CVE-2007-5393
- bzip the source
* Tue Jul 31 2007 lnussel@suse.de
- fix xpdf buffer overflow (#291690, CVE-2007-3387)
* Mon Jan 15 2007 lrupp@suse.de
- added MOAB-06-01-2007 patch (233113)
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Dec 15 2005 lrupp@suse.de
- fixed overflows found by Chris Evans and similiar ones
  no loop nor segfault with "bad pdfs" anymore - just exit
  see (#137156) for more details
* Tue Dec  6 2005 lrupp@suse.de
- fixed xpdf overflow CVE-2005-3193 (#137156)
- added more files to doc
* Tue Oct 18 2005 lrupp@suse.de
- added pdftohtml-HtmlLinks.h.patch to avoid errors on gcc4.1
- removed 'rm -rf $RPM_BUILD_ROOT' from %%install
* Thu Sep 29 2005 dmueller@suse.de
- add norootforbuild
* Wed Jan 19 2005 ke@suse.de
- New xpdf-decrypt.patch provided by upstream author to fix
  CAN-2005-0064 [#49840].
* Fri Jan 14 2005 ke@suse.de
- Apply xpdf-decrypt.patch to fix buffer overflow CAN-2005-0064
  [#49840].
* Mon Jan 10 2005 meissner@suse.de
- Applied xpdf security patch. CAN-2004-1125/#49463
* Wed Nov  3 2004 ke@suse.de
- Continue with fixing arithmetic flaws; using patches provided by
  Marcus Meissner [#43082].
* Mon Oct 18 2004 meissner@suse.de
- Added yet another sizeof() check that was missed (#44963)
* Wed Sep 29 2004 thomas@suse.de
- added fix for integer overflows in xpdf code
* Fri Jul 25 2003 ke@suse.de
- Add Obsoletes/Provides for pdf2html; reported by Adrian Schroeter.
* Wed Jul 16 2003 ke@suse.de
- Update to version 0.35:
  * Add support for different Ghostscript output devices (-dev).
  * Update Xpdf to 2.02 (security fix).
  * A couple of fixes and tweaks for better output.
  * Fix bug which caused bold to spread from one sentence to the entire
    document.
  * Support for document outlines (bookmarks).
* Tue Jul  1 2003 coolo@suse.de
- fix build for debug
* Wed Jan 15 2003 ke@suse.de
- Update to version 0.34:
  * Better HTML 4.01 compliance.
  * Add meta author, keywords and date.
  * Add mechanism for correct charsets.
  * Fix bug with links pointing nowhere for '-c -noframes'.
  * Fix bug with page numbering.
  * Fix bug with collapsing text for '-c -noframes -i'.
  * Update Xpdf to 2.01.
* Wed Jul 10 2002 ke@suse.de
- Update to version 0.34:
  * Bugfixes
  * Add pdf-vector drawings extraction
  * output for XML post-processing
  * zoom option
  * experimental ability to specify output encoding (UTF-8 might work)
  * ability to specify user/master password
  * fix core dump on documents with type 3 fonts only
  * fix bug with inline images not being handled properly
  * Ghostscript is executed from the program itself, no need for
    external script
  * ps output (for complex mode) is produced by pdftohtml, got rid of pdftops
  * several memory leaks fixed (should not crash on large files now)
  * join multiple <b></b>'s and <i></i>'s together
  * command line option to extract hidden text
  * parts of hrefs (links) are joined together (just like <b> and <i>)
  * paragraphs joined together
  * updated Xpdf to 1.01
  * can produce noframes (single html file) output for complex mode
- goo/gfile.c: Make sure to use mkstemp instead of tmpnam.
* Sun Dec 10 2000 schwab@suse.de
- Fix missing declarations.
* Tue Apr 11 2000 ke@suse.de
- make version 0.21 an official package.
* Tue Feb 15 2000 ke@suse.de
- Initial package: version 0.20.
