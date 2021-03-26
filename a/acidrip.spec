%global __requires_exclude	perl\\(AcidRip::.*\\)

Summary:	Simple GUI for MEncoder
Name:		acidrip
Version:	0.14
Release:	28.1
Source:		http://prdownloads.sourceforge.net/acidrip/%{name}-%{version}.tar.bz2
URL:		http://untrepid.com/acidrip
License:	GPLv2
Group:		Video/Editors and Converters
Patch0:		%{name}-0.14-xvid_options.patch
Patch1:		%{name}-0.14-mencoder.patch
Patch2:		%{name}-0.14-gtk2.patch
BuildRequires:	lsdvd
#BuildRequires:	mencoder
BuildRequires:	perl-Gtk2
BuildRequires:	perl-devel
Requires:	lsdvd
Requires:	mencoder
Requires:	perl-Gtk2
BuildArch:	noarch

%description
AcidRip is a Gtk::Perl application for ripping and encoding DVD's. It neatly
wraps MPlayer and MEncoder, which I think is pretty handy, seeing as MPlayer
is by far the best bit of video playing kit around for Linux. As well as
creating a simple Graphical Interface for those scared of getting down and
dirty with MEncoders command line interface, It also automates the process in
a number of ways:
    * Parses DVD into contents tree
    * Finds longest title
    * Calculate video bitrate for given filesize
    * Finds black bands and crops them
    * Gives suggestions for improved performance
    * Other stuff!

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
sed -i -e '58,75d' -e 's/mp3lame/copy/g' Makefile.PL

%build
perl Makefile.PL
make
										
%install
%make_install INSTALLDIRS=vendor

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=AcidRip
Comment=Video ripping and conversion
Exec=%{name}
Icon=/usr/share/perl5/vendor_perl/AcidRip/logo.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Video;AudioVideo;AudioVideoEditing;GTK;
EOF

%files
%doc CHANGELOG COPYING TODO
%{_bindir}/%{name}
%{perl_vendorlib}/AcidRip
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%exclude %{_libdir}/perl5/perllocal.pod
%exclude %{_libdir}/perl5/vendor_perl/auto/AcidRip/.packlist

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.14
- Rebuild for Fedora
* Wed Oct 15 2014 umeabot <umeabot> 0.14-15.mga5
+ Revision: 742132
- Second Mageia 5 Mass Rebuild
  + tv <tv>
    - fix excludes
* Tue Sep 16 2014 umeabot <umeabot> 0.14-14.mga5
+ Revision: 677685
- Mageia 5 Mass Rebuild
  + tv <tv>
    - use %%global for req/prov exclude
    - autoconvert to new prov/req excludes
* Fri Oct 18 2013 umeabot <umeabot> 0.14-13.mga4
+ Revision: 502445
- Mageia 4 Mass Rebuild
* Fri Jan 11 2013 umeabot <umeabot> 0.14-12.mga3
+ Revision: 345223
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Wed Dec 26 2012 pterjan <pterjan> 0.14-11.mga3
+ Revision: 335272
- Revert dependency changes, the problem with mplayer is from libffi
- Fix license
- Fix group
- fix dependencies, it needs both mencoder and mplayer
* Sun May 15 2011 pterjan <pterjan> 0.14-10.mga1
+ Revision: 98912
- Rebuild for fixed find-requires
* Mon Apr 25 2011 wally <wally> 0.14-9.mga1
+ Revision: 90216
- change .desktop file name (mga#954)
- add requires exceptions for self provided perl modules
* Thu Apr 14 2011 ennael <ennael> 0.14-8.mga1
+ Revision: 85518
- clean spec file
- imported package acidrip
* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 0.14-8mdv2010.0
+ Revision: 423862
- rebuild
* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.14-7mdv2009.0
+ Revision: 218436
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.14-7mdv2008.1
+ Revision: 135813
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'
* Fri Jul 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.14-7mdv2008.0
+ Revision: 56365
- provide Gtk2 patch
* Mon Jul 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.14-6mdv2008.0
+ Revision: 52453
- provide patch 0 (default xvid options)
- provide patch 1 (mencoder new crop syntax)
- drop old menu style
- remove X-MandrivaLinux from desktop file
- Import acidrip
* Wed Aug  2 2006 Götz Waschk <waschk@mandriva.org> 0.14-5mdv2007.0
- xdg menu
* Tue Jun 27 2006 Lenny Cartier <lenny@mandriva.com> 0.14-4mdv2007.0
- rebuild
* Fri Feb 17 2006 Götz Waschk <waschk@mandriva.org> 0.14-3mdk
- fix installation
* Tue Nov 16 2004 Götz Waschk <waschk@linux-mandrake.com> 0.14-2mdk
- fix provides
* Mon Nov 15 2004 Götz Waschk <waschk@linux-mandrake.com> 0.14-1mdk
- fix URL
- new version
* Tue Jan 27 2004 Götz Waschk <waschk@linux-mandrake.com> 0.12-1mdk
- new version
* Tue Nov 11 2003 Götz Waschk <waschk@linux-mandrake.com> 0.11-1mdk
- this one needs perl-Gtk2
- new version
* Wed Jul 16 2003 Götz Waschk <waschk@linux-mandrake.com> 0.9-3mdk
- fix buildrequires again
* Tue Jul 15 2003 Götz Waschk <waschk@linux-mandrake.com> 0.9-2mdk
- fix buildrequires
* Mon Jun 2 2003 Austin Acton <aacton@yorku.ca> 0.9-1mdk
- 0.9
* Fri May 30 2003 Austin Acton <aacton@yorku.ca> 0.8-1mdk
- initial package
