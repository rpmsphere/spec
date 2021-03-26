Name:           xstereograph
BuildRequires:  libpng-devel
BuildRequires:  libXaw-devel
BuildRequires:  Xaw3d-devel
%define		version_libsx 2.03
Summary:        Stereogram generator
License:        GPL-2.0+ and LGPL-2.1+
Group:          Amusements/Games/Other
Requires:       ImageMagick
Requires:       emacs-x11
Requires:       xless
Version:        2.1
Release:        823.1
URL:            http://freshmeat.net/projects/xstereograph/
Source0:        %{name}-%{version}.tar.bz2
Source1:        libsx-%{version_libsx}.tar.bz2
Patch0:         %{name}-%{version}.patch
Patch1:         %{name}-%{version}-ia64.patch
Patch2:         %{name}-%{version}-strings.patch
Patch3:         %{name}-%{version}-dialogs.patch
Patch4:         %{name}-%{version}-gcc4.patch
Patch5:         %{name}-%{version}-uninitialized.patch
# libpng15.patch not sent to upstream (is project alive?)
Patch6:         %{name}-%{version}-libpng15.patch
# libpng16.patch not sent to upstream (is project alive?)
Patch7:         %{name}-%{version}-libpng16.patch

%description
Stereograph is a stereogram generator. In detail it is a single image
stereogram (SIS) generator. That's a program that produces
two-dimensional images that seem to be three-dimensional (surely you
know the famous works of "The Magic Eye", Stereograph produces the same
output). You do _not_ need any pair of colored spectacles to regard
them - everyone can learn it.

Authors:
--------
    fabian.linux@januszewski.de
    demailly@fourier.ujf-grenoble.fr

%prep
%setup -q -a 1
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
sed -i 's|trunc|mytrunc|' libsx-%{version_libsx}/src/colorsel.c
sed -i 's|-lm|-lm -Wl,--allow-multiple-definition|' stereograph-0.28a/Makefile

%build
# libsx
cd libsx-%{version_libsx}/src
make
cd ../..
#
# xstereograph
make X11_LIBDIR=/usr/%{_lib}

%install
make DESTDIR=$RPM_BUILD_ROOT install
install -d -m 755 $RPM_BUILD_ROOT/usr/share/xstereograph/
cp -r depth_maps textures mathfiles magic-eye.xpm stereo_dia.png \
      $RPM_BUILD_ROOT/usr/share/xstereograph/      
#
# documentation
install -d -m 755 $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/
install -m 644 AUTHORS COPYING README $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/
#
# documentation stereograph
cd stereograph-0.28a
install -d -m 755 $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/stereograph/
install -m 644 AUTHORS COPYING INSTALL README TODO \
	       $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/stereograph/
cd ..
#
# libsx
cd libsx-%{version_libsx}/src
make DESTDIR=$RPM_BUILD_ROOT \
     LIBDIR=%{_libdir} \
     INCLUDEDIR=%{_includedir}/SX \
     SHAREDIR=%{_datadir}/libsx \
     install
#
# libsx documentation
cd ..
install -d -m 755 $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/libsx/
install -m 644 CHANGES HELP HINTS LICENSE README \
               $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/libsx/
cd ..
%{__rm} -f %{buildroot}%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT



%files
%doc %{_defaultdocdir}/%{name}/
%doc %{_mandir}/man1/*
%{_bindir}/*
%{_includedir}/SX
%{_datadir}/xstereograph
%{_datadir}/libsx
%{_libdir}/lib*

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuild for Fedora
* Fri Feb 15 2013 pgajdos@suse.com
- builds also with libpng16
  * libpng16.patch
* Fri Feb  1 2013 coolo@suse.com
- update license to new format
* Tue Sep  4 2012 pgajdos@suse.com
- builds also with libpng15
  * libpng15.patch
* Fri Jun 19 2009 coolo@novell.com
- disable as-needed for this package as it fails to build with it
* Fri Apr 17 2009 crrodriguez@suse.de
- remove static libraries
* Wed Aug 22 2007 anosek@suse.cz
- changed prefix /usr/bin/X11 -> /usr/bin
- dropped obsoleted xstereograph-X11R7.patch
* Fri Jun  1 2007 dmueller@suse.de
- fix buildrequires
* Thu Aug 17 2006 cthiel@suse.de
- fix build with X.Org 7.1
* Mon Jul 24 2006 mmarek@suse.de
- workaround build with modular Xorg
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan 16 2006 schwab@suse.de
- Use RPM_OPT_FLAGS.
- Don't strip binaries.
* Tue Jan  3 2006 mmarek@suse.cz
- fix uninitialized variable warning
  [#140092] (uninitialized.patch)
* Wed Apr 27 2005 ro@suse.de
- fix build with gcc-4
* Sun Jan 11 2004 adrian@suse.de
- build as user
* Wed Aug 27 2003 kukuk@suse.de
- Use Xaw3d instead of Xaw95
* Mon Jun 16 2003 ro@suse.de
- added directory to filelist
* Tue Mar 18 2003 pmladek@suse.cz
- fixed to find /usr/X11R6/share/libsx/dialogs.xx
* Mon Nov 11 2002 pmladek@suse.cz
- fixed multiline string literals for the new gcc-3.3 (strings patch)
- installed correctly under the /usr/X11R6 direcory tree
- used %%run_ldconfig in the %%post and %%postun sections
* Fri Apr  5 2002 pmladek@suse.cz
- more used macro %%{_lib} to fix for lib64
- fixed LDFLAGS for libpng and libz
* Thu Jan 31 2002 ro@suse.de
- changed neededforbuild <libpng> to <libpng-devel-packages>
* Wed Jan 23 2002 pmladek@suse.cz
- used macro %%{_lib} to fix for lib64
* Thu Jan 10 2002 ro@suse.de
- no subdirs in /usr/games
* Fri Nov 30 2001 sf@suse.de
- lots of missing includes added
- libsx compiles now with -fPIC
* Thu Oct 25 2001 pmladek@suse.cz
- package created, version 2.1
- with libsx, version 2.03
