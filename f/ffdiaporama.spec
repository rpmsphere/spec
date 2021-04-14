%define oname   ffDiaporama

Name:           ffdiaporama
# Version 2.2.devel.2014.0701
Version:        2.1.9
Release:        8.1
Summary:        Movie creator from photos and video clips
License:        GPLv2
URL:            http://ffdiaporama.tuxfamily.org
Group:          Video/Editors and Converters
Source:         http://download.tuxfamily.org/%{name}/Packages/Stable/%{name}_bin_2.2.devel.2014.0701.tar.gz
# http://ffdiaporama.tuxfamily.org/Forum/viewtopic.php?id=781
Patch0:         ffDiaporama-2.2-devel-2014.0701-mga-i18n-semicolon-desktop.patch
Patch1:         ffdiaporama-ffmpeg-2.4.patch
Patch2:         ffdiaporama-audiodecode.patch
Patch3:         ffdiaporama-nodownload.patch
Patch4:         ffdiaporama-workingdir.patch
Patch5:         ffdiaporama-2.2-ffmpeg-3.2.patch
BuildRequires:  desktop-file-utils
BuildRequires:  compat-ffmpeg28-devel
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Widgets)
Recommends:     ffdiaporama-texturemate
Recommends:     ffdiaporama-openclipart

%description
ffDiaporama is an application for creating video sequences consisting of
* titles, fixed or animated.
* images or photos, fixed or animated.
* movie clips
* music

These sequences are assembled into a slide show by means of transitions
to produce complete videos
The following options are available:

* Reframing of images and photos
* Cutting of video clips
* Adding text, notes to images, photos, sequences and animations
* Graphical filters on the images and the videos (conversion into
  black and white, dust removal, equalization of colors, etc.)
* Creation of animation by zoom, rotation or Ken Burns Effect on
  images or photos
* Correction of the images and the videos during animations
  (luminosity, contrast, gamma, colors, etc.)
* Transitions between sequences with definition of the transition type,
  sequence by sequence.
* Addition of a background sound (wav, mp3 or ogg) with customizable
  effects for volume, fade in/out and passage in pause, sequence by sequence.
* Generation of videos usable on most current video equipment
  (DVD player/smartphone, multimedia box, hard drive, etc.)
  but also publishable on the main video-sharing Websites
  (YouTube, Dailymotion, etc.)
* Video formats from QVGA (320×240) to Full HD (1920×1080)
  by way of the DVD and HD 720 formats.
* Image geometry (aspect ratio) : 4:3, 16:9 or 2.35:1 (cinema)
* Possible formats for rendering : avi, mpg, mp4, webm, mkv

%prep
%setup -q -n %{oname}
%autopatch -p1
chmod -x *.*
sed -i 's|include/ffmpeg|include/compat-ffmpeg28|' src/ffDiaporama/ffDiaporama.pro

%build
cp /usr/share/automake-*/config.guess .
%qmake_qt5 QMAKE_CFLAGS_ISYSTEM= %{oname}.pro
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

install -m 0644 locale/*  %{buildroot}%{_datadir}/%{oname}/locale/
find %{buildroot}%{_datadir}/%{oname}/locale -name "*.ts" | xargs rm -f

(cd %{buildroot} && find . -name '*.q*') | sed -e 's|^.||' | sed -e \
    's:\(.*/locale/\)\([_a-z_A-Z]\+\)\(.q\):%lang(\2) \1\2\3:' >> %{name}.lang

# Keep only the language code in lang tags like: '%%lang{wiki_xx}'
%__sed -i -e 's:\(%lang(\)\([A-Za-z]\+_\)\([a-z)]\+\):\1\3:' %{name}.lang

%files -f %{name}.lang
%{_datadir}/%{oname}
%{_bindir}/%{oname}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/mime/packages/%{oname}-mime.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Wed Jul 04 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.9.devel.2014.0701
- Rebuilt for Fedora
* Fri Feb 16 2018 daviddavid <daviddavid> 2.1.9.devel.2014.0701-11.mga7
+ Revision: 1201765
- add QMAKE_CFLAGS_ISYSTEM= qmake option to fix build with gcc6+
* Tue Jun 20 2017 neoclust <neoclust> 2.1.9.devel.2014.0701-10.mga6
+ Revision: 1108014
- Rebuild against new exiv2
* Tue May 02 2017 akien <akien> 2.1.9.devel.2014.0701-9.mga6
+ Revision: 1098353
- Rebuild for ffmpeg 3.3
* Wed Mar 08 2017 akien <akien> 2.1.9.devel.2014.0701-8.mga6
+ Revision: 1089849
- Rebuild for ffmpeg 3.2.4
* Tue Feb 21 2017 cjw <cjw> 2.1.9.devel.2014.0701-7.mga6
+ Revision: 1087161
- patch5: fix build with ffmpeg 3.2
* Sun Feb 14 2016 umeabot <umeabot> 2.1.9.devel.2014.0701-6.mga6
+ Revision: 960060
- Mageia 6 Mass Rebuild
* Sun Nov 16 2014 cjw <cjw> 2.1.9.devel.2014.0701-5.mga6
+ Revision: 797447
- patch1: fix build with ffmpeg 2.4
- patch2: drop error message about not being able to decode an audio frame
- patch3: use locale files in /usr/share instead of trying to download them
- patch4: the application's files are in /usr/share so don't look for them in other places
  + fwang <fwang>
    - rebuild for new ffmpeg
