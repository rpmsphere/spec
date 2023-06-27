%undefine _debugsource_packages

Name:           fox17
Version:        1.7.82
Release:        1
License:        LGPL-3.0+
Summary:        Shared Libraries for the FOX Toolkit
URL:            https://www.fox-toolkit.org/
Group:          Development/Languages/C and C++
Source:         ftp://ftp.fox-toolkit.org/pub/fox-%version.tar.gz
Source1:        calculator.png
Source2:        pathfinder.png
Source3:        adie.png
Source5:        adie.desktop
Source6:        calculator.desktop
Source7:        pathfinder.desktop
BuildRequires:  autoconf
BuildRequires:  bzip2
BuildRequires:  cups-devel
BuildRequires:  doxygen
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%define _adie_version       3.1.0
%define _shutterbug_version 2.1.0
%define _calculator_version 2.1.0
%define _pathfinder_version 1.1.0
%define _controlpanel_version 1.1.0
BuildRequires:  libGLU-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXi-devel
BuildRequires:  xorg-x11-proto-devel xorg-x11-xtrans-devel libX11-devel
Provides: fox

%description
FOX is a C++-based library for graphical user interface development.

FOX supports modern GUI features such as drag-and-drop, tooltips, tab
books, tree lists, icons, multiple document interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for 3D
graphics. Subclassing of basic FOX widgets allows for easy extension
beyond the built-in widgets by application writers.

%package devel
Summary:        Development Files and Documentation for the FOX GUI Toolkit 1.7
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       bzip2-devel
Requires:       libjpeg-devel
Requires:       libpng-devel
Requires:       libtiff-devel
Provides:       fox-devel = %{version}
Requires:       mesa-libGL-devel
Conflicts:      fox-devel

%description devel
FOX is a C++-based library for graphical user interface development.

The devel package contains the files necessary to develop applications
using the FOX GUI toolkit: the header files, the reswrap resource
compiler, and manual pages.

%package static
Summary:        A version of the FOX GUI toolkit for static linking
Group:          Development/Libraries/C and C++
Requires:       %name-devel = %version

%description static
The fox-static package contains the files necessary to link applications
to the FOX GUI toolkit statically (rather than dynamically). Statically
linked applications do not require the library to be installed on the system
running the application.

%package doc
Summary:        Documentation for the FOX Toolkit 1.7
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
FOX is a C++-based library for graphical user interface development.

The doc subpackage contains the HTML documentation to the FOX toolkit 1.7.

%package utils
Summary:        Utility applications based on fox
Group:          Productivity/Editors/Other

%description utils
This package contains some utility applications based on fox.

%prep
%setup -q -n fox-%{version}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags} -DNDEBUG -Wuninitialized -fno-strict-aliasing"
sed -i -e 's|include/lib|include/lib64|' -e 's|-Wall|-Wall -fPIC|' configure
%configure  \
    --enable-threadsafe \
    --enable-release \
    --enable-cups \
    --with-xft \
    --with-x \
    --with-xcursor \
    --with-xrender \
    --with-xrandr \
    --with-opengl \
    --with-shape \
    --with-xshm \
    --with-xim \
    --without-profiling

%{__make} %{?_smp_mflags}

%install
%makeinstall
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}/html
# FIXME: to be done via configure
if [ -d %{buildroot}%{_datadir}/doc/fox-1.7 ]; then
    mv %{buildroot}%{_datadir}/doc/fox-1.7/* %{buildroot}%{_defaultdocdir}/%{name}/
    rm -rf %{buildroot}%{_datadir}/doc/fox-1.7
fi
install -m644 ADDITIONS AUTHORS LICENSE* README TRACING index.html %{buildroot}%{_defaultdocdir}/%{name}/
%{__mv} %{buildroot}%{_bindir}/reswrap %{buildroot}%{_bindir}/reswrap17
%{__mv} %{buildroot}%{_mandir}/man1/reswrap.1 %{buildroot}%{_mandir}/man1/reswrap17.1
# install desktop files for example applications
mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}
install -m 644 %SOURCE1 %{buildroot}%{_datadir}/pixmaps/
install -m 644 %SOURCE2 %{buildroot}%{_datadir}/pixmaps/
install -m 644 %SOURCE3 %{buildroot}%{_datadir}/pixmaps/
install -m 644 %SOURCE5 %{buildroot}%{_datadir}/applications/
install -m 644 %SOURCE6 %{buildroot}%{_datadir}/applications/
install -m 644 %SOURCE7 %{buildroot}%{_datadir}/applications/

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post devel
test -f %{_bindir}/fox-config || ln -s fox17-config %{_bindir}/fox-config
test -f %{_bindir}/reswrap || ln -s reswrap17 %{_bindir}/reswrap
test -f %{_mandir}/man1/reswrap.1.gz || ln -s reswrap17.1.gz %{_mandir}/man1/reswrap.1.gz

%files doc
%doc %{_defaultdocdir}/%{name}

%files
%{_libdir}/libCHART-*.so.*
%{_libdir}/libFOX-*.so.*

%files devel
%{_mandir}/man1/reswrap17*
%{_bindir}/reswrap17
%{_bindir}/fox-config
%{_includedir}/fox-*/
%{_libdir}/pkgconfig/fox*.pc
#{_libdir}/libCHART-*.la
#{_libdir}/libFOX-*.la
%{_libdir}/libFOX-*.so
%{_libdir}/libCHART-*.so

