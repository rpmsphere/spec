Name:				 notify-osd
Version:			 0.9.25
Release:			 15.1
Summary:			 Ephemeral Overlay On-Screen-Display Notification Agent
# https://launchpad.net/notify-osd/trunk/ubuntu-9.10-sru/+download/notify-osd-%{version}.tar.gz
Source:			 notify-osd-%{version}.tar.bz2
URL:				 https://launchpad.net/notify-osd
Group:			 System/Libraries
License:			 GNU General Public License version 3 (GPL v3)
BuildRequires:   libpng-devel
BuildRequires:	 libwnck-devel
BuildRequires:	 glib2-devel gtk2-devel
BuildRequires:	 GConf2-devel notification-daemon sane-backends-devel
BuildRequires:	 libnotify-devel >= 0.4.5
BuildRequires:	 dbus-devel dbus-glib-devel
BuildRequires:	 gcc make glibc-devel
BuildRequires:	 autoconf automake libtool pkgconfig
Patch0:			%{name}-notify_notification_new.patch

%description
Canonical's on-screen-display notification agent, implementing the
freedesktop.org Desktop Notifications Specification with semi-transparent
click-through bubbles.

The freedesktop.org Desktop Notifications Specification provides a standard way
for applications to display pop-up notifications. These are designed to make
you aware of something, without interrupting your work with a window you must
close.

Notify OSD presents these notifications as ephemeral overlays, which can be
clicked through so they don't block your work. It queues notifications, to
prevent them from flooding your screen. And as well as handling standard
notification updates, Notify OSD introduces the idea of appending  allowing
notifications to grow over time, for example in the case of instant messages
from a particular person.

%prep
%setup -q
%patch0 -p1

%build
export LDFLAGS="-lX11 -lpixman-1 -lm"
%configure \
	 --enable-compile-warnings=maximum

%__make %{?jobs:-j%{jobs}} V=1 \
	 notify_osddir="%{_bindir}"

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__make \
	 DESTDIR="$RPM_BUILD_ROOT" \
	 notify_osddir="%{_bindir}" \
	 install

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/notify-osd
%{_datadir}/notify-osd
%{_datadir}/dbus-1/services/org.freedesktop.Notifications.service

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.25
- Rebuilt for Fedora
* Wed Mar 31 2010 pascal.bleser@opensuse.org
- initial package (0.9.25)
