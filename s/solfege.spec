%undefine _debugsource_packages

Name:           solfege
Summary:        An ear-training program
Version:        3.23.4
Release:        5
License:        GPLv3+
Group:          Sound/Utilities
URL:            https://www.solfege.org/
Source0:        https://alpha.gnu.org/gnu/solfege/%{name}-%{version}.tar.gz
Source1:        %{name}48.png
Source2:        %{name}32.png
Source3:        %{name}16.png
Patch1:         solfege-3.20.0-link.patch
Patch2:         solfege-3.23.4-usrmove.patch
Patch3:         solfege-3.23.4-py3-webbrowser.patch
Patch4:         solfege-3.23.4-texinfo-non-utf8-input-fix.patch
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gnome-doc-utils
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base
BuildRequires:  swig
BuildRequires:  texinfo
BuildRequires:  txt2man
BuildRequires:  libxslt-devel
BuildRequires:  python-rpm-macros
Requires:       python3-gobject-base
Requires:       TiMidity++

%description
GNU Solfege is an ear-training program. These are the exercises written so far:
    * Recognise melodic and harmonic intervals
    * Compare interval sizes
    * Sing the intervals the computer asks for
    * Identify chords
    * Sing chords
    * Scales
    * Dictation
    * Remembering rhythmic patterns

%prep
%setup -q
%autopatch -p1

%build
FILE=$(ls %_datadir/sgml/docbook/xsl-stylesheets-1.*/html/chunk.xsl)
%configure --enable-docbook-stylesheet=$FILE --disable-oss-sound
%make_build

%install
%make_install
#chmod 755 %{buildroot}%{_libdir}/%{name}/*.so

# menu
desktop-file-install --vendor="" \
  --set-comment='Music education software' \
  --remove-category="Application" \
  --add-category="GTK" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# icons
install -Dpm644 %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -Dpm644 %SOURCE2 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -Dpm644 %SOURCE3 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

