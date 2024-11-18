Summary:        An X Window System image editing or paint program
Name:           xpaint
Version:        3.1.4
Release:        1
License:        GPLv3+
Group:          Applications/Multimedia
URL:            https://sourceforge.net/projects/sf-xpaint
Source0:        https://downloads.sourceforge.net/sf-xpaint/%{name}-%{version}.tar.bz2
BuildRequires: bison flex imake chrpath
BuildRequires: desktop-file-utils
BuildRequires: openjpeg-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel 
BuildRequires: libtiff-devel
BuildRequires: libSM-devel 
BuildRequires: libXaw-devel 
BuildRequires: libXdmcp-devel 
BuildRequires: libXext-devel 
BuildRequires: libXp-devel
BuildRequires: Xaw3d-devel
BuildRequires: libXaw3dXft-devel
BuildRequires: netpbm-devel
BuildRequires: libpgf-devel
#BuildRequires: neXtaw-devel
Requires: cups, gv, psutils

# The only way of compiling and linking plugins on the fly.
Obsoletes: %{name}-devel < %{version}-%{release}
Provides:  %{name}-devel = %{version}-%{release}

%description
XPaint is an X Window System color image bitmap editing program. 
It also supports advanced features, such as image processing
algorithms, scripting and batch jobs. XPaint allows the edition 
of multiple images simultaneously and supports a wide variety of 
image formats, including: GIF, JPG, PNG, PPM, TIFF, XBM, XPM, etc.

xpaint is now fully UTF8 compliant, and is capable of using anti-aliased
truetype fonts in its operations and in the menus (in particular,
translating to oriental languages should now be quite easy - also
the X core font protocol is no longer used anywhere.)

xpaint also offers optional editing features based on programmable filters 
and user defined procedures written as scripts in plain C. 
The package includes a substantial list of examples and 
some support for batch processing.

%prep
%setup -q

sed -i -e 's|-lXext|-lXext -lfontconfig|g' Local.config
sed -i -e 's|/lib |/%{_lib} |g' Local.config
sed -i -e 's|@XPMDIR@|%{_prefix}|g' Local.config
sed -i -e 's|/usr/lib|%{_libdir}|g' configure
sed -i -e 's|/usr/lib|%{_libdir}|g' configure.old
sed -i -e 's|ln -s xpaint|ln -sf xpaint|g' configure.old
sed -i -e 's|CFLAGS="-O3 -s -DNDEBUG=1"|CFLAGS=$RPM_OPT_FLAGS|g' util/pdfconcat.c
sed -i -e 's|@echo|echo|g' util/Makefile
for f in ChangeLog README; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf8
    touch -r $f $f.utf8
    mv $f.utf8 $f
done

%build
#sed -i -e "s/\(XCOMM CDEBUGFLAGS =\)/CDEBUGFLAGS = $RPM_OPT_FLAGS\nCXXDEBUGFLAGS = $RPM_OPT_FLAGS/g" Local.config
# this is for debugging, to save the temporary file Imakefile.c
touch fake
ln fake Imakefile.c
#./configure.old --libdir=%{_libdir}
%configure
# avoids laygram.h not found
make
cd util
make CXXFLAGS+="-std=c++98 -fPIE"

%install
rm -rf %{buildroot}
make \
        DESTDIR=%{buildroot} \
        BINDIR=%{_bindir} \
        LIBDIR=%{_libdir} \
        MANDIR=%{_mandir}/man1 install

# menu entry
desktop-file-install --delete-original                  \
        --vendor ""                                     \
        --dir %{buildroot}%{_datadir}/applications      \
        $RPM_BUILD_DIR/%{name}-%{version}/%{name}.desktop