%files static
%{_libdir}/libFOX-*.a
%{_libdir}/libCHART-*.a

%files utils
%{_bindir}/adie
%{_bindir}/Adie.stx
%{_mandir}/man1/adie.1*
%{_datadir}/applications/adie.desktop
%{_datadir}/pixmaps/adie.png
%{_bindir}/calculator
%{_mandir}/man1/calculator.1*
%{_datadir}/applications/calculator.desktop
%{_datadir}/pixmaps/calculator.png
%{_bindir}/PathFinder
%{_mandir}/man1/PathFinder.1*
%{_datadir}/applications/pathfinder.desktop
%{_datadir}/pixmaps/pathfinder.png
%{_bindir}/shutterbug
%{_mandir}/man1/shutterbug.1*
%{_bindir}/ControlPanel
%{_mandir}/man1/ControlPanel.1*

%changelog
* Sun May 21 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7.82
- Rebuilt for Fedora
* Mon Dec 15 2014 lars@linux-schulserver.de
- the -devel-static package must require the -devel-package,
  see https://en.opensuse.org/openSUSE:Packaging_guidelines#Exception
* Mon Nov 17 2014 lars@linux-schulserver.de
- update to 1.7.50:
  + Major changes in the regular expression engine. New API amatch()
    for anchored match, and new API search which replaces match().
    More sensible parameter order and moved some flags from run-time
    to compile time.
  + Internals of FXRex are now ready for UTF8 matching; however parsing
    part will need to follow before these new capabilities can be put to use.
  + FXRex::substitute() now interprets the usual escape sequences when
    creating replacement pattern from regular expression match captures.
  + Speedup in FXText getByte(), getChar(), etc. by introduction of
    branch-free handling of gapped-buffer accesses.
  + Moved hard-wired search and replace dialogs out of FXText and into
    Adie text editor; this is part of the FXText widget slim-down program.
  + Adie text editor search and replace improvements.
    Basically, stream-lines mouse-free usability.
  + Adie incremental search bar now pops up at bottom of window. This
    is much less disruptive as text does not get "pushed down" when
    this toolbar pops up.
  + The FXHash find() routine now returns the slot index, or -1 if not
    found. If you use FXHash you should be aware that simply replacing
    find() by at() will fix your code to the new system. This was done
    based on request from a user who noted the find() API in FXHash
    behaved differently from the find() in FXDictionary.
  + Strip leading and trailing space from display in Adie's bookmark menu.
  + Added ParallelMax constant declaration for FXParallelFor.
  + Change to FXText findText() API. The new version can perform not only
    forward and backward search, but also anchored match. The anchored match
    is performed if neither SEARCH_FORWARD or SEARCH_BACKWARD flags are passed.
  + Goto Line dialog moved from FXText to Adie text editor proper
    (also part of FXText widget slimdown program).
  + Adie Replace Dialog now has Search button.
  + Adie Replace Dialog Replace function now first checks if current
    highlighted text is the one being searched for, and only searches further
    if it isn't. This logic will therefore replace already highlighted selection,
    and make it less likely you accidentally "skip" the first item in a
    search-and-replace session.
  + Also, Search and Replace dialogs stay up until explicitly closed.
    It was often the case that the first search is not always the desired one,
    and one had to bring up the dialog a second time. Note that Escape hides
    the dialog, so no mouse interaction is required for "Power Users".
  + Search and Replace dialog can now replace within selected text only.
  + Some language pattern updates in Adie syntax coloring file.
  + CMake coloring patterns added to syntax file.
  + New match modes added to FXRex: Exact, and NotEmpty. The Exact mode
    succeeds only if a successful match eats the entire string. The NotEmpty
    mode succeeds only if the match eats at least one character. Note these
    are compile time flags, and implemented through special asserts in the
    matching engine. Thus, the engine will potentially backtrack earlier
    matches to try other possibilities!
  + Regular expression match engine speeded up by streamlining
    matcher-setup internally; this particularly affects search().
  + Fixed bug in FXHash::at().
  + Eliminated recursion in simple possessive match in FXRex.
  + Added handy isNull(), isBool(), etc. APIs to FXVariant.
  + Made selection-changing APIs virtual in FXText, for subclassing.
* Fri Aug 29 2014 jengelh@inai.de
- Use verifiable https://en.opensuse.org/SourceUrls and
  original tarball
- Source uses AC_DISABLE_OPTION_CHECKING which requires
  autoconf >= 2.62
- Follow shared library package naming guidelines a bit closer
- Remove redundant %%clean section
* Fri Aug 15 2014 lars@linux-schulserver.de
- update to 1.7.49:
  + a lot of changes, please refer to
    /usr/share/doc/packages/fox17/html/news.html
    for details
