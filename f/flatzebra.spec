Name:		flatzebra
Version:	0.1.7
Release:	1
Summary:	A Generic Game Engine library for 2D double-buffering animation
Group:		System/Libraries
License:	GPLv2
URL:		https://sarrazip.com/dev/burgerspace.html
Source:		https://sarrazip.com/dev/%{name}-%{version}.tar.gz
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	zlib-devel
BuildRequires:	gcc-c++

%description
Generic Game Engine library suitable for BurgerSpace, Afternoon Stalker
and Cosmosmash.

%package devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
%ifarch aarch64
%configure
%else
./configure --prefix=/usr
%endif
make

%install
%__rm -rf $RPM_BUILD_ROOT
%makeinstall
%__rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING README INSTALL NEWS
%{_libdir}/lib*.so.*

%files devel
%dir %{_includedir}/%{name}-0.1
%{_includedir}/%{name}-0.1/%{name}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Sun Apr 25 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.7
- Rebuilt for Fedora
* Mon Mar 12 2012 Andrey Bondrov <abondrov@mandriva.org> 0.1.5-3mdv2012.0
+ Revision: 784453
- Rebuild to deal with .la issue, spec cleanup
* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 0.1.5-2mdv2011.0
+ Revision: 604386
- rebuild for zlib
* Wed Oct 13 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.1.5-1mdv2011.0
+ Revision: 585394
- new version
* Thu Apr 22 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.1.4-1mdv2010.1
+ Revision: 537779
- update to 0.1.4
* Sat Jul 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.3-2mdv2010.0
+ Revision: 399766
- obsoletes previous library package with wrong major
* Sat Jul 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.3-1mdv2010.0
+ Revision: 399695
- new version
- fix major number
- new devel policy
* Fri May 15 2009 Samuel Verschelde <stormi@mandriva.org> 0.1.2-1mdv2010.0
+ Revision: 376146
- fix buildrequires
- fix licence
- fix URL
- new version 0.1.2
  + Michael Scherer <misc@mandriva.org>
    - adapt gentoo patch to be able to properly regenerate autotools script, by
      hardcoding the needed library, and by removing unknows macros TRY_LINK*
    - regenerate autotools script so compilation do not fail with new libtool
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot
* Sun May 27 2007 Funda Wang <fwang@mandriva.org> 0.1.1-3mdv2008.0
+ Revision: 31751
- build against directfb 1.0
- Import flatzebra
* Thu May 05 2005 Marcel Pol <mpol@mandriva.org> 0.1.1-1mdk
- 0.1.1
- new SONAME
- move pkgconfig file to devel package
* Fri Jun 04 2004 Marcel Pol <mpol@mandrake.org> 0.1.0-5mdk
- rebuild
* Sat Sep 06 2003 Marcel Pol <mpol@gmx.net> 0.1.0-4mdk
- buildrequires
- devel package provides flatzebra-devel
* Wed Jul 16 2003 Marcel Pol <mpol@gmx.net> 0.1.0-3mdk
- rebuild for new rpm provides
- own dir
- formatting
* Thu Jun 12 2003 Marcel Pol <mpol@gmx.net> 0.1.0-2mdk
- buildrequires
* Tue Jun 03 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.1.0-1mdk
- new