# icons
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -a $RPM_BUILD_DIR/%{name}-%{version}/icons/* %{buildroot}%{_datadir}/pixmaps

# rpath
#chrpath --delete %{buildroot}%{_bindir}/xpaint

# remove needless symlink to /etc/X11/app-defaults
rm -rf %{buildroot}%{_libdir}/app-defaults

#mkdir -p %{buildroot}%{_includedir}
#mv %{buildroot}%{_datadir}/%{name}/include %{buildroot}%{_includedir}/%{name}
#ln -s ../../include/%{name} %{buildroot}%{_datadir}/%{name}/include

%files
%doc AUTHORS ChangeLog COPYING NEWS README README.old README.PNG TODO Doc/sample.Xdefaults Doc/Operator.doc Doc/TextFormat.doc
%{_bindir}/*
%{_libdir}/libxpaintrw.*
%{_sysconfdir}/X11/app-defaults/XPaint*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/xpaint.svg
%{_datadir}/pixmaps/%{name}*
%{_datadir}/pixmaps/XPaintIcon*.png
%{_mandir}/man1/*
   
%changelog
* Sun Sep 19 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1.4
- Rebuilt for Fedora
* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Sep 21 2013 Paulo Roma <roma@lcg.ufrj.br> 2.9.9.4-1
- Updated to 2.9.9.4
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 2.9.8.3-6
- rebuild due to "jpeg8-ABI" feature drop
* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.9.8.3-5
- rebuild against new libjpeg
* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Thu Feb 09 2012 Rex Dieter <rdieter@fedoraproject.org> 2.9.8.3-3
- rebuild (openjpeg)
* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Tue Nov 15 2011 Paulo Roma <roma@lcg.ufrj.br> 2.9.8.3-1
- Updated to 2.9.8.3
* Mon Jun 27 2011 Paulo Roma <roma@lcg.ufrj.br> 2.9.8.2-1
- Updated to 2.9.8.2
- Added new png files.
* Fri Dec 24 2010 Paulo Roma <roma@lcg.ufrj.br> 2.9.8.1-1
- Updated to 2.9.8.1
- Removed deprecated gcc 4.5 patch.
* Sat Nov 07 2010 Paulo Roma <roma@lcg.ufrj.br> 2.9.8-1
- Update to 2.9.8
- Patched for gcc 4.5
* Sat Nov 06 2010 Paulo Roma <roma@lcg.ufrj.br> 2.9.7-1
- Update to 2.9.7
* Sun Aug 01 2010 Paulo Roma <roma@lcg.ufrj.br> 2.9.2-1
- Update to 2.9.2
- Added BR openjpeg-devel.
* Mon Mar 08 2010 Paulo Roma <roma@lcg.ufrj.br> 2.8.19-1
- Update to 2.8.19
- BRs: xaw/xaw3d are optional.
- Added BR libXft-devel.
* Sat Feb 14 2010 Paulo Roma <roma@lcg.ufrj.br> 2.8.16-1
- Update to 2.8.16
- Removed obsolete patch text-ctrlH-segfault.
- Source is no longer stripped by default.
* Sat Feb 13 2010 Paulo Roma <roma@lcg.ufrj.br> 2.8.15-3
- Fixed the ImplicitDSOLinking.
* Fri Feb 05 2010 Paulo Roma <roma@lcg.ufrj.br> 2.8.15-2
- Applied patch text-ctrlH-segfault.
* Tue Feb 02 2010 Paulo Roma <roma@lcg.ufrj.br> 2.8.15-1
- Updated to 2.8.15: #BUG 559938
- Added BR psutils.
* Fri Jan 29 2010 Paulo Roma <roma@lcg.ufrj.br> 2.8.13.1-3
- Obsoleting xpaint-devel.
* Fri Jan 29 2010 Paulo Roma <roma@lcg.ufrj.br> 2.8.13.1-2
- Not stripping xpaint: #BUG 540223
- Dropped devel package.
* Fri Jan 29 2010 Paulo Roma <roma@lcg.ufrj.br> 2.8.13.1-1
- Updated to 2.8.13.1
- Removed emacs dependency: #BUG 542967
* Wed Nov 19 2009 Paulo Roma <roma@lcg.ufrj.br> 2.8.7.3-1
- Updated to 2.8.7.3
* Wed Nov 16 2009 Paulo Roma <roma@lcg.ufrj.br> 2.8.7.2-1
- Updated to 2.8.7.2
* Wed Nov 04 2009 Paulo Roma <roma@lcg.ufrj.br> 2.8.7-1
- Updated to 2.8.7
- Changed license to GPLv3+
- Applied patch xpaint-2.8.7-graphic.c.patch
* Mon Nov 02 2009 Paulo Roma <roma@lcg.ufrj.br> 2.8.6.1-2
- Moved c_scripts and the include symbolic link to the
  main package, as they are not needed to compile 3th party 
  plugins (if there will ever be a 3th party plugin).
* Tue Oct 27 2009 Paulo Roma <roma@lcg.ufrj.br> 2.8.6.1-1
- Updated to 2.8.6.1
- Added devel subpackage as noarch.
* Wed Oct 22 2009 Paulo Roma <roma@lcg.ufrj.br> 2.8.5-8
- Updated to 2.8.5
- Using %%configure.
- Removed rpath.
* Wed Oct 14 2009 Paulo Roma <roma@lcg.ufrj.br> 2.8.4-7
- Changed license to GPLv3.
* Mon Oct 05 2009 Paulo Roma <roma@lcg.ufrj.br> 2.8.3-6
- Removed devel package.
* Sat Oct 03 2009 Paulo Roma <roma@lcg.ufrj.br> 2.8.3-5
- Updated to 2.8.3
- Using supplied desktop entry.
* Thu Oct 01 2009 Paulo Roma <roma@lcg.ufrj.br> 2.8.2-5
- Updated to 2.8.2
- New icons.
* Sat Jun 30 2007 Paulo Roma <roma@lcg.ufrj.br> 2.7.8.1-4
- Created devel package.
- Fixed configure.
- Conditionally building with Xaw3d or neXtaw.
* Mon Apr 02 2007 Paulo Roma <roma@lcg.ufrj.br> 2.7.8-4
- Rebuilt for x86_64.
- Moved rm -rf %%{buildroot} from "prep" to "build".
- Fixed rm -rf %%{buildroot}%%{_libdir}/app-defaults
- Removed all .c and .h files.
* Sun Dec 31 2006 Paulo Roma <roma@lcg.ufrj.br> 2.7.8-3
- Included missing build requirements.
* Thu Sep 14 2006 Paulo Roma <roma@lcg.ufrj.br> 2.7.8-1
- Update to 2.7.8
- Changed spec file for Fedora.
* Mon Apr 04 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.7.6-1mdk
- 2.7.6
* Mon Mar 14 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.7.4-1mdk
- 2.7.4
* Mon Jan 31 2005 Lenny Cartier <lenny@mandrakesoft.com> 2.7.3-1mdk
- 2.7.3
* Tue Oct 19 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.7.2-1mdk
- 2.7.2
* Wed Sep 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.7.1-1mdk
- 2.7.1
* Fri Aug 20 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.7.0-4mdk
- fix typo in menu entry
* Mon Dec 29 2003 Michael Scherer <misc@mandrake.org> 2.7.0-3mdk 
- fix BuildRequires ( remove lib )
- remove /usr/X11R6/lib/X11/app-defaults link to /etc
* Sun Sep 14 2003 Michael Scherer <scherer.michael@free.fr> 2.7.0-2mdk
- BuildRequires flex 
* Mon Jun 16 2003 Stew Benedict <sbenedict@mandrakesoft.com> 2.7.0-1mdk
- 2.7.0
* Mon Apr 28 2003 Stew Benedict <sbenedict@mandrakesoft.com> 2.6.9-2mdk
- BuildRequires, distriblint
 * Fri Apr  4 2003 Stew Benedict <sbenedict@mandrakesoft.com> 2.6.9-1mdk
- 2.6.9, new URL, Source tag 
- some new features finally, add patch1 to fix make install
* Mon Dec 30 2002 Stew Benedict <sbenedict@mandrakesoft.com> 2.6.2-2mdk
- rebuild for new glibc/rpm, add patch1 for errno
* Sat Nov 16 2002 Stew Benedict <sbenedict@mandrakesoft.com> 2.6.2-1mdk
- new version, add installed but unpackaged file, icons->png
* Fri Oct 19 2001 Sebastien Dupont <sdupont@mandrakesoft.com> 2.6.1-2mdk
- License
- srcs permissions
- remove patchs: xpaint-2.4.7-config.patch & xpaint-2.4.7-glibc.patch.
* Sun May 27 2001  Daouda Lo <daouda@mandrakesoft.com> 2.6.1-1mdk
- release 2.6.1
- stop Nono complains.
- cleanups
* Tue Oct 03 2000 Daouda Lo <daouda@mandrakesoft.com> 2.6.0-2mdk
- icons should be transparent
- let spec helper do its jobs
- menu entry in the body of the spec
- more macroz..
* Sun Aug 27 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 2.6.0-1mdk
- new and shiny version.
* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.4.9-16mdk
- automatically added BuildRequires
* Mon May 15 2000 David BAUDENS <baudens@mandrakesoft.com> 2.4-9-15mdk
- Fix build for i486
- Use %%{_tmppath} for BuildRoot
* Wed May 03 2000 dam's <damien@mandrakesoft.com> 2.4.9-14mdk
- Corrected icons.
* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 2.4.9-13mdk
- Convert gif icon to xpm.
* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 2.4.9-12mdk
- Added menu entry.
* Mon Mar 27 2000 dam's <damien@mandrakesoft.com> 2.4.9-11mdk
- Release.
* Tue Nov 02 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- corrected status of resource file
* Thu May 06 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS
* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 8)
* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0
* Mon Aug  3 1998 Jeff Johnson <jbj@redhat.com>
- build root.
* Tue Jun 09 1998 Mike Wangsmo <wanger@redhat.com>
- changed the docs from being %%config files.
* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
* Thu Apr 16 1998 Erik Troan <ewt@redhat.com>
- built against libpng 1.0
* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- new release
- wmconfig
* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>
- build against new libpng
* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- "make install.man" places man page in wrong location
