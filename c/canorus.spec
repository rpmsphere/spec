%global _python_bytecompile_errors_terminate_build 0

Name:           canorus
Version:        0.7.3rc3
Release:        5.1
License:        GPL-2.0+
Summary:        Free cross-platform music score editor
URL:            http://www.canorus.org/
Group:          Productivity/Multimedia/Sound/Midi
Source0:        https://sourceforge.net/projects/canorus/files/0.7.2/%{name}-%{version}.tar.bz2
Source1:        canorus.1
Source2:        canorus.xpm
# PATCH-FIX-openSUSE -- added german translation
Patch1:         canorus-0.5-desktopfile.patch
# PATCH-FIX-UPSTREAM -- userguide does not honour DESTDIR: add it
Patch2:         canorus-0.7.2-DESTDIR.patch
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  zlib-devel
BuildRequires:  python3
BuildRequires:  swig

%description
Canorus is a free music score editor. It supports note writing, scripting
support, import/export of various file formats, MIDI input and output and more!

Note that Canorus is still in early stage of development and not nearly all the
features are implemented yet!

%prep
%setup -q
# do not build with inline zlib - use the distribution package instead:
find . -type d -name "zlib" | xargs rm -rf
%patch1 -p0
%patch2 -p1
sed -i '1i #include <cmath>' src/layout/drawabletuplet.cpp

%build
cmake \
    -DCMAKE_C_FLAGS="-Wno-error -Wno-misleading-indentation -Wno-deprecated-declarations -Wno-parentheses" \
    -DCMAKE_CXX_FLAGS="-Wno-error -Wno-misleading-indentation -Wno-deprecated-declarations -Wno-parentheses" \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}   \
    -DCMAKE_EXE_LINKER_FLAGS="${CMAKE_EXE_LINKER_FLAGS} -lz" \
    -DCANORUS_INSTALL_DATA_DIR=%{_datadir}/%{name} \
    -DCANORUS_INSTALL_BIN_DIR=%{_bindir} \
    -DCANORUS_INSTALL_LIB_DIR=%{_libdir} \
    -DCMAKE_SKIP_RPATH:BOOL=TRUE       \
    .
%cmake_build

%install
%cmake_install
install -D -m644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
install -D -m644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1
rm doc/cmake_install.cmake
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS DEVELOPERS NEWS README TODO doc
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_libdir}/CanorusPython.py
%{_libdir}/_CanorusPython.so

