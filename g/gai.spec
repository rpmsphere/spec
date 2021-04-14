Name:		gai
Version:	0.5.10
Release:	33.4
Summary:	Generic Applet Interface
Group:		User Interface/Desktops
License:	LGPLv2+
URL:		http://gai.sourceforge.net
Source0:	http://download.sf.net/gai/gai-%{version}.tar.bz2
Patch0:		gai-0.5.9-pkgconfig.patch
Patch1:		gai-0.5.10-nls.patch
Patch2:		gai-0.5.10-xorg.patch
Patch3:		gai-0.5.10-build.patch
Patch4:		gai-0.5.10-exit.patch
# work around the dropped libgnomeui-2.0 dependency in libpanelapplet-2.0.pc
Patch5:		gai-0.5.10-gnome-panel-2.25.patch
BuildRequires:  libpng-devel
BuildRequires:	libgnomeui-devel, mate-panel-devel, sane-backends-devel
BuildRequires:	SDL-devel, gtkglext-devel, gettext, xorg-x11-proto-devel
BuildRequires:	w3m, fedora-logos, udisks2

%package	devel
Summary:	Library and headers for Generic Applet Interface
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig, mate-panel-devel
Requires:	libgnomeui-devel, gtkglext-devel, xorg-x11-proto-devel

%description
This library provides a generic interface for developing applets for Gnome 2
and Windowmaker(Dockapps).

This is the package required to run precompiled GAI applets.

%description devel
This library provides a generic interface for developing applets for Gnome 2
and Windowmaker.

You should install the gai-devel package if you would like to compile
GAI applets.

%prep
%setup -q
%patch0 -p1 -b .pkgconfig
%patch1 -p1 -b .nls
%patch2 -p1 -b .xorg
%patch3 -p1 -b .build
%patch4 -p1 -b .exit
%patch5 -p1 -b .gnome-panel-2.25

%build
export CFLAGS="-fPIC $RPM_OPT_FLAGS -Wno-format-security"
%configure --disable-rox
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%doc AUTHORS BUGS COPYING.LIB ChangeLog README* THANKS TODO WINDOWMANAGERS
%{_libdir}/libgai.so.*

%files devel
%doc docs/*
%{_includedir}/gai/
%{_libdir}/pkgconfig/*
%{_libdir}/libgai.so

%changelog
* Wed May 18 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.10
- Rebuilt for Fedora
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Tue Feb  3 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5.10-17
- Patch to make build with gnome-panel >= 2.25, which drops the
  libgnomeui-2.0 dependency from libpanelapplet-2.0.pc
* Sat Dec 13 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5.10-16
- Rebuild to get automatic pkgconfig(..) Requires.
* Thu Aug  7 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.5.10-15
- Fix one segfault-on-exit situation.
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.5.10-14
- Autorebuild for GCC 4.3
* Fri Jan 18 2008 Michel Salim <michel.sylvan@gmail.com> - 0.5.10-13
- Rebuilt for Fedora 9 (development tree)
* Mon Oct 15 2007 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.5.10-12
- Patch gai/Makefile.in CFLAGS to find PangoFT2.
* Mon Sep 17 2007 Michel Salim <michel.sylvan@gmail.com> - 0.5.10-11
- License field updated
* Sun Jan 21 2007 Michel Salim <michel.salim@gmail.com>
- Remove unnecessary BR on mesa-libGLU-devel (added to gtkglext-devel)
* Sat Jan  6 2007 Michel Salim <michel.salim@gmail.com>
- Use -fPIC on all architecture (bz #220993, fix by Michael Schwendt)
* Mon Oct 02 2006 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt
* Tue Sep 19 2006 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt
* Thu Mar  2 2006 Michel Salim <michel.salim@gmail.com> - 0.5.10-6
- Rebuilt for Fedora Extras 5
* Mon Jan 30 2006 Michel Salim <michel.salim[AT]gmail.com> - 0.5.10-5
- regenerate configure to account for modular xorg's location change
- BuildReq changes: removed implicit dependencies, added xorg-x11-proto-devel and mesa-libGLU-devel that are now no longer pulled in
* Wed Aug 17 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.5.10-4
- rebuilt
* Tue Jun 28 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- remove work-around from 0.5.10-3 again, bug has been fixed
* Tue Jun 28 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.5.10-3
- temporarily add BR libpng-devel to work around a broken
  cairo-devel package, which is pulled in and breaks the pkg-config
  dependency chain (#161688)
* Tue Jun 28 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.5.10-2
- Fix NLS detection. Fix dgettext detection for 64-bit.
* Tue Jun 28 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.5.10-1
- Update to 0.5.10, as preferences dialog was broken in 0.5.9.
- BR gettext, and pull in first .mo with %%find_lang macro
- obsolete patches: multilib, gcc4
* Sun Jun 12 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.5.8-9
- Fix libdir and includedir in pkgconfig file.
- Disable ROX panel support explicitly.
- Install cleanly via DESTDIR.
* Fri Apr  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.5.8-8
- Include gai headers directory.
* Sun Mar 20 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.5.8-7
- Fix lvalue assignment errors for GCC4.
* Sun Mar 20 2005 Fabrice Colin <fabrice.colin[AT]gmail.com> - 0.5.8-6
- Make gai.pc multilib friendly so that 'pkg-config --exists gai' 
  doesn't fail on x86_64.
* Sun Mar 13 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.5.8-5
- Really add gtkglext-devel dependencies (Fabrice Colin).
* Sun Feb 27 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.5.8-4
- licence LGPL
- BR SDL-devel gtkglext-devel
* Tue Feb 25 2005 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.5.8-3
- add multilib-patch
- compile with -fPIC on x86_64
* Mon Nov 22 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0.5.8-2
- s/gnome-panel/gnome-panel-devel/g for FC2.
* Sat Nov  6 2004 Michel Alexandre Salim <michel.salim@gmail.com> - 0.5.8-0.fdr.1
- Updated to latest release
* Fri Oct 31 2003 Michel Alexandre Salim <salimma[AT]users.sf.net> - 0.5.0-0.fdr.0.4.pre4
- BuildRequires: gnome-panel added
* Thu Oct 30 2003 Michel Alexandre Salim <salimma[AT]users.sf.net> - 0.5.0-0.fdr.0.3.pre4
- Added missing dependency on libgnomeui-devel (bad gnome-panel dep)
- Minimum version specified for gtk2
* Wed Oct 29 2003 Michel Alexandre Salim <salimma[AT]users.sf.net> - 0.5.0-0.fdr.0.2.pre4
- Added dependencies to gai-devel
- Removed unnecessary macros from URLs
- Moved libgai.so to -devel
* Tue Oct 28 2003 Michel Alexandre Salim <salimma[AT]users.sf.net> - 0.5.0-0.fdr.0.1.pre4
- Fixed broken library naming (thanks Michael Schwendt)
* Mon Oct 27 2003 Michel Alexandre Salim <salimma[AT]users.sourceforge.net> - 0.5.0-0.fdr.0.pre4
- Update to 0.5.0pre4; API change between 0.4.x and 0.5.0.
- Most GAI applets now developed for 0.5.0, since 0.4.1 is not in Fedora yet one might as well move to 0.5.0 now.
* Tue May 13 2003 Michel Alexandre Salim <salimma[AT]users.sourceforge.net> - 0.4.1-0.fdr.1
- Adapted from upstream spec
