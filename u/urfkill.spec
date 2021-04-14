Name:           urfkill
Version:        0.4.0
Release:        13.1
URL:            http://github.com/lcp/urfkill
Summary:        A daemon to control radio killswitches
License:        GPL-2.0+
Group:          System/Daemons
Source:         %{name}-%{version}.tar.xz
Patch0:         urfkill-change-default-user.patch
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  expat-devel
BuildRequires:  libudev-devel
BuildRequires:  polkit-devel
BuildRequires:  xz
BuildRequires:  w3m
Requires:       polkit
BuildRequires:  python

%description
Urfkill is a daemon to control radio killswitches through /dev/rfkill
and supports PolicyKit authorization mechanism.

%package glib
Summary:        The glib binding library for urfkill
Group:          System/Daemons

%description glib
Urfkill add-on library to integrate the standard urfkill library with
the GLib thread abstraction and main loop.

%package glib-devel
Summary:        The glib binding library for urfkill
Group:          Development/Libraries/Other
Requires:       glib2-devel
Requires:       urfkill-glib = %{version}-%{release}

%description glib-devel
Urfkill add-on library to integrate the standard urfkill library with
the GLib thread abstraction and main loop.
http://freedesktop.org/wiki/Software/urfkill

%prep
%setup -n %{name}-%{version} -q
%patch0 -p1

%build
%configure\
  --disable-static \
  --libexecdir=%{_libexecdir}/urfkill \
  --disable-gtk-doc
make %{?jobs:-j%jobs}

%install
%makeinstall
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -r urfkill 2> /dev/null || :
/usr/sbin/useradd -r -o -g urfkill -s /bin/false \
-c "killswitch control daemon" -d /var/lib/urfkill urfkill 2> /dev/null || :
/usr/sbin/usermod -g urfkill -G urfkill -s /bin/false urfkill 2> /dev/null

%post glib -p /sbin/ldconfig

%postun glib -p /sbin/ldconfig

%files
%doc AUTHORS COPYING NEWS README
%{_libexecdir}/urfkilld
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/polkit-1/actions/org.freedesktop.*.policy
%{_mandir}/man?/*
%config %{_sysconfdir}/dbus-1/system.d/*.conf
%config %{_sysconfdir}/urfkill

%files glib
%{_libdir}/liburfkill-glib.so.*
%{_libdir}/girepository-1.0/*.typelib

%files glib-devel
%{_datadir}/gir-1.0/Urfkill-*.gir
#%{_datadir}/gtk-doc/html/urfkill
%{_includedir}/liburfkill-glib
%{_libdir}/liburfkill-glib.so
%{_libdir}/pkgconfig/urfkill-glib.pc

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
* Fri Jun  8 2012 glin@suse.com
- Version bump to 0.4.0
  + Migrate from dbus-glib to gdbus
  + Improve the input device matching
  + Fix a memory leak in urf-config
- Remove dbus-1-glib-devel from Requires
* Wed Feb 15 2012 vuntz@opensuse.org
- Move dbus xml interface files from devel subpackage to main
  subpackage: those files might be needed at runtime.
* Thu Jan 26 2012 coolo@suse.com
- some cleanups
* Mon Jan  9 2012 glin@suse.com
- Move the typelib file from liburfkill-glib0 to
  typelib-1_0-Urfkill-0_0
- Update email address.
* Tue Oct  4 2011 uli@suse.com
- cross-build workaround: gobject-introspection is impossible to
  cross-compile, so we have to disable it
* Thu Sep 15 2011 glin@suse.com
- Version bump to 0.3.0
  New Features:
  + added fork option for urfkill
  + urf-device: New property: platform
  + urf-killswitch: export UrfKillswitch to D-Bus
  + glib/urf-client: Add a new function urf_client_enumerate_devices_sync()
  + glib/urf-device: Make the "soft" property writable
  + glib/urf-killswitch: New objects for killswitches
  + Generate .xz tarballs
* Mon Jun 13 2011 glin@novell.com
- Version bump to 0.2.0
  New Features:
  + All DBus methods, signals, and properties were revised and amended
  + Support the individual key control settings for each user
  + GObject introspection support in liburfkill-glib
  + Documents for the daemon, the DBus interfaces, and liburfkill-glib
  + Test cases for the daemon and liburkill-glib
- Enable gobject-introspection
* Tue Apr 19 2011 glin@novell.com
- Version bump to 0.1.1
- New dependency: expat
- Drop merged patches
  + urfkill-correct-config-name.patch
  + urfkill-new-input-devices.patch
- Remove rpmlintrc (bnc#688328)
* Tue Mar 15 2011 glin@novell.com
- Add urfkill-new-input-devices.patch to support more input devices
- Add urfkill-rpmlintrc for openSUSE 11.4 and wait for security review
* Tue Mar 15 2011 glin@novell.com
- Add urfkill-correct-config-name.patch to correct the config variable
* Tue Mar  1 2011 glin@novell.com
- Version bump to 0.1.0
- Add urfkill-change-default-user.patch to change the default user
- Drop deprecated patches:
  + urfkill-polkit-0.9.patch
  + urfkill-drop-privilege.patch
  + urfkill-killswitch-error-handle.patch
* Tue Nov 23 2010 glin@novell.com
- Amend urfkill-drop-privilege.patch to setuid to the dedicated user,
  urfkill, instead of nobody. bnc#646608
- Create the user, urfkill, in %%pre
- Add urfkill-killswitch-error-handle.patch to handle critical errors
  from urf_killswitch
* Wed Nov 10 2010 glin@novell.com
- Add urfkill-drop-privilege.patch to drop privilege after open
  /dev/rfkill. bnc#646608
* Tue Oct 12 2010 glin@novell.com
- Update to 0.0.1
  + License liburfkill-glib under LGPL v2.1
  + Support Block/Unblock by index
- Add patch urfkill-polkit-0.9.patch to support PolicyKit 0.9
* Fri Oct  1 2010 glin@novell.com
- Initial import 0.0.0~20101001
