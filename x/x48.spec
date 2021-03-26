Name:		x48
Summary:	HP 48 GX emulator
Version:	0.6.4
Release:	13.1
License:	GPL
Group:		Sciences/Mathematics
URL:		http://x48.berlios.de/
Source0:	http://downloads.sourceforge.net/project/x48.berlios/%{name}-%{version}.tar.bz2
Source1:    x48.png
Patch0:		x48-0.6.1-mdv-fix-string-format.patch
BuildRequires:	readline-devel
BuildRequires:	libX11-devel libXt-devel
#BuildRequires:	x11-util-cf-files
BuildRequires:	ncurses-devel
Requires:  	readline
#Requires:  	x48-data

%description
This is an emulator of the HP 48 SX and GX calculator.
Romdumps are available from http://x48.berlios.de/

%prep
%setup -q -c
%patch0 -p1 -b .format
sed -i '698s|^inline int|static inline int|' src/emulate.c

%build
./autogen.sh
%configure --with-x
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/

cat << EOF > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Exec=x48 -rom /usr/share/x48/rom
Name=x48
Icon=x48
Comment=HP48 Emulator
Categories=Office;
EOF

install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

cat > README.urpmi << EOF
x48 needs a rom to function, so please read the README to see how to dump it
from your HP48 or just use the rpm x48-gxrom or x48-sxrom from plf.
If you dump the rom, please put it in the /usr/share/x48 directory.
***
The first time you launch x48, it will copy the rom to ~/.hp48.
So if you like to change from sx to gx rom, please remove this directory first
EOF

make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc README README.urpmi
#%{_sysconfdir}/X11/app-defaults/X48
%{_bindir}/checkrom
%{_bindir}/dump2rom
%{_bindir}/mkcard
%{_bindir}/x48
%{_datadir}/%{name}
%{_datadir}/X11/app-defaults/X48
%{_mandir}/man1/x48.*
%{_datadir}/applications/x48.desktop
%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Aug 06 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.4
- Rebuild for Fedora
* Tue Apr 03 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.6.4-1
+ Revision: 788981
- version update 0.6.4
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.3-2mdv2011.0
+ Revision: 615489
- the mass rebuild of 2010.1 packages
* Mon Mar 08 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.3-1mdv2010.1
+ Revision: 515650
- new upstream release 0.6.3
* Thu Dec 10 2009 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.1-1mdv2010.1
+ Revision: 476213
- Update to 0.6.1
- remove imake stuff, not needed any more
- add patch1 to fix string format
* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.4.3-10mdv2010.0
+ Revision: 445862
- rebuild
* Tue Mar 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4.3-9mdv2009.1
+ Revision: 347887
- rebuild for latest readline
* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.4.3-8mdv2009.0
+ Revision: 262225
- rebuild
* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.4.3-7mdv2009.0
+ Revision: 256558
- rebuild
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.4.3-5mdv2008.1
+ Revision: 171179
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix no-buildroot-tag
* Wed Jan 02 2008 Thierry Vignaud <tv@mandriva.org> 0.4.3-4mdv2008.1
+ Revision: 140791
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
  + Erwan Velu <erwan@mandriva.org>
    - Rebuild
    - Fixing buildrequires
    - Fixing buildrequires
    - Fixing buildrequires
    - Oups, %%files is wrong
    - /usr/X11R6 conflicts
    - Fixing buildrequires
    - Import x48
