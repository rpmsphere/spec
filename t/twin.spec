%undefine _debugsource_packages

Summary:        A text mode Windows Manager
Name:           twin
Version:        0.9.0
Release:        1
License:        GPLv2
Group:          Terminals
URL:            https://sourceforge.net/projects/twin/
Source0:        https://downloads.sourceforge.net/twin/%{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  gpm-devel
#BuildRequires: libggi-devel
BuildRequires:  ncurses-devel
BuildRequires:  libX11-devel
BuildRequires:  libXpm-devel

%description
Twin is a text-mode windowing environment.
It draws and manages text windows on a text-mode display,
like X11 does for graphical windows. It has a built-in window manager
and terminal emulator, and can be used as server for remote clients
in the same style as X11. It can display on Linux console, on X11
and inside itself.

%package devel
Summary:        Devellopment files from twin
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description devel
Twin is a text-mode windowing environment.
You need this package to build twin applications.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure \
        --enable--shlibs=yes \
        --enable--modules=yes \
        --enable--unicode=yes \
        --enable--asm=yes
make

%install
%makeinstall

%files
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/%{name}.*
%{_datadir}/%{name}
%{_libdir}/*.so.*
%{_libdir}/twin

%files devel
%{_includedir}/Tw
%{_includedir}/Tutf
%{_libdir}/*.so
%{_libdir}/*.a

%changelog
* Sun Jul 23 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.0
- Rebuilt for Fedora
* Wed Aug 21 2013 wally <wally> 0.6.2-5.mga4
+ Revision: 468862
- drop major from devel pkg name
* Mon Jan 14 2013 umeabot <umeabot> 0.6.2-4.mga3
+ Revision: 384923
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu Sep 29 2011 fwang <fwang> 0.6.2-3.mga2
+ Revision: 150246
- tighten br
* Tue Apr 19 2011 ennael <ennael> 0.6.2-2.mga1
+ Revision: 88303
- fix build require
- clean spec file
- imported package twin
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.2-2mdv2011.0
+ Revision: 615280
- the mass rebuild of 2010.1 packages
* Mon Feb 15 2010 Shlomi Fish <shlomif@mandriva.org> 0.6.2-1mdv2010.1
+ Revision: 506241
- Upgrade twin to version 0.6.2
* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.6.0-3mdv2010.0
+ Revision: 445570
- rebuild
* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-2mdv2009.0
+ Revision: 269443
- rebuild early 2009.0 package (before pixel changes)
  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
* Fri Jun 06 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-1mdv2009.0
+ Revision: 216301
- update to new version 0.6.0
- drop not needed patch
- spec file clean
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - BR gtk-devel & xpm-devel
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
  + Olivier Thauvin <nanardon@mandriva.org>
    - Import twin
* Mon Nov 01 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.4.6-5mdk
- fix build with new autotools
- add BuildRequires: X11-devel libgtk+-devel libgpm-devel libggi-devel
* Sat Aug 30 2003 Marcel Pol <mpol@gmx.net> 0.4.6-4mdk
- buildrequires bison
* Sun May 25 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4.6-3mdk
- distlint again
* Thu May 01 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4.6-2mdk
- distlint fix
* Mon Mar 31 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4.6-1mdk
- 2.4.6
* Wed Feb 26 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4.5-2mdk
- fix configure
* Tue Feb 25 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.4.5-1mdk
- First mdk package
