%undefine _debugsource_packages

Name:           xtexit
BuildRequires:  libX11-devel, libXt-devel, libXaw-devel, imake
License:        X11/MIT
Group:          System/X11/Utilities
Requires:       Xaw3d
Version:        0.42
Release:        2478.1
Summary:        Prompt on exiting X
Source:         xtexit.tar.gz
Patch0:         xtexit.dif
Patch1:         xtexit-Imakefile_comments.dif
%define _x11data    %{_datadir}/X11
%define _appdefdir  %{_x11data}/app-defaults

%description
`xtexit` sends an request to all clients to shut down. If the
application still needs an user interaction (e.g., if a file should be
saved) this is possible.

If you answer by the affirmative, all applications will be closed. This
method is not fully waterproof, but better than killing each and every
client without being able to interfere.

xterm applications anyway are killed immediately!

If this package is installed, it will be automatically integrated into
the sample user fvwm menu.

Authors:
--------
    Klaus Franken <kfr@suse.de>
    Teemu Torma, Front End Oy <tot@frend.fi>
    Paul Raines <raines@slac.stanford.edu>

%prep
%setup -q -n xtexit
%patch 0
%patch 1

%build
xmkmf -a
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
%if %{fedora}<21
mkdir -p $RPM_BUILD_ROOT/usr/share/X11/app-defaults
mv $RPM_BUILD_ROOT/usr/lib/X11/app-defaults/* $RPM_BUILD_ROOT/usr/share/X11/app-defaults
%endif
rm -rf $RPM_BUILD_ROOT/usr/lib

%files
%doc README README.SuSE
%{_bindir}/xtexit
%config %{_appdefdir}/XTexit

%changelog
* Tue Sep 27 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.42
- Rebuilt for Fedora
* Wed Aug  2 2006 werner@suse.de
- Make it build with X11R7
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon May 10 2004 hmacht@suse.de
- added #norootforbuild in specfile
* Fri Jun 13 2003 coolo@suse.de
- use BuildRoot
* Tue Jan 14 2003 pmladek@suse.cz
- fixed comments prefix in the Imakefile from "/**/#" to "XCOMM"
* Tue Sep 17 2002 ro@suse.de
- removed bogus self-provides
* Thu Dec 14 2000 werner@suse.de
- Group tag
* Wed May 31 2000 ro@suse.de
- specfile cleaned, doc relocation
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
