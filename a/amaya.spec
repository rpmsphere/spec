Name:		amaya
Version: 	11.4.7
Release: 	40.1
Summary: 	W3C's browser/web authoring tool
Group:   	Networking/WWW
Source0: 	http://www.w3.org/Amaya/Distribution/amaya-sources-%{version}.tgz
Source1: 	%name.1.bz2
License: 	W3C License
URL:     	http://www.w3.org/Amaya/
BuildRequires:	libpng-devel libpng10-devel
BuildRequires: 	giflib-devel libjpeg-devel zlib-devel
BuildRequires: 	gcc-c++ perl bison flex imake
BuildRequires:	libX11-devel libXt-devel freetype-devel wxGTK-devel w3c-libwww-devel
BuildRequires:	redland-devel raptor-devel openssl-devel
Obsoletes:	amaya-common amaya-gtk amaya-lesstif
Provides:	amaya-common amaya-wx 

%description
Amaya is a WYSIWYG browser/web authoring tool from the W3C.

This graphical HTML Editor supports many of the latest
draft standards for HTML/XHTML.

%prep
%setup -q -n Amaya%{version}
##sed -i -e 's|FILE \*|gzFile |' -e 's|FILE\*|gzFile |' Amaya/amaya/*ml2thot.c Amaya/amaya/f/*ml2thot_f.h
##sed -i -e 's/-lssl -lcrypto/-lssl -lcrypto -lz -ljpeg -lpng10/' -e 's/-lGL -lGLU/-lGL -lGLU -lz -ljpeg -lpng10/' Amaya/configure*
sed -i 's|-Wall|-Wall -fpermissive -fPIC|' configure*
sed -i 's|png\.h|libpng10/png.h|' thotlib/image/pnghandler.c
sed -i "s|'\\\0'|NULL|" thotlib/include/thot_sys.h

%build
##cd Amaya
#export CXXFLAGS=-fpermissive
mkdir -p wx-build
cd wx-build
../configure --prefix=%_libdir --exec=%_libdir --libdir=%_libdir --enable-system-redland --enable-system-wx --enable-system-raptor --enable-system-libwww --with-mesa
##%ifarch x86_64
##cp -f Mesa/configs/linux-x86-64 Mesa/configs/current
##%endif
sed -i -e 's|$$STR|../wx-build/bin/str|' -e 's|$$PRS|../wx-build/bin/prs|' -e 's|$$TRA|../wx-build/bin/tra|' amaya/Makefile
make

%install
cd Amaya
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1
mkdir -p $RPM_BUILD_ROOT/%_bindir
cd wx-build
make install prefix=$RPM_BUILD_ROOT%_libdir

#rm -rf $RPM_BUILD_ROOT%_libdir/bin
pushd $RPM_BUILD_ROOT/%_bindir/
ln -sf ../../usr/%_lib/Amaya/wx/bin/amaya amaya-wx
ln -sf ../../usr/%_lib/Amaya/wx/bin/amaya amaya
popd

# Mandriva menu entry
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=%{name} 
Icon=%{_libdir}/Amaya/resources/icons/misc/logo.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Network;
EOF

# Man pages
bzcat %SOURCE1 > $RPM_BUILD_ROOT%_mandir/man1/%name.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Amaya/README* Amaya/amaya/COPYRIGHT*
%_libdir/Amaya*
%_mandir/man1/%name.*
%_bindir/%name
%_bindir/%name-wx
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Jun 22 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 11.4.4
- Rebuild for Fedora

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 10.0-1mdv2009.0
+ Revision: 218429
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Feb 27 2008 Frederik Himpe <fhimpe@mandriva.org> 10.0-1mdv2008.1
+ Revision: 175926
- Final version 10.0

* Sat Feb 02 2008 Funda Wang <fundawang@mandriva.org> 10.0-0.pre.1mdv2008.1
+ Revision: 161333
- New version 10.0 pre

* Thu Jan 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 9.99-3mdv2008.1
+ Revision: 160819
- reverse dep fix (amaya-0.99.9 seems fixed regarding this)

* Tue Jan 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 9.99-2mdv2008.1
+ Revision: 159763
- add missing require on lib64wxgtkglu2.6 (#35671)

* Thu Jan 17 2008 Crispin Boylan <crisb@mandriva.org> 9.99-1mdv2008.1
+ Revision: 154503
- New release#
- New release

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 13 2007 Crispin Boylan <crisb@mandriva.org> 9.55-3mdv2008.1
+ Revision: 108560
- Drop patch 2
- Fix symbolic links (#34539)

* Sat Oct 13 2007 Crispin Boylan <crisb@mandriva.org> 9.55-1mdv2008.1
+ Revision: 97993
- Update patch1 (amd64 fixes)
- New version

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'
    - fix man pages

* Sat Jan 06 2007 Crispin Boylan <crisb@mandriva.org> 9.53-1mdv2007.0
+ Revision: 104990
- Respin patch 1
- Various spec fixes
- XDG Menu
- New version
- Import amaya

* Wed Nov 30 2005 Thierry Vignaud <tvignaud@mandriva.com> 9.2.2-1mdk
- new release
- use system redland library
- patch 0: fix build with current redland
- patch 1: 64bit fixes for x86_64
- patch 2: first bits toward using system w3c library
- fix binary link on x86_64 (blino)

* Tue Aug 17 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 8.6-1mdk
- new release

* Thu May 20 2004 Austin Acton <austin@mandrake.org> 8.5-1mdk
- 8.5
- disable bookmarks (redlan mayhem)
