Summary: 	Media center
Name: 		enna
Version: 	0.4.1
Release: 	0.20120722
License: 	e16-like
Group: 		Graphical desktop/Enlightenment
URL:		https://github.com/naguirre/enna
Source0: 	enna-master.tar.gz
BuildRequires:  autoconf, gettext
BuildRequires:  evas-devel
BuildRequires:  ecore-devel
BuildRequires:	edje
BuildRequires:  edje-devel
BuildRequires:	eet-devel
BuildRequires:	embryo
BuildRequires:	embryo-devel
BuildRequires:	elementary-devel
BuildRequires:	dbus-devel
BuildRequires:	libplayer-devel
BuildRequires:	libvalhalla-devel
BuildRequires:	libcddb-devel
BuildRequires:	lirc-devel
BuildRequires:  ethumb-devel
BuildRequires:  libtool
BuildRequires:  gettext-devel
BuildRequires:  gupnp-av-devel
BuildRequires:  e_dbus-devel
Source1: enna-0.4.0.zh_TW.po
Source2: wqy-microhei.ttc
Source3: wqy-microhei-lite.ttc
Patch0: enna-0.4.0-gettext-label.patch
Patch1: enna-0.4.0-get_lang.patch

%description
A media center based on the Enlightenment libraries.

%prep
%setup -q -n enna-master
%patch0 -p1
%patch1 -p1
##cp -f %{SOURCE1} po/zh_TW.po
cp -f %{SOURCE2} data/theme/default/fonts/content_bold.ttf
cp -f %{SOURCE3} data/theme/default/fonts/content.ttf
##sed -i -e '/\.ttf/d' data/theme/default/default.edc
##sed -i '28i #include <Ethumb_Client.h>' src/bin/view_wall.c
##sed -i '/PLAYER_TYPE_SPOTIFY/d' src/bin/mediaplayer.c
##sed -i 's|^Exec=enna|Exec=enna -t /usr/share/enna/theme/default.edj|' data/other/enna.desktop
sed -i -e 's/weather=/oe=utf-8\&weather=/' -e 's/Paris/Taipei/' src/bin/weather_api.c
#sed -i -e '367s/ NULL,//' -e '394s/ NULL,//' src/bin/view_list2.c
###sed -i -e 's|//elm_object_style_set|elm_object_style_set|' -e 's|elm_label_slide_set|//elm_label_slide_set|' src/bin/mediaplayer_obj.c
###sed -i -e 's/elm_layout_data_get/elm_layout_text_get/' src/bin/infos.c
sed -i 's/"Main Menu",/_("Main Menu"),/' src/bin/browser_obj.c
#sed -i '/Wind:/d' src/bin/weather_api.c data/theme/*/*.edc
###sed -i -e '184i \            fixed: 1 1;' -e '301i \            fixed: 1 1;' -e '331i \            fixed: 1 1;' data/theme/default/activity_video.edc
###sed -i 's|elm_box_homogenous_set|elm_box_homogeneous_set|' src/bin/mediaplayer_obj.c src/bin/box.c
sed -i 's|Elm_Slideshow_Item |Elm_Object_Item |' src/bin/mainmenu.c src/modules/activity/photo/photo_slideshow_view.c
sed -i 's|Elm_Genlist_Item |Elm_Object_Item |' src/bin/view_list2.h src/bin/view_list.c src/modules/input/wiimote/wiimote.c src/bin/weather_api.c src/bin/view_list2.c src/bin/module.c
###sed -i 's|elm_genlist_item_bring_in(....|&, ELM_GENGRID_ITEM_SCROLLTO_IN|' src/bin/view_list2.c
sed -i 's|ecore-input > 1\.2\.0|ecore-input >= 1.2.0|' configure.ac

%build
./autogen.sh --disable-rpath --disable-static --prefix=/usr --enable-browser-upnp
sed -i 's/\$(LIBS)/\$(LIBS) -lm -lecore_input -lX11 -leina -lecore_x -lethumb_client -lgthread-2.0/' src/bin/Makefile
%__make

%install
rm -rf %{buildroot}
%makeinstall
msgfmt %{SOURCE1} -o %{buildroot}%{_datadir}/locale/zh_TW/LC_MESSAGES/enna.mo

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Fri Mar 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> 0.4.1-0.3777.ossii
- Update to r3777

* Mon Jan 03 2011 Wei-Lun Chao <bluebat@member.fsf.org> 0.4.0-3.ossii
- Add zh_TW locale
- Rebuild for OSSII

* Sun Jan 03 2010 Funda Wang <fwang@mandriva.org> 0.4.0-1mdv2010.1
+ Revision: 485875
- fix file list
- New version 0.4.0

* Wed Oct 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.3.0-6mdv2010.0
+ Revision: 455798
- rebuild for new curl SSL backend

* Mon Sep 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-5mdv2010.0
+ Revision: 450716
- fix build dependencies
- rebuild for missing binaries

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 0.3.0-4mdv2010.0
+ Revision: 411299
- renew tarball to build with latest evas

* Thu Jul 09 2009 Funda Wang <fwang@mandriva.org> 0.3.0-3mdv2010.0
+ Revision: 393867
- rebuild

* Wed Jun 10 2009 Funda Wang <fwang@mandriva.org> 0.3.0-2mdv2010.0
+ Revision: 384637
- drop devel files

* Tue Mar 03 2009 Antoine Ginies <aginies@mandriva.com> 0.3.0-1mdv2009.1
+ Revision: 347947
- fix path to libdevel
- add missing files
- add embryo buildrequires
- SVN SNAPSHOT 20090227, release 0.3.0, update buildrequires
- SVN SNAPSHOT 20090227, release 0.3.0, update buildrequires

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - fix no-buildroot-tag

* Fri Dec 21 2007 Adam Williamson <awilliamson@mandriva.org> 0.2.1-1mdv2008.1
+ Revision: 136153
- rebuild to get rid of expat0 dependency
- correct license (e16-like not GPL)
- new license policy
- sane buildrequires
- spec clean
- new version 0.2.1

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

  + Antoine Ginies <aginies@mandriva.com>
    - fix url

* Sat May 26 2007 Antoine Ginies <aginies@mandriva.com> 0.1.0-1mdv2008.0
+ Revision: 31386
- add cvs buildrequires
- first release
- Import enna
