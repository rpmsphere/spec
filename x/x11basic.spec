%undefine _debugsource_packages

Name: x11basic
Version: 1.28
Release: 1
License: GPL
Group: Development/Languages
Summary: A Basic Interpreter with X11-Graphics capabilities
Source0: https://github.com/kollokollo/X11Basic/archive/refs/tags/%{version}.tar.gz#/X11Basic-%{version}.tar.gz
URL: http://x11-basic.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	libX11-devel
BuildRequires:	libpng-devel
BuildRequires:	readline-devel
BuildRequires:	transfig
BuildRequires:	ImageMagick
BuildRequires:  potrace

%description
X11-Basic implements the most common elements of the basic langugage. With
X11-graphics. The structure of the language is similar to the old ATARI ST
GFA-Basic. GFA-Basic programs should run with only few changes. 

This package includes the basic interpreter named x11basic. It can be used as a
shell, can run basic-scripts. You can make excecutable  scripts p.ex.
*.cgi-Scripts for handling web-input. A pseudo compiler (xbc) is included which
makes stand alone binaries out of the scripts. Also a ANSI-Basic-to-X11-Basic-
converter is now included.

%prep
%setup -q -n X11Basic-%{version}
#sed -i 's|-Wall|-Wall -std=c99 -fPIC|' Makefile.in
sed -i 's|-Wall|-Wall -fPIC|' src/Makefile.in
#sed -i -e 's|\.\./logo/|logo/|' -e 's|\.\./examples/|examples/|' src/Makefile.in
#sed -i 's|key_t|__key_t|' sysVstuff.h
#sed -i 's|inline int input_bit|int input_bit|' decode.*

%build
cd src
%configure
#sed -i 's|#define HAVE_ALSA 1|#undef HAVE_ALSA|' config.h
sed -i '1,24s|/usr|%{buildroot}/usr|' Makefile
sed -i 's|ln -s -f $(LIBDIR)/|ln -s -f |' Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
%ifarch x86_64 aarch64
mkdir -p $RPM_BUILD_ROOT/usr/lib64
%endif
cd src
%make_install
chmod +x $RPM_BUILD_ROOT%{_libdir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc *.md COPYING RELEASE_NOTES
%doc doc/ACKNOWLEGEMENTS doc/editors doc/HISTORY doc/manual doc/AUTHORS
%doc examples
%{_mandir}/man1/*.1.*
%{_bindir}/*
%{_libdir}/*%{name}*
%{_includedir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.28
- Rebuilt for Fedora
* Sat Apr 07 2007 Markus Hoffmann <kollo@users.sourceforge.net>
  New release (1.14)
* Sat Mar 17 2007 Markus Hoffmann <kollo@users.sourceforge.net>
  Corrected typos in description
* Tue Sep 16 2003 Markus Hoffmann <kollo@users.sourceforge.net>
  Added bas2x11basic + man page
* Sun Jun 22 2003 Markus Hoffmann <kollo@users.sourceforge.net>
  New release (1.09)
* Sun Jan 26 2003 Markus Hoffmann <kollo@users.sourceforge.net>
  changed manual, my email address has changed, changed installdir
* Mon Dec 16 2002 Markus Hoffmann <m.hoffmann@uni-bonn.de>
  included xbc
* Thu Mar 07 2002 Markus Hoffmann <m.hoffmann@uni-bonn.de>
  included manual
* Tue Jan 01 2002 Markus Hoffmann <m.hoffmann@uni-bonn.de>
  2nd release
* Tue Aug 28 2001 Markus Hoffmann <m.hoffmann@uni-bonn.de>
  1st release
