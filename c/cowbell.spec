Name: 	 	cowbell
Summary: 	Music collection organizer and editor
Version: 	0.2.7.1
Release: 	12.1
Source:		https://more-cowbell.org/releases/%{name}-%{version}.tar.bz2
URL:		https://more-cowbell.org/
License:	GPLv2+
Group:		Productivity/Multimedia
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
BuildRequires:	mono-devel gtk-sharp2-devel
BuildRequires:	taglib-devel
BuildRequires:  perl(XML::Parser)
BuildRequires:  desktop-file-utils

%description
Do you ever pull your hair out trying to hand-edit all your tags with some
arcane editor? Tell your inner OCD to take a hike because Cowbell is coming
to town.

Cowbell is an elegant music organizer intended to make keeping your
collection tidy both fun and easy.

Infused with Amazon Web Services SOAP-fu, Cowbell can whip your music
platoon into shape without even getting your boots muddy. And, if that isn't
enough to make you want to rush to the Download link, Cowbell can also
snatch album art and rename your music files like a pro.

%prep
%setup -q

%build
perl -p -i -e 's/lib\/cowbell/%{_lib}\/cowbell/g' Makefile* cowbell.in
%configure
make
										
%install
rm -rf $RPM_BUILD_ROOT
%make_install

desktop-file-install --vendor="" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%name
%{_libdir}/%name
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*

%changelog
* Sun Nov 18 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.7.1
- Rebuilt for Fedora
* Mon Feb 01 2010 JÃ©rÃŽme Brenier <incubusss@mandriva.org> 0.2.7.1-8mdv2010.1
+ Revision: 499152
- fix path in cowbell.in too
- do path fixes before configure
* Sun Jan 31 2010 JÃ©rÃŽme Brenier <incubusss@mandriva.org> 0.2.7.1-7mdv2010.1
+ Revision: 498916
- fix License tag
* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.2.7.1-6mdv2010.0
+ Revision: 425049
- rebuild
  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick
* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2.7.1-5mdv2009.0
+ Revision: 243689
- rebuild
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Fri Feb 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.2.7.1-3mdv2008.1
+ Revision: 168999
- rebuild
  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.2.7.1-2mdv2008.1
+ Revision: 136345
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import cowbell
* Wed Sep 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.7.1-2mdv2007.0
- XDG
* Wed May 24 2006 Austin Acton <austin@mandriva.org> 0.2.7.1-1mdk
- New release 0.2.7.1
* Wed May 03 2006 Emmanuel Andry <eandry@free.fr> 0.2.7-1mdk
- New release 0.2.7
* Fri Mar 03 2006 Austin Acton <austin@mandriva.org> 0.2.6.1-1mdk
- New release 0.2.6.1
* Sat Dec 17 2005 Austin Acton <austin@mandriva.org> 0.2.5.1-1mdk
- New release 0.2.5.1
* Fri Nov 18 2005 Austin Acton <austin@mandriva.org> 0.2.5-2mdk
- fix buildreuires
- lib64 fix
* Fri Nov 18 2005 Austin Acton <austin@mandriva.org> 0.2.5-1mdk
- New release 0.2.5
* Thu Oct 06 2005 Austin Acton <austin@mandriva.org> 0.2.4-1mdk
- New release 0.2.4
* Wed Sep 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.3-3mdk
- Fix BuildRequires
* Thu Aug 25 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.2.3-2mdk
- rebuild for new gtk-sharp2
* Sat Aug 13 2005 Austin Acton <austin@mandriva.org> 0.2.3-1mdk
- New release 0.2.3
* Mon Aug 8 2005 Austin Acton <austin@mandriva.org> 0.2.2-1mdk
- 0.2.2
- source URL
* Sun Jul 24 2005 Austin Acton <austin@mandriva.org> 0.2-1mdk
- initial package
