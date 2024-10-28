%undefine _debugsource_packages

Name:           tea
Version:        62.4.0
Release:        1
Summary:        A text editor with the hundreds of features
URL:            https://github.com/psemiletov/tea-qt
Group:          Productivity/Text/Editors
License:        GPL
Source0:        https://semiletov.org/tea/dloads/%{name}-qt-%{version}.tar.gz
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  qt5-qtbase-devel
AutoProv:       false
#Provides:       teaqt

%description
TEA is the text editor for UNIX-like systems and Windows.
With an ultimate small size TEA provides you hundreds of functions.

%prep
%setup -q -n %{name}-qt-%{version}
sed -i 's|62\.0\.1|62.0.2|' CMakeLists.txt meson.build tea-qmake.pro

%build
qmake-qt5
make %{?jobs:-j%{jobs}}

%install
install -Dm 755 bin/%{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}
install -Dm 644 icons/tea_icon_v2.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{name}.png
install -Dm 644 desktop/%{name}.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS NEWS-RU README.md TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Apr 07 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 62.4.0
- Rebuilt for Fedora
* Sun Jul 11 2010 Detlef Reichelt <detlef@links2linux.de> - 28.1.0
- new upstream version <28.1.0>
* Wed Jun 16 2010 Detlef Reichelt <detlef@links2linux.de> - 28.0.0
- new upstream version <28.0.0>
* Thu Apr 15 2010 Detlef Reichelt <detlef@links2linux.de> - 27.1.0
- new upstream version <27.1.0>
* Sat Mar 27 2010 Detlef Reichelt <detlef@links2linux.de> - 27.0.1
- new upstream version <27.0.1>
  * Add: File - File actions - Set UNIX end of line
  * Add: File - File actions - Set Windows end of line
  * Add: File - File actions - Set traditional Mac end of line
  * Fix: Fm - File information - Full info //now detects the end of line of
    the selected file
* Sat Mar 27 2010 Detlef Reichelt <detlef@links2linux.de> - 27.0.1
- new upstream version <27.0.1>
  * Web-gallery tool fixed
  * Morse encoder can handle the lower case text
  * A few Russian manual fixes
* Sat Feb 27 2010 Detlef Reichelt <detlef@links2linux.de> - 27.0.0
- new upstream version <27.0.0>
* Mon Jan 25 2010 Detlef Reichelt <detlef@links2linux.de> - 26.2.2
- new upstream version <26.2.2>
* Fri Jan 08 2010 Detlef Reichelt <detlef@links2linux.de> - 26.2.1
- new upstream version <26.2.1>
* Wed Jan 06 2010 Detlef Reichelt <detlef@links2linux.de> - 26.2.0
- new upstream version <26.2.0>
* Mon Dec 07 2009 Detlef Reichelt <detlef@links2linux.de> - 26.1.0
- new upstream version <26.1.0>
* Sat Oct 03 2009 Detlef Reichelt <detlef@links2linux.de> <26.0.1>
- new upstream version <26.0.1>
* Sat Jul 18 2009 Detlef Reichelt <detlef@links2linux.de> <24.0.0>-<0.pm.1>
- new upstream version <24.0.0>
  * all dynamic menus can be teared off
  * Lout IncludeGraphic support on Insert image..
  * Add: Functions - Math - Binary to decimal //works with unsigned int binary numbers only
  * Add: Search - Regexp mode //affect the searching, tables
  * Add: more UI tweaks for smalls-screen devices
  * all options from UI::Tune::Rare moved to UI::Tune::Common
  * "Tab width in spaces" option moved to UI::Tune::Interface
  * fixes at the tables engine
  * main window can be resized to any size //useful for EEE PC 701 users
  * Add: Functions - Tables
  * win32: Templates and snippets were been fixed
  * Add: Functions - Math - Decimal to binary //use with decimal representation
  * Add: Functions - Math - Flip bits (bitwise complement) //use with binary representation
  * Add: Markup - HTML tools - Strip HTML tags
  * Add: "+" and "-" keys scales image at the image viewer
  * Add: drag from the TEA's file manager to outside......
  * some file manager improvenents
  * Add: "+" and "-" keys scales image at the image viewer
  * Add: drag from the TEA's file manager to outside......
  * some file manager improvenents
  * Add: View - Highlighting mode menu to set the hl-mode manually
  * Add: File manager::places - configs item //to speed-up access to TEA config files
  * Add: Markup - Mode - Lout..
  * Add: FIF works to search at the Tune/Keyboard/Shortcuts list.
  * Add: Lout syntax HL (if the file has the extension "lout" - foobar.lout)
  * Tune window fixes
  * Add: PHP syntax hl - made by Boo-boo
  * Add: D syntax hl
  * Add: "Fm - File information - Full info" can read WAV file properties and calculate
    the RMS. RMS is calculated for 16 bit PCM files only.
  * Add: Enter key work at the file name entry at the file manager. If user
    used Open file, Enter key acts to open file, if the "Save as" is used,
    Enter acts like fileman's "Save as" button.
