%undefine _package_note_file
%undefine _debugsource_packages

Name:           imgview
Version:        2.6.1
Release:        1
Summary:        Image Viewer
Group:          Graphics
License:        GPL
Source:         https://wolfsinger.com/~wolfpack/packages/iv-%{version}.tar.bz2
Patch1:         iv-2.5.1-fix-lib64-build.patch
BuildRequires:	libpng-devel
BuildRequires:	libpng12
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libXpm-devel
BuildRequires:  gtk+-devel
BuildRequires:  imlib-devel
BuildRequires:  ghostscript-core ImageMagick
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmng-devel
BuildRequires:  sane-backends-libs
BuildRequires:  automake

%description
Sometimes reffered to as ImgView or IV, this is a basic image viewer
with pan and zoom capabilities, depends on GTK+ and Imlib. Can also
save to many different formats, display transparency, crop, print, and
do window grabs.

%prep
%setup -q -n iv-%{version}
%patch1 -p 1
sed -i '10i #include <time.h>' iv/imgio_mng.c
sed -i -e 's|TRUE|true|' -e 's|GifCloseFile(ctx->gif_file)|GifCloseFile(ctx->gif_file, NULL)|' iv/imgio_gif.c
sed -i -e '1632a ,NULL' -e '2135a ,NULL' -e '4111a ,NULL' -e 's|GIF_LIB_VERSION|"5.1.9"|' iv/imgio_gif.c
sed -i -e 's|EGifPutExtensionFirst|EGifPutExtension|' -e 's|EGifPutExtensionLast|EGifPutExtension|' iv/imgio_gif.c
sed -i -e 's|FreeMapObject|GifFreeMapObject|' -e 's|MakeMapObject|GifMakeMapObject|' iv/imgio_gif.c
sed -i '/GifLastError/d' iv/imgio_gif.c

%build
export CFLAGS="%{optflags} -I%{_includedir}/endeavour2" 
%ifarch x86_64
%define platform Linux64
%else
%define platform Linux
%endif
./configure %{platform} \
    -v --disable=arch-i686 --disable=debug --disable=libpng

make all

%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT%_prefix MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 install
mv $RPM_BUILD_ROOT%{_bindir}/iv $RPM_BUILD_ROOT%{_bindir}/%{name}
bunzip2 -c $RPM_BUILD_ROOT%{_mandir}/man1/iv.1.bz2 > $RPM_BUILD_ROOT%{_mandir}/man1/imgview.1

# icons
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
mv $RPM_BUILD_ROOT%{_datadir}/icons/iv.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.xpm

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/applications
cat >  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=ImgView
Comment=Image Viewer
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=Graphics;Viewer;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%exclude %{_mandir}/man1/iv.1*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Aug 29 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.1
- Rebuilt for Fedora
* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.5.2-1mdv2010.0
+ Revision: 390411
- update to new version 2.5.2
* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.5.1-1mdv2009.1
+ Revision: 354872
- new version
- new version
- import iv
  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
* Sun May 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.4-1mdv2009.0
- new version
* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.2-2mdv2007.0
- xdg menu
* Thu May 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.2-1mdk
- New release 1.4.2
* Wed Mar 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.1-1mdk
- New release 1.4.1
- %%mkrel
* Mon Apr 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-1mdk
- New release 1.2.1
- spec cleanup
* Thu Jul 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.3.8-2mdk 
- explicit libdir
* Fri Jun 04 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.3.8-1mdk 
- new version
- rpmbuildupdate aware
* Fri Jan 30 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.3.3-1mdk
- new version
- dropped patch
* Thu Jan 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.3.2-1mdk
- new version
- corrected URL
- buildrequires
- fix build
* Sun Jan 04 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.3.1-1mdk
- new version
* Fri Dec 12 2003 Guillaume Rousse <guillomovitch@mandrake.org> 0.1.15-1mdk
- new version
- rediff patch
- used ImageMagick for icons
* Thu May 01 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.1.12-1mdk
- 0.1.12
* Fri Sep 06 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.1.9-3mdk
- rebuild
* Wed May 29 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.1.9-2mdk
- build with gcc3.1
* Fri Feb 08 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.1.9-1mdk
- first mdk release
