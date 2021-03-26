%global debug_package %{nil}

Name:		swm
Version:	1.3.4c
Release:	15.1
License:	GPL
URL:		http://www.small-window-manager.de/
Source0:	http://www.small-window-manager.de/%{name}-%{version}-src.tgz
BuildRequires:	libX11-devel
BuildRequires:	libXpm-devel
Group:		Graphical desktop/Other
Summary:	A small window manager for X11

%description 
Swm is a small window manager for X11 designed for very small laptop-screens
with a resolution of 640x400 pixels and above. (Or with PDA-mode 
320x240) SWM is even smaller than a rxvt!

%prep
%setup -q -n swm-1.3.4
sed -i -e 's|/usr/X11R6|/usr|' -e '/wmsession.d/d' src/Makefile-xpm

%build
make -C src -f Makefile-xpm

%install
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc

make INSTALLROOT=$RPM_BUILD_ROOT install -C src -f Makefile-xpm
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT%{_mandir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/xsessions
cat << EOF > $RPM_BUILD_ROOT%{_datadir}/xsessions/swm.desktop
[Desktop Entry]
Encoding=UTF-8
Name=sWM
Comment=Small Window Manager
TryExec=swm
Exec=startswm
Type=Xsession
EOF

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/doc/*
%{_datadir}/xsessions/%{name}.desktop
%{_datadir}/%{name}

%changelog
* Mon Jan 20 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.4c
- Rebuild for Fedora
* Fri Oct 18 2013 umeabot <umeabot> 1.2.5-12.mga4
+ Revision: 521272
- Mageia 4 Mass Rebuild
* Sat Jan 19 2013 fwang <fwang> 1.2.5-11.mga3
+ Revision: 389792
- cleanup spec
  + umeabot <umeabot>
    - Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Wed Feb 02 2011 dmorgan <dmorgan> 1.2.5-10.mga1
+ Revision: 46421
- imported package swm
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 1.2.5-10mdv2011.0
+ Revision: 634642
- bunzip2 the patch
- fix linkage
- turn to regular prefix
* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 1.2.5-9mdv2010.0
+ Revision: 434250
- rebuild
* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 1.2.5-8mdv2009.0
+ Revision: 261308
- rebuild
* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.2.5-7mdv2009.0
+ Revision: 253946
- rebuild
- kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Wed Dec 12 2007 Thierry Vignaud <tv@mandriva.org> 1.2.5-5mdv2008.1
+ Revision: 118961
- buildrequires X11-devel instead of XFree86-devel
- use %%mkrel
- import swm
* Thu Feb 26 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2.5-5mdk
- own %%datadir/swm
* Sat Sep 06 2003 Marcel Pol <mpol@gmx.net> 1.2.5-4mdk
- buildrequires
* Sun Jul 13 2003 Per Řyvind Karlsen <peroyvind@sintrax.net> 1.2.5-3mdk
- cosmetics
- rebuild
- quiet setup
- use $RPM_OPT_FLAGS
* Wed Oct 17 2001 Daouda LO <daouda@mandrakesoft.com> 1.2.5-2mdk
- s/Copyright/License
- right permissions on file 
* Sun Sep  2 2001 Daouda LO <daouda@mandrakesoft.com> 1.2.5-1mdk
- release 1.2.5
* Wed Apr 11 2001  Daouda Lo <daouda@mandrakesoft.com> 1.2.4-2mdk
- add Wmsession . 
* Wed Apr 11 2001  Daouda Lo <daouda@mandrakesoft.com> 1.2.4-1mdk
- release ( bug fixes )
*Thu Feb 01 2001 Daouda Lo <daouda@mandrakesoft.com> 1.2.2-1mdk
- first mdk release  