- add freeglut-devel to BuildRequires
- remove support for really old (< 10.0) SUSE distributions
- refreshed fox-1.7-remove_date_from_adie.patch
- added fox-1.7-remove_date_from_pathfinder.patch
* Fri Oct 25 2013 lars@linux-schulserver.de
- update to 1.7.43:
  + Added FXJSON JavaScript Object Notation I/O class. FXJSON loads
    and saves JSON, and has a great number of options, extensive error
    reporting, and great degree of control over output.
  + Problems in Windows version of fxcpuid.cpp fixed.
  + Line segment to box and line segment to sphere intersection
    routines added; also computes intersection point..
  + FXString escape() and unescape() now do \uXXXX unicode escaping.
    Old functions for these, fromAscii() and toAscii() have been
    removed. The new implementation properly handles surrogate pairs.
  + Added some API's to FXGLGroup.
  + FXListBox current item fix.
  + Added new functions to FXElement.h. Particularly,
    bulk-comparison function.
  + Use new fxstrlcpy() and fxstrlcat() where appropriate; these will
    always produce null-terminated strings.
  + Passed wrong handle for error FD in FXProcess under Windows.
  + Fix introduced bugs in FXHash and FXDict.
  + Some extra checks added in GIF loader header detection.
  + Typo fix in lock-free queue class FXLFQueue.
  + Fast accessors added to FXVariant; they can be used if type
    already known.
  + Fixed minor issues with FXVariant implementation.
  + Missing FXAPI declaration in FXArrayBase added.
  + Added area() and volume() calculation to FXRange and FXSphere
    classes; added area() to FXExtent classes.
  + Added new FXDictionary class; this will replace FXDict at some
    point in the future.
* Mon Sep 16 2013 lars@linux-schulserver.de
- split out controlpanel package from libfox1_7 package
- added fox17-remove_date_from_pathfinder.patch to avoid unneeded
  rebuilds in OBS
- update to 1.7.42:
  + Added class FXVariant, and supporting classes FXVariantMap and
    FXVariantArray. The FXVariant class can store basic types like
    bool, int, or float, but also arrays of variants, or maps of
    variants. Thus, FXVariant can be used to store an arbitrarily
    complex tree-like data structure.
  + Fix cased from (__m128) to _mm_castsi128_ps() intrinsic for portability.
  + Fix compare operation in FXSize.h.
  + Added fxstrlcpy() and fxstrlcat() for safe string copy and
    string concatenation.
  + Added __noreturn macro for flagging non-returning functions like
    fxerror(). This may help compilers generate better code for places
    where these functions are called.
  + Removed fxsleep(), obsoleted by FXThread::sleep() and FXThread::wkaeat().
  + Allow out-of-source builds of FOX on configure-based systems.
  + Force end-of-string in value returned by gethostname().
  + Fix introduced bugs in FXHash and FXDict.
  + Added swapElms() to FXElement.h. Also added templated swap().
  + Added internal function memswap().
  + Don't include intrinsics header files unless target
    architecture is x86 or x86-64.
  + Many changes to Matrix classes for AVX and SSE.
  + FXHash hash-table improvements.
  + FXHash, FXPtrList needlessly had virtual destructors.
  + API's equalElms() added to FXElement.h.
  + Problems with initial list fixed in FXFileList and FXDirList.
  + Dropped default parameter value for FXString::mid() API.
  + Signed/unsigned warning issues fixed in FXArray.h.
  + FXArray and FXHash now use FXival to allow truly large arrays
    and dictionaries.
  + Fixed some warnings compiling synchronization classes.
  + Use FXuval for fxmalloc() and ilk.
  + Minor additional tweaks to CPU identification.
  + FXRefPtr moved into the Atomic Age:- use atomic swap when
    changing pointer value.
  + Add overloads for long, unsigned long in FXElement.h.
  + FXArray now consists of single (never NULL) pointer, same as
    FXString. This means FXArray takes up only a pointer's worth
    of space when empty.
  + Sign-extend macro added to fxdefs.h.
  + Updated fxcpuid() with AVX, AVX2, FMA, XOP, etc. detection.
  + Updated tables for fxascii.cpp.
  + Added various macros for memory alignment in fxdefs.h.
  + Added API's to FXTreeList and FXFoldingList to replace one
    item with custom item.
  + Added API to return processor index of calling thread in FXThread.
  + Bounds check in FXTabBook's setCurrent().
  + Added isAccessible API to FXStat.
  + Added API to rotate vector by quaternion to FXQuatd, FXQuatf.
  + Check valid path in FXPath.
  + FXFileList Drag and Drop now enabled.
  + Improvements to File Open Dialog right-click menu.
  + Add ability to remove as well as add directory bookmarks in
    File Open Dialogs.
  + AVX capabilities added to matrix and vector classes
    (if compiled with avx intrinsics).
  + FXThread sleep() function reverts to sleep if interrupted
    by signal.
  + 4x4 Double matrix transpose using AVX permute intrinsic.
  + Check UTIME_OMIT before using utimensat().
  + Updates to PathFinder file manager.
  + Check for NULL name in FXMetaClass hash table additions.
  + Added isBinDigit() and isOctDigit() to Ascii character
    class functions.
