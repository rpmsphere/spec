%undefine _debugsource_packages
%define srcname	2ManDVD

Name:		2mandvd
Version:	1.8.5
Release:	1
Summary:	Video DVD creation tool, successor to ManDVD
# GPLv2 and LGPL for some icons
License:	GPLv2 and LGPL
Group:		Video/Editors and Converters
URL:		https://2mandvd.tuxfamily.org/website/
Source0:	https://download.tuxfamily.org/2mandvd/%{srcname}-%{version}.tar.gz
Patch1:		2ManDVD-1.8.4-fix_install.patch
Patch2:		2ManDVD-1.8.5-libavformat54.patch
BuildRequires:	qt4-devel >= 4.6
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(sdl)

Requires:	dvd+rw-tools
Requires:	dvdauthor
Requires:	ffmpeg
Requires:	ffmpegthumbnailer
Requires:	mencoder
Requires:	mjpegtools
Requires:	mkisofs
Requires:	mplayer
Requires:	netpbm
Requires:	sox
Requires:	exif
Recommends:	transcode
Obsoletes:	2ManDVD

%description
2ManDVD is a graphical tool for creating Video DVDs and slideshows, including
menus.

N.B. Executable name is 2ManDVD

%prep
%setup -q -n %{srcname}
%autopatch -p1
sed -i -e '86d' -e '430i GLfloat light_position[];' tetrahedron.h
sed -i -e 's|PIX_FMT_RGB24|AV_PIX_FMT_RGB24|' -e 's|avcodec_alloc_frame|av_frame_alloc|' videowrapper.cpp

%build
#qmake_qt4 2ManDVD.pro
qmake-qt4
sed -i 's|-O2|-O|' Makefile
make

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.txt
%{_bindir}/%{srcname}
%{_bindir}/fake.pl
%dir %{_datadir}/%{srcname}
%{_datadir}/%{srcname}/2mandvd_*.qm
%{_datadir}/%{srcname}/Bibliotheque
%{_datadir}/%{srcname}/mandvdico.png
%{_datadir}/applications/%{srcname}.desktop

%changelog
* Mon May 16 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.5
- Rebuilt for Fedora

* Tue Nov 24 2015 daviddavid <daviddavid> 1.8.5-1.mga6
+ Revision: 905727
- new version: 1.8.5
- update URL
- BR pkgconfig(sdl)
- rename and rediff patch2 libavformat54

* Fri Nov 14 2014 cjw <cjw> 1.8.4-9.mga5
+ Revision: 797094
- patch3: fix build with ffmpeg 2.4

  + fwang <fwang>
    - add gentoo patch to make it build with latest ffmpeg
    - rebuild for new ffmpeg

* Wed Oct 15 2014 umeabot <umeabot> 1.8.4-8.mga5
+ Revision: 745887
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 1.8.4-7.mga5
+ Revision: 677628
- Mageia 5 Mass Rebuild

  + tv <tv>
    - s/uggests:/Recommends:/

* Sat Oct 19 2013 umeabot <umeabot> 1.8.4-6.mga4
+ Revision: 529783
- Mageia 4 Mass Rebuild

* Fri Jul 12 2013 fwang <fwang> 1.8.4-5.mga4
+ Revision: 453232
- more ffmpeg patch
- rebuild for new ffmpeg

* Fri Jan 11 2013 umeabot <umeabot> 1.8.4-4.mga3
+ Revision: 345045
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Tue Jan 08 2013 fwang <fwang> 1.8.4-3.mga3
+ Revision: 341585
- rebuild for new ffmpeg

* Fri Nov 09 2012 zezinho <zezinho> 1.8.4-2.mga3
+ Revision: 316731
- fix missing files

* Mon Oct 08 2012 juancho <juancho> 1.8.4-1.mga3
+ Revision: 303401
- Updated to 1.8.4

* Mon Jun 25 2012 fwang <fwang> 1.8.3-1.mga3
+ Revision: 263421
- new version 1.8.3

* Tue May 29 2012 fwang <fwang> 1.7.3-2.mga3
+ Revision: 249056
- try another method
- fix build with latest ffmpeg
- rebuild for new ffmpeg

* Tue Dec 27 2011 juancho <juancho> 1.7.3-1.mga2
+ Revision: 188139
- Updated to 1.7.3

* Mon Dec 12 2011 doktor5000 <doktor5000> 1.7.2-1.mga2
+ Revision: 181031
- add missing BuildRequires on ffmpeg-devel
- remove obsolete BuildRoot
- new version 1.7.2
- added necessary Requires on exif
- define Description and Summary more precisely

* Wed Jun 15 2011 kharec <kharec> 1.5.5-1.mga2
+ Revision: 106776
- new version

* Mon Mar 14 2011 steletch <steletch> 1.5.3-1.mga1
+ Revision: 71450
- Update to 1.5.3
- imported package 2mandvd


* Sat Oct 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4-1mdv2011.0
+ Revision: 584384
- Update to new version

* Fri Jul 30 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.3.5-1mdv2011.0
+ Revision: 563290
- update to 1.3.5
- drop patch0, merged upstream
- improve description
- Exec in the .desktop file must be 2ManDVD, lower case doesn't work
- drop the .desktop file from SOURCES and create it in the spec instead, this way
  it's easier to spot necessary changes

* Mon Apr 19 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.3.3-4mdv2010.1
+ Revision: 536759
- Adjust ppegtopnm detection, fixes #58695

* Mon Apr 19 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.3.3-3mdv2010.1
+ Revision: 536729
- Add missing fake.pl script

* Sun Mar 28 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3.3-2mdv2010.1
+ Revision: 528474
- rebuild
- Update to 1.3.3

* Sat Mar 13 2010 Funda Wang <fwang@mandriva.org> 1.3.2-1mdv2010.1
+ Revision: 518684
- new version 1.3.2

* Mon Mar 08 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.3.1-2mdv2010.1
+ Revision: 515906
- Correct growisofs requires

* Mon Mar 01 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3.1-1mdv2010.1
+ Revision: 513035
- Update to 1.3.1

* Thu Feb 25 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.3-2mdv2010.1
+ Revision: 511190
- Forgot to bump rel
- Add missing Requires
- Transform trancode requires into suggests since this package is not available in official mandriva repositories

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - 1.3 now requires qt >= 4.6

* Wed Feb 24 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.3-1mdv2010.1
+ Revision: 510789
- rename back the symlink in bindir, otherwise it doesn't work??
- adapt spec for package renaming
- rename to lowercase
- clean spec
- fix license
- update to 1.3
- name the executable 2mandvd, more robust this way
- use "EXEC=2mandvd -graphicssystem raster" as per upstream's recomendation
- fix requires (again)
- fix requires

* Wed Jan 27 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.2-3mdv2010.1
+ Revision: 497157
- only suggest transcode

* Wed Jan 27 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.2-2mdv2010.1
+ Revision: 496931
- use %%qmake_qt4 and %%make macors (the latter to enable parallel build
  which seems to work)
- make .desktop file compliant with xdg specs

* Mon Jan 18 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.2-1mdv2010.1
+ Revision: 493378
- import 2ManDVD