* Mon Mar 09 2009 Detlef Reichelt <detlef@links2linux.de> <23.2.0>-<0.pm.1>
- new upstream version <23.2.0>
  * Add FB2 format read-only support (via the inner ABW tio module)
  * Add file manager fixes
  * string list functions fixes
  * OOP design fixes, tea binary site has been reduced by ~10 kbytes.
  * resourses cleanup
  * Add Functions - Sort - Sort case insensitively
* Sat Mar 07 2009 Detlef Reichelt <detlef@links2linux.de> <23.1.1>-<0.pm.1>
- new upstream version <23.1.1>
* Sat Feb 28 2009 Detlef Reichelt <detlef@links2linux.de> <23.1.0>-<0.pm.1>
- new upstream version <23.1.0>
* Tue Feb 10 2009 Detlef Reichelt <detlef@links2linux.de> <23.0.0>-<0.pm.1>
- new upstream version <23.0.0>
  * Add BASIC syntax hl
  * Add new logo at the About window
  * Add LaTeX syntax hl
  * Add Fm - ZIP - Create new ZIP
  * Add Fm - ZIP - Add to ZIP
  * Add Fm - ZIP - Save ZIP
  * Add SLA (Scribus) format //read only
  * Add Functions - Text - Escape regexp
  * Add weak RTF support //read only
  * Add input box for Save session //instead of file name in FIF
  * Add ODT, SXW (old OOo format), KWD (old KWord format), ABW (AbiWord), DOCX documen
    read only
  * Add Fman - Image conversion - Scale by side
  * Add Fman - Image conversion - Scale by percentages
    1. put the val into the FIF
    2. select images
    3. apply the function
  * Fortran hl fixes
  * Add Tune - Functions - Image conversion output format
  * Add Tune - Functions - Scale images with bilinear filtering
  * Add Tune - Functions - Output images quality
    mainly for JPEG. Use -1 for default settings, otherwise 0..100
  * Add Tune - Functions - Zip directory with processed images
* Thu Jan 22 2009 Detlef Reichelt <detlef@links2linux.de> <22.3.0>-<0.pm.1>
- new upstream version <22.3.0>
  * Add initial Fortran syntax hl. The fortran.xml is based on Fortran 90 spec
  * Add C# syntax hl
  * Add Functions - Text - Remove trailing spaces //on the each line
* Mon Jan 19 2009 Detlef Reichelt <detlef@links2linux.de> <22.2.1>-<0.pm.1>
- new upstream version <22.2.1>
  * Aplly to each line - fixed
  + Snippets, Scripts, Sessions and Templates now can hold submenus
  - Qt version checking in src.pro is removed (it never worked fine on some distros)
  * Search options are saving now
  * Image viewer hides itself when the file manager lost a focus
  + Autocompletion for the FIF
* Mon Jan 12 2009 Detlef Reichelt <detlef@links2linux.de> <22.1.0>-<0.pm.1>
- new upstream version <22.1.0>
  * MD5 checksum evaluation - fixed
  * paired braces hl - fixed
  * Toggle header/source - fixed
  * Add Functions - Analyze - Count the substring (regexp)
  * Add Functions - Analyze - Count the substring
    the "Search - Case sensitive" is used as an option
    Use the FIF to define a substring.
  * text to html - fixed
  * several memory leaks - fixed
  * markup engine inner changes
* Sat Jan 03 2009 Detlef Reichelt <detlef@links2linux.de> <22.0.1>-<0.pm.1>
- new upstream version <22.0.1>
  * shortcuts bug - fixed
  * "keys" file is renamed to "shortcuts", so all your previous hotkeys were lost
    assign them again!
  * "famous input field" is used instead of FEF :)
  * shortcuts engine - fixed
  * the "fte" script object is renamed to "fef" according to the FTE > FEF renaming
  * Add File manager :: backspace navigates the fman to the directory at the upper level
  * Delete old image viewer
  * syntax hl engine can be case insensetive
  * Add Seed7 syntax hl
  * Add much better C/C++ hl
  * Add Search - Whole words option
  * Add Search - Case sensitive
  * the "setup" tab has been renamed to "tune"
  * "replace all" - fixed
  * the "setup" tab has been renamed to "tune"
  * "replace all" - fixed
  * Add Functions - Analyze - UNITAZ quantity sorting
  * Add Functions - Analyze - UNITAZ sorting alphabet
  * Delete Functions - Analyze - UNITAZ
  * Ctrl-F can be assigned twise - for Search and for the Focus the Famous entry field.
    Please remove the first assignment manually to make the second one working properly