* Fri May 17 2013 lars@linux-schulserver.de
- update to 1.7.39:
  + Small changes to return types in FXIO (and subclasses) for
    flush(), eof().
  + FXMat4d and FXMat2d AVX accelerated when compiled for AVX.
  + ADA programming language patterns added to Adie's syntax file.
  + Fix in PathFinder escapement of filenames prior to spawning process
    to open document.
  + Compile-time check improved before implementing call to
    utimensat() in FXStat.
  + Totally revamped implementation of FXThreadPool. The new FXThreadPool
    is organized about a lock-free queue, with semaphores managing
    synchronization between producer- and worker-threads. Thus, threads
    never block unless two edge conditions are reached: either the task-queue
    is empty, in which case worker threads will block (nothing to do), or
    task queue is filled up, and producer thread will block.
  + An important new capability is for an additional thread to enter into
    the task-processing loop temporarily. Finally, the thread starting
    FXThreadPool, as well as the worker threads belonging to the FXThreadPool
    now have a thread-local variable referencing the FXThreadPool. This
    allows the threads involved to locate the address of the FXThreadPool,
    for instance to create an FXTaskGroup.
  + New FXTaskGroup class manages groups of task to be executed in parallel
    on a FXThreadPool. Tasks started through the FXTaskGroup interface are
    guaranteed to be completed within the lifetime of the FXTaskGroup instance.
  + New FXParallelInvoke and FXParallelFor template functions to implement
    parallel function call, and parallel for loop. This uses the new
    FXTaskGroup, and indirectly, FXThreadPool.
  + Pass optional stacksize when constructing FXWorker. Added stacksize
    option to FXThreadPool with which new workers will be started.
  + FXBarrier wait primitive now sports API's to change break-through
    threshold, and forced-release option.
  + FXSemaphore now has API's for timed wait, and try-wait for
    non-blocking semaphore decrement.
  + Added additional atomic variable types in FXAtomic.h.
  + Added check for maximum dash-pattern length in FXDC and FXDCWindow.
  + Fixed some issues with FXStat of files.
  + Off-by-one error fixed in FXRex counted repeat of complex subpatterns.
  + Clear internal text pointers in FXRex prior to a match.
  + Added a few missing print-patterns to Adie.stx syntax file.
  + Added FXSemaphore-protected queue class FXSemaQueue; this is
    itself a wrapper around FXPtrQueue.
  + Added lock-free queue class FXLFQueue.
  + Numeric conversion issues fixed in fxstrtod.cpp; in particular,
    some corner cases now give more accurate results.
  + The function fxscanf.cpp does no longer eat the "e" when scanning
    for a number, unless actually followed by digits.
  + Switch to statvfs() from statfs() in FXStat.
  + Indexing operator added to FXAutoPtr.
  + Added new class FXScopedThread. FXScopedThread automatically
    performs a join() upon destruction.
* Tue Mar 12 2013 lars@linux-schulserver.de
- added glu-devel to build requires
- refreshed patches
  >>>>>>> ./fox17.changes.r95
* Wed Jan 23 2013 lars@linux-schulserver.de
- update to 1.7.37:
  + Added auto-numbering in FXHeader.
  + Added alpha-numbering in FXHeader.
  + Fixes to FXProcess implementation on Windows.
  + Fixed aligned to unaligned store in FXMat2f SSE implementation.
  + Slightly stricter TGA header recognition.
  + Removed FXSemaphore value() API. Never used, and not really
    useful.
  + FXRecentFiles allows for up to 32 entries;
    still defaults to 10, however.
  + Fix in Windows non-UNICODE implementation of FXStat created(),
    accessed(), and modified() API's.
  + Added API's to FXWorker class.
  + Added API to FXPtrQueue class.
  + FXPath::contract() should only replace whole path-components.
  + Prototype of wndproc() was not correct for 64-bit Windows.
* Sun Sep  9 2012 lars@linux-schulserver.de
- update to 1.7.36:
  + FXPath::match is now UTF-8 aware in matching filenames.
  + Keep directories up front in FXFileList.
  + FXTable API additions for spanning cells.
  + FXTable fixes to issue only single callback for spanning cells
    if multiple columns/rows fall in selection rectangle.
  + Added GO Language support for Adie Text Editor.
  + Added TENA .tdl Language support for Adie Text Editor.
  + Switch to C++ casts in certain places kills of const
    cast warnings
  + The fox-config file for FOX project development has
    been re-instated
  + New feature in FXHeader control: auto-renumbering captions based
    on renumbering function; if a renumbering function (which computes
    the caption from the caption index) is set, then captions are
    automatically recomputed when the number of items in the FXHeader
    is changed.
  + Updated FXTable to use this new feature in FXHeader. The old
    options for renumbering have been removed.
  + Porting problem in FXMat4d, FXMat4f fixed, for CYGWIN32.
  + Added API's to FXTable to return first and last row (or column)
    of a spanning cell.
  + Added API to check if a cell is horizontally spanning or
    vertically spanning.
  + Cutoff angles in FXQuatd are smaller than in FXQuatf, due to much
    greater precision of doubles versus floats.
