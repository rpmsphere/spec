Summary:	X Printing Panel
Name:		xpp
Version:	1.5
Release:	23.1
License:	GPL
Group:		Publishing
Source0:	http://cups.sourceforge.net/xpp/%{name}-%{version}cvs.tar.gz
Patch0:		01_old_debian_changes.patch
Patch1:		02_build_system.patch
Patch2:		xpp-new-fltk.patch
URL:		http://cups.sourceforge.net/xpp/
BuildRequires:	cups-devel
BuildRequires:	fltk-devel
BuildRequires:	fltk-fluid
BuildRequires:	libstdc++-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:  libXext-devel

%description
The X Printing Panel (XPP) is a completely free tool for easy choosing of
the desired printer out of a list of all available printers and
for setting printer options by an easy-to-use graphical user interface.
One simply calls the program (xpp) instead of the usual utilities
(lpr or lp) at the command line or out of applications.

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoreconf -fi
%configure
make FLUID=fluid

%install
%make_install

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=X Printing Panel
Comment=Frontend for easy printing with CUPS
Exec=%{name}
Icon=printer
Terminal=false
Type=Application
StartupNotify=true
Categories=Settings;HardwareSettings;
EOF

# Use update-alternatives to make printing with XPP also possible with
# the "lpr" command

( cd $RPM_BUILD_ROOT%{_bindir}
  ln -s xpp lpr-xpp
)

%post
# Set up update-alternatives entry
%{_sbindir}/update-alternatives --install %{_bindir}/lpr lpr %{_bindir}/lpr-xpp 8

%preun
if [ "$1" = 0 ]; then
  # Remove update-alternatives entry
  %{_sbindir}/update-alternatives --remove lpr /usr/bin/lpr-xpp
fi

