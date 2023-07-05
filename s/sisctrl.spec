Name:           sisctrl
BuildRequires:  libpng-devel
BuildRequires:  libXxf86vm-devel, libXv-devel, gtk2-devel pkgconfig
URL:            https://www.winischhofer.net/
License:        GPL v2 or later
Group:          System/X11/Utilities
Version:        0.0.20051202
Release:        461.1
Summary:        SiS Display Control Panel
Source:         %name-%version.tar.gz
Patch:          sisctrl.diff

%description
Utility to set some display properties during server runtime.

Authors:
--------
    Thomas Winischhofer <thomas@winischhofer.net>

%prep
%setup -q
%patch
sed -i 's|gdk-pixbuf-xlib|gdk-pixbuf|g' src/sisctrl_stray.c

%build
autoreconf -fi
export LDFLAGS=-lm
./configure --prefix=/usr \
            --mandir=%{_mandir} \
            --with-xv-path=%{_libdir}
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/sisctrl
%{_mandir}/man1/sisctrl.1x.*

%changelog
* Thu Sep 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.20051202
- Rebuilt for Fedora
* Tue Mar 10 2009 sndirsch@suse.de
- define functions, which don't return anything, as void
  (bnc #483401)
* Tue Nov  7 2006 sndirsch@suse.de
- added missing return value (Bug #218755)
* Sun Jul 23 2006 sndirsch@suse.de
- fixed build for X.Org 7
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Dec  5 2005 sndirsch@suse.de
- update to 2005-12-02 version
* Wed Nov 30 2005 sndirsch@suse.de
- created package
