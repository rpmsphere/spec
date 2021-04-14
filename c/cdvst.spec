Summary:	Certain Death via Space Things
Name:		cdvst
Version:	0.18
Release:	20.4
Source0:	http://kokido.sourceforge.net/%{name}-.18.tar.bz2
Source1:	%{name}-icons.tar.bz2
Patch0:		%{name}-optflags.patch
Patch1:		%{name}-shared.patch
License:	GPL
URL:		http://kokido.sourceforge.net/cdvst.html
Group:		Games/Arcade
BuildRequires:	SDL_mixer-devel SDL_image-devel
BuildRequires:  desktop-file-utils

%description
The space things will certainly kill you :)
A top down scrolling putting you in the pilot seat of a space fighter.
Reminiscent of many old arcade games.
 
%prep
%setup -q -n %{name}-.18

%patch0 -p0
%patch1 -p0

%build
%__make OPTFLAGS="$RPM_OPT_FLAGS -lm" DATA_PREFIX=%{_datadir}/%{name}/

%install
install -m755 cdvst -D $RPM_BUILD_ROOT%{_bindir}/%{name}
chmod 644 readme.txt data/*
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a data $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=CDvST
Comment=%{Summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

install -d ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/{16x16,32x32,48x48}/apps
tar -xOjf %{SOURCE1} icons/16x16.png > ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
tar -xOjf %{SOURCE1} icons/32x32.png > ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
tar -xOjf %{SOURCE1} icons/48x48.png > ${RPM_BUILD_ROOT}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Jul 24 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.18
- Rebuilt for Fedora

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.18-11mdv2011.0
+ Revision: 616992
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.18-10mdv2010.0
+ Revision: 424793
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.18-9mdv2009.0
+ Revision: 243471
- rebuild
- drop old menu
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.18-7mdv2008.1
+ Revision: 136291
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import cdvst

* Mon Sep 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.18-7mdv2007.0
- XDG

* Thu Jan 05 2005 Lenny Cartier <lenny@mandriva.com> 0.18-6mdk
- rebuild

* Mon Nov 15 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.18-5mdk
- rebuild

* Sat Aug 02 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.18-4mdk
- dos2unix P1 (dunno *why* this patch got b0rked!!! weeeird)

* Sun Jul 13 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.18-3mdk
- change summary macro to avoid possible conflicts if we were to build
  debug package

* Fri Mar 14 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.18-3mdk
- added libSDL_image-devel to BuildRequires
- bzip2 sources

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com 0.18-2mdk
- rebuild

* Thu Nov 14 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.18-1mdk
- from Per Øyvind Karlsen <peroyvind@delonic.no> :
	- First release
