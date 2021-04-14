%undefine _debugsource_packages

Summary:	Unicode Text Editor
Name:		yudit
Version:	3.0.7
Release:	1
License:	GPL
Group:		Applications/Editors
Source:		http://yudit.org/download/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	libXaw-devel

%description
Yudit is a unicode text editor for  the X Window
System.  She  can  do True  Type font rendering,
printing,   transliterated  keyboard  input  and
handwriting recognition with no dependencies  on
external  engines. Her conversion  utilities can
convert    text   between   various   encodings.
Keyboard  input   maps  can  also  act like text
converters. There is no need for a pre-installed
multi-lingual environment. Menus are  translated
into many languages.

GNU (C) 1997-2005 Gaspar Sinai <gsinai@yudit.org> 

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir}
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 644 gnome-yudit.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/yudit.png

cat >$RPM_BUILD_ROOT%{_datadir}/applications/yudit.desktop <<EOF
[Desktop Entry]
Name=Yudit
GenericName=Unicode text editor
Comment=Edits and creates unicode files.
Exec=yudit
Icon=yudit
Type=Application
Terminal=false
Encoding=UTF-8
Categories=Application;Utility;TextEditor;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/uniconv
%{_bindir}/uniprint
%{_bindir}/yudit
%{_bindir}/mytool
%{_mandir}/man1/*

%dir %{_datadir}/yudit
%{_datadir}/yudit/data
%{_datadir}/yudit/fonts
%{_datadir}/yudit/src
%{_datadir}/yudit/doc
%{_datadir}/yudit/syntax

%dir %{_datadir}/yudit/locale
%{_datadir}/yudit/locale/am
%{_datadir}/yudit/locale/ar
%{_datadir}/yudit/locale/az
%{_datadir}/yudit/locale/bg
%{_datadir}/yudit/locale/bn
%{_datadir}/yudit/locale/cs
%{_datadir}/yudit/locale/de
%{_datadir}/yudit/locale/el
%{_datadir}/yudit/locale/en
%{_datadir}/yudit/locale/es
%{_datadir}/yudit/locale/fi
%{_datadir}/yudit/locale/fr
%{_datadir}/yudit/locale/gu
%{_datadir}/yudit/locale/ga
%{_datadir}/yudit/locale/hi
%{_datadir}/yudit/locale/hu
%{_datadir}/yudit/locale/ja
%{_datadir}/yudit/locale/ko
%{_datadir}/yudit/locale/mn
%{_datadir}/yudit/locale/mr
%{_datadir}/yudit/locale/pa
%{_datadir}/yudit/locale/pl
%{_datadir}/yudit/locale/sl
%{_datadir}/yudit/locale/sr
%{_datadir}/yudit/locale/ru
%{_datadir}/yudit/locale/ta
%{_datadir}/yudit/locale/uk
%{_datadir}/yudit/locale/ur
%{_datadir}/yudit/locale/vi
%{_datadir}/yudit/locale/yi
%{_datadir}/yudit/locale/zh
%{_datadir}/yudit/locale/zh_CN

%dir %{_datadir}/yudit/config
%config %{_datadir}/yudit/config/*
%config %{_datadir}/applications/yudit.desktop
%config %{_datadir}/pixmaps/yudit.png

%doc CHANGELOG.TXT COPYING.TXT FAQ.TXT README.TXT TODO.TXT doc/*.utf8 doc/notinstalled doc/problems doc/HOWTO-*.txt doc/otfsupport.txt

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.7
- Rebuilt for Fedora
* Fri Jul 31 2009 J. Krebs <rpm_speedy@yahoo.com> - 2.9.0-2
  Added require for c++ (gcc-c++), patches.
* Mon Dec 24 2007 J. Krebs <rpm_speedy@yahoo.com> - 2.9.0-1
  Updated to version 2.9.0
* Thu Feb 15 2007 J. Krebs <rpm_speedy@yahoo.com> - 2.8.1-1
  Updated to version 2.8.1
* Mon Mar 21 2005 Gaspar Sinai <gsinai@yudit.org>
  - Merged Marathi and Gujarati menu.
  - Merged jodakshar.hwd marathi.hwd roman.hwd handwrinting recognition files
  - Merged CS-qwerty keymap, SpanishPrefix.kmap, Sanskrit-Translit.kmap, GreekAncient.kmap
  - Updated Tibetan-Wylie.kmap 
  - Merged Telugu, Italian FAQ
  - Merged HOWTO greekancient
  - Merged AMD 64 fixes to InputMethod.cpp.
* Sat Sep 6 2003 Gaspar Sinai <gsinai@yudit.org>
  Release 2.7.6
  Better positioning for complex (indic) scripts.
  Comments are preserved now in ~/.yudit/yudit.properties
  Fixed buffer overflow bugs in
   stoolkit/SString.cpp
   stoolkit/SParagraph.cpp
  Yudit -nus command line option turns off uniscribe emulation.  
  Added Punjabi (pa) translations from
     Madhusudan Singh <chhabra@eecs.umich.edu>.
  Added more substitution types. The matrix is documented in
  doc/otfsupport.txt.
  The following font-range filters have been added:
     indic: U+0900..U+0FFF
     deva:  U+0900..U+097F
     beng:  U+0980..U+09FF
     guru:  U+0A00..U+0A7F
     gujr:  U+0A80..U+0AFF
     orya:  U+0B00..U+0B7F
     taml:  U+0B80..U+0BFF
     telu:  U+0C00..U+0C7F
     knda:  U+0C80..U+0CFF
     mlym:  U+0D00..U+0D7F
     sinh:  U+0D80..U+0DFF
     thai:  U+0E00..U+0E7F
     lao:   U+0E80..U+0EFF
     tibt:  U+0F00..U+0FFF
     jamo:  U+1100..U+11FF
  usage: ani.ttf:beng,raghu.ttf:deva
* Sat Jun 14 2003 Gaspar Sinai <gsinai@yudit.org>
  Updated with Miikka's patch for Unicode 4.0.
  Added many patches and contributions
  Added entry level (not full) Tibetan support with some Open Type Fonts 
  Added yudit.editor.xinputs.style property to yudit.properties.
     possible values: root,over-the-spot,off-the-spot
  New menu translations: Czech, Greek, Mongolian, Serbian (cyrillic)
  New keymaps: Telugu-Rts, CS, Kazakh-prefix, Runes,
  Dakelh (Carrier syllabics), ArabicBuck, GeorgianB, 
  BengaliSona, Slavic, Serbian, Kanji,
  Added new configurable xinput styles:
  preedit-over-status-over, preedit-over-status-under,
  preedit-under-status-under, preedit-root-status-root
  NewYudit specific Private Use Area assignment: 
  mytool/uni/BLISSYMBOLICS.TXT (BlissSymbolics.kmap, yudit.ttf)
  Bugfixes and hopefully not many new bugs :)
  Stable version 2.7.5 is ready
* Mon Jan 14 2003 Gaspar Sinai <gsinai@yudit.org>
  o changed names of yudit.editor.xinputs.style
    preedit-over-status-over
    preedit-over-status-under
    preedit-under-status-under
    preedit-root-status-root
* Sun Jan 11 2003 Gaspar Sinai <gsinai@yudit.org>
  Applied SAMPA.patch,patch1,patch2,patch3,patch4
  Added BengaliSona.kmap
  Removed dependency on ws2_32.dll - this means it will work on Windows 95
  Added yudit.editor.xinputs.style property to yudit.properties.
    possible values: root,over-the-spot,off-the-spot,over-the-spot-off
* Sun Jan 5 2003 Kevin Patrick Scannell <scannell@slu.edu>
  Added Irish (ga).
* Sun Dec 1 2002 Gaspar Sinai <gsinai@yudit.org>
  Added kmap and Russian menu from Vyacheslav Dikonov <sdiconov@mail.ru>
  Added berbere from Bruno Cauchy Lefebvre <bb.lefebvre@free.fr>
  Added Farsi.kmap from  Seyed-allaei <allaei@sissa.it>
  Reorganized kmaps a bit
  Largefont redrawing fix
  Added 'C' locale -> '' local patch from Jean-Marc Lienher <oksid@bluewin.ch> 
  Added simple-dark syntax highlight for light background setup
  Made composing mark work within ligatures too, when shaped.
  Keymap cleanups 
  OldHungarian keymap became HungarianRunes keymap.
  Fixed printing for WindowsXP+ghostscript (Window98 was ok)
* Sun Nov 10 2002 Gaspar Sinai <gsinai@yudit.org>
  Added full, Unicode compliant bi-directional support
  Added Sanskrit.kmap from Yves Codet <ycodet@club-internet.fr>
  Added Polish gui translations from Pawel Zawila-Niedzwiecki <zawel@wgt.com.pl>
  Added Perian.kmap from Roozbeh Pournader <roozbeh@sharif.edu>
  Added ZWJ ZWNJ RLM LRM as a visible glyph when editing.
  Optimized code for speed
  Added Inuktitut-ICI.kmap, Inuktitut-KBD.kmap, Chinese-Pinyin.kmap, 
   Chinese-WB.kmap from "Johnson, Howard" <Howard.Johnson@nrc.ca>
  Added OpenType GPOS support for composing characters
* Sat Oct 10 2002 Gaspar Sinai <gsinai@yudit.org>
  Added Urdu/Pakistan ur locale from S H A N <shanali@singnet.com.sg>
  Added new ligatures for URDU: U+06A9 U+0627 and U+06A9 U+0644
  Modified Amharic/Ethiopia am locale Daniel Yacob <locales@geez.org>
  Updated FAQs.
  Added better composing support. Undo/Redo for composing characters
   that are added on the fly.
  Removed clustering feature from several kmaps as cluster now can be 
  built on the fly.
  IS_AS,IS_BN,IS_DV,IS_GJ,IS_KN,IS_ML,IS_OR,IS_PJ,IS_RM,IS_TL,IS_TM
  converters from Anirban.
* Tue Sep 03 2002 Gaspar Sinai <gsinai@yudit.org>
  Applied patches and contibutions:
  Rendering fixes (Miikka-Markus Alhonen)
  Bengali menu (Anirban Mitra <mitra_anirban@yahoo.co.in>)
  Color Highlighting, word wrapping and other fixes:
     Maarten van Gompel <proycon@anaproy.homeip.net>
* Sun May 31 2002 Gaspar Sinai <gsinai@yudit.org>
- OpenType font shaping support for shaped characters that are not
  among Ararbic presentation forms. This inlcudes quite a few Arabic 
  and Syriac shapes.  
- Support for unifont syriacforms.hex and arabforms.hex files with
  direct font rendering.
- Fixed crash on Sparc computers (alignment problem)
- Koran menu and FAQ translations from Jungshik Shin <jshin@mailaps.org>
- Amharic menu translations from Daniel Yacob <locales@geez.org>
- Cherokee.kmap from Steve Juranich <sjuranic@ee.washington.edu>
- Added Vietnamese FAQ.TXT HOWTO-vietnamese.txt and message.po
  from Hoan <hoan@wanadoo.fr>
- Added Urdu.kmap from Miikka-Markus.Alhonen@tigatieto.com
* Wed Apr 25 2002 Gaspar Sinai <gsinai@yudit.org>
- Unicode 3.2 changes
- X Locale and Input Method Support 
- Added direct rendering for iso10646 encoded .bdf font files 
  and unifont .hex files. It is useful on platforms that do not have X11.
- Locale name for Chinese has been corrected to be zh (ISO639)
- True Type cmap 12 (needed for plane1,2..) and X11 (iso10646p2-\d+) added
- True Type cmap 2 with external converter added
- True Type uses now nonzero winding rule now by default.
- UTF-16 UTF-16-LE UTF-16-BE support.
- New converters for utf-16 utf-16-le utf-16-be, gb-18030, 
  Shift_JISX0213 (shift-jis-3), EUC-JISX0213 (euc-jp-3), 
  ISO-2022-JP-3 (iso-2022-jp-3) 
- Old Italic software glyph mirroring added
- Updated ksx-1001 (replacement for ksc-5601-old), ksc-5601-r ksc-5601-l
- Updated HOWTO-Japanese.txt
- JIS X 0213 X11 (jisx0213.2000-1,jisx0213.2000-2) font support
- Shift_JISX0213 encoded True Type font support with shift-jis-3 converter
* Sat Feb 28 2002 Gaspar Sinai <gsinai@yudit.org>
- Malayalam support (Miikka-Markus Alhonen)
- Kannada support (Miikka-Markus Alhonen)
- Telugu support (Miikka-Markus Alhonen)
- koi8-c support (Miikka-Markus Alhonen)
- koi8-u support (Gaspar)
- ncr converter (Miikka-Markus Alhonen)
- rovas converter (Gaspar)
- iso-8859-15 converter (Gaspar)
- iso-8859-16 converter (Gaspar)
- Mirrored characters (Miikka-Markus Alhonen-Gaspar)
- Old Hungarian support with ligatures in Private Use Area (Gaspar)
- Ukrainian kmap and translations (Solotskyy)
* Wed Jan 26 2002 Gaspar Sinai <gsinai@yudit.org>
- Pango X11 Ligature support
- Devanagari support (Miikka-Markus Alhonen)
- Bengali support (Miikka-Markus Alhonen)
- Gujarati support (Miikka-Markus Alhonen)
- Gurmukhi support (Miikka-Markus Alhonen)
- Oriya support (Miikka-Markus Alhonen)
- Hindi menu (Sanjay)
* Wed Jan 02 2002 Gaspar Sinai <gsinai@yudit.org>
- Tamil support (Vasee)
- Added Hangul Jamos (Miikka-Markus Alhonen)
- OpenType Ligature substitution support
- Testing other Indic scripts.
- Fixed bumap.
* Tue Nov 27 2001 Gaspar Sinai <gsinai@yudit.org>
- Prepearing for 2.5 with shaping (Arabic) support.
- Changed (removed -e, added auto-tmpfile): yudit.default.preview.command=gv
* Fri Nov 09 2001 Gaspar Sinai <gsinai@yudit.org>
- Fixed shift-jis converter
- Optimized speed
- Fixed layout manager bugs, made it nicer.
- Optimized memory usage (vut it by a factor of 2)
- Added freehand (handwriting) input method.
- Added hiragana and katakana handwriting data (hwd 2.0)
  generated by Yuko Inui <yuko@yudit.org>
* Thu Oct 25 2001 Gaspar Sinai <gsinai@yudit.org> patch 1,2,3,4,5,7,8
- renamed yudit-2.4-destdir.patch to //yudit.org/download/yudit-2.4.patch5.txt
- added 7,8
- renamed bz2 to gz in Source:
- removed doc from being doc because yudit uses it.
* Wed Aug 29 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.3-4
- Fix build as non-root
- Add patches from yudit.org
- Set prefix correctly
- Use %%configure
- Add docs
- Add desktop file
- Fix up specfile