- create symlinks in devel package where the binaries live
* Thu Jul 12 2012 lars@linux-schulserver.de
- update to 1.7.34:
  + Added FXRandom fast, long-period, thread-safe psuedo-random
    number generator.
  + Gamma-corrected image scaling option added.
  + FXPath::relative() corner-cases fixed.
  + FXPath::isHidden() now faster by scanning backward.
  + Adie syntax highlight algorithm had some possible issues.
    Now expand context when incrementally recoloring.
  + Include glext.h on Windows; missing symbol otherwise.
  + Updated list of C++ keywords in Adie.stx style coloring file.
  + Added enable/disable item API's to FXComboBox, FXListBox, FXTreeListBox.
  + Added expression evaluate feature to Adie text editor.
  + Internal anynymous name spaces introduced in FXExpression and
    FXRex due to symbol clashes on some compilers.
  + Added ?: alternative expression to FXExpression.
  + Array indexing problem fixed in FXFont.
  + Typo fixed in FXAtomic.cpp.
  + Fixed TIFF image save/load.
  + Fixed quaternion arc() for vectors that are 180 degrees apart.
  + Some tweaks in FXAtomic: more optimal code for non-PIC compiles;
    also, check for PIE (position independent executable).
  + Fixed problem in FXRex regarding non-ASCII characters.
  + Repaired some broken syntax patterns in Adie.stx syntax file.
  + SSE-ified lerp() API added to vector classes.
  + Fixed SSE unaligned store problem in FXMat4d; exhibited itself
    on 32-bit systems.
  + Setjmp()/longjmp() issue fixed in fxpngio.cpp.
  + Operator FXbool in FXAutoPtr and FXRefPtr interfered with
    comparison operators; removed it.
  + Added API's to FXMat4 classes.
  + Added serialization capability to FXExpression class.
  + New FXWEBPIcon and FXWEBPImage image support classes; this requires
    libwebp from google.
  + Some changes and speedups in FXHash implementation.
  + Define cpu_set_t for FreeBSD.
  + Undefine VOID if defined (Windows thing).
  + Removed copy constructor and assignment operator for FXDict;
    was never correct anyway, and its not used.
  + Issue with FXMenuCheck and FXMenuRadio reimplementing ID_SETVALUE
    with a boolean argument, whereas baseclass implements ID_SETVALUE
    with string (since there is no check) This caused some breakage in apps.
  + Scrolling widgets like FXIconList no longer do makeItemVisible if
    user clicks on item:- this was disconcerting and unnecessary; if
    you can click on it, then you must have been able to see it!
  + Fixed few issues with incremental search bar visibility.
- specfile cleanup:
  + ran spec-cleaner
  + format license in spdx format
  + add new specfile header
- added fox17-remove_date_from_adie.patch to be able to support
  build compare
* Tue Dec 13 2011 lars@linux-schulserver.de
- update to 1.7.31:
  + Adie text editor Incremental Search Capability implemented.
  + Started on WebP image I/O support.
  + Problem in FXTable clipboard copy/cut operation fixed.
  + Fixes in FXAtomic for VC++.
  + Default value in FXURL url parser.
  + Fixed bounded repeat bug in FXRex.
  + Patch for FreeBSD processor affinity mask.
  + Fixed case-insensitive FXString comparecase() routine for UTF8.
  + Fixed potential issue using FXRex on non-x86 machines.
  + Major FXRex regular expression engine overhaul and bug fixes.
  + Startup of Adie editor now more sensible (thanks to Sander's
    manu suggestions); start with initial directory set properly and
    properly located untitled file.
  + FXDirList's setCurrentFile() improved.
  + Improvements in FXFileList and FXFileSelector; all and all removed
    many unnecessary directory parses, with concomitant speedups of the
    FXFileDialog panel.
  + Bookmarks popup menu in Adie text editor.
  + New Ctl-K keybinding clears current text line in FXTextField and FXText.
  + FXDirSelector cleaned up a little.
  + FXArrowButton made ever so slightly smaller/more distinguished.
  + Ability to set style flags in Adie syntax color setup subpanel.
  + Updated Adit text editor syntax style setup subpanel.
  + FXColorWell no longer grabs primary selection (was awkward to use!).
  + FXColorWell looks improvement: focus rectangle now inside well, well
    observes frame style now, so you may need to update your code unless
    default parameters were used.
  + API's added to FXColors: blendOver(), blendOverBlac(),
    blendOverWhite() added.
  + Fixes and improvements to SyntaxParser in Adie.
