Summary: Tool for finding and fixing problems in MP3 files
License: GPL
Group: Applications/Multimedia
Name: mp3diags
Release: 4.2
Source: MP3Diags-%{version}.tar.gz
URL: http://mp3diags.sourceforge.net/
Version: 1.0.11.076
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildRequires: libpng-devel
BuildRequires: qt-devel zlib-devel boost-devel gcc-c++

%description
Finds problems in MP3 files and helps the user to fix many of them.
Looks at both the audio part (VBR info, quality, normalization)
and the tags containing track information (ID3.)

Has a tag editor, which can download album information (including cover art)
from MusicBrainz and Discogs, as well as paste data from the clipboard.
Track information can also be extracted from a file's name.

Another component is the file renamer, which can rename files based on the
fields in their ID3V2 tag (artist, track number, album, genre, ...)

%prep
%setup -q -n MP3Diags-%{version}
#sed -i '1i #include <unistd.h>' src/Helpers.cpp

%build
./AdjustMt.sh STATIC_SER
qmake-qt4
make
sed -i 's/Exec=MP3Diags/Exec=mp3diags/' desktop/MP3Diags.desktop

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 bin/MP3Diags $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 desktop/MP3Diags.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 desktop/MP3Diags16.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/MP3Diags.png
install -Dm644 desktop/MP3Diags22.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps/MP3Diags.png
install -Dm644 desktop/MP3Diags24.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps/MP3Diags.png
install -Dm644 desktop/MP3Diags32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/MP3Diags.png
install -Dm644 desktop/MP3Diags36.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/36x36/apps/MP3Diags.png
install -Dm644 desktop/MP3Diags40.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/40x40/apps/MP3Diags.png
install -Dm644 desktop/MP3Diags48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/MP3Diags.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/??x??/apps/MP3Diags.png

%changelog
* Fri Jun 22 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.11.076
- Rebuilt for Fedora

* Sun Nov 29 2009 Marian Ciobanu <ciobi@inbox.com> 1.0.00.045
- wording changes to reflect non-beta status
- pressing CTRL+C when viewing full-size images in the tag editor or in "Tag details" in the main window copies the image to the clipboard
- added "Rating" and changed field order in "Tag details" to match the Tag editor

* Wed Nov 04 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.06.044
- fixed a crash in folder filter
- fixed bug causing non-normalized files having any TXXX frame to appear normalized
- case is ignored for file extension, so .Mp3 or .mP3 files are recognized
- better support and more consistent handling for TXXX and text frames in ID3V2
- reduced number of locales by eliminating redundant ones
- disabled CTRL+A selection in the main window
- static link for serialization
- added trace details for web downloads

* Tue Oct 27 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.06.043
- "Simple view" in file configuration
- fixed crash on empty text frames in ID3V2
- generic binaries for Linux
- BuildMp3Diags.hta detects VS version
- documentation updates

* Tue Oct 20 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.06.042
- better support for binary frames in ID2V2.4.0
- fixed bug resulting in crash when files were modified in external tools
- fixed bug resulting in crash when renaming files if a filter is applied
- fixed bug resulting in crash when going to "Tag details" for files using Unicode in USLT (issue 40)
- added option to include styles in Discogs info
- added case-change option to the tag editor
- better detection and notification for changed files before applying transformations or saving from the tag editor
- file renamer allows file names to be changed manually
- file renamer can use "duplicate" label for unrated songs
- images shown for Lyrics tags
- improved case-change transformation
- removing images from the tag editor now works even for non-cover images

* Fri Oct 09 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.06.041
- brought documentation up to date
- added test for ReplayGain info stored inside Id3V2
- failing to read text frames from files no longer causes crashes
- fixed bug resulting in crash when 2 ID3V2 tags are present and "Discard invalid ID3V2 data" gets called
- XML export now works when names contain double quotes
- locale in export dialog
- locale lists are now sorted
- long text frames are now truncated when shown in the "File info" area
- changed names and order for tabs under Config/Files
- made transformation options work correctly in MSVC

