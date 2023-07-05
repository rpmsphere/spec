Name: mp3blaster
Version: 3.2.6
Release: 1
Group: Sound
Summary: An interactive text-console based mp3 player
License: GPLv2
URL: https://mp3blaster.sourceforge.net
Source: https://easynews.dl.sourceforge.net/sourceforge/mp3blaster/mp3blaster-%version.tar.gz
Patch1: mp3blaster-3.2.0-alt-id3cyr.patch
Patch2: mp3blaster-3.2.0-alt-id3show.patch
Patch3: mp3blaster-alt-makefile-system_getopt.patch
BuildRequires: gcc-c++ ncurses-devel libstdc++-devel

%description
Mp3blaster is an audio player with a user-friendly interface that will run
on any text console. The interface is built using ncurses, and features all
common audio player controls. The playlist editor is very flexible and allows
nested groups (albums). Supported audio media: mp3, ogg vorbis, wav, sid and
streaming mp3 over HTTP.

%prep
%setup -q
%patch1 -p1
#patch2 -p1
%patch3 -p2
rm -fv -- src/getopt*
sed -i 's|0-1, 0-1|128, 128|g' mpegsound/huffmantable.cc

%build
autoreconf -ifv
%configure
make --silent --no-print-directory

%install
%make_install --silent --no-print-directory

%files
%doc AUTHORS ChangeLog CREDITS README TODO
%_bindir/mp3blaster
%_bindir/mp3tag
%_bindir/splay
%_bindir/nmixer
%_datadir/%name/
%_mandir/man1/mp3blaster.1*
%_mandir/man1/nmixer.1*
%_mandir/man1/splay.1*

%changelog
* Mon Oct 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.6
- Rebuilt for Fedora
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.2.5-alt1.qa1
- NMU: rebuilt for debuginfo.
* Sun Apr 12 2009 Slava Semushin <php-coder@altlinux.ru> 3.2.5-alt1
- Updated to 3.2.5
- New maintainer
- Updated Url tag
- Updated Summary field
- More proper License tag
- Exclude useless COPYING, INSTALL and NEWS files from package
- Include CREDITS file to package
- Directory /usr/share/mp3blaster now belongs to package
- Enabled _unpackaged_files_terminate_build
* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.2.0-alt9.1
- Rebuilt with libstdc++.so.6.
- Remove gcc3.3-c++ and libstdc++3.3-devel from BuildReq.
* Wed May 12 2004 Nick S. Grechukh <gns@altlinux.ru> 3.2.0-alt9
- spec cleaned as for alt-packaging
* Wed May 12 2004 Nick S. Grechukh <gns@altlinux.ru> 3.2.0-alt7
- fixed packager
* Tue May 10 2004 Nick S. Grechukh <gns@altlinux.ru> 3.2.0-alt6
- added buldreq
- fixed building on sisyphus - explicit req gcc3.3
* Wed Feb 12 2004 Nick S. Grechukh <ngrechukh@ua.fm> 3.2.0-alt2
- applied id3show.patch
* Wed Jan 28 2004 Nick S. Grechukh <ngrechukh@ua.fm> 3.2.0-alt2
- applied own id3cyr.patch for correct display id3 with ascii>127.
* Mon Jan 26 2004 Nick S. Grechukh <ngrechukh@ua.fm> 3.2.0-alt1
- first build for Sisyphus
