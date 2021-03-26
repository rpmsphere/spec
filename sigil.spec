Name:			sigil
Version:		0.4.2
Release:		2%{?dist}
Summary:		A WYSIWYG ebook editor
Group:			Productivity/Other
License:		GPLv3
URL:			http://code.google.com/p/sigil/
Source0:		http://sigil.googlecode.com/files/Sigil-%{version}-Code.zip
Source1:		lang_tw.qm
BuildRequires:		cmake, freetype-devel, qt4-devel
Patch0:			sigil-qt-4.6.3.patch
Patch1:			sigil-0.4.2-lang.patch

%description
Sigil is a multi-platform WYSIWYG ebook editor. It is designed to edit books in ePub format. 
Now what does it have to offer...

    * Free and open source software under GPLv3
    * Multi-platform: runs on Windows, Linux and Mac
    * Full Unicode support: everything you see in Sigil is in UTF-16
    * Full EPUB spec support
    * WYSIWYG editing
    * Multiple Views: Book View, Code View and Split View
    * Metadata editor with full support for all possible metadata entries (more than 200) with full descriptions for each
    * Table Of Contents editor
    * Multi-level TOC support
    * Book View fully supports the display of any XHTML document possible under the OPS spec
    * SVG support
    * Basic XPGT support
    * Advanced automatic conversion of all imported documents to Unicode
    * Currently imports TXT, HTML and EPUB files; more will be added with time
    * Currently exports EPUB and SGF (Sigil native format); more will be added with time
    * Embedded HTML Tidy; all imported documents are thoroughly cleaned; changing views cleans the document so no matter 
      how much you screw up your code, it will fix it (usually )
    * An actually usable user interface
    * Native C++ application
    * Bugs :)
    * And a lot more... 

%prep
%setup -q -c
%patch0 -p1
%patch1

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

install -Dm644 src/Sigil/Resource_Files/icon/app_icon_48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

#Desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Sigil
Comment=ebook editor
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Categories=Development;
EOF

install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/lang/zh_TW.qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc COPYING.txt ChangeLog.txt INSTALL.txt README.txt
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Thu Oct 27 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2-1.ossii
    - Update to 0.4.2

* Tue Mar 02 2010 Harry Chen <harry.chen@ossii.com.tw> - 0.1.9-1.ossii
    - Update to 0.1.9

* Wed Nov 25 2009 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.4-1.ossii
    - Update to 0.1.4

* Tue Sep 29 2009 Kami <kami@ossii.com.tw> Sigil v0.1.3 - ossii
    - Build for OSSII

* Wed Sep 02 2009 Sigil v0.1.3
    - implemented a work-around for a bug in Qt causing documents with "us-ascii" encoding
    specified in the XML declaration to crash Sigil (issue #109)
    - resource path updating rewritten; should be more robust
    - fixed an issue where EPUB files from Google Books could not be opened (issue #106)
    - fixed regression for storing the folder from which the user last imported an image (issue #105)  
    - refactored HTML file import resource loading: should be a lot more robust now
    - fixed an issue with loading HTML files that reference the same images multiple times (issue #90)
    - implemented non-live View position synchronization; the Views are now synced
    by HTML element: moving the caret in one View will center the other View (upon switching)
    to the same HTML element that held the caret in the first View (issue #8)
    - newlines are now removed from TOC headings to avoid rendering problems in ADE (issue #96)
    - Sigil now creates a unique book identifier (if one is not provided by the user)
    using the UUID standard instead of a radnom sequence of characters and numbers;
    the old "SigilGEN" scheme is replaced with "UUID"
    - initial support for calibre interoperability (issue #94)
    - book updates from TOC editor are now faster and have a much smaller memory overhead
    - fixed issue with removing headings from TOC in TOC editor (issue #88, part 2 and issue #21);
    also made TOC editor updates to headings MUCH more robust
    - all headings are now by default included in TOC... heuristics for "guessing" which
    headings the users wants have been removed (issue #88, part 1)
    - fixed critical issue with Sigil hanging when loading certain SGF files (issue #87)
    - fixed rare issue with duplicate image loading (issue #86)
    - implemented a workaround for a webkit bug causing the first character of a heading
    created after a chapter break to be displayed incorrectly (issue #78)
    - the "makedmg" target for Macs is not build by default anymore and needs to be
    invoked directly; this was done to speed rebuilds
    - Macs now have a standard multiple document interface: opening a new file opens it
    in a new window, not in the old one (issue #22)
    - fixed a bug with warning dialog not informing the user of unsaved changes
    if he tried to load from the recent files list

* Wed Aug 12 2009 Sigil v0.1.2
    - added the ability to specify the main publication identifier directly,
    through the "CustomID" basic metadata property (issue #3)
    - fixed a bug with warning dialog not informing the user of unsaved changes
    when editing in code view (issue #30)
    - Sigil is now a universal Mac application (ppc and i386, in 32bit) (issue #5)
    - implemented a workaround for a bug in QTextCodec causing bad HTML codec detection (issue #74)
    - SVG elements are not removed anymore (issue #24)
    - inter-document HTML links are now fully supported (issue #53)
    - fixed rare issue where CSS style rules could get duplicated when changing views
    - fixed issue with inline style tags in OPS documents not being loaded (issue #58)
    - Sigil can now accept a file to load as the first command line argument; this also
    provides support for "Open With..." operating system features (issue #63)
    - fixed an issue where the reported build time in the About dialog was actually the execution
    time (issue #65)
    - loading of missing files in the recent files list is now improved (issue #57)
    - fixed a rare issue where the wrong view could be sent to the printer on print actions
    - Sigil now creates a guide element with a cover page in the OPF if the content of the first
    OPS document is less than 1000 characters long (issue #48)
    - support for importing UTF-16 encoded documents (not just UTF-8)
    - provided install target for linux; the binary is now also named "sigil"
    (lower case 's') on Unix systems (except Mac) for the sake of convention (issue #46)
    - removed dependency on "data" directory (issue #51)

* Thu Aug 06 2009 Sigil v0.1.1
    - applied provided patch for NetBSD support
    - fixed issue with loading images in HTML and EPUB docs that have regexp special characters
    in filenames. (issue #39)
    - if headings have the 'title' attribute set, it is now used as the TOC text entry. (issue #26)
    - tags are now removed from headings before they are converted to TOC entries (issue #47)
    - Sigil now remembers the last folder from which you loaded an image (issue #34)
    - choosing 'cancel' in TOC editor now no longer forces the views to update
    - fixed bug with new headings getting existing IDs. (issue #36)
    - printing support! new file menu actions: "print" and "print preview"
    - fixed an issue when sometimes switching between views didn't enable/disable appropriate actions
    - fixed an issue with mixed-up CSS classes on Mac and Linux (issue #16)
    - added line numbering for Code View (issue #9)
    - added current line highlighting for Code View 
    - fixed crashing bug with some calibre generated epubs (issue #16)

* Sat Aug 01 2009 Sigil v0.1.0
    - initial release
