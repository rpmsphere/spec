Summary: epub viewer
Name: oxepubview
Version: 2.0
Release: 19X
License: commercial
Group: System/Publishing
#Source0: oxEpubView-%{version}.tar.gz
Source0: %{name}-%{version}-ox.tgz
#Source2: %{name}.png
#Source3: %{name}.xml
BuildRequires: desktop-file-utils, shared-mime-info
#Requires: oxzilla, oxzilla-epub,  oxzilla-jscollections
Requires: oxzilla, oxzilla-jscollections
BuildArch: noarch

%description
epub viewer using OXZilla.

%prep
rm -rf $RPM_BUILD_ROOT

#%setup -q -n oxEpubView-%{version}
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

#%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
#%__cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/pixmaps
%__cp %{_builddir}/%{name}-%{version}/oxepubview.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/

%{__mkdir_p} %{buildroot}%{_datadir}/applications
# Install desktop entry
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=OX EPub Reader 2.0
Name[zh_TW]=OX Epub 電子書閱讀器 2.0
Icon=%{_builddir}/%{name}-%{version}/Sources/oxepubview.png
Comment=ePub reader written in OXZilla
Comment[zh_TW]=利用 OXZilla 編寫的電子書閱讀器
Categories=Application;Utility;
Exec=%{name}
Terminal=false
Type=Application
Hidden=false
Encoding=UTF-8
Icon=%{name}
EOF

# install binary 
%__mkdir_p ${RPM_BUILD_ROOT}%{_bindir}/
%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/sh
#
# Copyright (C) 2011 OSS Integral Institute Co. Ltd. 
# All Rights Reserved.
# Author: Wilson Tien
#
# This small shell program is to unzip the epub files and call the necessary 
# program to read it
#
UNZIP=/usr/bin/unzip
EZIPDIR=/usr/share/ezips
# check to see whether fuse kernel module loaded
/sbin/lsmod|/bin/grep fuse > /dev/null
USEFUSE=\$?
# ezip ezipfile dir
# places ezipfile to dir
ezip(){
    if [ \${USEFUSE} = 0 ]; then
	/usr/bin/fuse-zip \$1 \$2
    else
        # There is no fuse-zip, have to use unzip stuff
	/usr/bin/unzip \$1 -d \$2
    fi
}

# unezip dir
# remove the dir
unezip() {
    [ \${USEFUSE} = 0 ] && /usr/bin/fusermount -u \$1
    /bin/rm -rf \$1
}

