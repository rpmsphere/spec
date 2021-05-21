# export CVSROOT=:pserver:anonymous@cvs.lri.fr:/users/asspro/ihm/metisse-cvs
# DATE=$(date +%Y%m%d)
# cvs login # no password
# cvs co fvwm-insitu
# tar cvjf fvwm-insitu-$DATE.tar.bz2 fvwm-insitu
# cvs co -d metisse-$DATE metisse
# tar cvjf metisse-$DATE.tar.bz2 metisse-$DATE

%define name metisse
%define metisse_version 0.4.1
%define fvwm_cvs rc4
%define release 11
%define distname %{name}-%{metisse_version}
%define fvwm_name fvwm-insitu-%{fvwm_cvs}
%define fvwm_version 2.5.20

%define lib_major 1

%define lib_name %{name}-libs
%define develname %{name}-devel

%define common_description Metisse is an experimental X desktop with some OpenGL capacity.  It consists of a virtual X server called Xmetisse, a special version of FVWM, and a FVWM module FvwmCompositor.

#workaround buggy perl.req
%define _requires_exceptions perl(Gtk)

Summary: X-based window system 
Name: %{name}
Version: %{metisse_version}
Release: %{release}
Source0: %{distname}.tar.bz2
#Source1: %{fvwm_name}.tar.bz2
Source2: Xmetisse.defaults
Source3: metisse-start-fvwm.defaults
Source4: 29metisse

# (fc) 0.4-0.20061130.1mdv force cursor to be handled by FvwmCompositor (workaround ARGB cursor bad rendering)
Patch0: metisse-20061130-fixcursor.patch
# (fc) 0.4-0.20061130.1mdv use blue background as default background
Patch1: metisse-20061130-background.patch
# (fc) 0.4-0.20061201.1mdv enable accessibility by default
Patch2: metisse-20061201-a11y.patch
# (fc) 0.4.0-20061208.1mdv change defaults (Ia Ora theme, only pager, 1 workspace)
Patch3: metisse-defaults.patch
# (gb) 64-bit + other smaller fixes
Patch4: metisse-20070112-64bit-fixes.patch
# (fc) 0.4.0-1.rc4.1mdv fix build with glx enabled
Patch5: metisse-0.4.0-rc4-fixglx.patch
# (fc) 0.4.0-1.rc4.1mdv fix kde tray icon support
Patch6: fvwm-insitu-20070117-fixkdetray.patch
# (fc) 0.4.0-1.rc4.2mdv fix pager mode border color (CVS)
Patch7: metisse-0.4.0-rc4-fixpagerborder.patch
# (fc) 0.4.0-1.rc4.3mdv fix utf8 encoding for titlebar font (Mdv bug #29019) (CVS)
Patch8: metisse-0.4.0-rc4-fixutf8title.patch
# (fc) 0.4.0-1.rc4.5mdv kill Xmetisse when exiting from a session, hide restart when running in a session manager (CVS)
Patch9: metisse-0.4.0-rc4-restart.patch
# (fc) 0.4.0-1.rc4.6mdv add gray and free color theme
Patch10: metisse-0.4.0-rc4-addcolors.patch
# (fc) 0.4.0-1.rc4.7mdv rename locale file 
Patch11: metisse-0.4.0-rc4-textdomain.patch
# (fc) 0.4.0-1.rc4.8mdv fix build with gcc 4.2
Patch12: metisse-0.4.0-rc4-fixgcc42.patch
# (fc) 0.4.0-1.rc4.9mdv don't bind Alt-F1/F2 when running under GNOME/KDE (Mdv bug #29444)
Patch13: metisse-0.4.0-rc4-keybindings.patch
# (aw) from upstream CVS: fix build with gcc 4.3
Patch14: metisse-0.4.0-rc4-gcc43.patch

# Security fixes from stock x11-server - AdamW 2008/08
Patch100: x11-server-1.1.1-rh-CVE-2008-1379.patch
Patch101: x11-server-1.1.1-rh-CVE-2008-2360.patch
Patch102: x11-server-1.1.1-rh-CVE-2008-2361.patch
# Had to add a bit to this one to make it build - AdamW 2008/08
Patch103: metisse-x11-server-1.1.1-rh-CVE-2008-2362.patch