* Wed Sep 30 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.06.040
- "Various Artists" support
- all pictures are shown and can be viewed in full size in "Tag details"
- all pictures from a file are shown in the tag editor
- patterns in the tag editor may now be disabled
- export as M3U or XML
- better handling of text frames containing null characters
- auto-size for the tag editor's "current file" area
- better column widths in the tag editor
- improved HTA for Windows build

* Wed Sep 23 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.05.038
- fixed bug introduced in 0.99.05.037 causing crashes when finding empty ID3V2 frames
- new build process for Windows
- 4th custom transf list now defaults to a "fix-all" approach

* Thu Sep 17 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.05.037
- fixes on right-click
- UTF-8 strings recognized in ID3V2.3.0
- fixed bug 35 (assertion failure)
- faster tracer
- code compilable with VS 2008 (port by Sebastian Schuberth)

* Mon Sep 07 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.05.034
- drive labels shown in Windows
- mp3gain can be started now if it's in a directory containing spaces
- configurable invalid characters and replacement for file renamer
- automatic check for new versions
- text inside square, curly, and angle brackets removed from web queries
- improved tracing code
- no longer rescan the files if exiting tag editor without changes
- replace non-alphanumeric chars with spaces in web queries (issue 2)
- better sorting in the tag editor for albums with unusual track numbers
- a default .ini name is generated in most cases
- (probably) fixed an assert (not sure because couldn't reproduce it)
- tracks without a track number are put at the end in the tag editor
- let the user know about reporting support notes and about patterns
- better detection of exceptions in threads
- exceptions that propagate from slots are now caught
- default "actions to be taken" no longer shown when applying transforms
- file info for StreamWriter

* Wed Sep 02 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.05.033
- fixed crash in Windows when checking a whole drive
- fixed crash when saving data from the tag editor
- improved trace speed on Windows
- fixed potential crash at startup
- fixed crash when changing a file that is being used by other program
- more details and better formatting in assert messages and trace files
- MPEG2 Layer3 streams no longer show Support note
- improved temporary file generation, which can result in faster transforms
- F1 help now works for the first session dialog
- smaller TABs in the "Tag details" area make "Other info" more readable
- better HTML paragraph formatting

* Sun Aug 23 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.05.032
- restructured crash detector
- fixed Windows issue with rectangles being shown instead of letters
- Lyrics partial support
- warning that may corrupt data
- note about how to change selected files
- HTML clean up

* Wed Aug 19 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.05.031
- crash detection
- fixed small memory leak in config dialog
- fixed small memory leak in the tag editor
- content is shown for GEOB frames
- .ID3 files are now loaded in addition to .MP3
- made the counter shown when applying transforms increment on new file(until now it was incremented for each transform)
- "Various artists" no longer set as "artist" when downloading track info from MusicBrainz
- fixed "current cell" in the tag editor (until now, when dragging the mouse to select several cells, the current cell was wrong, leading to setting values incorrectly
- fixed a bug that didn't allow removal of the track number
- slightly improved the normalizer, so a "busy" cursor is shown when the connection to the underlying process is lost (the program seems frozen, but it resumes after about 30 seconds)

* Tue Jul 28 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.05.030
- fixed a bug that caused the tag editor to reserve more space than needed even if the "fast save" option was turned off
- fixed a bug that prevented removal of elements from lists
- fixed a bug in the ID3V2 tag writer that prevented "Discard invalid ID3V2 data" and other transformations to properly work with ID3V2.4.0 tags that contain UTF8-encoded strings, resulting in a broken ID3V2.3.0 tag
- file renamer now accepts patterns with no directory separators, in which case the renamed files are placed in the source directory
- pattern dialogs now show the current line and column
- fixed an assertion in the code that determines the file list
- added tooltips for all the notes in the main file table
- improved speed for "Discard invalid ID3V2 data" when no changes are done
- transformation name included in the dialog that shows which file is currently processed
- broken ID3V2 streams get removed when saving from the tag editor
- the tag editor no longer triggers an assertion failure if non-default settings in the file section of the configuration dialog; (e.g. until now saving from the tag editor while original files weren't deleted resulted in this assertion failure)
- fixed a bug in the "Change case for ID3V2 text frames" that resulted in a program crash if some fields were missing from the ID3V2 tag

* Sun Jul 26 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.05.029
- fast save in the tag editor
- file renamer can work with the list of visible files instead of the current album if the user holds CTRL down when pressing the button
- configurable visible transformations
- new transform for keeping a single image, as front cover
- new transform for removing ID3V1
- button to remove image files
- improved paste in tag editor (it is possible to paste to multiple cells or to paste file names copied from file browsers)
- configurable max image size
- tooltips for the transformations menu
- more checks + fixed error reporting in file renamer
- "sessions" button visible by default for second and later sessions
- directory filter no longer shows some directories that don't make sense
- fixed loading images from current dir
- fixed a bug in tag editor patterns that prevented patterns ending with a static text from working
- fixed some bugs in the directory filter

* Sat Jul 18 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.04.026
- non-ASCII file names can now be seen on Windows
- tag editor now looks at filter
- USLT Lyrics inside ID3V2 are now shown
- better alignment for text in note column header on Ubuntu
- size grip on most dialogs
- F1 help
- files changed in the tag editor no longer show up in the main window if a filter is applied and they don't match the filter

* Fri Jul 10 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.03.022
- 2-letter labels
- gradient grouping of notes
- configurable colors
- app no longer crashes when files are changed by external tools
- tooltips are shown for the column headers in the file table
- more consistent font handling

* Sun Jul 05 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.02.020
- file renamer now replaces invalid characters in file names
- duration is now shown for audio streams
- fixed assertion caused by files with too many streams
- multiple ID3 stream remover no longer included by default in second list
- some changes to the .spec file in the hope it will work on Mandriva

* Sun Jul 05 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.02.020
- file renamer now replaces invalid characters in file names
- duration is now shown for audio streams
- fixed assertion caused by files with too many streams
- multiple ID3 stream remover no longer included by default in second list
- some changes to the .spec file in the hope it will work on Mandriva

* Wed Jun 24 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.02.018
- made -mt suffix default for Boost Serialization

* Wed Jun 24 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.02.017
- always use multithreaded libraries (single-threaded ones may lead to crashes)
- improved assert dialog; now it has more data, which can be copied and even emailed directly
- the tag editor shows a warning in some cases when a user action would result in discarded images

* Sun Jun 21 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.02.016
- fixed an assertion failure that was triggered by an unsupported text encoding in APIC
- added support for UTF8 text encoding in APIC
- made the documentation look slightly better on IE6

* Sat Jun 20 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.02.015
- made compilable on Fedora 11 and added Fedora 11 build
- copying missing ID3V1 fields to ID3V2 no longer part of the default custom transformation list 2

* Thu Jun 18 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.02.014
- the tag editor loads albums much faster than before; this is most visible when navigating to the next / previous album

* Sun Jun 14 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.02.012
- added support for UTF8 in ID3V240
- added maximize button to most windows in Windows (but could not get this to work with Gnome)
- removed "What's this" button from most windows
- now the main window shows the session name if more than 1 session was defined
- now the main window shows up maximized in Gnome and Windows if it was maximized when it was closed
- changed documentation links to point to new site, at SourceForge
- minor documentation improvements

* Sat Jun 06 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.02.011
- added missing dependency for SVG icons
- fixed a bug in "Save as ..."

* Thu Jun 04 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.02.010
- fixed a bug that could cause removal of audio data
- fixed a bug that prevented single-image-saving from working

* Wed Jun 03 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.02.009
- Ubuntu binaries
- minor UI tweaks

* Mon May 25 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.02.008
- improved font handling
- minor UI tweaks

* Tue May 19 2009 Marian Ciobanu <ciobi@inbox.com> 0.99.02.007
- initial version
