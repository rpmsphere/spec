Name:           xtermset
License:        GPL v2 or later; X11/MIT
Group:          System/X11/Terminals
Summary:        A program to change the settings of an xterm
Version:        0.5.2
Release:        526.1
URL:            https://sourceforge.net/projects/clts/
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}.dif
Patch1:         %{name}-%{version}-strcat.patch
Patch2:         %{name}-%{version}-dash.patch

%description
Xtermset allows you to change the characteristics of an xterm window
from the command line. Most options have the same names as those that
you would give an xterm at startup.



Authors:
--------
    Breyten Ernsting <bje@dds.nl>
    Decklin Foster <decklin@home.com>

%prep
%setup -q
%patch 0
%patch 1
%patch 2

%build
aclocal
automake -a
autoconf
CFLAGS="$RPM_OPT_FLAGS" ./configure \
                        --prefix=/usr \
                        --mandir=%{_mandir}
make

%install
rm -rf  $RPM_BUILD_ROOT
make "DESTDIR=$RPM_BUILD_ROOT" install

%files
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
/usr/bin/xtermset
%{_mandir}/man?/*
/usr/share/xtermset/

%changelog
* Mon Sep 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.2
- Rebuilt for Fedora

* Wed Aug 30 2006 anosek@suse.cz
- changed prefix /usr/X11R6 -> /usr

* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires

* Tue Nov  8 2005 dmueller@suse.de
- don't build as root

* Fri Jul 25 2003 postadal@suse.cz
- update to version 0.5.2
  * tiny bugs fixed

* Thu Mar 14 2002 pmladek@suse.cz
- fixed usage of strcat() to do not write outside of static strigs
- removed improper test on dash because some values in options
  can begin with dash, for example font name
- /usr/X11R6/share/xtermset is owned by this package now

* Fri Sep  7 2001 ro@suse.de
- added "-a" to automake

* Tue Mar 13 2001 cihlar@suse.cz
- update to version 0.5.1

* Tue Feb 13 2001 cihlar@suse.cz
- fixed limits of switches and fn

* Wed Nov 22 2000 cihlar@suse.cz
- update to version 0.5
- added suse_update_config

* Thu Apr 27 2000 cihlar@suse.cz
- added BuildRoot

* Thu Oct 21 1999 kukuk@suse.de
- Update to version 0.4

* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.

* Tue Apr 27 1999 kukuk@suse.de
- Spec file created from xtermset-0.3.tar.gz by autospec
