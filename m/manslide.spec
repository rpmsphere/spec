%undefine _debugsource_packages
Name:		manslide
Summary:	Graphical slideshow creation program
Version:	2.0.3
Release:	1
Source0:	https://www.mandrivalinux-online.eu/%{name}-%{version}.tar.gz
Source1:	%{name}.png
URL:		https://www.kde-apps.org/content/show.php?content=72739
Group:		Graphics
License:	GPLv2+
BuildRequires:	qt-devel, mesa-libGL-devel
Requires:	netpbm-progs, sox, mjpegtools, vorbis-tools, ImageMagick, mencoder, mplayer

%description
Manslide is a slideshow creation application which makes it easy to
produce attractive slideshows with optional background music. Manslide
uses the QT4 toolkit.

%prep
%setup -q
rm -f moc_*.cpp

%build
qmake-qt4
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}

install -m 755 Manslide %{buildroot}%{_datadir}/%{name}/%{name}
install -m 644 *.qm %{buildroot}%{_datadir}/%{name}/
cp -a Interface %{buildroot}%{_datadir}/%{name}/
cp -a BIB_ManSlide %{buildroot}%{_datadir}/%{name}/
ln -s %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Manslide
Comment=Slideshow generator
Comment[zh_TW]=投影秀產生器
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=AudioVideo;AudioVideoEditing;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.3
- Rebuilt for Fedora

* Tue Aug 05 2008 Funda Wang <fundawang@mandriva.org> 2.0.3-4mdv2009.0
+ Revision: 263933
- rebuild for new compile flags

* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0.3-3mdv2009.0
+ Revision: 251857
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Mar 09 2008 Funda Wang <fundawang@mandriva.org> 2.0.3-1mdv2008.1
+ Revision: 182755
- New version 2.0.3

* Sun Mar 02 2008 Funda Wang <fundawang@mandriva.org> 2.0.2-1mdv2008.1
+ Revision: 177543
- New version 2.0.2

  + Frederik Himpe <fhimpe@mandriva.org>
    - Add X-MandrivaLinux-CrossDesktop category to desktop entry:
      There's no GTK+/GNOME similar application, so no need to hide
      it in the More submenu for GNOME users.

* Sun Feb 24 2008 Funda Wang <fundawang@mandriva.org> 2.0.1-1mdv2008.1
+ Revision: 174317
- New version 2.0.1

* Mon Feb 18 2008 Funda Wang <fundawang@mandriva.org> 2.0-1mdv2008.1
+ Revision: 171426
- New version 2.0

* Wed Feb 13 2008 Funda Wang <fundawang@mandriva.org> 1.9.13-1mdv2008.1
+ Revision: 167088
- New version 1.9.13

* Sat Feb 09 2008 Funda Wang <fundawang@mandriva.org> 1.9.11-1mdv2008.1
+ Revision: 164403
- New version 1.9.11

* Sun Feb 03 2008 Funda Wang <fundawang@mandriva.org> 1.9.10-1mdv2008.1
+ Revision: 161801
- New version 1.9.10

* Mon Jan 28 2008 Funda Wang <fundawang@mandriva.org> 1.9.9-1mdv2008.1
+ Revision: 159052
- New version 1.9.9

* Sat Jan 26 2008 Funda Wang <fundawang@mandriva.org> 1.9.8-1mdv2008.1
+ Revision: 158394
- New version 1.9.8

* Sun Jan 20 2008 Funda Wang <fundawang@mandriva.org> 1.9.7-1mdv2008.1
+ Revision: 155203
- New version 1.9.7

* Sat Jan 19 2008 Funda Wang <fundawang@mandriva.org> 1.9.6-1mdv2008.1
+ Revision: 155017
- New version 1.9.6
- fix URL

* Thu Jan 10 2008 Funda Wang <fundawang@mandriva.org> 1.9.5-1mdv2008.1
+ Revision: 147488
- update to new version 1.9.5

* Sat Jan 05 2008 Funda Wang <fundawang@mandriva.org> 1.9.4-1mdv2008.1
+ Revision: 145751
- New version 1.9.4

* Sat Jan 05 2008 Funda Wang <fundawang@mandriva.org> 1.9.3-1mdv2008.1
+ Revision: 145653
- New version 1.9.3

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Funda Wang <fundawang@mandriva.org> 1.9.1-1mdv2008.1
+ Revision: 119111
- New version 1.9.1

* Sun Nov 18 2007 Funda Wang <fundawang@mandriva.org> 1.9-1mdv2008.1
+ Revision: 109819
- update to new version 1.9

* Tue Nov 06 2007 Funda Wang <fundawang@mandriva.org> 1.8-1mdv2008.1
+ Revision: 106309
- New version 1.8

* Sat Nov 03 2007 Funda Wang <fundawang@mandriva.org> 1.7.2-1mdv2008.1
+ Revision: 105530
- New version 1.7.2

* Sun Sep 02 2007 Funda Wang <fundawang@mandriva.org> 1.7-1mdv2008.0
+ Revision: 77744
- New version 1.7

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Wed Aug 22 2007 Adam Williamson <awilliamson@mandriva.com> 1.6-2mdv2008.0
+ Revision: 68817
- add a bunch of missing files

* Fri Aug 17 2007 Adam Williamson <awilliamson@mandriva.com> 1.6-1mdv2008.0
+ Revision: 64688
- try to fix icon
- Fedora license policy
- new release 1.6

* Wed Jun 20 2007 Adam Williamson <awilliamson@mandriva.com> 1.5.9-1mdv2008.0
+ Revision: 41673
- new release 1.5.9; drop X-Mandriva menu category

* Thu May 17 2007 Adam Williamson <awilliamson@mandriva.com> 1.5.7-1mdv2008.0
+ Revision: 27697
- Import manslide