* Fri Dec  9 2011 lars@linux-schulserver.de
- update to 1.7.30:
  + Vastly expanded code docs for FXText widget.
  + Improved Syntax parser for Adie text editor.
  + FXFileList now issues proper callbacks when files or directories
    are changed on the disk while FXFileList is displaying them.
  + FXFileSelector puts FXFileList into ICONLIST_SINGLESELECT mode
    when SELECTFILE_ANY mode is in effect. This is as it should be
    since the user may type a filename that doesn't yet exist.
  + Several unnecessary directory scans have been eliminated when
    FXFileDialog first appears. This makes the FXFileDialog much
    faster than it was before.
  + Python syntax rules updated in Adie.stx.
  + Added coloring rules for merge-conflicts for C, C++, and a
    few other languages to Adie.stx.
  + Fixed bugs in Adie.stx now flagged by stricter syntax parser.
  + Non-recursive forceRefresh() in FXWindow.
  + FXIconList generates SEL_DELETED, SEL_INSERTED instead of
    SEL_REPLACED. These callbacks are more useful.
  + PathFinder shows useful information in its status line.
  + Can now change permissions of multiple files from PathFinder
    properties panel.
  + PathFinder can now change file-associations and icon-assignments,
    just like ControlPanel. For now, these have effect only in PathFinder
    itself, but this should change in the future.
  + Typo in FXComplexd fixed.
  + Workarounds for disk stat for MacOSX and other non-Linux Unices.
  + Fixed bug in FXMat3d SSE2 code. Was using aligned access.
  + FXFileList and FXDirList items keep track of mode-bits.
    This actually simplifies stuff quite a bit.
  + Useless directory rescan eliminated when sort-function changed in
    FXFilelist and FXDirList.
  + Issue SEL_CHANGED if current item is replaced in FXIconList,
    FXList, etc.
  + Adie remembers if extension-less file syntax was changed by hand;
    next time same file is loaded, syntax will be restored properly.
  + First-time bug in ControlPanel fixed; rare, issue only occurs
    ControlPanel is ran first time and no registry exists yet on disk.
  + Option added to PathFinder to scale image to available space when
    using internal image viewer.
  + Vendor-key in FXApp's constructor now defaults to FXString::null.
    This is the more common usage pattern.
  + Option added to PathFinder to control file-item space and whether
    or not to auto-size columns display.
  + Bold, strikethrough, underline style flags now saved in Adie.
  + New syntax rule option in Adie.stx: all-matching "background" rule.
    When used, you can colorize all text not matched with the regular
    rules, as override to the default colors used by the Adie editor.
* Thu Sep 15 2011 lars@linux-schulserver.de
- update to 1.7.29:
  +  Updated to Unicode 6.0 tables! This is a massive change!
    Added Arabic Joing groups table.
  +  We now have a FOX Forum! Register and log in to post articles
    and converse with other FOX Users!
  +  Added flag to FXString's shouldEscape() and escape(). If set,
    escape utf8 strings, otherwise only escape control characters.
  +  FXStatusLine bug fix: order is (1) text from help source (widget
    under the cursor), (2) text from GUI update callback to its target,
    (3) fallback text value supplied by setNormalText().
  +  Fleshed out some missing API's in FXDirList, FXFileList.
  +  Small problem in SSE2 in FXMat4f fixed.
  +  File bindings setup panel in PathFinder added.
  +  FXWindow::forceRefresh() now non-recursive (faster, stack-friendly).
  +  Meaningful stuff displayed on status line in PathFinder.
  +  FXString typo fixed.
  +  Don't assume filename order is stable when listing directory
    contents (FXFileList, FXDirList).
  +  Suspect float to double promotions fixed (thanks to CLang++/LLVM
    compiler!).
  +  Fixed problem in FXFileList and FXDirList with dead symlinks.
  +  Signed byte type added (FXschar).
  +  Updated Python syntax coloring for Adie. Also added JavaScript
    syntax coloring.
  +  First-time use of FOX ControlPanel didn't work properly; fixed
    this problem.
  +  Updated and clarified doc-comments in FXThread.
  +  Removed operator FXbool from FXComplexd and FXComplexf.
  +  Fixed typo in FXComplexf and FXComplexd.
  +  Added byte-swap built-ins for Microsoft C++ compiler.
  +  Updated Doxygen scripts for reference documentation generation
    from header files.
  +  Fix small bug in FXThreadPool.
* Fri Aug  5 2011 lars@linux-schulserver.de
- update to 1.7.28:
  + FXConcurrent can be subclassed to create subclassed FXWorker
    threads.
  + Portability issue in FXFileList fixed.
  + Cleanups in FXGLVisual.
  + Added processor-affinity API's for FXThread.
  + Added __prefetch() macro to invoke underlying (GNU C++ only)
    cache-prefetch instruction.
  + Added FXScopedReadLock and FXScopedWriteLock.
  + Fix to FXAutoPtr assignment operator.
* Mon Jul 25 2011 lars@linux-schulserver.de
- update to 1.7.27:
  + New class FXProcess to manage child process creation in a
    platform-independent way.
  + Split out FXThread into constituent files, one for each class
    (FXMutex, FXSemaphore, etc).
  + Overstrike mode behaviour improved in FXText.
  + New collection of functions to deal with utf8/utf16/utf32 conversions
  + New macros for testing utf8, utf16 lead/follow properties.
  + New fxendian.h header file for fast byte swapping primitives
  + New macro FXLONG() to embed 64-bit integer constants in your code,
    in a way that survives various compilers.
  + Added FXIO::Inheritable flag for i/o devices
  + Added new FXConcurrent class
  + Better method to force thread signal masks when starting new
    threads using FXThread.
  + Issues in fxscanf() for parsing doubles fixed
  + API's added to determine free disk space
  + Some members of FXEvent were not initialized in the constructor
  + New intermediate class FXIODevice
  + New class FXWorker is a thread that runs a FXRunnable
  + Renamed FXMutexLock to FXScopedMutex; added FXScopedSpinLock as well
  + Fix to FXAutoPtr when using implicitly called constructors or
    conversion operators
