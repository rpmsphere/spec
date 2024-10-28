%undefine _debugsource_packages

Name:           cpdf
License:        GPLv3+
Group:          Productivity/Office/Other
Summary:        Lightweight pdf viewer
Version:        0.8.5
Release:        3
Source:         %{name}-%{version}.tbz2
BuildRequires:  qt4-devel
BuildRequires:  poppler-qt5-devel
URL:            https://build.opensuse.org/package/show?package=cpdf&project=home%3Apashov_d

%description
Merrily see PDFs without abusing your RAM. 

A Qt excersise pdf viewer which 
features most basic features 
found in most other viewers. 
        
%prep
%setup -q 
sed -i 's|poppler/qt4|poppler/qt5|' %{name}.pro
sed -i 's|poppler-qt4|poppler-qt5|' *.h %{name}.pro
sed -i '/found = spage->search/i double pleft=place.left();double ptop=place.top();double pright=place.right();double pbottom=place.bottom();' bpage.cxx dcm.cxx
sed -i 's|txt, place, Poppler|txt, pleft, ptop, pright, pbottom, Poppler|' bpage.cxx dcm.cxx

%build
qmake-qt4 prefix=%{_prefix} docspref=%{_defaultdocdir} cpdf.pro
%__make %{?jobs:-j%jobs}

%install
%__make INSTALL_ROOT=%{buildroot} install
%__chmod +x %{buildroot}%{_datadir}/applications/cpdf.desktop

%files
%{_bindir}/cpdf
%{_datadir}/applications/cpdf.desktop
%{_defaultdocdir}/cpdf
%{_datadir}/icons/hicolor

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.5
- Rebuilt for Fedora
* Tue Feb  8 2011 d.pashov@gmail.com
-The caching broke the auto-reloading. fixed now.
* Mon Feb  7 2011 d.pashov@gmail.com
-The beginning of the next page is not shown any longer in the presentation mode.
  This was discvered late because it only appears if the screen is more square
  than the page and these screens are rare nowdays.
* Mon Feb  7 2011 d.pashov@gmail.com
-The pages restored from cache did not include links. Fixed now.
* Sun Feb  6 2011 d.pashov@gmail.com
-The buttons' icons are now bundled in the executable
* Sat Feb  5 2011 d.pashov@gmail.com
-Tipped by Fedora fixed the location of the document files.
* Sat Feb  5 2011 d.pashov@gmail.com
-Second try. Now only for Fedora and Mandriva since RHEL5 is hopeless.
* Sat Feb  5 2011 d.pashov@gmail.com
-Firt attempt to compile on RHEL/Fedora derivatives.
* Sat Feb  5 2011 d.pashov@gmail.com
-Introduced the caching again. Still basic linear overwritting of fixed size
  but quite noticeable especialy in presentation mode.
-Fixed some typos
* Fri Jan 14 2011 d.pashov@gmail.com
-Bug in the redrawing on zoom/scroll was fixed.
* Wed Dec 22 2010 d.pashov@gmail.com
-Since the threaded rendering was introduced
  the search highlighters bacame fully opaque on first appearance.
  This was a bug which is now fixed.
* Fri Dec 17 2010 d.pashov@gmail.com
-Small regression fix. The total number of pages is visible again.
* Fri Dec 17 2010 d.pashov@gmail.com
- The rendering pdf->QImages is now done is separate threads.
  As a result scrolling and zooming feels much snappier.
  This is interesting because in fact it is slower now because waiting time of a few ds is introduced.
  The memory required during continuous zooming or scrolling at rates between 1 and 128 steps/s
  especially near the high limit, may increase the memory footprint substantially. Fortunately it should be back to normal  in about a second.
* Wed Dec 15 2010 d.pashov@gmail.com
-Bugfix: the total number of pages should change
  when the reloaded document's size changes
* Tue Dec 14 2010 d.pashov@gmail.com
- Not building with -g anymore.
- SSE2 added on x86_64.
* Mon Dec 13 2010 d.pashov@gmail.com
-A workaround for a bug in libqt4-4.7.1-150.2.x86_64. See the NOTE in dsa.cxx
* Mon Dec 13 2010 d.pashov@gmail.com
-fixed the spec as expected
* Mon Dec 13 2010 d.pashov@gmail.com
-Adding maemo to the build
* Sun Dec  5 2010 d.pashov@gmail.com
-A few typos
* Sun Dec  5 2010 d.pashov@gmail.com
-Fixed the calculation of dpi which was causing the page separation to vary.
-Fixed the zoom line.
* Sun Dec  5 2010 d.pashov@gmail.com
-Bugfixes/improvements in the handling of single page documents.
* Wed Dec  1 2010 d.pashov@gmail.com
-Added README file and few more shortcuts.
* Tue Nov 30 2010 d.pashov@gmail.com
-Fixed resizing issue when a file is reopened after another is resized.
-Fixed opening 1-page documents.
-Fixed repositioning on teturn from presentation mode.
* Tue Nov 30 2010 d.pashov@gmail.com
-Fixed the installation
* Tue Nov 30 2010 d.pashov@gmail.com
- Mouse scroll flips slides in presentation mode.
- The grand toolbar is split again. Ctrl+H still works as before.
- The buttons are now QActions.
- The open menu is part of the button.
- F5 and F7 shortcuts are swapped. Had to be done from th beginning.
  F5 is for presentation. F7 for fullscreen reading.
- The shortcuts for focusing on the search/goto/zoom lines now also select the content.
* Tue Nov 30 2010 d.pashov@gmail.com
-Tooltips added.
* Mon Nov 29 2010 d.pashov@gmail.com
-Added the ability to open arbitrary number of files from the command line.
  Each one is in separate process.
-Icons from the oxygen icon theme will be used unless compiled with -Uicons .
* Sun Nov 28 2010 d.pashov@gmail.com
-Open menu and recent files introduced. Starting with empty args will try to open the last used file.
* Sun Nov 28 2010 d.pashov@gmail.com
-Improved search highlighting of the search results.
-Now the main window resizes to the corret size on open.
* Sat Nov 27 2010 d.pashov@gmail.com
-The page counter starts from 1 by default now but is configurable;
* Sat Nov 27 2010 d.pashov@gmail.com
-Fixed the search and added primitive masking for better visualisation of the results
-A shortcut for hiding the toolbar was added CTRL+H
* Fri Nov 26 2010 d.pashov@gmail.com
-A major reshuffling.
* Sun Nov 21 2010 d.pashov@gmail.com
-The open button is fixed.
-Esc and q added for exitting from fullscreen mode.
* Sat Nov 20 2010 d.pashov@gmail.com
- Increased crash resistence by adding a bunch of checks.
- Search as expected. No unnecesary page jumps.
  Highlight past and present results differently.
  Find Next (F3)
- Some architectural changes.
- Buttons for more actions added.
* Fri Nov 19 2010 d.pashov@gmail.com
- Cursor shape awareness
- Basic printing capability //ctrl+p
- Zooming fixed
* Thu Nov 18 2010 d.pashov@gmail.com
-Added compatibility macros. Compiles with Qt 4.5.3 from openSUSE 11.2
* Thu Nov 18 2010 d.pashov@gmail.com
  New features:
- moving the document with the mouse
- text and image extraction
- the button flatness is user configurable, look in ~/.config/cpdf/cpdf.conf
* Thu Nov 18 2010 d.pashov@gmail.com
  Fixed aligning in presentation mode (f7).
* Thu Nov 18 2010 d.pashov@gmail.com
  Stability fixes.
  Smarter caching for slow page switching (e.g. presentation).