* Sun Dec 21 2008 Detlef Reichelt <detlef@links2linux.de> <21.1.3>-<0.pm.1>
- new upstream version <21.1.3>
  * some UNITAZ fixes and improvements
* Sat Dec 20 2008 Detlef Reichelt <detlef@links2linux.de> <21.1.2>-<0.pm.1>
- new upstream version <21.1.2>
  * Functions - Analyze - UNITAZ
  * c/c++ hl fixed
* Fri Dec 19 2008 Detlef Reichelt <detlef@links2linux.de> <21.1.1>-<0.pm.1>
- new upstream version <21.1.1>
  * hl fixes
  * Pascal hl file fixed
* Tue Dec 16 2008 Detlef Reichelt <detlef@links2linux.de> <21.0.5>-<0.pm.1>
- new upstream version <21.0.5>
  * "Functions - Statistics" is renamed to Analyze
  * Extraction - Exract words is moved to Analyze
  * - Extraction submenu
  * - Single application mode
* Thu Dec 11 2008 Detlef Reichelt <detlef@links2linux.de> <21.0.5>-<0.pm.1>
- new upstream version <21.0.5>
  * + File - File actions - Reload //i.e. revert to saved
  * + File - File actions - Reload with encoding //use double click to reload current document with the selected charset
* Tue Dec 09 2008 Detlef Reichelt <detlef@links2linux.de> <21.0.4>-<0.pm.1>
- new upstream version <21.0.4>
  * Pascal hl fixed
  * some other bug fixes
* Sun Nov 30 2008 Detlef Reichelt <detlef@links2linux.de> <21.0.3>-<0.pm.1>
- new upstream version <21.0.3>
  * spellchecker is fixed!!!
  * add progressbar for the spellchecker
* Thu Nov 27 2008 Detlef Reichelt <detlef@links2linux.de> <21.0.2>-<0.pm.1>
- new upstream version <21.0.2>
  * src.pro: QT version checking is disabled due to some reasons
  * the inner changes to improve the loading speed
  * IDE switched to QDevelop ;)
  * Ctrl-F is now assigned for Focus the Famous text entry
  * some bugs were fixed
* Wed Nov 19 2008 Detlef Reichelt <detlef@links2linux.de> <21.0.0>-<0.pm.1>
- new upstream version <21.0.0>
* Sat Oct 11 2008 Detlef Reichelt <detlef@links2linux.de> <20.0.0>-<0.pm.1>
- new upstream version <20.0.0>
* Thu Sep 04 2008 Detlef Reichelt <detlef@links2linux.de> <19.1.1>-<0.pm.1>
- new upstream version <19.1.1>
  * Fix: Apply to each line
* Wed Sep 03 2008 Detlef Reichelt <detlef@links2linux.de> <19.1.0>-<0.pm.1>
- new upstream version <19.1.0>
  * Add Statistics: author's sheets
  * Add File - Sessions
  * Add File - Save different - Save session
  * Add Prefs: Restore the last session on start-up
  * Add View - Stay on top
  * Add Qt version detection on the qmake stage
  * Add Functions - Math - Enumerate
  * Add Syntax: step~zero_padding~prefix
* Mon Aug 18 2008 Detlef Reichelt <detlef@links2linux.de> <19.0.5>-<0.pm.1>
- new upstream version <19.0.5>
  * 2008/08/04 //19.0.4: spellchecker words parser is fixed
  * 2008/08/04 //19.0.3: more fixes
  * 2008/08/04 //19.0.2: some file manager fixes
* Tue Aug 05 2008 Detlef Reichelt <detlef@links2linux.de> <19.0.1>-<0.pm.1>
- new upstream version <19.0.1>
  * Add: Preferences - Override locale option
  * Add: Single instance mode for Windows
* Sat Aug 02 2008 Detlef Reichelt <detlef@links2linux.de> <19.0.0>-<0.pm.1>
- new upstream version <19.0.0>
  * Add: File manager
  * Add: single-instance mode
  * Del: TEAVisor
  * Fix: Restore the positions of toolbars
  * Fix: Dialogs remembers their sizes
  * "Insert image" calls the file manager page
  * Preferences - Use traditional File save/open dialogs
* Sat Jul 19 2008 Detlef Reichelt <detlef@links2linux.de> <18.1.1>-<0.pm.1>
- initial build <18.1.1>