License: MIT
Group: Graphical desktop/Other
Url: http://insitu.lri.fr/metisse/ 
BuildRequires: automake
BuildRequires: mesa-libGLU-devel libjpeg-devel libexif-devel freetype-devel
BuildRequires: nucleo-devel at-spi-devel libXt-devel 
BuildRequires: readline-devel libtermcap-devel libstroke-devel
BuildRequires: libXpm-devel libpng-devel fribidi-devel
BuildRequires: fribidi-devel
# not enabled gnome-libs-devel librplay-devel
BuildRequires: python
Requires: x11-server-xmetisse
Requires: %{name}-fvwm
Requires: gnome-python-bonobo
Requires: compositing-wm-common

%description
%{common_description}

Xmetisse is a mix of Xvnc and XDarwin. It draws nothing on your screen; 
everything is drawn into pixmaps. Similarly to Xvnc, but with a different 
protocol, Xmetisse can send these pixmaps (and other information) to a 
"viewer". FvwmCompositor is such a viewer; it uses OpenGL for rendering 
the X desktop into a window of a "regular" 3D accelerated X server.

%package -n x11-server-xmetisse
Summary: Mix of Xvnc and XDarwin with improved protocol
Group: System/X11
Requires: compositing-server-common
Provides: compositing-server

%description -n x11-server-xmetisse
It draws nothing on your screen, every things is drawn into pixmaps. Similarly
as Xvnc, but with a different protocol, Xmetisse can send these pixmaps (and
others information) to a "viewer". FvwmCompositor is such a viewer, it uses
OpenGL (via nucleo) for rendering the X desktop into a window of a "regular"
3D accelerated X server.
%description
%{common_description}

%package -n	%{lib_name}
Summary:	Library for metisse
Group:		System/Libraries

%description -n	%{lib_name}
%{common_description}

This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{develname}
Summary:	Development tools for programs using %{name}
Group:		Development/C
Requires:	%{lib_name} = %{metisse_version}
Provides:	%{name}-devel = %{metisse_version}-%{release}

%description -n	%{develname}
%{common_description}

This package contains the header files and libraries needed for
developing programs using the %{name} library.

%package fvwm
Summary: Modified version of the FVWM window manager to be used with metisse
Group: Graphical desktop/FVWM based
Version: %{fvwm_version}
Obsoletes: metisse-fvwm-i18n-ar
Obsoletes: metisse-fvwm-i18n-de
Obsoletes: metisse-fvwm-i18n-de
Obsoletes: metisse-fvwm-i18n-sv_SE
Obsoletes: metisse-fvwm-i18n-zh_CN

%description fvwm
A modified version of the FVWM window manager to be used with metisse

%prep
%setup -q -n %{distname} 
#%patch0 -p1 -b .fixcursor
%patch1 -p1 -b .blueblackground
%patch2 -p1 -b .a11y
##%patch3 -p1 -b .defaults
##%patch4 -p1 -b .64bit-fixes
##%patch5 -p1 -b .fixglx
##%patch6 -p1 -b .fixkdetray
##%patch7 -p1 -b .fixpagerborder
##%patch8 -p1 -b .fixutf8title
##%patch9 -p1 -b .restart
##%patch10 -p1 -b .addcolors
%patch11 -p1 -b .textdomain
##%patch12 -p1 -b .fixgcc42
##%patch13 -p1 -b .keybindings
##%patch14 -p1 -b .gcc43

##pushd xserver
##%patch100 -p1
##%patch101 -p1
##%patch102 -p1
##%patch103 -p1
##popd

#needed by patches5 and 10
#autoreconf

%build
%configure  --enable-mmx --with-gtk-prefix=/ --with-imlib-prefix=/ \
 --without-rplay-library --enable-bidi --enable-xinerama \
 --with-fontdir=%_datadir/fonts --enable-freetype \
%ifarch %ix86
 --enable-glx-x86
%endif


%__make

%install
rm -rf %{buildroot}
%makeinstall
install -d %{buildroot}%{_datadir}/compositing-server %{buildroot}%{_datadir}/compositing-wm %{buildroot}%{_sysconfdir}/X11/xinit.d/
install -m644 %{SOURCE2} -t %{buildroot}%{_datadir}/compositing-server/
install -m644 %{SOURCE3} -t %{buildroot}%{_datadir}/compositing-wm/
install -m755 %{SOURCE4} -t %{buildroot}%{_sysconfdir}/X11/xinit.d/

#remove unpackaged files
rm -f %{buildroot}%{_mandir}/man1/FvwmGtkDebug %{buildroot}%{_libdir}/fvwm-insitu/2.5.20/FvwmGtkDebug

