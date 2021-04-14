Name:           xselection
URL:            http://sunsite.mff.cuni.cz/MIRRORS/ftp.xfree86.org/pub/mirror/X.Org/R5contrib/
BuildRequires:  libX11-devel, libXext-devel, imake
License:        MIT
Group:          System/X11/Utilities
Summary:        Manipulate the XSelection
Version:        1.6.1
Release:        1597.1
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}.patch
Patch1:         %{name}-%{version}-qt.patch
Patch2:         %{name}-%{version}-help.patch
Patch3:         %{name}-%{version}-warnings.patch
%define _xorg7libs %_lib
%define _xorg7libs32 lib
%define _xorg7bin bin
%define _xorg7_mandir %_mandir
%define _xorg7pixmaps include
%define _xorg7libshare share
%define _xorg7_xkb /usr/share/X11/xkb
%define _xorg7_termcap /usr/lib/X11/etc
%define _xorg7_serverincl /usr/include/xorg
%define _xorg7_fonts /usr/share/fonts
#%define _xorg7_config /usr/share/X11/config #use libshare macro
%define _xorg7_prefix /usr

%description
With this little tool, pipe the currently selected text under X into a
file or vice versa.

Help can be found by reading the man page with
man xselection

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3

%build
xmkmf -a
make %{?jobs:-j%jobs} CCOPTIONS="$RPM_OPT_FLAGS"

%install
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man
%if %{fedora}<21
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1
mv $RPM_BUILD_ROOT/usr/man/man1/* $RPM_BUILD_ROOT/usr/share/man/man1
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/%{_xorg7bin}/xselection
%doc %{_xorg7_mandir}/man1/xselection.1x.gz

%changelog
* Thu Sep 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.1
- Rebuilt for Fedora
* Mon Nov  8 2010 coolo@novell.com
- remove support for pre-9.1
* Fri Jul 28 2006 lmichnovic@suse.cz
- builds also with new X.org 7.x, detecting prefix in X.org
- building with icecream
- using RPM_OPT_FLAGS
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Apr 18 2005 ro@suse.de
- build with gcc-4
* Fri May  7 2004 hmacht@suse.de
- building as non-root user
* Fri Apr 16 2004 pmladek@suse.cz
- fixed some compiler warnings
* Fri Aug  9 2002 pmladek@suse.cz
- added help option which will be used by less mouse support
* Fri May 31 2002 pmladek@suse.cz
- fixed for qt (kde) applications where TARGETS request must be
  answered before the request on selected data
* Wed Oct 10 2001 pmladek@suse.cz
- renamed from xselect to xselection
- bzippped sources
- fixed copyright tag
- added BuildRoot
- cleaned up spec file
* Thu Mar  8 2001 uli@suse.de
- added # neededforbuild xf86
- added proper Group tag
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Wed Oct 29 1997 kgw@suse.de
- ready for autobuild
* Thu Jan  2 1997 maddin@suse.de
  first SuSE version