* Wed Oct 15 2014 umeabot <umeabot> 2.1.9.devel.2014.0701-4.mga5
+ Revision: 745648
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 2.1.9.devel.2014.0701-3.mga5
+ Revision: 679165
- Mageia 5 Mass Rebuild
* Mon Sep 15 2014 alexl <alexl> 2.1.9.devel.2014.0701-2.mga5
+ Revision: 676919
- fixed executable permissions
- translated desktop file
  + tv <tv>
    - s/uggests:/Recommends:/
* Fri Jul 04 2014 dglent <dglent> 2.1.9.devel.2014.0701-1.mga5
+ Revision: 643260
- New 2.2 devel version 2014.0701
* Mon May 12 2014 dglent <dglent> 2.1.9.devel.2014.0510-1.mga5
+ Revision: 622241
- New version 2.2.devel.2014.0510
- Don't remove the TXT files with version of locales
- Qt5 build
* Thu Mar 27 2014 dglent <dglent> 2.1-3.mga5
+ Revision: 608905
- Add qt4-database-plugin-sqlite in requires
* Mon Mar 24 2014 fwang <fwang> 2.1-2.mga5
+ Revision: 607766
- rebuild for new ffmpeg
* Sun Mar 23 2014 dglent <dglent> 2.1-1.mga5
+ Revision: 606716
- New version 2.1
- Restore translations from commit 589446
- Update %%source url
- Update %%description
- No more needed to create new folder in %%setup
* Tue Feb 11 2014 dams <dams> 2.0.1-2.mga5
+ Revision: 589446
- clean specfile for the locale part
* Mon Feb 10 2014 dams <dams> 2.0.1-1.mga5
+ Revision: 588995
- rebuild for new exiv2
* Fri Dec 13 2013 dglent <dglent> 2.0.1-1.mga4
+ Revision: 556585
- Remove patch for ffmpeg 2.0 (Support for ffmpeg 2.0 since ffDiaporama 2.0)
- New version 2.0.1
- Drop ffmpeg 2.0 patch
- Add Suggests ffDiaporama extensions
- Add lang tags for wiki
- Remove lang in double for zh_TW
- Remove qimageblitz from br (integrated in ffDiaporama 2.0)
- Add comment for removing br in next version
* Sat Oct 19 2013 umeabot <umeabot> 1.6-3.mga4
+ Revision: 529684
- Mageia 4 Mass Rebuild
  + dglent <dglent>
    - Remove duplicate lang tag
    - Add %%lang tags in spec
* Thu Jul 11 2013 fwang <fwang> 1.6-1.mga4
+ Revision: 452897
- use new avcodecid
  + dglent <dglent>
    - Update SPEC
    - New version 1.6
    - New version 1.6 beta5
* Fri Jan 11 2013 umeabot <umeabot> 1.5-3.mga3
+ Revision: 350257
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Tue Jan 08 2013 fwang <fwang> 1.5-2.mga3
+ Revision: 341617
- rebuild for new ffmpeg
  + dglent <dglent>
    - New version 1.5
* Sun Oct 07 2012 dglent <dglent> 1.4-1.mga3
+ Revision: 303202
- New version 1.4
* Mon Oct 01 2012 obgr_seneca <obgr_seneca> 1.3.1-1.mga3
+ Revision: 301627
- adapted to new rpm group policy
  + dglent <dglent>
    - New version 1.3.1
* Mon Jun 18 2012 fwang <fwang> 1.3-3.mga3
+ Revision: 261628
- rebuild for new libexiv
* Fri Jun 01 2012 fwang <fwang> 1.3-2.mga3
+ Revision: 252799
- drop unused requires, those requires are alrady promoted by binary deps
  + dglent <dglent>
    - 'licences.txt' was listed twice
* Mon May 28 2012 dglent <dglent> 1.3-1.mga3
+ Revision: 247821
- New version 1.3 stable
- New version 1.3beta1
* Mon Apr 09 2012 dglent <dglent> 1.2.1-1.mga2
+ Revision: 229802
- New stable version 1.2.1
* Tue Mar 06 2012 obgr_seneca <obgr_seneca> 1.2-1.mga2
+ Revision: 220460
- removed unneeded Requires
  + dglent <dglent>
    - New version 1.2 stable
    - imported package ffdiaporama