* Mon Feb  7 2011 lars@linux-schulserver.de
- update to 1.7.25:
  + Small fixes in FXAutoPtr.h.
  + Added FXMat2f, FXMat2d.
  + Vectorized many functions in FXMat2d, FXMat2f, FXMat3d, FXMat3f,
    FXMat4d, FXMat4f (using SSE/SSE2/SSE3).
  + Some fixes to FXPath::isInside().
  + New API FXPath::relativize() returns shortest (unique) relative
    filename of file given a list of search directories and absolute
    filename.
  + Added intrinsics includes to xincs.h
  + Small layout changes to FXFontDialog.
  + FXRegistry now uses the FreeDesktop.Org specification.
  + Better FXString::upper() and FXString::lower() implementation.
  + Major cleanup of xincs.h.
  + Major performance improvements in FXThreadPool
  + Improved FXString::escape() and FXString::unescape().
  + Updates to Adie syntax file.
  + and many other changes
* Sun Dec 13 2009 lars@linux-schulserver.de
- update to 1.7.21:
  * Added fastnormalize() API's in FXVec{2,3,4}f, which use SSE
    rsqrtss and one Newton-Raphson step for fast and quite accurate
    vector normalization.
  * Added JPEG 2000 support (FXJP2Icon, FXJP2Image).
  * Added soft-tab insert, force auto-indent and no-auto-indent
    character entry.
  * Fixed cursor-overhang issue (off-by-one redraw).
  * Fixed FXCondition::wait().
  * Added a few convenience-API's in FXMat{3,4}{d,f}.
  * Obtain number of processors improved.
  * Some small fixes in FXRex.
  * Faster fxrandom() implementation using Marsaglia's algorithm;
    its better as well!
  * Fix issue in FXThreadPool waking threads.
  * Variable amount of wait adding job to FXThreadPool.
  * Fixed a few warnings.
  * Fixes in FXFont rolled in.
  * Outer product added in FXMat3{d,f} and FXMat4{d,f}.
- removed upstreamed fox-1.7.20-am111.patch
- add libmesagl-devel buildrequires for Mandriva
* Mon Aug 24 2009 lars@linux-schulserver.de
- update to 1.7.20:
  * too many changes to list here. Please read
    https://www.fox-toolkit.org/news.html for all details
- added fox-1.7.20-am111.patch to fix build with automake 1.11
* Tue Jun 16 2009 lrupp@suse.de
- update to 1.7.19:
  + FXSettings APIs now sport versions which take FXString reference
  + Added volume to FXStat
  + FXDirVisitor split off into its own file
  + Major speed improvement in FXMat4d, FXMat4f matrix inversion
  + Block editing of FXTable cells which are disabled
  + Eliminated automatic conversion of FXColor to- and from
    FXVec4 and FXVec3
  + Added FXAtomicPtr template class for lock-free programming
    support on SMP type systems
  + New code in FXThread for determining #processors
  + New API's added to FXImage. The colorize() API colorizes an
    image by multiplying its luminance by a given color argument.
    The fade() API fades the image to a uniform given color, based
    on a fading-factor
  + Some more stringent checking and tracing in FXGLVisual
    matching added
  + Workaround added for non-conforming handling or GLX 1.3 or newer
    by allowing 0 for glXCreateWindow() in older glX implementations
- rename fox17-static to fox17-devel-static to follow the new
  naming schema for static libs
* Tue Nov 25 2008 behrisch@informatik.hu-berlin.de
- update to 1.7.18
- fixing Mandriva requirements
* Fri Oct 31 2008 behrisch@informatik.hu-berlin.de
- patch added to remove double entry of icons.cpp in src/Makefile.am
- files section updated for ControlPanel
- minor modifications for requirements on non-SUSE distros
* Thu Jul  3 2008 lrupp@suse.de
- update to 1.7.17:
  + New Image Type supported: FXDDSImage and FXDDSIcon support
    ".dds" file type images;
  + Added transform() API to FXSphere; it may be used to
    transform bounding
  + sphere by affine transformation matrix.
    Also added transform to FXRange.
  + Again, matrix must be an affine transformation matrix.
  + Editor improvements.  Added head() and tail() API's to FXArray
    and FXObjectList.
  + DND_ASK type.  FXIconSource now supports FXDDSImage and FXDDSIcon.
  + Reimplemented utf2wcs(), utf2ncs(), wc2utfs() and nc2utfs()
    to be buffer overrun-safe.
  + New API stackingOrder() added to FXTopWindow to control
    window stacking order explicitly.
- remove the realversion tag
* Wed Jan 30 2008 lars@linux-schulserver.de
- update to 1.7.15:
  + Implemented PropertyNotify message from X11 to intercept
    _NET_WM_STATE changes. This allows us to send SEL_RESTORE,
    SEL_MAXIMIZE and SEL_MINIMIZE when the user manipulates an
    application's top-level window.
