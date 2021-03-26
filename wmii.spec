Summary: Window Manager Improved 2
Name: wmii
Version: 3.10
License: MIT
Release: 21.2
Group: Graphical desktop/Other
URL: http://wmii.suckless.org/
Source0: hg.suckless.org/wmii/archive/f3d88385ea7c.tar.gz
BuildRequires: freetype-devel
BuildRequires: cairo-devel
BuildRequires: Pyrex
BuildRequires: libX11-devel
BuildRequires: libXinerama-devel
BuildRequires: libXrandr-devel
BuildRequires: libXext-devel
BuildRequires: libixp-devel > 0.5
BuildRequires: python2-devel
Requires:	xterm
Requires:	xmessage

%description
WMii is a dynamic window manager for X11 hackers. It supports classic and tiled
window management with extended keyboard, mouse, and 9P-based remote control.
It consists of the wmii window manager and wmiir: the remote access utility.

%package python
Summary: Window Manager Improved 2 python files
Group: Graphical desktop/Other

%description python
Python files for %{name}.

%package devel
Summary: Window Manager Improved 2 devel files
Group: Development/C

%description devel
Development files for %{name}.

%prep
%setup -qn %{name}-f3d88385ea7c
sed -i 's|/usr/bin/env python|/usr/bin/python2|' alternative_wmiircs/python/*.py
sed -i \
    -e "/PYTHON/s|python|python2|" \
    -e "/^PREFIX/s|=.*|= /usr|" \
    -e "/ETC/s|=.*|= /etc/X11|" \
%ifarch x86_64 aarch64
    -e "s|/usr/lib|/usr/lib64|g" \
    -e "/ LIBDIR/s|=.*|= /usr/lib64|" \
%endif
    config.mk

%build
export LDFLAGS=-Wl,--allow-multiple-definition
make

%install
%makeinstall DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_includedir}/%{name}
find lib* -name '*.a' -exec cp {} %{buildroot}%{_libdir} \; -print
find lib* -name '*.h' -exec cp {} %{buildroot}%{_includedir}/%{name} \; -print

mkdir -p $RPM_BUILD_ROOT%{_datadir}/xsessions
cat > $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=WMII
Comment=Window Manager Improved 2
TryExec=%{name}
Exec=%{name}
Type=Xsession
EOF

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}/etc/X11/wmii-hg/python/wmiirc

%files
%doc LICENSE README FAQ
%{_docdir}/*
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%dir %_sysconfdir/X11/wmii-hg/
%attr(0755,root,root) %config(noreplace) %_sysconfdir/X11/%{name}-hg/*
%{_datadir}/xsessions/%{name}.desktop

%files python
%{python2_sitelib}/*

%files devel
%{_libdir}/*.a
%attr(0755,root,root) %{_libdir}/*.so
%{_includedir}/%{name}

%changelog
* Sat Nov 24 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 3.10
- Rebuild for Fedora
* Tue Oct 18 2011 Matthew Dawkins <mattydaw@mandriva.org> 3.10-0.b1.1mdv2012.0
+ Revision: 705294
- new version 3.10 b1 changeset f3d88385ea7c
  dropped wmipaper.pdf source
  patches 02, 03, & 04
  cleaned up spec
  fixed build for 64bit
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 3.6-8
+ Revision: 634813
- simplify BR
* Wed Oct 28 2009 Rémy Clouard <shikamaru@mandriva.org> 3.6-7mdv2010.0
+ Revision: 459793
- fix build due to libixp changes
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 3.6-5mdv2009.0
+ Revision: 262054
- rebuild
* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 3.6-4mdv2009.0
+ Revision: 256184
- rebuild
* Tue Jan 08 2008 Jérôme Soyer <saispo@mandriva.org> 3.6-2mdv2008.1
+ Revision: 146959
- Bump Release
- Fix Caps
- Fix sed
  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Thu Dec 13 2007 Jérôme Soyer <saispo@mandriva.org> 3.6-1mdv2008.1
+ Revision: 119211
- New release
- Add three patchs from debian
- Fix make and make install
- Disable parralel build
* Thu May 25 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 3-1mdv2007.0
- 3
* Sun May 14 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 3-0.rc5.1mdk
- 3 rc5
* Fri May 12 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 3-0.rc4.1mdk
- 3 rc4
* Tue May 09 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 3-0.rc3.1mdk
- 3 rc 3
* Sat May 06 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 3-0.rc2.1mdk
- 3 rc2
- rediff patch0
* Tue May 02 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 3-0.rc1.1mdk
- 3 rc1
- no more require 9base
* Tue Dec 06 2005 Antoine Ginies <aginies@mandriva.com> 0.20051114-4mdk
- fix x86_64 build
* Mon Dec 05 2005 Antoine Ginies <aginies@mandriva.com> 0.20051114-3mdk
- add buildrequires libxorg-x11-static-devel
* Mon Dec 05 2005 Antoine Ginies <aginies@mandriva.com> 0.20051114-2mdk
- add missing Buildrequires libxorg-x11-devel
* Mon Dec 05 2005 Antoine Ginies <aginies@.mandriva.com> 0.20051114-1mdk
- 20051114 release
- add 9base requires
* Wed Nov 30 2005 Antoine Ginies <aginies@n3.mandriva.com> 0.20050730-1mdk
- supposed stable release Boyd [2005-07-30]
- need to relocate all wmii scripts
* Fri May 27 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.20050526-1mdk
- initial contrib
