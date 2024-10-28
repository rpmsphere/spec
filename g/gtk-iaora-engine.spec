%define _name ia_ora-gnome

Summary:        GTK2 engine for Ia Ora theme
Name:           gtk-iaora-engine
Version:        1.0.25
Release:        3.1
License:        GPL
Group:          System/Libraries
URL:            https://www.mandrivalinux.com/
BuildRequires:  libpng-devel
BuildRequires:  gtk2-devel
Source0:        %{_name}-%{version}.tar.bz2
Source1:        abstrakciya-siniy-fon-linii-hq.jpg
Patch0:         ia_ora-gnome-1.0.25-automake-1.13.patch

%description
GTK2 engine for Ia Ora theme.

%package -n iaora-gnome-theme
Summary: Ia Ora Mandriva GNOME theme
Group: Graphical desktop/GNOME
BuildArch: noarch
Requires: gnome-themes-extras
Requires: gtk-iaora-engine

%description -n iaora-gnome-theme
Mandriva Ia Ora GNOME theme.

%prep
%setup -q -n %{_name}-%{version}
%patch 0 -p1

%build
./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
cp %{SOURCE1} "$RPM_BUILD_ROOT%{_datadir}/themes/Ia Ora Arctic"
sed -i 's|IconTheme=gnome|IconTheme=Gion|' $RPM_BUILD_ROOT%{_datadir}/themes/*/index.theme
sed -i '$a BackgroundImage=/usr/share/themes/Ia Ora Arctic/abstrakciya-siniy-fon-linii-hq.jpg' $RPM_BUILD_ROOT%{_datadir}/themes/*/index.theme

