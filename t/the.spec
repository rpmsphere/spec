Name:           the
URL:            http://hessling-editor.sourceforge.net/
Version:        3.3rc7
Release:        1
Summary:        The Hessling Editor
License:        GFDL v1.1 ; GPL v2 or later
Group:          Productivity/Editors/Other
Source0:        http://dl.sourceforge.net/project/hessling-editor/hessling-editor/3.3%20Release%20Candidate%207/THE-3.3RC7.tar.gz
BuildRequires:  flex ncurses-devel regina-rexx-devel

%description
THE is a text editor that uses both command line commands and key
bindings to operate. It is intended to be similar to the VM/CMS System
Product Editor, XEDIT, and to Mansfield Software's, KEDIT.

%prep
%setup -q -n THE-3.3RC7

%build
./configure \
	--prefix=/usr \
	--mandir=%{_mandir} \
	--with-curses=ncurses \
	--with-rexx=regina
#make CFLAGS="$RPM_OPT_FLAGS" 
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc FAQ INSTALL README THE_Help.txt
%doc TODO COPYING HISTORY
%doc app*.htm*
%doc appendix.*
%doc doc/*
%{_bindir}/*
%{_datadir}/THE
%{_mandir}/man1/the.1.*

%changelog
* Sun Jul 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 3.3RC7
- Rebuilt for Fedora
* Tue Nov  3 2009 coolo@novell.com
- updated patches to apply with fuzz=0
* Sat Jan 12 2008 coolo@suse.de
- fix build with glibc 2.7
* Thu Mar 29 2007 meissner@suse.de
- added buildrequires ncurses-devel
* Thu Jan 18 2007 ssommer@suse.de
- fix same variable used twice error
- renamed the-3.1.spec -> the.spec
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue May 10 2005 meissner@suse.de
- use RPM_OPT_FLAGS. Fixed the bug the strict-aliasing
  code exposed (now using short instead of short*).
* Fri May 21 2004 ro@suse.de
- add -fno-strict-aliasing
* Mon Jan 12 2004 adrian@suse.de
- added %%defattr
* Tue Aug  5 2003 mge@suse.de
- fixed lib64 patch
* Tue Aug  5 2003 mge@suse.de
- added pdf-documentation
* Tue May 27 2003 ro@suse.de
- fix man-page installation and add man-page to filelist
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Fri Aug 16 2002 mge@suse.de
- fix building on 64bit
* Thu Aug 15 2002 mge@suse.de
- update to 3.1
* Mon May 27 2002 meissner@suse.de
- %%_lib fixes again. (coolos stuff did not work).
* Tue May 21 2002 coolo@suse.de
- update config and add lib64 patch
* Wed May  9 2001 mfabian@suse.de
- bzip2 sources
* Wed Jul  5 2000 mge@suse.de
- patch for regina 2.0.0
* Sun Feb 13 2000 mge@suse.de
- update to 3.0
- group tag
* Tue Dec 14 1999 uli@suse.de
- added "#undef PPC" to the.h to avoid conflicts with PPC identifier
* Mon Oct 25 1999 mge@suse.de
- moved /usr/THE to /usr/share/THE,
- removed useless "requires"
* Mon Oct 25 1999 mge@suse.de
- initial SuSE-RPM
