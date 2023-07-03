Summary:        X driver for the USBD480 display
Name:           xorg-x11-drv-usbd480
Version:        0.9.906
Release:        5.1
License:        MIT
Group:          System/X11/Servers
URL:            https://www.lcdinfo.com
Source0:        xf86-video-usbd480-%{version}.tar.bz2
BuildRequires:  libusb1-devel xorg-x11-server-devel
#BuildRequires:  clang
BuildRequires:  xorg-x11-server-source

%description
This package contains a libusb based X driver for
Henri Skippari's USBD480 display (https://www.lcdinfo.com).

%prep
%setup -q -n xf86-video-usbd480-%version
#sed -i -e 's|scrnIndex, pScreen|pScreen|' -e '/mibstore\.h/d' src/usbd480_driver.c

%build
#export CFLAGS='-std=c99'
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir /etc/X11/usbd480/
%config(noreplace) /etc/X11/usbd480/*
%{_libdir}/xorg/modules/drivers/*
%{_bindir}/*

%changelog
* Fri Nov 13 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.906
- Rebuilt for Fedora
* Thu Sep 29 2011 max@suse.com
- Version 0.9.904:
  * Disbling other input devices doesn't seem to be needed anymore.
* Wed Nov  3 2010 max@suse.de
- Version 0.9.903:
  * Adjust the code to the latest X.org driver API changes.
  * Add the Xusbd480 startup script to the source tarball.
  * Include a set of config snippets under /etc/X11/usbd480.
* Wed Nov  4 2009 max@suse.de
- Version 0.9.902
* Sat Oct 17 2009 max@suse.de
- Version 0.9.901 with a few minor fixes.
- Fix crashes caused by improper region handling.
* Sat Sep 19 2009 max@suse.de
- Initial build of version 0.9.900.
