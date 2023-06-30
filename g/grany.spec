Name: grany
Summary: The cellular automaton simulator
Version: 2.0.3
Release: 36.1
License: GPL
Group: Sciences/Physics
Source0: https://guillaume.cottenceau.free.fr/html/grany-resource/grany-%{version}.tar.bz2
Source1: %{name}-pngicons.tar.bz2
Patch2:	grany-2.0.3-gettext.patch
URL: https://guillaume.cottenceau.free.fr/html/grany.html
BuildRequires: pkgconfig(gtkmm-2.4)
BuildRequires: libX11-devel

%description
Grany is a cellular automaton simulator. With it you can conduct computerized
experiments on cellular environments with a full-featured GUI.

%prep
%setup -q -a1
%patch2 -p2 -b .datadir
sed -i 's|gtkmm-2.0|gtkmm-2.4|' configure*
sed -i 's|slot|sigc::mem_fun|' interface/src/*.cpp
sed -i 's|Gtk::Menu::AccelKey|Gtk::AccelKey|' interface/src/*.cpp

#FIXME:
sed -i '/using namespace Gtk::Toolbar_Helpers;/d' interface/src/*.cpp
sed -i '/_toolBar.tools/d' interface/src/*.cpp
sed -i '/_pixmap = NULL;/d' interface/src/MainWindow.cpp

sed -i 's|AM_GNU_GETTEXT|AC_PROG_RANLIB|' configure.in

%build
autoreconf -ifv
%configure
sed -i 's|@USE_INCLUDED_LIBINTL@|no|' intl/Makefile
sed -i 's|@INTLLIBS@||' */src/Makefile
sed -i 's|@DATADIRNAME@|share|' intl/Makefile interface/src/Makefile
echo -e 'all:\ninstall:' > po/Makefile
make CXXFLAGS+="-std=c++11"

%install
sed -i 's| $(pkgdatadir)| $(DESTDIR)$(pkgdatadir)|' interface/src/Makefile
%make_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat << EOF > %buildroot%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Name=Grany
Exec=grany
Icon=grany
Comment=The cellular automaton simulator
Categories=Education;Science;
EOF

# icons
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp icons/grany-icon-48x48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%files
%doc README FAQ AUTHORS docs/BASICS docs/CUSTOMIZATION
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.3
- Rebuilt for Fedora
* Thu Jan 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0.0-2mdv2008.1
+ Revision: 142109
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import grany
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Fri Jul 16 2004 Michael Scherer <misc@mandrake.org> 2.0.0-2mdk 
- rebuild for new gcc, patch 0
* Tue Apr  8 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 2.0.0-1mdk
- new release
* Wed Aug 21 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-4mdk
- rebuild for gcc 3.2
* Tue Jul 30 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-3mdk
- recompile against latest libstdc++
* Mon Jun 10 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.0.1-2mdk
- png icons (out xpm!)
* Tue May 14 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-1mdk
- new release that is friendly with g++-3.1
* Fri Feb 22 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-5mdk
- rebuild to fix invalid-packager
* Tue Oct 16 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-4mdk
- fix obsolete-tag Copyright
* Tue Sep 11 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-3mdk
- rebuild
* Fri Jan  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-2mdk
- rebuild
* Sun May  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-1mdk
- first build
