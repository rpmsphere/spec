Name:           beaver
Summary:        An Early AdVanced EditoR
Version:        0.4.1
Release:        20.1
License:        GPL-2.0
Group:          System/GUI/GNOME
URL:            http://beaver-editor.sourceforge.net
Source0:        %name-%version.tar.bz2
Patch0:         %{name}-add-mime-types.patch
BuildRequires:  autoconf automake gcc-c++ make
BuildRequires:  doxygen gtk2-devel intltool

%description
Beaver starts up fast and doesn't use a lot of memory.
Beaver's only dependency is GTK+2, so no need to install
other libraries eating your disk space. These things make
Beaver very suitable for old computers and use in small Linux distributions.

%prep
%setup -q
%patch0 -p1
sed -i 's|inline void refresh_markers|void refresh_markers|' src/editor.c

%build
LDFLAGS=-Wl,--allow-multiple-definition
%configure
make V=1 %{?_smp_mflags} all doc

%install
%makeinstall
%__mkdir_p %buildroot/%_datadir/doc/beaver
cp -R docs/html %buildroot/%_datadir/doc/beaver
rm %buildroot/%_libdir/beaver/plugins/*.la
# remove sample plugin doing nothing
rm %buildroot/%_libdir/beaver/plugins/sample.so

%files
%_bindir/beaver
%dir %_libdir/beaver
%dir %_libdir/beaver/plugins
%_libdir/beaver/plugins/ascii.so
%_libdir/beaver/plugins/tools.so
%_datadir/applications/beaver.desktop
%dir %_datadir/beaver
%dir %_datadir/beaver/pixmaps
%dir %_datadir/beaver/resource
%_datadir/beaver/pixmaps/*
%_datadir/beaver/resource/*
%dir %_datadir/doc/beaver/
%dir %_datadir/doc/beaver/html
%_datadir/doc/beaver/html/*
%_datadir/icons/hicolor/*x*/apps/*
%_datadir/pixmaps/beaver.png
%_mandir/man1/*.gz
%_includedir/beaver.h

%changelog
* Tue Dec 10 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuilt for Fedora
* Sat Sep 17 2011 jengelh@medozas.de
- Remove redundant tags/sections from specfile
- Use %%_smp_mflags for parallel build
* Mon Mar 14 2011 gber@opensuse.org
- call %%desktop_database_post/un and %%icon_theme_cache_post/un
* Wed Dec 29 2010 gber@opensuse.org
- added beaver-add-mime-types.patch in order to claim support for
  additional MIME types
* Sun Aug 29 2010 andrea@opensuse.org
- new upstream version 0.4.1 (bugfix release)
- removed all patches, they was taken from upstream code
* Sun Aug 22 2010 andrea@opensuse.org
- added beaver-0.4.0-fix-sf3030801.patch and
  beaver-0.4.0-fix-sf3033684.patch to fix upstream bug regarding
  syntax highlighting and undo/redo actions
* Fri Aug 20 2010 andrea@opensuse.org
- added beaver-0.4.0-fix-sf3033975.patch to fix sf#3033975
  (a not freed pointer made beaver crash because of lack of memory)
* Sat Jul 17 2010 andrea@opensuse.org
- new upstream version 0.4.0
- fixed undo/redo bug sf#3030800
* Sun Jul  4 2010 andrea@opensuse.org
- upgrade to 0.4.0 rc2
- removed all the patches now into upstream code
- fixed project URL now is http://beaver-editor.sourceforge.net/
- plugins now built from source tarball
* Wed Jun 30 2010 andrea@opensuse.org
- fixed a bug into package VERSION that will not allow to upgrade
  easly to stable version 0.4.0
* Sun Jun 13 2010 andrea@opensuse.org
- fixed plugins Makefile, and allow plugins compilations to work
  again.
* Sat Jun 12 2010 andrea@opensuse.org
- install beaver man page
* Fri Jun 11 2010 andrea@opensuse.org
- added beaver-fix-include-dir.patch, beaver --include-dir now
  returns the correct headers path
- improved beaver-gcc-warns.patch, adding missing prototype to
  the header file fix an 'implicit function declaration'
* Tue May  4 2010 meissner@suse.de
- disable strip --strip-all (to generate debuginfos)
- fix voidreturn warning
- add missing ; to desktop file
* Sun Oct 25 2009 andrea@opensuse.org
- fixed gcc critical warnings
* Thu Oct  1 2009 andrea@opensuse.org
- first spec making
