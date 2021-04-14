%define         soname 5
%define         gtksoname  gtk2

Name:           libindicate
Version:        0.5.0
Release:        1
License:        GNU LGPLv2.1 ; GNU LGPLv3
Summary:        Library to raise flags on dbus
Url:            http://launchpad.net/libindicate
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
Source99:       libindicate-rpmlintrc
# PATCH-FIX-UPSTREAM openSUSE-python-fix-detection.patch lp#690555 nmarques@opensuse.org -- fixes python static version
Patch0:         openSUSE-python-fix-detection.patch
BuildRequires:  doxygen
BuildRequires:  gnome-common
BuildRequires:  gnome-doc-utils
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dbusmenu-gtk-0.4)
BuildRequires:  pkgconfig(gapi-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(mono)
BuildRequires:  vala-devel

%description
A small library for applications to raise "flags" on DBus for other components
of the desktop to pick up and visualize. Currently used by the messaging
indicator.

%package -n %{name}%{soname}
Summary:        Library to raise flags on DBus
Group:          System/Libraries
Provides:       %{name}%{soname}-sharp

%description -n %{name}%{soname}
A small library for applications to raise "flags" on DBus for other components
of the desktop to pick up and visualize. Currently used by the messaging
indicator.

%package %{gtksoname}
Summary:        Indicate sharp libraries
Group:          Development/Libraries/Other

%description %{gtksoname}
This package provides the mono bindings for libindicate.
A small library for applications to raise "flags" on DBus for other components
of the desktop to pick up and visualize. Currently used by the messaging
indicator.

%package sharp
Summary:        Sharp extentions for libindicate
Group:          Development/Languages/Other
BuildRequires:  pkgconfig

%description sharp
This package provides the sharp extensions for libindicate.
A small library for applications to raise "flags" on DBus for other components
of the desktop to pick up and visualize. Currently used by the messaging
indicator.

%package gtk-sharp
Summary:        Sharp extensions for libindicate-gtk
Group:          Development/Languages/Other

%description gtk-sharp
This package provides the gtk-sharp extensions for libindicate.
A small library for applications to raise "flags" on DBus for other components
of the desktop to pick up and visualize. Currently used by the messaging
indicator.

%package -n python-indicate
Summary:        Python bindings for libindicate
Group:          Development/Libraries/Other
BuildRequires:  pygobject2-devel
BuildRequires:  pygtk2-devel
Requires:       %{name}%{soname} = %{version}
Requires:       %{name}-%{gtksoname} = %{version}

%description -n python-indicate
This package provides the python bindings for libindicate.
A small library for applications to raise "flags" on DBus for other components
of the desktop to pick up and visualize. Currently used by the messaging
indicator.

%package devel
Summary:        Development files for libindicate
Group:          Development/Libraries/Other
Requires:       %{name}%{soname} = %{version}
Requires:       %{name}-%{gtksoname} = %{version}
Requires:       pkgconfig
Requires:       python2-indicate = %{version}
Provides:       %{name}-%{gtksoname}-devel

%description devel
A small library for applications to raise "flags" on DBus for other components
of the desktop to pick up and visualize. Currently used by the messaging
indicator.

%prep
%setup -q
%patch0
sed -i '/g_type_init();/d' examples/*
sed -i -e 's|gmcs|mcs|' -e 's|pyglib-2.0-python|pyglib-2.0-python2|' configure.ac
sed -i 's|GTimeVal |GDateTime *|' libindicate/*

%build
# Warning, reconf required by patch
autoreconf -fi
%configure\
   --disable-static \
   --enable-introspection=yes \
   --enable-gtk-doc=no \
   --enable-doxygen-man
# Known problems with parallel builds. Let's try to stay away from them.
sed -i -e 's|-Werror$|-Wno-error|' -e 's|-Werror=[a-z\-]*||g' Makefile */Makefile
sed -i 's|-Wall|-Wall -Wno-error -Wl,--allow-multiple-definition|' Makefile */Makefile */*/Makefile
make

%install
%make_install
# Remove libtool archives
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%clean
rm -rf %{buildroot}





%files -n %{name}%{soname}
%doc COPYING
%{_libdir}/libindicate.so.*
%{_libdir}/girepository-1.0/Indicate-0.5.typelib

%files %{gtksoname}
%{_libdir}/libindicate-gtk.so.*
%{_libdir}/girepository-1.0/Indicate-Gtk-0.5.typelib

%files sharp
%dir /usr/lib/mono/gac/indicate-sharp
%dir /usr/lib/mono/gac/indicate-sharp/0.4.1.0__2e8e49ba7d172cb0
%dir /usr/lib/mono/indicate
/usr/lib/mono/gac/indicate-sharp/0.4.1.0__2e8e49ba7d172cb0/*
/usr/lib/mono/indicate/indicate-sharp.dll
%{_libdir}/indicate-sharp-0.1/
%{_libexecdir}/im-client
%{_libexecdir}/indicate-alot
%{_libexecdir}/indicate-and-crash
%{_libexecdir}/listen-and-print
%{_libexecdir}/show-hide-server

%files gtk-sharp
/usr/lib/mono/gac/indicate-gtk-sharp/
%dir /usr/lib/mono/indicate-gtk
/usr/lib/mono/indicate-gtk/indicate-gtk-sharp.dll
%{_libdir}/indicate-gtk-sharp-0.1/

%files -n python-indicate
%{python2_sitearch}/indicate/
%{_datadir}/pygtk/2.0/defs/indicate.defs

%files devel
%dir %{_datadir}/doc/libindicate
%dir %{_includedir}/libindicate-0.5
%{_includedir}/libindicate-0.5/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/doc/libindicate/examples
%{_datadir}/gtk-doc/html/libindicate/
%{_datadir}/gir-1.0/Indicate*
%{_datadir}/vala/

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuilt for Fedora
* Mon Apr  4 2011 nmo.marques@gmail.com
- Update to version 0.5.0:
  + Fix dbus error codes (lp#736249).
- Removed patch, fix-dbusmenu-build.patch - no longer required.
- Minor fixes on spec, some fixes in %%files, friendlier comments.
* Fri Feb 11 2011 nmarques@opensuse.org
- Add fix-dbusmenu-build.patch: Fixes build for latest changes on
  dbusmenu.
* Thu Feb  3 2011 nmarques@opensuse.org
- Update to version 0.4.92:
  + Switch to standard dbus property processing
    (lp#706408) (lp#711987)
  + Watch the DBus signals for name owner changes
  + Protect the tuple builder to avoid segfaults
- Drop fix-segfault.patch: fixed upstream
* Thu Feb  3 2011 nmarques@opensuse.org
- Add fix-segfault.patch: several applications crash when compiled
  or using plugins for libindicate. This patch fixes
  those situations.
* Tue Jan 18 2011 nmarques@opensuse.org
- Update to version 0.4.91:
- Rebased openSUSE-python-fix-detection.patch
* Mon Dec 13 2010 nmarques@opensuse.org
- Initial packaging from source: libindicate-0.4.4.tar.bz2