%files -n iaora-gnome-theme
%{_datadir}/themes/*

%files
%doc README
%{_libdir}/gtk-2.0/*/engines/*.so
%exclude %{_libdir}/gtk-2.0/*/engines/*.la

%changelog
* Mon Jul 18 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.25
- Rebuilt for Fedora
* Fri Apr 30 2010 Frederic Crozat <fcrozat@mandriva.com> 1.0.24-1mdv2010.1
+ Revision: 541225
- Release 1.0.24 :
  - enable auto-memonics by default. Create .gtkrc-2.0 with "gtk-auto-mnemonics = 0" in your home to disable it, if you don't like it
* Wed Apr 14 2010 Frederic Crozat <fcrozat@mandriva.com> 1.0.23-1mdv2010.1
+ Revision: 534921
- Release 1.0.23
 - improve tooltips
 - allow window grab from menubar
 - remove some deprecrated functions call
- Release 1.0.23
 - improve tooltips
 - allow window grab from menubar
 - remove some deprecrated functions call
* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.22-3mdv2010.1
+ Revision: 522890
- rebuilt for 2010.1
* Fri Oct 23 2009 Frederic Crozat <fcrozat@mandriva.com> 1.0.22-2mdv2010.0
+ Revision: 459106
- Force rebuild
- Release 1.0.22 :
 - fix check color for Ia Ora Steel
* Fri Oct 23 2009 Frederic Crozat <fcrozat@mandriva.com> 1.0.21-1mdv2010.0
+ Revision: 459062
- Release 1.0.21 :
 - new themes Ia Ora Steel / Ia Ora Night
* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.20-3mdv2010.0
+ Revision: 425195
- rebuild
* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.20-2mdv2009.1
+ Revision: 351242
- rebuild
* Tue Aug 05 2008 Frederic Crozat <fcrozat@mandriva.com> 1.0.20-1mdv2009.0
+ Revision: 264013
- Release 1.0.20 :
 - Fix EOG collection scrollbar rendering
 - Fix entry field focus drawing for Firefox3 (Mdv bug #39915)
* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.19-2mdv2009.0
+ Revision: 221391
- rebuild
* Fri Mar 28 2008 Frederic Crozat <fcrozat@mandriva.com> 1.0.19-1mdv2008.1
+ Revision: 190938
- Release 1.0.19 :
 - Fix buttons in Cheese not being rendered properly
 - Fix Metacity decorations being misrendered when using Compositing mode
* Wed Mar 26 2008 Emmanuel Andry <eandry@mandriva.org> 1.0.18-2mdv2008.1
+ Revision: 190544
- Fix lib group
* Thu Feb 28 2008 Frederic Crozat <fcrozat@mandriva.com> 1.0.18-1mdv2008.1
+ Revision: 176485
- Release 1.0.18 :
- Ia Ora Free is now called Ia Ora Arctic
- Ia Ora One is now called Ia Ora Smooth
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill file wrongly added by saispo in r117685 on 2007-12-12
  + Jérôme Soyer <saispo@mandriva.org>
    - New release 1.0.1
* Fri Nov 30 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0.17-1mdv2008.1
+ Revision: 114048
- Release 1.0.17
 - Fix crash in gimp when using Small theme (Mdv bug #31354)
* Wed Sep 05 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0.16-1mdv2008.0
+ Revision: 80268
- Release 1.0.16 :
 - allow to change all colors with gnome appearance dialog
* Tue Sep 04 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0.15-1mdv2008.0
+ Revision: 79422
- Release 1.0.15 :
 - new Ia Ora One theme
* Fri Aug 31 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0.14-1mdv2008.0
+ Revision: 77039
- Release 1.0.14 :
 - Fix clipping error, causing strange scrollbar in FF / TB (Mdv bug #26313)
* Wed Jul 11 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0.13-1mdv2008.0
+ Revision: 51355
- Release 1.0.13 : add theming support for GtkTooltip
* Fri Jun 01 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0.12-1mdv2008.0
+ Revision: 34225
- Release 1.0.12 :
 * improve progress bar rendering, specially inversed and vertical ones
* Tue Mar 20 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0.11-1mdv2007.1
+ Revision: 147056
- Release 1.0.11 :
- do not center title which are larger than window width, left align them
* Tue Mar 13 2007 Frederic Crozat <fcrozat@mandriva.com> 1.0.10-1mdv2007.1
+ Revision: 143170
-Release 1.0.10 :
 - Fix toggle button for VMWare and in normal conditions too (TheWidgetFactory)
 - Make Ia Ora gtk themes color scheme compliant
 - Fix shaded mode in Ia Ora Orange metacity theme
 - Center title on Ia Ora metacity theme
 - Fix warning when starting gnome-panel
  + Jérôme Soyer <saispo@mandriva.org>
    - Import ia_ora-gnome
* Sat Oct 07 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.9-1mdv2007.0
- Release 1.0.9 :
 - Right-to-Left languages are now supported and shadows are inversed, 
   following reading direction
 - Fix buttons missing borders in VMWare
 - Fix columns drawing in evolution messages list
 - Fix buttons drawing in gnomine (Mdv bug #26293)
 - Code cleanup
* Wed Sep 13 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.8-1mdv2007.0
- Release 1.0.8 :
 - fix text color on combobox popup (in f-spot for instance)
* Tue Sep 05 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.7-1mdv2007.0
- Release 1.0.7 :
 - add color focus for text entry
 - remove workaround for GNOME bug #346751, GTK+ is now fixed
* Sat Sep 02 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.6-1mdv2007.0
- Release 1.0.6 :
  - tune colors used in black_check mode
  - fix text positioning for radio and checkbutton
* Fri Sep 01 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.5-1mdv2007.0
- Release 1.0.5 :
 - increase metacity window border for easier grab and use two colors for it
 - change text color on unfocused and focused window title
 - clean gtk2 engine code
 - workaround GNOME bug #346751 by not using symbolic colors for properties
 - improve sliders : enhanced mouseover, remove gradient, fix center
 - fix progressbar background and readability
 - draw radiobutton/checkbutton in black/gray for  free/gray/orange themes
   (use black_check as engine parameter to restore previous behaviour)
 - fix spinbutton size and arrow position in it
 - fix colors used for point in handlers
 - fix various colors in evolution
 - fix highlight text for open menu in combobox
* Wed Aug 30 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.4-1mdv2007.0
- Release 1.0.4 :
 - Replace cross with check, can be overwritten by setting use_cross=TRUE
   in gtkrc engine parameter
 - rename Ia Ora Yellow into Ia Ora Orange
* Sat Aug 19 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.3-1mdv2007.0
- Release 1.0.3 :
 - code / palette / gtkrc cleanup
 - fix crash when changing enable_gradient
 - fix diskdrake colored buttons (Mdv bug #24377)
 - fix arrow size and position
* Fri Aug 18 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.2-1mdv2007.0
- Release 1.0.2 :
 - fix crash (Mdv bug #24292)
 - don't use gtk theme colors in metacity themes
 - don't export unneeded symbols and don't accept undefined symbols either
* Fri Aug 11 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.1-1mdv2007.0
- Split package to allow install in both 32 and 64bits
* Thu Aug 10 2006 Frederic Crozat <fcrozat@mandriva.com> 1.0.0-2mdv2007.0
- Initial package
