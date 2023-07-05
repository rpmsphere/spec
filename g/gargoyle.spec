Name:         gargoyle
License:      GPL-2.0 and GPL-3.0 and Artistic-2.0 and MIT and OFL-1.0 and SUSE-NonFree and SUSE-Liberation
Group:        Amusements/Games/Other
Version:      2015
Release:      5.4
Summary:      Multi-format interactive fiction player with excellent readability
URL:          https://ccxvii.net/gargoyle/
# Source:       https://garglk.googlecode.com/files/%%{name}-%%{version}-sources.zip
Source:       garglk-master.zip
Source1:      README.games
BuildRequires: SDL_mixer-devel gtk2-devel jam libpng-devel gcc-c++ SDL_sound-devel
BuildRequires: libjpeg-devel
# libvorbis-devel libsmpeg-devel no longer buildrequired in svn version
BuildRequires:  hicolor-icon-theme

%description
Gargoyle is an IF player that supports all the major interactive fiction
formats.

Most interactive fiction is distributed as portable game files. These
portable game files come in many formats. In the past, you used to have to
download a separate player (interpreter) for each format of IF you wanted to
play.

Gargoyle is based on the standard interpreters for the formats it supports.
Gargoyle is free software released under the terms of the GNU General Public License.

All of the following interpreters have been compiled for Gargoyle and are included in the package:
* agility       | 1.1.1.1
* advsys        | 1.2
* alan          | 2.8.6
* alan3         | 3.0b2
* bocfel        | 0.6.1
* frotz         | 2.5.0
* geas          | 0.4
* git           | 1.2.9
* glulxe        | 0.4.7
* hugo          | 3.1.03
* jacl          | 2.9.0
* level9        | 5.1
* magnetic      | 2.3
* nitfol        | 0.5
* scare         | 1.3.10
* scottfree     | 1.14
* tads2         | 2.5.15
* tads3         | 3.1.0
These interpreters are freely distributable, but are still copyrighted by their authors and covered by their own licenses. 

Gargoyle cares about typography! In this computer age of typographical
poverty, where horrible fonts, dazzling colors, and inadequate white space
is God, Gargoyle dares to rebel!

* Subpixel font rendering for LCD screens.
* Unhinted anti-aliased fonts: beautiful, the way they were designed.
* Adjustable gamma correction: tune the rendering for your screen.
* Floating point text layout for even spacing.
* Kerning for even more even spacing.
* Smart quotes and other punctuation formatting.
* Ligatures for 'fi' and 'fl'. 
* Plenty o' margins.
* Plenty o' line spacing.
* Integrated scrollback.

The default font for Gargoyle is Bitstream Charter and Luxi Mono. Two vastly
underrated fonts that I find just perfect for screen reading. They are
included, so there is no need to install anything on your system.

Gargoyle does not use any operating system functions for drawing text, so it
can use any TrueType, OpenType or Postscript font file you specify in the
configuration file.

%prep
%setup -q -n garglk-master
%{__cp} -p %{SOURCE1} .
%{__sed} -i -e '/^Icon=/s/\..*$//' -e 's|^Categories=Game;|Categories=Game;Emulator;|' garglk/%{name}.desktop

%build
# I: Program is likely to break with new gcc. Try -fno-strict-aliasing -fpermissive
export CFLAGS="${CFLAGS:-%optflags} -fno-strict-aliasing -fpermissive"
export LDFLAGS=-Wl,--allow-multiple-definition
jam %{?_smp_mflags}

%install
jam -s_BINDIR=%{_libdir}/%{name} -s_LIBDIR=%{_libdir}/%{name} -s_APPDIR=%{_libdir}/%{name} -sDESTDIR=%{buildroot} -sEXEMODE=755 -sFILEMODE=755 install
install -d -m 755 %{buildroot}/%{_bindir}
ln -s %{_libdir}/%{name}/%{name} %{buildroot}/%{_bindir}
ln -s %{_libdir}/%{name}/libgarglk.so %{buildroot}/%{_libdir}
install -D -m 644 garglk/garglk.ini %{buildroot}/etc/garglk.ini
install -D -m 644 garglk/%{name}.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop 
install -D -m 644 garglk/%{name}-house.png %{buildroot}/%{_datadir}/pixmaps/%{name}-house.png

%files
%doc licenses License.txt README.games
%{_bindir}/%{name}
%{_libdir}/libgarglk.so
%{_libdir}/%{name}
%config /etc/garglk.ini
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-house.png

%changelog
* Mon Jan 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2015
- Rebuilt for Fedora
* Tue Dec  4 2012 fa0sck@gmail.com
- Improve spec - fix icon name in desktop file
* Sun Nov 25 2012 fa0sck@gmail.com
- Created package for gargoyle svn 2012-11-25
  (With svn checkout https://garglk.googlecode.com/svn/trunk/ garglk-read-only)
  * See also https://garglk.googlecode.com