* Sat Jan  5 2008 lars@linux-schulserver.de
- update to 1.7.14:
  + Added 3DConnexion SpaceNavigator support.
  + Revamped OpenGL support with GLX 1.3 or higher
    (frame buffer config supprt).
  + Updated FXGLCanvas. FXGLCanvas now has the capability of using
    externally created FXGLContext or to use a private FXGLContext.
  + FXGLContext has been rewritten to use the updated FXGLVisual.
  + Fixed bug in fxprintf.cpp with "%%n" format.
  + Fixed core dump in fxtifio.cpp which was due to crappy TIFF
    library not handling errorhandling function-pointers nicely.
  + Fixed GCC type-punning warnings in FXThread.cpp.
  + Fixed some warnings in FXApp.cpp.
  + Simplified some code in FXDCWindow.cpp, and FXVisual.
  + Added flag to force visual ID in FXVisual; this allows you to
    create a 2D drawable with a compatible visual to a 3D drawable.
  + Added Space ball support for rotation, panning, and zooming
    in FXGLViewer.
- split libfox1_7 package to follow the shared library packaging
  policy of openSUSE
- added desktop files for adie, calculator and pathfinder
* Wed Oct 10 2007 lrupp@suse.de
- update to 1.7.12:
  + Added additional API's to FXMat3d, FXMat3f, FXMat4d, FXMat4f.
  + FXSlider, FXRealSlider didn't update tickmarks (if shown) when
    slider range was changed.
  + Small typo found in fxfilematch() was found which affected
    character-range matching.
  + Change in the order FXSphered, FXSpheref is expanded when
    bounding box is added, resulting, in most cases, in a smaller
    bounding sphere.
  + API added to FXTreeListBox, FXListBox, to set shrink-wrap mode
    for popup pane; this allows minimum size depending on actual
    number of items in list.
  + Logic of sizing items in FXIconList changed slightly.
  + switched to Lesser GPL Version 3
  + Major improvements to FXChart widget, and introduced FX2DChart
    and FX2DPlot widgets.
  + Extra constructors and set() API's added to FXRangef, FXRanged.
    Made radius have default parameter value in FXSphere to match
    the idea in FXRange.
  + Fixed FXDockSite moveToolBar() problem when FXDockSite is
    docked at bottom side.
  + Fixed FXComboBox, FXListBox, FXTreeListBox potentially reading
    freed memory.
  + FXIconSource now recognizes ".jpeg" extension.
  + Added "special stacking orders" capability for FXTopWindow.
  + FXSettings has had a major overhaul. Arbitrary size limits for
    the strings have been removed.
  + FXMat3d, FXMat3f, FXMat4d, FXMat4f have equality operators now.
  + Added setOrtho(), setFrustum() to FXMat4d and FXMat4f.
  + FXMat3f, FXMat3d, FXMat4d, FXMat4f function eye() has been
    replaced with identity().
  + New API getItem() added to FXOptionMenu.
- removed old Provides and Obsoletes for fox-unstable
- added fox17-rpmlintrc
* Tue Jun  5 2007 lrupp@suse.de
- update to 1.7.10:
  + fxIsFinite(), fxIsInf(), fxIsNan() API's added.
  + FXGradientBar visual aspects have more control now.
  + FXShutter didn't issue message when shutter-item was pressed.
  + The fxgetticks() API is now official. It returns the CPU's clocktick-
    counter, where supported. Otherwise it returns time in nanoseconds.
  + Fixed rare corner-case with active-line coloring in FXText.
  + Fixed regression in glUseFXFont() when using Xft instead of XLFD.
  + Small subtlety fixed with list widgets and drag-n-drop initiation.
  + Fixed bug in FXMemMap.
  + Fixed bug in FXVisual which caused drawing to FXBitmap to fail.
  + Fixed bug FXWindow setDNDData() which affected MS-Windows clipboard
    operations.
  + FXbool can not be relied upon to be 1-byte size. Removed the FXASSERT
    inside FXApp to that effect. Serialization should be OK since its cast
    to FXuchar.
  + Added ability to set file-associations table in FXFileDialog,
    FXDirDialog so the associations may be shared between multiple widgets.
  + Fixed issue with bold-face text not drawing correctly in FXText if gap
    happens to be in the text-fragment being drawn.
  + Implemented __vsscanf() and __sscanf(). Since this native FOX
    implementation, and its now used on all platforms, there will be no
    more issues with 32-bit v.s. 64-bit architectures, or Windows v.s.
    Solaris v.s. GLIBC based systems.
    The new routine will always behave the same and support the same
    conversions.
  + Decoration options interpreted under Windows-XP and UNIX as follows:
    DECOR_SHRINKABLE means window may be smaller, but not larger, than
    default size;
    DECOR_STRETCHABLE means window may be larger, but not smaller, than
    default size; and finally,
    DECOR_RESIZE means window may be both smaller or larger than
    default size.
  + Implemented __snprintf() and __vsnprintf(). This takes care of all
    variability in these API's across platforms, and also 64- v.s. 32-bit issues.
  + FXMDIChild resize animation speed changed a little bit.
  + Added some exciting new applications to the list of projects.
- Remove libbz2 from BuildRequires (in buildsystem now)
- removed --with-xim option: breaks keyboard support
* Thu May  3 2007 lrupp@suse.de
- update to 1.7.9
* Thu Mar 15 2007 lrupp@suse.de
- update to 1.7.8
* Thu Dec 14 2006 lrupp@suse.de
- initial package 1.7.7