%changelog
* Mon Aug 06 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.3rc3
- Rebuilt for Fedora
* Tue Mar 15 2016 freitag@owncloud.com
- Spec cleanup
* Tue Mar 15 2016 freitag@owncloud.com
- Update to version 0.7.2rc1:
  * Set SelectMode instead of NoDocumentMode when a new document.was created
  * Added ruler to show the bar number on top of the score view
  * Updated translations
  * Fix some issues to get Canorus running with Qt5
  * Introduced official support for Qt5
  * Bar reference list added to CAStaff
  * Fixed Repeat bar lines in lilypond export
  * Removed obsolete clipping from CAScoreView
  * Add icon for upcoming shortcuts feature
  * Added newDocument() fallback for environment without Python.
  * Added "Canorus is compiled with Python support." to about dialog box.
  * Requires Python 3.x; updated corresponding bindings
  * Added basic MusicXML export.
  * CATempo: Removed obsolete dotted property
  * Lilypond export: Added support for CATempo and CARitardando.
  * Scoreview: Fixed crash when adding lines marks
  * Added MIDI pitch offset property to voice
  * Lilypond export: Fixed indentination
  * Lilypond export: Export instrument names.
  * Lilypond export: Set rehersal marks drawn in box.
  * Fixed horizontal scrolling regression introduced with new speed optimizations.
  * Fixed MusicXML import regression introduced in R1282.
  * Significant speed improvement for getting the current clef.
  * Fixed crash in KDTree when adding notes.
  * Significant speed improvement for finding elements in range for canvas.
  * Moved drawable map from KDTree to ScoreView.
  * Removed several obsolete KDTree functions.
  * Removed several obsolete ScoreView functions
  * Midi import gives staffs and voices a name
  * Compatibility fix with recent Qt4
  Also added changes from 0.7.1:
  * Updated translations
  * Deprecated version 1 usage of swig, we no longer maintain this.
  * Added support for ignoring Lilypond comments when importing it
  * Fixed problem that undo command doesn't correctly update the cloned sheet
  * Fixed crash when undoing source commits for the first time
  * Fixed Lilypond comments import when parsing newlines (cr/lf)
  * Fixed crash when importing lilypond lyrics
  * Fixed warnings throughout the code with newer gcc compiler versions
    (See separate file large-warn-fixes.txt for technical details)
  * Added Break of Compilation when warning occurs
  * Fixed Lilypond melismatic lyrics when used in combination with hyphens
  * Set autobeamOff for printing when lyrics is applied to the voice
  * Added Lilypond export for forced accidentals
  * Added underscores as spaces in Lilypond export
  * Fixed compilation errors using Swig2
  * Fixed note marks time start calculation
  * Fixed importing of slurs times inside the tuplet
  * Fixed importing of canorus files containing tuplet+slur combination
  * Fixed settings dialog page on startup, if playback device not available anymore
  * Fixed crash in reposit method, check for valid slur during creation
  * Implemented degree-based accidentals detection for the given diatonic midi key
  * Fixed semitiones calculation of diminished intervals
  * Fixed midi notes import real times and for tempo > 240bmp
  * Fixed wrong calculation from midi pitch to diatonic pitch
  * Added parameter for scrolling the score view on newly selected music elements
  * Fixed wrong semitones interval calculation
  * Added midi support for (GM) instruments
  * Fixed midi time and length calculation for midi import
  * Fixed brackets and quotes lilypond export
  * Fixed importing the tempo mark on a slured element
  * Added notes, events to midi import and allow control via scripting
  * Added list of shortcuts (midi and UI) in a special file to be used for
    user defined shortcuts
  * Started work on backend for editing shortcuts (loading/saving/parsing)
  * Fixed exporting text on chords to lilypond
  * Added preliminary documentation of canorus libraries
  * Fixed problem that make it impossible to save the document (#16606)
  * Added support for moving sheets using drag&drop and double click
  * Fixed unsaved changes warning dialog when opening recent documents
  * Fixed sheet properties toolbar when removing the last sheet.
  * Fixed update of the sheet tab name when renaming the sheet
  * Fixed properties dialog layout
  * Fixed default note stem direction
  * Fixed that no time signature/barlines are shown when there are none in the score
  * Fixed licensing issues with examples (and remove example with undefined license)
  * Renamed license file to COPYING
  * Added volta bracket support through special text mark
  * Added release build possibility (including compiler optimizations)
  * Fixed problem on text display with cleanup and chord creation
  * Enforce UTF-8 encoding for the canorus and lilypond formats
  * Fixed midi time scaling and quantisation for all events
  * Fixed crash when opening an empty XML file
  * Fixed crash with using certain styles in GNOME environment
  * Fixed midi import adjustment of notes being left over
  * Added articulation, fingering, dynamic marks to lilypond export
  * Fixed problem with tuplet export by returning the last note of a chort
    instead of the first
  * Fixed freeze in the GUI during import
  * Fixed Midi export and repeats
  * Fixed repeat in multiple staffs
  * Fixed arbitrary placed key signature changes
  * Added Midi support of key signature changes
  * Added more examples
  * Created undo only for a whole chord at midi keyboard input
  * Fixed tuplet and chords saving
  * Expanded scripting engine for figured bass
  * Added some user interface settings
  * Allowed midi import with no document opened
  * Fixed minor problems on lilypond export
  * Added GUI, support, load/save for figured bass marks
  * Updated documentation
  * Added support for melisma and syllabic lyrics in MusicXML import
  * Moved view to the right if right border is hit on insert of new elements
  * Fixed crash when reinterpreting accidentals
  * Added reinterpret accidentals in transpose view
  * Added support for key signature in midi export/playback
  * Fixed default mode for the toolbar when creating a new document.
  * Improved midi device (names)
  * Use base name of midi imported file as sheet name
  * Added support for time signatures in midi import
  * Added factoring of music elements to scripting library
  * Fixed automatic bar placement to work with future time signatures
  * Added default time signature (midi recorder)
  * Improvement for midi export: music length and tempo
  * Now using newer RtMidi-1.0.9 library.
  * Preserved midi channels and fixed hangover notes (midi import)
  * Added multiple voices and tempo to midi import
  * Added progress bar for opening and importing documents
  * Use PMidi on all platforms
  * Added some self-made midi examples
  * Added Midi Import based on PMidi
  * Fixed handling of sheets for midi export
  * Added shortcut for cycling through sheets
  * "Print Preview" is used for the current sheet only (same as for printing)
  * Fixed problems when adding lyrics
  * Added debian (ubuntu) build support (amd64)
  * Started adding support for all kind of actions in Canorus
  * Improved layout of properties dialog
  * Added project file for the smallish IDE geany
  * Fixed tempo for playback when starting outside of the beginning
  * Fixed breve syntax in lilypond export
  * Fixed back-scroll for repeats
  * Moved "Use animated scroll" to settings dialog
  * Fixed, lock (optionally, default), store scroll (position) on playback
  * Fixed playback of multiple voices with different timelengths
  * Fixed MusicXML import (midi, grace notes)
  * Added ArgoUML sources of the score model
  * Parse movement title of MusicXML scores
  * Fixed MusicXML import crash on multiple staffs and clefs and on unset <attributes>
  * Added Czesh translation
  * Started adding the action editor (to be finished in 0.7.2)
  * Added support for Tab/Shift-Tab keys in Insert mode for voices
  * Fixed crash when manipilating a slured chord
  * Fixed dots offset and tuplet settings when editing the first time
  * Fixed transposition bug in UI
  * Fixed a crash when closing the document
  * Removed some special characters on example file names.
  * Added support for fermata in lilypond export
  * Fixed a pasting problem
  * Fixed UTF-8 file names in archives
  * Added examples to the installer
- removed patch canorus-linker_flags.patch not longer needed.
- removed patch canorus-0.7-DESTDIR.patch replaced by patch
  canorus-0.7.2-DESTDIR.patch
* Sun Oct  7 2012 lars@linux-schulserver.de
- added specfile header
* Tue Feb 14 2012 lars@linux-schulserver.de
- fix library requirement inside the package
  ( canorus-linker_flags.patch )
- use font from distribution and not the one inside the package
  ( added freefont as required package )
- added manpage and xpm icon file from Debian
  ( thanks to Tobias Quathamer )
* Sat Aug  1 2009 lars@linux-schulserver.de
- strip the binary
* Sun Apr 19 2009 andrea@opensuse.org
- added DESTDIR patch (no mkdir outside buildroot, done manually)
- fixed spec file (rpm succeded)
* Mon Mar 30 2009 lars@linux-schulserver.de
- update to 0.7:
  + Added support for printing and preview of score using LilyPond
    backend.
  + Added integrated Midi recorder.
  + Added resources storage inside the document.
  + Added User's guide.
  + Added transposition support.
  + GUI improvements
  + Import/Export improvements
  + Plugin improvements
  + Model improvements
  + ...and many more
* Thu Dec 11 2008 lars@linux-schulserver.de
- added missing clean section
- use fdupes
- fix desktop file
- install desktop icon
* Mon Apr  7 2008 Detlef Reichelt <detlef@links2linux.de> <0.5>-<0.pm.1>
- initial build <0.5>
