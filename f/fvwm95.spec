%undefine _debugsource_packages

Name: fvwm95
Version: 2.0.43f
Release: 13.1
Summary: Window Manager with Windows '95 look
Source: http://sourceforge.net/projects/fvwm95/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch: fvwm95-2.0.43b-redhat.patch
License: GPL
Group: X11/Window Managers
Requires: fvwm95-icons
BuildRequires: libX11-devel, libXt-devel, libXpm-devel, libXext-devel, libXmu-devel

%description
fvwm95 is a version of the popular "Feeble Virtual Window Manager" that
emulates the look and feel of Windows '95. Now you can have the look and
feel of the the Windows world with the power and convenience of Linux. 
NOTE: this is a version based on the original fvwm95-2.0.43a (patched) 
with enhanced taskbar, new modules and new pixmaps/mini-icons

%package icons
Summary: Pixmaps and mini-icons for fvwm95
Group: X11/Window Managers
BuildArch: noarch

%description icons
This package contains pixmaps and mini-icons for fvwm95

%prep
%setup -q
%patch -p 1
sed -i 's/-shared/-shared -fPIC/' modules/FvwmTaskBar/Makefile*
sed -i 's/(void \*)//' modules/FvwmTaskBar/BatStatModule.c
rm modules/FvwmConsole/FvwmConsoleC modules/FvwmConsole/*.o
sed -i 's|getline|mygetline|' modules/FvwmConsole/getline.c modules/FvwmConsole/FvwmConsoleC.c

%build
export CC="gcc -Wl,--allow-multiple-definition"
./configure --prefix=/usr
make

%install
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1/
install -d $RPM_BUILD_ROOT%{_libdir}/X11/mini-icons
install -d $RPM_BUILD_ROOT%{_libdir}/X11/fvwm95
install -d $RPM_BUILD_ROOT%{_libdir}/X11/fvwm95/scripts
install -d $RPM_BUILD_ROOT%{_libdir}/X11/fvwm95/plugins
install -d $RPM_BUILD_ROOT%{_libdir}/X11/pixmaps

install -m 755 fvwm/fvwm95 \
                        $RPM_BUILD_ROOT/%{_bindir}
install -m 644 fvwm/fvwm95.man \
                               $RPM_BUILD_ROOT%{_mandir}/man1/fvwm95.1x
install -m 755 xpmroot/xpmroot \
                        $RPM_BUILD_ROOT%{_bindir}
install -m 644 xpmroot/xpmroot.man \
                               $RPM_BUILD_ROOT%{_mandir}/man1/xpmroot.1x

cd modules
#FvwmBacker FvwmIconMan
for module in FvwmAudio FvwmAuto FvwmBanner FvwmButtons FvwmCpp \
	FvwmDebug FvwmForm FvwmIconBox FvwmIdent FvwmM4 \
	FvwmPager FvwmSave FvwmSaveDesk FvwmScript FvwmScroll FvwmTalk \
        FvwmWinList FvwmWharf FvwmTaskBar; do \
	install -m 755 $module/$module \
		$RPM_BUILD_ROOT%{_libdir}/X11/fvwm95; \
	install -c -m 644 $module/$module.man \
		$RPM_BUILD_ROOT%{_mandir}/man1/$module.1x; \
	done
install -m 755 FvwmConsole/FvwmConsole \
		$RPM_BUILD_ROOT%{_libdir}/X11/fvwm95; 

install -m 755 FvwmConsole/FvwmConsoleC \
		$RPM_BUILD_ROOT%{_libdir}/X11/fvwm95; 


for script in BellSetup Buttons Date DeskSetup FileBrowser KeyboardSetup \
	PointerSetup Quit ScreenDump ScreenSetup ; do \
	install -c -m 644 FvwmScript/Scripts/$script \
		$RPM_BUILD_ROOT%{_libdir}/X11/fvwm95/scripts; \
	done


install -m 755 FvwmTaskBar/*.so \
                               $RPM_BUILD_ROOT%{_libdir}/X11/fvwm95/plugins
cd ..

install sample.fvwmrc/system.fvwm95rc \
                               $RPM_BUILD_ROOT%{_libdir}/X11/fvwm95/system.fvwm95rc

install -m 0444 pixmaps/*.xpm \
                                $RPM_BUILD_ROOT%{_libdir}/X11/pixmaps/
install -m 0444 mini-icons/*.xpm \
                                $RPM_BUILD_ROOT%{_libdir}/X11/mini-icons/

install -m 755 utils/fvwmrc_convert \
                               $RPM_BUILD_ROOT/usr/bin
install -m 755 utils/quantize_pixmaps \
                               $RPM_BUILD_ROOT/usr/bin
ln -sf %{_libdir}/X11/fvwm95/system.fvwm95rc \
       $RPM_BUILD_ROOT%{_libdir}/X11/fvwm95/.fvwm95rc

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%doc README fvwm95-2.xx.lsm GPL Changelog FvwmTaskBar-plugins.patch.README
%doc pixmaps/README.mini 
%doc docs/modules.tex docs/m4_hacks docs/error_codes docs/color_combos
%doc docs/*.html docs/html 
%{_bindir}/*
%{_libdir}/X11/fvwm95
%{_mandir}/man1/*

%files icons
%{_libdir}/X11/mini-icons/
%{_libdir}/X11/pixmaps/

%changelog
* Sun Oct 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.43f
- Rebuilt for Fedora
* Mon Feb 16 1998 Manu Rouat <rouat@dsys.ceng.cea.fr>
  - at last version 2.043b!! See Readme.
* Thu Aug 07 1997 Corey Minyard <minyard@acm.org>
  - Added installation of man pages for fvwm95 and xpmroot.
  - Added the standard patch for empty name death and moved the redhat
    patch to *-rh.patch.
  - Removed gzipping of man pages.
  - For some reason stripping the fvwm95 executable caused it to not
    use pixmaps.  Removed stripping of the executable.
* Wed Mar 12 1997 Tomasz Kloczko <kloczek@rudy.mif.pg.gda.pl>
  - added xpmroot (forgotten on rewriting spec) and script quantize_pixmaps,
  - removed instaling FvwmConsole module (compiled with -DNO_CONSOLE),
  - man pages instaled with 1x extension,
  - new version fvwm95-2.0.43a:
  From Release notes:
   - Bug corrections: m4-preprocessing, taskbar's MailBox command problem,
     etc...
   - New taskbar option for showing only the buttons corresponding to the
     windows in the active desktop.
   - Support for side pixmaps in menus. Now you can make your start menu
     look like this
   - The TitleIcon style option now has MiniIcon as a synonym for
     compatibility with (future) fvwm2 similar directive.
   - Configuration changes: the menu colors are now specified by a
     MenuColors directive.
   - Name changes: the executable file is now fvwm95 instead of fvwm95-2.
     The user's config file is .fvwm95rc instead of .fvwm2rc95, the
     system-wide config file is system.fvwm95rc.
   - Slow-sliding taskbar when the AutoHide option is enabled. 
   - Corrected a bug in fvwm code that caused the window manager to die when
     using the taskbar option "*FvwmTaskBarAction Click3 PopUp Window-Ops2".
     Now the window-ops popup can be used correctly when right-clicking on a
     taskbar button.
   - Some more new mini-icons. 
* Mon Mar 10 1997 Tomasz Kloczko <kloczek@rudy.mif.pg.gda.pl>
  - all man pages are gziped,
  - spec file rewrited for using BuildRoot,
  - fixed default config file (removed fvwm95.0.41f-FSSTND.patch, added
    fvwm95-2.0.42-fvwm2rc95.patch),
  - added lacking icons and bitmaps.