view_epub() {
    ebookname=\`/bin/basename \$1\`
    epubdir=\`/bin/mktemp -d\`
    ezip \$1 \${epubdir}
    if [ -z \${DEBUG} ]; then
	debugopt=
    else
	debugopt="&debug=\${DEBUG}"
    fi
	oxzilla -j /usr/lib/oxzilla/js/oxim_keyboard.js --noresize "/usr/share/oxepubview.oxz/oxepub.html?epubdir=\${epubdir}&ebookname=\${ebookname}\${debugopt}"
    unezip \${epubdir}
    
}

#make sure the dir for bookmark, notes, and highlights is there
mkdir -p /usr/share/content/ebook_extra
chmod 777 /usr/share/content/ebook_extra
(view_epub \$1)
EOF
chmod +x ${RPM_BUILD_ROOT}%{_bindir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
#%__cp -a src/* $RPM_BUILD_ROOT%{_datadir}/%{name}/

# Now, we are going to zip+encode the src dir
cd src
TMPFILE=`/bin/mktemp`.zip
/usr/bin/zip -r ${TMPFILE} *
oxzencode ${TMPFILE} $RPM_BUILD_ROOT%{_datadir}/%{name}.oxz
rm -rf ${TMPFILE}

%post
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :


%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
#%{_datadir}/%{name}/*
%{_datadir}/%{name}.oxz
%{_datadir}/pixmaps/%{name}.png
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Fri Jul  8 2011 Wilson Tien <wilson@ossii.com.tw> - 2.0-19X
- oxepubview.spec: deliverables change to OXZ file so details of the oxzilla
  application code is invisible.

* Thu Jun 09 2011 Chris Lin <chris@ossii.com.tw> - 2.0-18
- src/js/Page.js: modify double page mode turning next page cause problem

* Mon Jun 07 2011 Chris Lin <chris@ossii.com.tw> - 2.0-17
- src/js/TouchSlide.js: join toolbar hide/show and forward ,backward callback Change back
- src/js/Page.js: modify 16:9 or 4:3 screen be can auto adjust
- src/js/oxepub.js: add panel_determine function to change panel css width and page
- src/js/readchapter.js: add img css adjust on line 83.

* Sat May 28 2011 Chris Lin <chris@ossii.com.tw> - 2.0-16
- src/js/Highlight.class.js: remove Touchslide unbind event prevent cause double touch page

* Fri May 27 2011 Wilson Tien <wilson@ossii.com.tw> - 2.0-15
- src/js/oxepub.js: if meta identifier does not have many children, simply 
  use NCX (ie. not gutenberg). 
- src/js/mark.js: fix a bug that should unbind bookmark delete click 
  function but unbind notes delete click function. 

* Wed May 25 2011 Wilson Tien <wilson@ossii.com.tw> - 2.0-14
- src/js/mark.js: fix with disable single/double page view mode and if making nores/bookmark on the 
previously made notes/bookmark, only do adding new notes/bookmark. 
- src/js/mark.js: add isallspace function when adding marks and notes input blank char not increase 
- src/js/page.js & src/js/callback.js: fix fast TouchScroll pages will cause blank page bug 
previously made notes/bookmark, only do adding new notes/bookmark. 

* Fri May 20 2011 Chris Lin <chris@ossii.com.tw> - 2.0-13
- modify TouchScroll bugs 

* Fri May 20 2011 Wilson Tien <wilson@ossii.com.tw> - 2.0-12
- src/js/chapter.js: chapter_fini() now do reset_window() to remove the 
  animation affect by previous view, o/w search result will be incorrect.

* Fri May 20 2011 Chris Lin <chris@ossii.com.tw> - 2.0-11
- Remove the Requires: oxzilla-epub.

* Thu May 19 2011 Chris Lin <chris@ossii.com.tw> - 2.0-10
- src/js/LoadHighlight.js: rewrite this code , each chapter load contain 
  box and then load highlight 
- src/js/Highlight.class.js rewrite this code , Perform highlight function 
- src/js/callback.js if searching turn off Highlight 
- src/js/mouse_event.js remove archive
- add remove highlight

* Wed May 18 2011 Wilson Tien <wilson@ossii.com.tw> - 2.0-9
- src/js/readchapter.js: change all h1-h5 nodes to p node to solve the 
  problem of rendering slide problems. 
- src/js/page.js: clean up pagenumber when page_fini() to prevent 
  jump_realPage() uses pagenumber to decide whether really need a jump.

* Thu May 12 2011 Wilson Tien <wilson@ossii.com.tw> - 2.0-8
- src/js/mark.js: fix the bug for creating new bookmark and notes when using 
  vector length is no more reliable (ie. some deleting happened).

* Fri May  6 2011 Wilson Tien <wilson@ossii.com.tw> - 2.0-7
- oxepubview-2.0/src/js/page.js, oxepubview-2.0/src/js/oxepub.js,
  oxepubview-2.0/src/oxepub.html, oxepubview-2.0/src/js/loadmark.js: add in 
  double page view support. (also support bookmark/notes shown on double
  page view mode)

* Thu May  5 2011 Wilson Tien <wilson@ossii.com.tw> - 2.0-6
- oxepubview-2.0/src/js/loadmark.js, oxepubview-2.0/src/js/mark.js: bug 
  related to newly created notes/bookmark messed up name/content has been 
  fixed (a new field UID is added to the global notes/bookmark vector to 
  keep track the unique ID for this bookmark/notes).
- oxepubview-2.0/src/js/mark.js: all bookmark stuff are rewritten in a 
  simiar fashion like notes, so bookmark name is able to be modified now. 
- oxepubview-2.0/src/js/mark.js, oxepubview-2.0/src/oxepub.html: implement
  delete capability of bookmark and notes (by clicking trashcan icon).
- oxepubview-2.0/src/js/loadmark.js, oxepubview-2.0/src/js/page.js: all 
  bookmark/notes are sticked to BOX instead of CONTENT, ie., when the page 
  is viewed, then the corresponding bookmark/notes are created (by calling 
  show_all_{bookmark/notes}_in_current_page()). Therefore, when page is 
  shown, page_init() needs to be called, and when the current page is not 
  shown, page_fini() needs to be called to do the clean up work (in our case,
  to remove all bookmark/notes created for the page).
- oxepubview-2.0/src/js/readChapter.js: implement the capability when HTML 
  is loaded to really do view, <a/> and <b/> tags are removed (since they 
  will make highlight work almost impossible).
- oxepubview-2.0/src/oxepub.html: some icons related to notes/bookmark are 
  redrawn. 

* Thu Apr 28 2011 wilson Tien <wilson@ossii.com.tw> - 2.0-5
- (oxepubview-2.0/src/js/TouchSlide.js): disable viewing box mousemove for 
  sliding, o/w mouseup will delay for a long time.

* Mon Apr 25 2011 wilson Tien <wilson@ossii.com.tw> - 2.0-4
- (oxepubview.spec, oxepubview-2.0/src/layout_1024x600.css): handle default 
  1024x600 resolution, no scrollbar.

* Mon Apr 25 2011 wilson Tien <wilson@ossii.com.tw> - 2.0-3
- fix show notes bugs.

* Fri Apr 22 2011 wilson Tien <wilson@ossii.com.tw> - 2.0-2
- add `loading' image in the beginning so user knows the reader is still 
  reading content.

* Thu Apr 21 2011 Wilson Tien <wilson@ossii.com.tw> - 2.0-1
- add ebook content background. Remove some unused files.

* Thu Apr 21 2011 wilson Tien <wilson@ossii.com.tw> - 2.0-0
- Version 2.0. Rewrite everything. discard the Version 1 epub oxzilla plugin. 
  We now support bookmark/notes and some highlight now. However, to be able to
  support pages, we decide not to support resize.

* Thu Feb 10 2011 Wilson Tien <wilson@ossii.com.tw> - 1.1-8
- (index.html, oxepubview.js, layout_800x480.css, layout_1024x600.css): move 
  toolbar to top. embed the search box inside toolbar. auto focus on seach
  input box when search button is chosen.
- oxepubview.js: fix problem inside search (make use of the unpublished webkit
  window.find() 4th argument). it now supports wrap-search.

* Wed Feb  9 2011 Wilson Tien <wilson@ossii.com.tw> - 1.1-7
- oxepubview.js: according to oxzilla's change, add line to loadmodule() 
  epub plugin.
- (index.html, oxepubview.js): change all buttons to icons buttons. make
  search to automatically enable soft keyboard when clicked.

* Mon Jan 31 2011 Wilson Tien <wilson@ossii.com.tw> - 1.1-6
- disable bookmark functionality for now.

* Wed Jan 26 2011 Wilson Tien <wilson@ossii.com.tw> - 1.1-5
- if not 800x480 or 1024x600, use 1024x600 as default.

* Wed Jan 26 2011 wilson Tien <wilson@ossii.com.tw> - 1.1-4
- (index.html, oxepubview.js): Move javascript code to independent js file. 
- (oxepubview.js, layout_800x480.css, layout_1024x600): Change the viewer to 
  fit in both 800x480 and 1024x600 devices (therefore two style css were 
  created, and old style css file was deleted). Javascript code has changed 
  a bit to detect window size and use different style css.
* Tue Dec 07 2010 Wei-Lun Chao <bluebat@member.fsf.org> 1.1-2
- Add BuildRequires
* Mon Jun 28 2010 Harry <harry@ossii.com.tw> 1.1-1
- Initial build
* Mon Jun 21 2010 Harry <harry@ossii.com.tw> 1.0-1
- Initial build
* Mon Jun 7 2010 Harry <harry@ossii.com.tw> 0.9-2
- Initial build
* Fri Jun 4 2010 Harry <harry@ossii.com.tw> 0.9-1
- Initial build
* Thu May 13 2010 Harry <harry@ossii.com.tw> 0.8-1
- Initial build
* Tue Mar 30 2010 Harry <harry@ossii.com.tw> 0.7-1
- Initial build
* Thu Mar 25 2010 Harry <harry@ossii.com.tw> 0.6-1
- Initial build
* Wed Mar 24 2010 Harry <harry@ossii.com.tw> 0.5-1
- Initial build
* Tue Mar 23 2010 Harry <harry@ossii.com.tw> 0.4-1
- Initial build
* Fri Mar 19 2010 Harry <harry@ossii.com.tw> 0.3-1
- Initial build
* Thu Feb 4 2010 Harry <harry@ossii.com.tw> 0.2-2
- rebuild
- modify the desktop file
* Fri Jan 29 2010 Harry <harry@ossii.com.tw> 0.2-1
- Initial build
* Fri Jan 15 2010 Harry <harry@ossii.com.tw> 0.1-1
- Initial build
