Name:           qnotify
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++, libdrm-devel, libjpeg-devel, qt3-devel
Summary:        Notifications for multiple workspaces
Version:        0.6
Release:        179.1
License:        GPL v2 or later
URL:            https://qnotify.homac.de
Group:          System/GUI/Other
Source:         %{name}-%{version}.tar.bz2
Patch1:         qnotify-warn.dif
Patch2:         qnotify-header.patch

%description
QNotify is a small and windowmanager independent utility to inform you
of events of any kind. When a specific event occurres, a small window
will pop up showing a message or an image. The window does not take
away the focus of any other application. Additionally, it stays on top
of the Desktop and does not disappear when changing workspaces. The
graphical look can be controlled by a lot of option like colors, geome-
try, time shown, flickering or transparency.

The tool is especially designed for those who are not using KDE, but it
is written with the framework QT from Trolltech and so it usable any
windowmanager.

Since version 0.3, there is a daemon called qnotifyd which stays in
background and keeps track of all shown windows. It manages the
alignment of all qnotify windows and therefor avoids overlapping of
events. For further information about the daemon look at man qnotifyd.



Authors:
--------
    Holger Macht

%package libs
License:        GPL v2 or later
Summary:        Library to be used by other applications for displaying nice popups
Group:          Development/Libraries/C and C++

%description libs
LibQNotify is a library intended for use with other Qt or KDE
applications. It provides an easy to use API for displaying highly
configurable popups and even animations on the desktop. The commandline
application QNotify supports all of its features.



Authors:
--------
    Holger Macht <holger@homac.de>

%prep
%setup -q
%patch1
%patch2 -p1

%build
autoreconf -fiv
%configure --x-libraries=%{_libdir} --with-qtdir=%_libdir/qt-3.3 --with-pic --disable-static
%{__make} %{?jobs:-j%jobs}

%install
make DESTDIR=$RPM_BUILD_ROOT install
sed -e "s,$RPM_BUILD_DIR,/," $RPM_BUILD_ROOT%{_libdir}/libqnotify.la > $RPM_BUILD_ROOT%{_libdir}/libqnotify.la.1
mv $RPM_BUILD_ROOT%{_libdir}/libqnotify.la.1 $RPM_BUILD_ROOT%{_libdir}/libqnotify.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/qnotify
%_libdir/qnotify/
%_mandir/man1/qnotify.1.gz

%files libs
%_libdir/lib*.so*
#_libdir/lib*.la
%_includedir/*

%changelog
* Wed Sep 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
* Mon Jun  6 2011 aj@suse.de
- Fix build with newer glibc.
* Wed Oct 15 2008 crrodriguez@suse.de
- fix build
* Wed Jun 18 2008 schwab@suse.de
- Use autoreconf.
* Thu May  8 2008 aj@suse.de
- Fix missing return values.
* Mon Feb  4 2008 hmacht@suse.de
- version 0.6:
  - Remove qnotifyd and implement functionality with local file
  - remove fix-includes.patch
* Thu Dec 27 2007 crrodriguez@suse.de
- fix library-without-ldconfig-* errors
* Tue Oct 23 2007 hmacht@suse.de
- add qnotify-fix-inlcudes.patch to fix errors due to gcc4.3
* Thu Aug 24 2006 cthiel@suse.de
- fix build
* Mon Jan 30 2006 hmacht@suse.de
- split package in library and separate command line tool
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Sun Oct  9 2005 hmacht@suse.de
- new version
- fix novell bug 119010
- fix compiler errors
- applied indent
* Sat Jul 23 2005 hmacht@suse.de
- update to new version --> removed patch
* Fri Apr 22 2005 ro@suse.de
- include errno where needed
* Wed Mar  9 2005 hmacht@suse.de
- initial checkin
