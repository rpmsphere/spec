%undefine _debugsource_packages

Name:           exult
Version:        1.6
Release:        1
Summary:        Ultima VII Engine
License:        GPL     
URL:            http://exult.sourceforge.net       
Source0:        exult-%{version}.tar.gz
BuildRequires:  SDL_mixer-devel SDL-devel
Requires:       SDL, SDL_mixer, SDL_image

%description
Exult: an implementation of the Ultima VII engine for modern Operating Systems.

%package tools
Summary: Tools and utilities for playing with Exult/Ultima VII data files
Group: Amusements/Games

%description tools
Exult Tools: a set of utilities for playing with Exult/Ultima VII data files.
Included in the tools are: expack (archiver), ucxt (decompiler),
ucc (compiler), splitshp (frame splitter), shp2pcx (shape converter),
ipack (image archiver), textpack (text archiver)

#%package studio
#Summary: An editor for the Exult engine.
#Group: Amusements/Games

#Ddescription studio
#Exult Studio: an editor for the Exult engin

%prep
%setup -q
#sed -i '1i #include <cstring>' shapes/pngio.cc
#sed -i 's|bool \*accept = false|bool *accept = NULL|' mapedit/shapeedit.cc

%build
./autogen.sh
%configure --disable-exult-studio --disable-exult-studio-support
#sed -i 's|-Wall|-Wall -Wno-narrowing|' Makefile */Makefile
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog NEWS README FAQ README.1ST
%{_bindir}/exult
   /usr/share/exult/u7sibetaintrinsics.data
%{_datadir}/exult/exultmsg.txt
%{_datadir}/exult/exult_bg.flx
%{_datadir}/exult/exult_si.flx
%{_datadir}/exult/exult.flx
%{_datadir}/exult/midisfx.flx
%{_datadir}/icons/exult.png
%{_mandir}/man6/exult.6.gz
%{_datadir}/applications/exult.desktop
%{_datadir}/exult/bg_mr_faces.vga
%{_datadir}/exult/bg_paperdol.vga
%{_datadir}/exult/exult_iphone.flx

%files tools
%doc tools/expack.txt
%{_mandir}/man1/*
%{_bindir}/expack
%{_bindir}/ipack
%{_bindir}/textpack
%{_bindir}/ucxt
%{_bindir}/cmanip
%{_bindir}/mklink
%{_bindir}/rip
%{_bindir}/wuc
#{_bindir}/ucc
%{_bindir}/splitshp
%{_bindir}/shp2pcx
%{_datadir}/exult/u7bgintrinsics.data
%{_datadir}/exult/u7siintrinsics.data
%{_datadir}/exult/u7sibetaintrinsics.data
%{_datadir}/exult/u7misc.data
%{_datadir}/exult/u7opcodes.data

%if 0
%files studio
%{_bindir}/exult_studio
%{_datadir}/exult/exult_studio.glade
%{_datadir}/exult/estudio/new/combos.flx
%{_datadir}/exult/estudio/new/faces.vga
%{_datadir}/exult/estudio/new/gumps.vga
%{_datadir}/exult/estudio/new/palettes.flx
%{_datadir}/exult/estudio/new/shapes.vga
%{_datadir}/exult/estudio/new/sprites.vga
%{_datadir}/exult/estudio/new/text.flx
%{_datadir}/exult/estudio/new/fonts.vga
%{_datadir}/exult/estudio/new/pointers.shp
%{_datadir}/exult/estudio/new/blends.dat
%{_datadir}/exult/estudio/new/paperdol.vga
%endif

%changelog
* Sun Apr 4 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6
- Rebuilt for Fedora
* Sun May 20 2012 Chih-Jen Nung <cj.nung@ossii.com.tw>-1.4.9.0.rc1.svn7114
- create newspec  
* Tue Jul 22 2003  Willem Jan Palensitjn <wjpalenstijn@users.sourceforge.net>
- updated for 1.1Beta1
- added a 'studio' package
* Wed Nov 06 2002  Willem Jan Palensitjn <wjpalenstijn@users.sourceforge.net>
- added tools manpages
* Fri Nov 01 2002  Willem Jan Palenstijn <wjpalenstijn@users.sourceforge.net>
- updated .spec to work with RH80
- removed studio and gimp plugin packages for 1.0 branch
* Fri Jun 07 2002  Willem Jan Palenstijn <wjpalenstijn@users.sourceforge.net>
- updated ucxt data files
* Wed Dec 05 2001  Tristan Tarrant <nadir@users.sourceforge.net>
- subpackages are here !!!
* Thu Nov 29 2001  Tristan Tarrant <nadir@users.sourceforge.net>
- allow setting of bindir and datadir
- build exult only (will be fixed with the addition of subpackages)
- added README.1ST
- optimizer flags should be set for CXXFLAGS too
* Mon Jun 25 2001  Willem Jan Palenstijn <wjpalenstijn@users.sourceforge.net>
- added exult_bg.flx, exult_si.flx
- removed explicit SDL req. (proper SDL version is added automatically)
* Tue Nov 7 2000  Tristan Tarrant <nadir@users.sourceforge.net>
- A few fixes
* Sat Sep 9 2000  Tristan Tarrant <nadir@users.sourceforge.net>
- Install exult.flx in the right place
* Tue Jul 11 2000  Tristan Tarrant <nadir@users.sourceforge.net>
- Created the .spec file
* Fri Feb 9 2000  Tristan Tarrant <nadir@users.sourceforge.net>
- Disable GIMP plugin by default.
- Include FAQ