for i in `find %{buildroot}%{_datadir}/locale -name '*.mo'` ; do
 mv $i "`dirname $i`/`basename $i .mo`-insitu.mo"
done

##%find_lang fvwm-insitu
##%find_lang FvwmScript-insitu
##%find_lang FvwmTaskBar-insitu

##cat FvwmScript-insitu.lang >> fvwm-insitu.lang
##cat FvwmTaskBar-insitu.lang >> fvwm-insitu.lang

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS NEWS README
%{_bindir}/metisse-*
%{_sysconfdir}/X11/xinit.d/29metisse
%dir %{_datadir}/metisse
%{_datadir}/metisse/*
%{_datadir}/compositing-wm/metisse-start-fvwm.defaults

%files -n x11-server-xmetisse
%{_bindir}/Xmetisse
%{_bindir}/Xwnc
%{_datadir}/compositing-server/Xmetisse.defaults

%files -n %{lib_name}
%{_libdir}/*.so.%{lib_major}*

%files -n %{develname}
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_includedir}/libmetisse
%{_libdir}/pkgconfig/*.pc

%files fvwm
%{_sysconfdir}/X11/dm/Sessions/fvwmi.desktop
%{_sysconfdir}/X11/dm/Sessions/mini-fvwmi.desktop
%{_sysconfdir}/X11/dm/Sessions/opale.desktop
%{_bindir}/FvwmCommand
%{_bindir}/facade-holder
%{_bindir}/fvwm*
%{_bindir}/opale-start-fvwmi
%{_libexecdir}/fvwm-insitu
/usr/lib/python2.*/site-packages/facade_setup.py*
%{_datadir}/fvwm-insitu
%{_mandir}/man1/Fvwm*
%{_mandir}/man1/fvwm*
%{_datadir}/locale/*/LC_MESSAGES/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Fri Jan 16 2009 Wei-Lun Chao <bluebat@member.fsf.org> 0.4.1-1.ossii
- Rebuild for OSSII

* Thu Aug 21 2008 Adam Williamson <awilliamson@mandriva.com> 0.4.0-1.rc4.11mdv2009.0
+ Revision: 274468
- use %%{buildroot} not $RPM_BUILD_ROOT
- add patches from 2008.1 xserver update for four vulnerabilities:
  	+ CVE-2008-1379
  	+ CVE-2008-2360
  	+ CVE-2008-2361
  	+ CVE-2008-2362
  	+ note that CVE-2008-1377 does not apply to metisse
- add gcc43.patch: fix build with gcc 4.3
- new devel policy

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Götz Waschk <waschk@mandriva.org>
    - fix package group

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.0-1.rc4.10mdv2008.1
+ Revision: 170427
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Frederic Crozat <fcrozat@mandriva.com>
    - Fix incorrect obsoletes

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 12 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-1.rc4.9mdv2008.1
+ Revision: 97352
- Patch13: don't bind Alt-F1/F2 when running under GNOME/KDE (Mdv bug #29444)

* Wed Sep 26 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-1.rc4.8mdv2008.0
+ Revision: 93033
- Fix invalid group on fvwm subpackage
- Patch12: fix build with gcc 4.2


* Thu Mar 22 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-1.rc4.7mdv2007.1
+ Revision: 147961
- Add patch10: merge all i18n package into metisse-fvwm package and make sure catalogs don't conflict with upstream fvwm

  + Gwenole Beauchesne <gbeauchesne@mandriva.com>
    - disable generic glx for now

* Tue Mar 06 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-1.rc4.6mdv2007.1
+ Revision: 134043
-Really change when we start metisse specific environment variables
-Patch10: add Ia Ora Free and Ia Ora Gray
-Update patch9 for pager font too

* Mon Mar 05 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-1.rc4.5mdv2007.1
+ Revision: 133352
- Update patch8 with CVS version
- Patch9 (CVS): add some session management, Xmetisse is killed when exiting a managed session

  + Olivier Blin <oblin@mandriva.com>
    - start Xmetisse with -depth 16

* Sun Mar 04 2007 Christiaan Welvaart <spturtle@mandriva.org> 0.4.0-1.rc4.4mdv2007.1
+ Revision: 132049
- drop exclusivearch

* Thu Mar 01 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-1.rc4.3mdv2007.1
+ Revision: 130477
-Patch8: force UTF-8 for titlebar font (Mdv bug #29019)

* Fri Feb 23 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-1.rc4.2mdv2007.1
+ Revision: 124842
-Patch7 (CVS): fix pager border color
-Enable xinerama and bidi
-Fix buildrequires and incorrect dependencies
-Disable libxklavier xmodmap backend until Xmetisse supports XKB
-Start xinit.d script before dbus (needed to propagate env variable to programs started by dbus)

* Wed Feb 07 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-1.rc4.1mdv2007.1
+ Revision: 117279
-Release 0.4.0-rc4
-enable GLX support (but it is only software)
-Patch5: fix GLX detection/build
-Patch6 (CVS): fix KDE tray support

  + Gwenole Beauchesne <gbeauchesne@mandriva.com>
    - 64-bit fixes and enable on x86_64

* Thu Jan 18 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-0.20070117.1mdv2007.1
+ Revision: 110141
-New snapshot for metisse and fvwm-insitu (fix nautilus open location stacking, various modality fixes, fix iconification)

* Mon Jan 15 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-0.20070112.1mdv2007.1
+ Revision: 109127
- New snapshot, should really fix crash when moving windows this time
- New snapshot (20070111)
 - fix crash when moving window with Alt key
 - improve mouse cursor behaviour when using alt-tab

* Mon Jan 08 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-0.20070108.1mdv2007.1
+ Revision: 106071
- New snapshot (improve theme, stability)
- Remove patch4, source 5, 6, merged upstream

* Thu Jan 04 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-0.20061227.4mdv2007.1
+ Revision: 104178
- Update patch4 to fix pager color for Ia Ora Orange

* Wed Jan 03 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-0.20061227.3mdv2007.1
+ Revision: 103797
- Fix patch 4 to correctly install all button images

* Wed Jan 03 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-0.20061227.2mdv2007.1
+ Revision: 103700
- Fix descriptions
- Patch4 / Source5-6 : improve Ia Ora theme : support mouseover and sticky buttons on titlebar

* Tue Jan 02 2007 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-0.20061227.1mdv2007.1
+ Revision: 103422
- New snapshot (20061217), sync with fvwm 2.5.20
- Remove patches 5, 6, 7 (merged upstream)
- Regenerate patch 3

* Tue Dec 19 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-0.20061217.1mdv2007.1
+ Revision: 100215
- New snapshot (fixes some issue with splash windows) 20061217
  Update Ia Ora patch with better colors
  Remove patch4, merged upstream
  Add source4, set a11y correctly for all environments

* Fri Dec 15 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-0.20061214.1mdv2007.1
+ Revision: 97520
- new cvs snapshot (20061214), theme improvement, shader support
  Fix defaults (theme, font size, disable panel by default)
  Reduce shadow size and improve folding colors

  + Olivier Blin <oblin@mandriva.com>
    - add defaults metisse-start-fvwm options for compositing-wm scripts
    - translate --sm-client-id if in fvwmArgs only
    - force geometry
    - rename COMPOSITING_SERVER_LATE_INIT as COMPOSITING_SERVER_SPAWNS_WINDOW (and add some doc)

* Wed Dec 13 2006 Olivier Blin <oblin@mandriva.com> 0.4.0-0.20061208.2mdv2007.1
+ Revision: 96569
- handle --sm-client-id option from gnome-wm (in metisse-start-fvwm)
- add defaults file for compositing-server-common

* Fri Dec 08 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-0.20061208.1mdv2007.1
+ Revision: 93715
- New snapshot (20061208) for Ia Ora theme
- Patch3: use Ia Ora theme by default
- add xpm-devel as BuildRequires
- Fix description

* Tue Dec 05 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-0.20061205.1mdv2007.1
+ Revision: 91312
- New snapshot (20051205)
- Disable patch0, only needed for i810
- Fix font path configure option

* Fri Dec 01 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-0.20061201.1mdv2007.1
+ Revision: 89832
- New snapshot (allow mmx build)
- Always enable a11y by default
- Fix buildrequires, enable stroke

* Thu Nov 30 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4.0-0.20061130.1mdv2007.1
+ Revision: 89335
- Add missing patches
- Update snapshot to 20061130
- Patch0: use software cursor for ARGB mouse cursor for now
- Patch1: use blue background by default
- Add dependency on gnome-python-bonobo (for facade)
- Update CVS snapshot to 20061129
- drop all patches, merged upstream
- rename packages to follow new upstream naming
- Patch1 : fix parallel build
- Patch1 : fix parallel build
- Add more buildrequires
- Fix default font path

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - importing metisse to the repository
