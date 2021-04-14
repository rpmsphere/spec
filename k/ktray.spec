Name:           ktray
BuildRequires:  libpng-devel, libjpeg-devel
BuildRequires:  gcc-c++, kdelibs3-devel
Summary:        Independent System Tray Applet
Version:        0.2
Release:        198.1
License:        GPL v2 or later
URL:            http://ktray.homac.de
Group:          System/GUI/KDE
Source:         %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
KTray is a system tray that holds dock icons of any application. It is
independent from the KDE Kicker so it can be used with any window
manager. It is based on the code from the original kicker system tray
panel applet.

Authors:
--------
    Holger Macht

%prep
%setup -q

%build
export CFLAGS="%optflags -I/usr/include/kde"
export CXXFLAGS="%optflags -I/usr/include/kde"
autoreconf -fiv
./configure --with-qtdir=%_libdir/qt-3.3 --with-kdedir=/usr --prefix=/usr
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-,root,root)
%{_bindir}/ktray
%{_datadir}/icons/ktray

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Wed May  7 2008 crrodriguez@suse.de
- use RPM_OPT_FLAGS
* Tue Feb  5 2008 hmacht@suse.de
- version 0.2: add addition cmd line options to specify the
  postition on the desktop, whether to use horizontal or vertical
  alignment and to draw ktray without decoration and focus
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Mar 22 2005 hmacht@suse.de
- kded is not started. It does not work if kded is not running.
  (no bugreport)
* Wed Mar  9 2005 hmacht@suse.de
- initial checkin