# python shebangs
python3 /usr/lib/rpm/redhat/pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_bindir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc README AUTHORS FAQ
%license COPYING
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/sol*
%{_mandir}/man1/*
#%{_libdir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sun Jan 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 3.23.4
- Rebuilt for Fedora
* Wed Mar 24 2021 daviddavid <daviddavid> 3.23.4-5.mga9
+ Revision: 1708558
- rebuild for python 3.9
* Tue Dec 15 2020 tv <tv> 3.23.4-4.mga8
+ Revision: 1657509
- BR python3-gobject-base
* Sun Feb 16 2020 daviddavid <daviddavid> 3.23.4-2.mga8
+ Revision: 1535985
- add patch to fix build with texinfo 6.7
+ umeabot <umeabot>
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%configure2_5x
* Sun Oct 13 2019 wally <wally> 3.23.4-1.mga8
+ Revision: 1452696
- new version 3.23.4
- switch to gtk3 and python3
* Sat Mar 09 2019 wally <wally> 3.22.2-10.mga7
+ Revision: 1373333
- drop unneeded requires
* Sun Sep 23 2018 umeabot <umeabot> 3.22.2-9.mga7
+ Revision: 1301102
- Mageia 7 Mass Rebuild
+ kekepower <kekepower>
- Update macros
* Wed Feb 17 2016 umeabot <umeabot> 3.22.2-8.mga6
+ Revision: 962868
- Mageia 6 Mass Rebuild
* Thu Oct 22 2015 danf <danf> 3.22.2-7.mga6
+ Revision: 894046
- Fixed permissions of library so debuginfo is extracted
* Wed Jan 07 2015 alexl <alexl> 3.22.2-6.mga5
+ Revision: 809188
- added Comment in desktop file
* Mon Nov 17 2014 wally <wally> 3.22.2-5.mga5
+ Revision: 797710
- add patch to fix possible startup issues after usrmove (mga#14574)
* Wed Oct 15 2014 umeabot <umeabot> 3.22.2-4.mga5
+ Revision: 742958
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 3.22.2-3.mga5
+ Revision: 689239
- Mageia 5 Mass Rebuild
* Mon Oct 21 2013 umeabot <umeabot> 3.22.2-2.mga4
+ Revision: 540528
- Mageia 4 Mass Rebuild
* Tue Oct 08 2013 bersuit <bersuit> 3.22.2-1.mga4
+ Revision: 493786
- Update to new upstream version 3.22.2
* Tue Sep 24 2013 bersuit <bersuit> 3.22.1-1.mga4
+ Revision: 485433
- Update to new upstream version 3.22.1
* Fri Jun 21 2013 bersuit <bersuit> 3.22.0-1.mga4
+ Revision: 445573
- Update to new version 3.22
* Mon Jan 14 2013 umeabot <umeabot> 3.21.2-3.mga3
+ Revision: 382294
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sat Dec 29 2012 barjac <barjac> 3.21.2-2.mga3
+ Revision: 336210
- changed group in line with new policy
* Wed Jun 06 2012 juancho <juancho> 3.21.2-1.mga3
+ Revision: 256073
- Updated to 3.21.2
* Tue Apr 03 2012 juancho <juancho> 3.20.4-1.mga2
+ Revision: 228018
- Removed unnecesary BR txt2man
+ gregorybravas <gregorybravas>
- initial package
- imported package solfege
* Mon Oct 24 2011 Joaquín Moreno <joaquinmandriva@gmail.com> 3.20.4-1.bdk.mga
- new version 3.20.4
* Mon Sep 26 2011 Joaquín Moreno <joaquinmandriva@gmail.com> 3.20.3-1.bdk.mga
- new version 3.20.3
* Tue Sep 20 2011 Joaquín Moreno <joaquinmandriva@gmail.com> 3.20.2-1.bdk.mga
- new version 3.20.2
* Wed Aug 16 2011 Joaquín Moreno <joaquinmandriva@gmail.com> 3.20.1-1.bdk.mga
- Packaged to Mageia (Blogdrake Repository)
* Sat Aug 13 2011 Funda Wang <fwang@mandriva.org> 3.20.1-1mdv2012.0
+ Revision: 694380
- new version 3.20.1
* Sun Jun 19 2011 Funda Wang <fwang@mandriva.org> 3.20.0-1
+ Revision: 686004
- rediff patch
- update to new version 3.20.0
* Wed Mar 16 2011 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 3.19.5-1
+ Revision: 645427
- update to new version 3.19.5
* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 3.18.6-2mdv2011.0
+ Revision: 590081
- rebuild for python 2.7
* Mon Oct 25 2010 Funda Wang <fwang@mandriva.org> 3.18.6-1mdv2011.0
+ Revision: 589247
- new version 3.18.6
* Mon Oct 25 2010 Funda Wang <fwang@mandriva.org> 3.18.5-1mdv2011.0
+ Revision: 589224
- update to new version 3.18.5
- fix desktop file categories
* Thu Oct 14 2010 Funda Wang <fwang@mandriva.org> 3.18.4-1mdv2011.0
+ Revision: 585525
- New version 3.18.4
* Sun Aug 29 2010 Funda Wang <fwang@mandriva.org> 3.16.4-1mdv2011.0
+ Revision: 574073
- update to new version 3.16.4
* Fri Apr 23 2010 Funda Wang <fwang@mandriva.org> 3.16.1-1mdv2010.1
+ Revision: 538052
- new version 3.16.1
* Thu Apr 01 2010 Funda Wang <fwang@mandriva.org> 3.16.0-1mdv2010.1
+ Revision: 530612
- update to new version 3.16.0
* Wed Mar 10 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.15.8-2mdv2010.1
+ Revision: 517487
- Drop patch applied upstream (thanks misc)
* Wed Mar 10 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.15.8-1mdv2010.1
+ Revision: 517275
- update to 3.15.8
- stop use patch1 because it breaks build but keep it.
* Wed Feb 10 2010 Frederik Himpe <fhimpe@mandriva.org> 3.14.11-1mdv2010.1
+ Revision: 503968
- update to new version 3.14.11
* Sun Dec 27 2009 Funda Wang <fwang@mandriva.org> 3.14.10-1mdv2010.1
+ Revision: 482670
- new version 3.14.10
* Wed Nov 11 2009 Funda Wang <fwang@mandriva.org> 3.14.9-1mdv2010.1
+ Revision: 464573
- new version 3.14.9
* Wed Sep 30 2009 Frederik Himpe <fhimpe@mandriva.org> 3.14.8-1mdv2010.0
+ Revision: 451841
- update to new version 3.14.8
* Wed Aug 19 2009 Frederik Himpe <fhimpe@mandriva.org> 3.14.7-1mdv2010.0
+ Revision: 417892
- update to new version 3.14.7
* Sat Aug 08 2009 Frederik Himpe <fhimpe@mandriva.org> 3.14.6-1mdv2010.0
+ Revision: 411513
- update to new version 3.14.6
* Mon Jun 29 2009 Funda Wang <fwang@mandriva.org> 3.14.5-1mdv2010.0
+ Revision: 390499
- New version 3.14.5
* Tue Jun 09 2009 Funda Wang <fwang@mandriva.org> 3.14.4-1mdv2010.0
+ Revision: 384464
- New version 3.14.4
* Tue Jun 09 2009 Funda Wang <fwang@mandriva.org> 3.14.3-2mdv2010.0
+ Revision: 384428
- use timidity as midi player by default, as most sound cards do not contain hard wavetable
* Tue Jun 02 2009 Funda Wang <fwang@mandriva.org> 3.14.3-1mdv2010.0
+ Revision: 382084
- New version 3.14.3
* Mon Jan 19 2009 Funda Wang <fwang@mandriva.org> 3.12.1-1mdv2009.1
+ Revision: 331082
- new version 3.12.1
* Mon Dec 01 2008 Funda Wang <fwang@mandriva.org> 3.12.0-1mdv2009.1
+ Revision: 308738
- fix BR and license
- New version 3.12.0
* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 3.10.4-3mdv2009.0
+ Revision: 269341
- rebuild early 2009.0 package (before pixel changes)
- swig-devel doesn't exist
  + Austin Acton <austin@mandriva.org>
    - requires TiMidity++ (Maxim Heijndijk)
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Wed Jun 11 2008 Austin Acton <austin@mandriva.org> 3.10.4-1mdv2009.0
+ Revision: 217844
- new version
  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot
* Fri Dec 14 2007 Thierry Vignaud <tv@mandriva.org> 3.6.5-2mdv2008.1
+ Revision: 119925
- patch 0: fix desktop entry so that desktop-file-install doesn't delete it
- rebuild b/c of missing subpackage on ia32
* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 3.6.5-1mdv2008.0
+ Revision: 16598
- 3.6.5
- BuildRequires libxslt-proc
* Tue Sep 12 2006 Emmanuel Andry <eandry@mandriva.org> 3.0.6-3mdv2007.0
- add buildrequires desktop-file-utils
* Tue Sep 12 2006 Emmanuel Andry <eandry@mandriva.org> 3.0.6-2mdv2007.0
- fix requires
- xdg menu
* Wed May 03 2006 Emmanuel Andry <eandry@free.fr> 3.0.6-1mdk
- 3.0.6
- removed pygtk-devel as it now use pygtk2.0-devel
- removed pygnome-devel because not available anymore
* Wed Oct 19 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.9.1-2mdk
- Fix BuildRequires
- %%mkrel
* Thu Jun 16 2005 Lenny Cartier <lenny@mandriva.com> 2.9.1-1mdk
- 2.9.1
* Mon Sep 13 2004 Austin Acton <austin@mandriva.org> 2.4.0-1mdk
- 2.4.0
- requires gnome-python-gnomevfs (Simon Oplatka Wenger)
- configure 2.5
- fudge date since nobody wants to fix it (s/b Thu May 26 2005)
* Mon Sep 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.0.6-1mdk
- 2.0.6
* Thu Jun 10 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.0.5-1mdk
- 2.0.5
* Sun May 16 2004 Michael Scherer <misc@mandrake.org> 2.0.4-2mdk 
- add Requires
- xsl stylesheet autodetection
* Sun Feb 29 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.0.4-1mdk
- 2.0.4
- Own dir
