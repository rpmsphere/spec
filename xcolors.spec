Name:           xcolors
BuildRequires:  libX11-devel, libXt-devel, libXaw-devel, imake
License:        Public Domain, Freeware
Group:          System/X11/Utilities
Version:        91.10.4
Release:        2458.1
Summary:        Displays colors defined in rgb.txt
Source:         xcolors-04oct91.tar.bz2
Patch0:         xcolors-04oct91.patch
Patch1:         xcolors-04oct91-xorg7_rgbtxt.patch
%define _xorg7libs %_lib
%define _xorg7libs32 lib
%define _xorg7bin bin
%define _xorg7_mandir %_mandir
%define _xorg7pixmaps include
%define _xorg7libshare share

%description
Xcolorsel displays colors defined in rgb.txt. You can create an RGB
file by redirecting the output of showrgb to a file.

%prep
%setup -q -n xcolors-04oct91
%patch0
%if "%(pkg-config --variable=prefix xft)" == "/usr"
%patch1
%endif

%build
xmkmf -a
make %{?jobs:-j%jobs} CCOPTIONS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man
%if %{fedora}<21
mkdir -p $RPM_BUILD_ROOT/usr/share/X11/app-defaults
mv $RPM_BUILD_ROOT/usr/lib/X11/app-defaults/* $RPM_BUILD_ROOT/usr/share/X11/app-defaults
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT%_datadir/man
%endif
rm -rf $RPM_BUILD_ROOT/usr/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/%{_xorg7bin}/xcolors
%config /usr/%{_xorg7libshare}/X11/app-defaults/Xcolors
%doc %{_xorg7_mandir}/man1/xcolors.1x.gz

%changelog
* Tue Sep 27 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 91.10.4
- Rebuild for Fedora
* Wed Nov 24 2010 ro@suse.de
- xft-config is gone
* Mon Nov  8 2010 coolo@novell.com
- remove support for pre-9.1
* Tue Aug 15 2006 lmichnovic@suse.cz
- changed path of file rgb.txt in X.org 7.x (xorg7_rgbtxt.patch)
* Tue Aug  8 2006 lmichnovic@suse.cz
- compiling with RPM_OPT_FLAGS
* Fri Jul 28 2006 lmichnovic@suse.cz
- builds also with new X.org 7.x, detecting prefix in X.org
- building with icecream
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Apr 22 2005 coolo@suse.de
- fix build
* Tue Jun  1 2004 hmacht@suse.de
- added # norootforbuild in specfile
* Wed May 19 2004 ro@suse.de
- added return value to non-void functions
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Thu Aug  9 2001 dan@suse.cz
- use bzip instead of gzip
* Thu May 11 2000 nadvornik@suse.cz
- added BuildRoot
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Mon Nov 24 1997 ro@suse.de
- ignore all lines starting with ! or # in rgb.txt
* Sun Jun  1 1997 bs@suse.de
- moved var/X11R6/lib/app-defaults to usr/X11R6/lib/X11/app-defaults
