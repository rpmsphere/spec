Summary:	Desktop background manager/changer/screensaver
Name:		chbg
Version:	2.0.1
Release:	29.1
License:	GPLv2+
Group:		Graphics/Utilities
URL:		http://www.beebgames.com/sw/gtk-ports.html
Source0:	http://www.beebgames.com/sw/%{name}-%{version}.tar.bz2
Source1:	%{name}_16x16.png
Source2:	%{name}_32x32.png
Source3:	%{name}_48x48.png
# (fc) 2.0.1-3mdv use correct colormap / depth 
Patch0:		chbg-2.0.1-colormap.patch
# (fc) 2.0.1-9mdv fix CFLAGS
Patch1:		chbg-2.0.1-cflags.patch
Patch2:		chbg-2.0.1-libpng1.5.patch
Patch3:		chbg-2.0.1-link.patch
BuildRequires:	gettext-devel
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires:	libpng-devel

%description
ChBg is for changing desktop backgrounds in a given period. It can
render images with 10 modes (such as tiled, centered, scaled, etc.). It
uses gdk_pixbuf-2.0 for loading images, so it supports many image formats. 
ChBg has a windowed setup program, is able to load setup files, 
can be used as slideshow picture previewer in its own window or as a
desktop background, and can be used as screensaver or as an xscreensaver
hack. It has a dialog for fast previewing of pictures and very usable
thumbnail previews.

%prep
%setup -q
%patch0 -p1 -b .composite
%patch1 -p1 -b .cflags
%patch2 -p0 -b .libpng
%patch3 -p0 -b .link

%build
autoreconf -fi
%configure --with-intl-includes=%{_datadir}/gettext/intl
make

%install
%makeinstall

# install icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48}/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

# menu stuff
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=ChBg
Comment=Desktop background manager/changer/screensaver
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Settings;DesktopSettings;
EOF

# touch the default sysconfig file so that it can be included
mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/chbgrc

%{find_lang} %{name}

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog README THANKS TODO chbgrc.sample xscreensaver*txt 
%{_bindir}/chbg
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man*/*
%attr(644,root,root) %config(noreplace,missingok) %{_sysconfdir}/chbgrc

%changelog
* Sun Jul 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.1
- Rebuilt for Fedora
* Mon Jun 03 2013 fwang <fwang> 2.0.1-19.mga4
+ Revision: 435803
- more linkage fix
- fix linkage
- rebuild for new libpng
* Fri Jan 11 2013 umeabot <umeabot> 2.0.1-18.mga3
+ Revision: 347639
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Tue Jan 08 2013 barjac <barjac> 2.0.1-17.mga3
+ Revision: 343254
- update group - again
* Sun Dec 30 2012 barjac <barjac> 2.0.1-16.mga3
+ Revision: 336451
- update group
- update .desktop
- minor spec clean
* Mon Jul 30 2012 sander85 <sander85> 2.0.1-15.mga3
+ Revision: 276172
- Fix build
* Wed Sep 14 2011 fwang <fwang> 2.0.1-14.mga2
+ Revision: 143160
- rebuild for new libpng
* Sun Jan 23 2011 ahmad <ahmad> 2.0.1-13.mga1
+ Revision: 34847
- drop old/unneeded scriptlets
- imported package chbg
