Name:           fontinfo
Version:        2020121
Release:        1
Summary:        Overview of Installed Fonts
License:        GPL-2.0+
Group:          Productivity/Publishing/Other
URL:            https://github.com/pgajdos/fontinfo/
#Source:         %{name}-%{version}.tar.bz2
Source0:        %{name}-master.zip
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  rpm-devel
Requires:       xdg-utils

%description
Fontinfo makes an overview over installed fonts on system
where it is called. It is able to generate rendering info,
language info, character set etc. for each font. Fontinfo
can also integrate with package manager. From pages it
generates, it is possible to directly install font packages
or switch between default and system rendering of specimen
and see differences.

%prep
%setup -q -n %{name}-master

%build
make CFLAGS+=-Wno-format-security %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%doc COPYING CHANGES doc/THANKS.md
%{_bindir}/*

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2020121
- Rebuilt for Fedora
* Fri Apr 10 2015 pgajdos@suse.com
- updated to version 20150410
  * prevent buffer overflow for Supplementary Private Use Area-B
  * reformat CHANGES file
  * remove 1-click install for 12.2
* Wed Oct 29 2014 pgajdos@suse.com
- updated to version 20141029
  * 1-click install for 13.2 and sle12
* Mon Jun  9 2014 pgajdos@suse.com
- updated to version 20140609
  * fixed 1-click-install link in detailed view
* Fri May 30 2014 pgajdos@suse.com
- updated to version 20140530
  * 1-click-install link even in detailed view
* Fri May 23 2014 pgajdos@suse.com
- updated to version 20140523
  * fix sle12 ymp distroversion
  * 1-click-install link explicitely visible on Font Card
  * 1-click-install link in Family Overview page
* Fri Feb 28 2014 pgajdos@suse.com
- updated to version 2014028
  * added sle12 and 13.2 to ymps
* Fri Feb 21 2014 pgajdos@suse.com
- updated to version 20140219
  * added sles11 to ymps
* Tue Feb  4 2014 pgajdos@suse.com
- updated to version 20140204
  * improved and added several specimen strings
  * better align t2b layout
* Mon Jan 20 2014 pgajdos@suse.com
- updated to version 20140120
  * use relative sorting for scripts again as absolute seem to
    have more cons than pros
* Wed Jan 15 2014 pgajdos@suse.com
- updated to version 20140115
  * add or fix some specimen strings
  * alow rotation of specimen images (needed for Phags Pa and
    Mongolian)
  * charset toggle links has now block interval ranges
  * minor fixes
* Fri Dec 20 2013 pgajdos@suse.com
- updated to version 20131220
  * charset: view by unicode blocks, individual
    pngs download on demand
  * fixed or improve some specimen strings
* Wed Dec 11 2013 pgajdos@suse.com
- updated to version 20131211
  * polishing specimen view
* Fri Dec  6 2013 pgajdos@suse.com
- updated to version 20131206
  * improve opentype shaping (fix script tag indexing)
* Thu Dec  5 2013 pgajdos@suse.com
- updated to version 20131205
  * improve opentype shaping
* Wed Dec  4 2013 pgajdos@suse.com
- call spec-cleaner
* Tue Dec  3 2013 pgajdos@suse.com
- updated to version 20131203
  * involve harfbuzz to opentype shaping (not completely done)
* Tue Nov 26 2013 pgajdos@suse.com
- updated to version 20131126
  * new string for Byzantine Musical Symbols (thanks to Konstantinos
    Terzopoulos)
* Thu Nov 21 2013 pgajdos@suse.com
- updated to version 20131119
  * no underscores in script names above specimens
  * languages <-> sentences mapping as preparation
    for opentype shaping
  * new sentences for e. g. Math, Sundanese, etc.
* Thu Nov 14 2013 pgajdos@suse.com
- updated to version 20131114
  * extend Math and Musical_Symbols collections coverage
  * added sentences for Math and Musical_Symbols collections
* Tue Nov 12 2013 pgajdos@suse.com
- updated to version 20131112
  * index fonts by unicode blocks
  * introduce 'collections' (now Math and Musical_Symbols); they
    are on the same level as scripts, but defined by fontinfo
  * display software package description
  * added CHANGES file
* Fri Nov  8 2013 pgajdos@suse.com
- updated to version 20131108
  * do not display 'unknown' language anywhere
* Thu Nov  7 2013 pgajdos@suse.com
- updated to version 20131107
  * check for markdown command in Makefile, and fallback to cat
    if not found
- build require discount
* Wed Nov  6 2013 pgajdos@suse.com
- updated to version 20131106
  * bento: very minor improvement in menu boxes
* Tue Nov  5 2013 pgajdos@suse.com
- updated to version 20131105
  * font format index marks fonts with bitmap strikes
  * bento: improved menu boxes
* Fri Nov  1 2013 pgajdos@suse.com
- updated to version 20131101
  * added specimen sentences for few scripts
  * better names for generated indexes
* Thu Oct 31 2013 pgajdos@suse.com
- updated to version 20131031
  * added specimen sentences for few scripts
  * script names displays now without underscores
* Wed Oct 23 2013 pgajdos@suse.com
- updated to version 20131023
  * display truetype tables used in font
  * do not crash when no fonts found
  * escape dashes in pattern
* Wed Oct 16 2013 pgajdos@suse.com
- updated to version 20131016
  * png charset as an table, generate vertical header
  * split long charsets in parts
* Tue Oct 15 2013 pgajdos@suse.com
- updated to version 20131015
  * better appearance of charsets and specimens of bitmap fonts
* Mon Oct 14 2013 pgajdos@suse.com
- updated to version 20131014
  * minor fixes in script and family indexes (do not display certain
    fonts multiple times)
* Fri Oct 11 2013 pgajdos@suse.com
- updated to version 20131011
  * larger default size for charsets, trim large specimens
* Thu Oct 10 2013 pgajdos@suse.com
- updated to version 20131010
  * added sentences which fit special fonts
  * debug output, see new -g option
* Tue Oct  8 2013 pgajdos@suse.com
- updated to 20131008
  * support for right to left text direction in specimens
  * polishing displaying specimens:
  - > if there is no script covered
  - > if font doesn't cover minispecimen sentence
  * legal stuff
* Fri Sep 13 2013 pgajdos@suse.com
- updated to 20130913
  * script font index displays script blocks with ranges
* Wed Sep 11 2013 pgajdos@suse.com
- updated to 20130911
  * minor fix in Makefile to be parallel buildable
- enable paralell build
* Wed Sep 11 2013 pgajdos@suse.com
- format specfile
* Thu Sep  5 2013 pgajdos@suse.com
- updated to 20130904:
  * script indexes
* Tue Sep  3 2013 pgajdos@suse.com
- updated to 20130903
  * added support for unicode scripts:
  - > on fontcard show scripts, which the font is covering well
  - > predefined example sentences for each script
  - > for given script, choose sentence which is covered by font
  - > possibility to alter script also for mini specimens (new -m option)
  * -s now 'enforces' one sentence for all fonts
  * new -e option specifies text direction of sentence specified in -s
* Fri May 10 2013 pgajdos@suse.com
- minor improvement of font format index
* Thu May  9 2013 pgajdos@suse.com
- updated to version 20130509:
  * new index added: Families by Font Formats
* Fri Apr 12 2013 pgajdos@suse.com
- updated to version 20130412:
  * slash in family name caught me unprepared
* Thu Apr 11 2013 pgajdos@suse.com
- updated to version 20130411:
  * font card lists also rgba and lcdfilter pattern elements
    if available
  * other minor improvements, such as embeddedbitmaps element
    is shown only if the font have at least one bitmap strike
* Mon Apr  8 2013 pgajdos@suse.com
- updated to version 20130408:
  * implement repository links (generic) and one click install
    (openSUSE); see new -n and -r options
* Thu Apr  4 2013 pgajdos@suse.com
- updated to version 20130404:
  * can display both bitmap and outline specimen and switch
    between them (to see the difference between font rendered
    by default and font rendered on client's system); see new -a
    option
* Mon Mar 25 2013 pgajdos@suse.com
- updated to version 20130325:
  * render embedded bitmaps correctly
* Thu Mar 21 2013 pgajdos@suse.com
- updated to version 20130321:
  * display use of embedded bitmaps and available bitmaps in font
  * better rendered specimen of bitmap fonts
* Fri Mar 15 2013 pgajdos@suse.com
- updated to version 20130315:
  * display tooltips in specimens: font sizes (see new -z option)
  * display more files in File(s): section for bitmap fonts
* Tue Mar 12 2013 pgajdos@suse.com
- updated to version 20130312:
  * use freetype2 and libpng for image rendering, don't use
    ImageMagick
* Fri Mar  1 2013 pgajdos@suse.com
- updated to version 20130301:
  * detailed view also for ALL families
  * other minor improvements
* Thu Feb 14 2013 pgajdos@suse.com
- updated to version 20130214:
  * added forgotten package-manager.sh, which caused empty
    Software Package Information section
  * do not leak file descriptors
* Wed Feb 13 2013 pgajdos@suse.com
- updated to version 20130213:
  * added Software Package Information section to Font Card
  * added foundry, capability and fontformat to Family Overview
* Thu Feb  7 2013 pgajdos@suse.com
- updated to version 20130207:
  * minor improvements
* Wed Feb  6 2013 pgajdos@suse.com
- updated to version 20130206:
  * minor improvements
* Tue Feb  5 2013 pgajdos@suse.com
- updated to version 20130205:
  * code refactorized to be able to easily add styles
  * added bento style
  * possibility to switch between plain and bento style,
    see new -y option
  * when charset doesn't cover given specimen sentence, take
    first few characters from the charset as sentence
* Tue Jan 15 2013 pgajdos@suse.com
- updated to version 20130115:
  * character set is enriched by tooltips, see new -u option
* Thu Dec 20 2012 pgajdos@suse.com
- updated to version 20121220:
  * implement some suggestions: offer splitted index of families,
    increase fontsize in character set, minispecimens along family
    names, etc.
  * fixed bug: some fonts have empty specimen and charset
  * export some options to command line parameters, namely:
  - d string: place all generated pages in dir [htmls]
  - o string: type of the font text output (specimens, charset) [png]
    possible values: html,svg,png
  - s string: specimen sentence [The quick brown fox jumps over the lazy dog.]
  - f int:    specimen: from pixel size [7]
  - t int:    specimen: to pixel size [25]
  - c bool:   display character set [on]
    possible values: on, off
  - x int:    charset pixel size [16]
  - p string: limit output only to pattern [:]
  - l string: describe where you take fonts from,
    e. g. localhost, M17N:fonts, etc. [localhost]
  - i bool:   generate indexes [on]
    possible values: on, off
* Mon Dec 10 2012 pgajdos@suse.com
- updated to version 20121210:
  * generates charset
* Thu Dec  6 2012 pgajdos@suse.com
- updated to version 20121206:
  * specimen is generated as PNG, it requires ImageMagick
    installed runtime, though
* Wed Nov 28 2012 pgajdos@suse.com
- fixed gcc warnings
- bundle fontinfo_browse.sh into tarball
- use make install
* Tue Nov 27 2012 jw@suse.com
- added allow_opt_flags.diff
- we now expose some warnings triggered by using $RPM_OPT_FLAGS
* Tue Nov 27 2012 pgajdos@suse.com
- updated to version 20121127.1:
  * fontinfo takes one parameter, html-root-dir; it will
    install there two index files and three directories
    (families, fonts and languages) which fills with
    appropriate contents.
  * simplify fontinfo_browse.sh thanks to above
  * usage() function implemented
* Tue Nov 27 2012 jw@suse.com
- added languages.txt (hope this is machine independant)
- BuildRequires added: freetype2-devel for SLE11
* Tue Nov 27 2012 pgajdos@suse.com
- updated to version 20121127, builds with fontconfig < 2.9.0
* Tue Nov 27 2012 jw@suse.com
- skipping FcLangSetDel is not an option. Removed compat280.diff
* Tue Nov 27 2012 jw@suse.com
- initial ci
