%undefine _debugsource_packages
Name:		stopmotion
Summary:	An application for creating stopmotion animations
Version:	0.6.1
Release:	1
Source0:	http://developer.skolelinux.no/info/studentgrupper/2005-hig-stopmotion/project_management/webpage/releases/%{name}-%{version}.tar.gz
Source1:	%{name}_zh_TW.ts
URL:		http://stopmotion.bjoernen.com/
Group:		Applications/Multimedia
License:	GPL
Requires:	SDL_image, libvorbis, libxml2, libtar, gamin
BuildRequires:	SDL_image-devel, libvorbis-devel, libxml2-devel, libtar-devel, ImageMagick, gamin-devel
BuildRequires: qt4-devel
Requires: qt4

%description
Stopmotion is a free application for creating stop-motion animation movies.
The users will be able to create stop-motions from pictures imported from
a camera or from the harddrive, add sound effects and export the animation
to different video formats such as mpeg or avi.

%prep
%setup -q
echo -e 'Name[zh_TW]=定格動畫編輯\nComment[zh_TW]=Stopmotion 建立定格動畫' >> stopmotion.desktop
sed -i '1i #include <unistd.h>' src/presentation/frontends/qtfrontend/mainwindowgui.cpp src/domain/animation/scene.cpp src/technical/projectserializer.cpp

%build
# Wrong permissions
chmod -R a+r *
for a in `find ./manual/`; do if [ ! -d $a ]; then chmod 644 $a;else chmod 755 $a;fi;done
PATH=%{_libdir}/qt4/bin:$PATH %configure	--with-html-dir=%{_datadir}/doc/%{name}-%{version}/manual
perl -pi -e "s#-pipe -O2#%{optflags}#g" Makefile
sed -i 's|-lSDL_image|-lSDL_image -lX11 |' Makefile
PATH=%{_libdir}/qt4/bin:$PATH %__make
# Generate icons. The 48x48 one might be a bit ugly, but it'll have to do
convert graphics/stopmotion.png -resize 16x16 graphics/stopmotion-16.png
convert graphics/stopmotion.png -resize 48x48 graphics/stopmotion-48.png

%install
rm -rf %{buildroot}

install -m755 stopmotion -Ds %{buildroot}%{_bindir}/%{name}
install -m644 stopmotion.desktop -D %{buildroot}%{_datadir}/applications/%{name}.desktop

install -m644 graphics/stopmotion.png -D %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -m644 graphics/stopmotion-48.png -D %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m644 graphics/stopmotion.png -D %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m644 graphics/stopmotion-16.png -D %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png

desktop-file-install	--vendor="" \
			--remove-category="Application" \
			--add-category="Qt" \
			--add-category="Video" \
			--add-category="AudioVideo" \
			--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

# Localization.
cp %{SOURCE1} translations
echo 'TRANSLATIONS += translations/stopmotion_zh_TW.ts' >> stopmotion.pro
# Uses a weird localization system, got to hardcode it *sigh* :)
%{_libdir}/qt4/bin/lrelease stopmotion.pro
mkdir -p %{buildroot}%{_datadir}/%{name}/translations/
install -m644 ./translations/*.qm %{buildroot}%{_datadir}/%{name}/translations/

%clean 
rm -rf $%{buildroot}

%files
%doc README AUTHORS manual/
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1
- Rebuilt for Fedora

* Fri May 04 2007 Adam Williamson <awilliamson@mandriva.com> 0.6.0-4mdv2008.0
+ Revision: 22562
- bump release
- doh, set PATH for configure too
- ok, let's do it this way
- bump release
- don't buildconflicts qt3-devel as SDL_image-devel implies it, just fix PATH instead
- correct fix for qmake (give path to qt4 version, don't require qt3 version)

* Wed Apr 25 2007 Adam Williamson <awilliamson@mandriva.com> 0.6.0-2mdv2008.0
+ Revision: 18380
- bump release for buildsystem weirdness
- lrelease is in /usr/lib not lib64 on x86-64
- buildrequires libqt3-devel (for /usr/bin/qmake)
- generate and install fd.o-compliant icons
- 0.6.0


* Fri Aug 25 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com>
+ 2006-08-25 15:59:24 (58098)
- fix summary macro use in menu
- compile with %%{optflags}
- cosmetics

* Thu Aug 03 2006 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2006-08-03 15:12:10 (43273)
- import stopmotion-0.5.3-1mdv2007.0

* Thu Jun 29 2006 Guillaume Bedot <littletux@mandriva.org> > 0.5.3-1mdv2007.0
- 0.5.3
- xdg menu

* Sat May 06 2006 Guillaume Bedot <littletux@mandriva.org> 0.5.1-1mdk
- New release 0.5.1
- Complete source0 URL

* Thu Apr 20 2006 Guillaume Bedot <littletux@mandriva.org> 0.5.0-3mdk
- Fix paths to translations and docs
- Use of qt4-linguist instead of qt3

* Wed Apr 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.5.0-2mdk
- Fix BuildRequires

* Wed Apr 19 2006 Lenny Cartier <lenny@mandriva.com> 0.5.0-1mdk
- 0.5.0

* Mon Mar 06 2006 Lenny Cartier <lenny@mandriva.com> 0.4.1-1mdk
- 0.4.1

* Sat Feb 11 2006 Eskild Hustvedt <eskild@mandriva.org 0.4.0-1mdk
- New version 0.4.0

* Sun Jan 22 2006 Eskild Hustvedt <eskild@mandriva.org> 0.3.4-1mdk
- 0.3.4
- Drop patch0 (now uses some perl magic in the spec instead)

* Mon Jan 16 2006 Lenny Cartier <lenny@mandriva.com> 0.3.3-1mdk
- 0.3.3

* Thu Dec 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.3.1-4mdk
- Fix  buildRequires

* Wed Oct 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.3.1-3mdk
- Fix BuildRequires

* Sun Aug 07 2005 Eskild Hustvedt <eskild@mandriva.org> 0.3.1-2mdk
- Bah, forgot to rediff p0 even though it says MUST BE REDIFFED ON A NEW RELEASE! in the spec

* Sun Aug 07 2005 Eskild Hustvedt <eskild@mandriva.org> 0.3.1-1mdk
- New version 0.3.1

* Sun May 22 2005 Eskild Hustvedt <eskild@mandriva.org> 0.3.0-2mdk
- Shut rpmlint up

* Sat May 21 2005 Eskild Hustvedt <eskild@mandrake.org> 0.3.0-1mdk
- Initial Mandriva Linux package
