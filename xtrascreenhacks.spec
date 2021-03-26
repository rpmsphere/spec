Name:           xtrascreenhacks
Version:        0.7
Release:        4.1
Summary:        Collection of openGL Screensavers
# http://home.comcast.net/~shegeek/xtrascreenhacks/xtrascreenhacks-%{version}.tar.gz
Source:         xtrascreenhacks-%{version}.tar.bz2
URL:            http://home.comcast.net/~shegeek/xtrascreenhacks/
Group:          Amusements/Toys/Screensavers
License:        GNU General Public License version 2 or later (GPL v2 or later)
BuildRoot:      %{_tmppath}/build-%{name}-%{version}
BuildRequires:  xscreensaver
BuildRequires:  bc
BuildRequires:  libX11-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  freeglut-devel
BuildRequires:  gtk2-devel
BuildRequires:  libglade2-devel
BuildRequires:  libxml2-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  xdg-utils
BuildRequires:  gcc make glibc-devel
BuildRequires:  autoconf automake libtool
Requires:       /usr/bin/xdg-open
Requires:       xscreensaver

%description
XtraScreenHacks is a collection of display modes that are based on and intended
to be run with the XScreensaver distribution. Requires Xlib and OpenGL.

Included screensavers:
* Skylark, the classic 1950s kitchen table top
* Soma, the 3d cube puzzle
* Berlin-Uhr, the Berlin Quantity Didactics Clock
* Flyer
* Daisy
* Twinkle

%prep
%setup -q

%build
CFLAGS="%{optflags} -DHAVE_SYS_WAIT_H"
%configure \
    --with-hackdir="%{_libdir}/xscreensaver" \
    --with-configdir="/etc/xscreensaver" \
    --with-xf86vmode-ext \
    --with-xf86gamma-ext \
    --with-xshm-ext \
    --with-xdbe-ext \
    --with-proc-interrupts \
    --with-gtk \
    --with-gl \
    --with-gle \
    --with-pixbuf \
    --with-jpeg \
    --with-image-directory=/usr/share/wallpapers \
    --with-text-file=/etc/issue \
    --with-browser=/usr/bin/xdg-open

#--with-xidle-ext \
#--with-readdisplay \
    
%__make %{?jobs:-j%{jobs}}

%install
%__make install_prefix="$RPM_BUILD_ROOT" install

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc README
%dir /etc/xscreensaver
%config(noreplace) /etc/xscreensaver/*.xml
%{_libdir}/xscreensaver/*
%{_datadir}/xtrascreenhacks
%doc %{_mandir}/man6/*

%changelog
* Wed Sep 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7
- Rebuild for Fedora

* Tue Mar 29 2011 pascal.bleser@opensuse.org
- update to 0.7:
  * adds a new hack called "Psychedelic", which is a re-implementation of the
    classic Smoking Clover hack
  * a bug in the Soma hack that caused the pieces to disappear in mono mode has
    been fixed
  * a malloc bug in Craters has been fixed, and multiple problems with its
    configuration screen have been corrected

* Fri Jun 25 2010 pascal.bleser@opensuse.org
- initial package (0.5)