%files
%doc README LICENSE ChangeLog
%_bindir/*
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuild for Fedora

* Wed Oct 15 2014 umeabot <umeabot> 1.5-16.mga5
+ Revision: 740375
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 1.5-15.mga5
+ Revision: 690753
- Mageia 5 Mass Rebuild

* Sun Nov 03 2013 fwang <fwang> 1.5-14.mga4
+ Revision: 549261
- call some old patches
- sync with debian packages
- use autoconf
- fix build with recent cups

  + umeabot <umeabot>
    - Mageia 4 Mass Rebuild

* Mon Jan 14 2013 umeabot <umeabot> 1.5-13.mga3
+ Revision: 387326
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Fri Dec 21 2012 cjw <cjw> 1.5-12.mga3
+ Revision: 333688
- patch 5 and 6: fix build with current cups and glibc header files

* Wed Aug 03 2011 fwang <fwang> 1.5-11.mga2
+ Revision: 131585
- build with fltk 1.3
- rebuild for new fltk

  + dmorgan <dmorgan>
    - Rebuild against new fltk

* Mon Jan 17 2011 dmorgan <dmorgan> 1.5-9.mga1
+ Revision: 21443
- Add missing %%post
- Add libxext-devel as buildrequire
- Remove mdv macros
- imported package xpp

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5-9mdv2011.0
+ Revision: 608230
- rebuild

* Sat Jan 09 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1.5-8mdv2010.1
+ Revision: 487928
- rebuild with new fltk

* Mon Sep 28 2009 Olivier Blin <oblin@mandriva.com> 1.5-7mdv2010.0
+ Revision: 450573
- force const char cast to fix build
- fix format error (from Arnaud Patard)

* Sun Dec 14 2008 Funda Wang <fwang@mandriva.org> 1.5-6mdv2009.1
+ Revision: 314160
- fix build with latest fltk
- rediff patch1

  + Thierry Vignaud <tv@mandriva.org>
    - fix BR for x86_64
    - rebuild for new fltk

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.5-5mdv2009.0
+ Revision: 218427
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Feb 25 2008 Marcelo Ricardo Leitner <mrl@mandriva.com> 1.5-5mdv2008.1
+ Revision: 174828
- Added patch bug27027. Closes: #27027
- Disabled parallel build as it's broken.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill explicit icon extension
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Mon Jun 18 2007 Adam Williamson <awilliamson@mandriva.org> 1.5-4mdv2008.0
+ Revision: 40706
- patch0 (fix build); XDG menu; clean buildrequires; drop unused icon; rebuild for new era

  + Marcelo Ricardo Leitner <mrl@mandriva.com>
    - Import xpp

* Mon Jan 23 2006 Till Kamppeter <till@mandriva.com> 1.5-3mdk
- Rebuilt for CUPS 1.2.
- Introduced %%mkrel.

* Sun Aug 28 2005 Till Kamppeter <till@mandriva.com> 1.5-2mdk
- CVS Update: Fixed many causes of segfaults. Fixed multiple password
  rquests on password-protected print queues.

* Tue Dec  7 2004 Till Kamppeter <till@mandrakesoft.com> 1.5-1mdk
- Updated to version 1.5.

* Mon Dec  6 2004 Till Kamppeter <till@mandrakesoft.com> 1.1-15mdk
- CVS Update: Support for numerical, string, and password options
  in Foomatic 3.x and for the fax number option of fax4CUPS.

* Sat Dec  4 2004 Till Kamppeter <till@mandrakesoft.com> 1.1-14mdk
- CVS Update: Job control options, more updates of CUPS-specific
  options, preview of images (JPG, PNG) in file dialog.

* Tue Nov  9 2004 Till Kamppeter <till@mandrakesoft.com> 1.1-13mdk
- CVS Update: Integrated patches upstream, updated CUPS-specific
  options.

* Mon Jun 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1-12mdk
- Rebuild

* Fri Feb 27 2004 Till Kamppeter <till@mandrakesoft.com> 1.1-11mdk
- Added patch to make window horizontally resizable and to allow
  choosing custom paper sizes (thanks to Egbert Eich, eich at xfree86 
  dot org).

* Sun Jul 27 2003 Till Kamppeter <till@mandrakesoft.com> 1.1-10mdk
- Rebuilt with FLTK 1.1.4rc1.

* Fri Jul 25 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.1-9mdk
- rebuild
- rm -rf $RPM_BUILD_ROOT at the beginning of %%install

* Mon Feb  3 2003 Till Kamppeter <till@mandrakesoft.com> 1.1-8mdk
- Rebuilt for new glibc.
- Fixed bug which broke compilation with current FLTK.

* Wed Oct  9 2002 Till Kamppeter <till@mandrakesoft.com> 1.1-7mdk
- CVS Update: Temporary files were not deleted, fixed.

* Thu Aug 29 2002 David BAUDENS <baudens@mandrakesoft.com> 1.1-6mdk
- Fix menu entry (category & icon)

* Wed Aug 14 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.1-5mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Fri Jul 26 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.1-4mdk
- Rebuild with gcc3.2
- Menu dir is %%_menudir

* Tue May 28 2002 Till Kamppeter <till@mandrakesoft.com> 1.1-3mdk
- CVS Update: Updated source code to compile with gcc 3.1.
- Rebuilt for new FLTK, libstdc++, gcc 3.1.

* Wed Jan 16 2002 Till Kamppeter <till@mandrakesoft.com> 1.1-2mdk
- Corrected date in main window.

* Wed Jan  9 2002 Till Kamppeter <till@mandrakesoft.com> 1.1-1mdk
- Version 1.1: Works correctly with PPD-O-Matic PPD files, supports the
  "natural-scaling" image size option, no function overloading for password
  dialog.

* Tue Jul 18 2001 Till Kamppeter <till@mandrakesoft.com> 1.0-6mdk
- Update alternatives stuff as with LPD/CUPS, so that one can also print 
  via XPP with the "lpr" command

* Tue Jul 17 2001 Till Kamppeter <till@mandrakesoft.com> 1.0-5mdk
- Rebuilt against the new CUPS library 1.1.9 due to an incompatibility.

* Mon Mar  4 2001 Till Kamppeter <till@mandrakesoft.com> 1.0-4mdk
- CVS Update: Made XPP able to read out the numerical options of the new 
  XML-Foomatic which will appear in the near future.

* Sun Jan 28 2001 Till Kamppeter <till@mandrakesoft.com> 1.0-3mdk
- Version 1.0 (final)
- Let jobs from standard input get the name "STDIN" instead of "(stdin)",
  because the parantheses caused problems with Samba or Windows servers.
- Let the first printer be selected when CUPS does not report a default
  printer.

* Sun Jan 28 2001 Till Kamppeter <till@mandrakesoft.com> 1.0-2mdk
- CVS Update: Support for banner pages and raw printing, comment about
  adding instances in "Instances" dialog.

* Sat Jan 27 2001 Till Kamppeter <till@mandrakesoft.com> 1.0-1mdk
- CVS Update: Support for adding, copying, renaming, and deleting
  instances, fixed probable bug of options being saved to wrong queue
  when number of queues/instances changes when XPP is running.

* Sat Jan 20 2001 Till Kamppeter <till@mandrakesoft.com> 0.7-5mdk
- CVS Update: Fixed bug in the media settings widgets.

* Thu Jan 18 2001 Till Kamppeter <till@mandrakesoft.com> 0.7-4mdk
- CVS Update: Rearranged option widgets for media settings on the "Basic"
  tab of the "Options" dialog.

* Wed Jan 17 2001 Till Kamppeter <till@mandrakesoft.com> 0.7-3mdk
- CVS Update: Fields for typing the values of numerical options added.

* Sun Jan 07 2001 David BAUDENS <baudens@mandrakesoft.com> 0.7-2mdk
- s/Copyright/License
- Fix BuildRequires
- %%setup -q
- Use %%_menudir macro
- Fix %%post and %%postun sections
- Clean %%files section
- Spec clean up

* Wed Dec 20 2000 Till Kamppeter <till@mandrakesoft.com> 0.7-1mdk
- Version 0.7
- FLTK 1.0.10 used
- Adapted to new cups package

* Wed Nov 15 2000 Till Kamppeter <till@mandrakesoft.com> 0.6-17mdk
- Recompiled with GCC 2.96

* Tue Oct  3 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.6-16mdk
- added BuildRequires on: cups-devel fltk-devel Mesa-common-devel libstdc++-devel.

* Tue Sep 26 2000 Till Kamppeter <till@mandrakesoft.com> 0.6-15mdk
- Updated URL to http://cups.sourceforge.net/xpp/

* Tue Sep 26 2000 Till Kamppeter <till@mandrakesoft.com> 0.6-14mdk
- CVS Update: Now numerical options can also be read in PPD files with
  dossy line ends ("\n\r" instead of "\n").

* Sun Sep 24 2000 Till Kamppeter <till@mandrakesoft.com> 0.6-13mdk
- CVS Update: Integer and floating point options of CUPS-O-MATIC PPDs are
  supported now.

* Sat Sep 23 2000 Till Kamppeter <till@mandrakesoft.com> 0.6-12mdk
- CVS Update: "Authentication ..." line in login/password dialog is 
  also displayed with CUPS 1.1.3.

* Thu Sep  7 2000 Till Kamppeter <till@mandrakesoft.com> 0.6-11mdk
- CVS Update: Main window is resizable now.

* Sat Aug 26 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 0.6-10mdk
- Removed hardcoded architecture-specific flags, used macros instead

* Fri Aug 25 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 0.6-9mdk
- Entry for Mandrake menu structure added

* Wed Aug 23 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 0.6-8mdk
- Clean-up of "./configure" call in specfile

* Wed Aug 23 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 0.6-7mdk
- Removed hardcoded "i586-mandrake-linux" from specfile

* Wed Aug 23 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 0.6-6mdk
- Deactivated positioning of the printer list to make default printer visible,
  a bug in FLTK messed up the display of the printer list.
- Optical enhancements of the printer list.

* Sun Aug 20 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 0.6-5mdk
- Updated to version 0.6: Full support for password-protected printers, more
  information in printer list, printing with or saving conflicting options
  is not possible any more.

* Wed Aug 16 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 0.5-4mdk
- Updated to version 0.5: Margin options for text file printing and options
  for HP-GL/2 printing, "Reverse" page orientations, window does not close
  when printing leads to an error

* Sun Aug 13 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 0.4-3mdk
- New CVS version: Now the widgets on the "Basic" tab of the options window
  are coupled to the appropriate PPD options, instance names are read, and
  types of destinations without PPD file are displayed.

* Thu Aug 10 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 0.4-2mdk
- Removed "fltk" from "Requires:" line.
- FLTK now linked statically into XPP -> Fast load and no widget lib needs
  to be installed.

* Wed Aug  9 2000 Till Kamppeter <tkamppeter@mandrakesoft.com> 0.4-1mdk
- Updated to version 0.4.
- Added "fltk" to "Requires:" line.

* Thu Jul  6 2000 François Pons <fpons@mandrakesoft.com> 0.2-0.1mdk
- patch for Makefile to link against optimized fltk.
- initial release.
