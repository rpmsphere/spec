Name: hildon-desktop
License: GPL
Group: Applications/System
Summary: Widgets for the Maemo environment
Version: 0.0.43
Release: 1
Source: https://moblin.org/build-results/projects/hildon-desktop/lpia/%{name}_%{version}-15.tar.gz
URL: https://www.moblin.org/projects/projects_ui.php
BuildRequires: gtk2-devel, libhildon-devel, libXtst-devel, esound-devel
Requires: gtk2, libhildon, libXtst, hildon-desktop-libs

%description
The Hildon Application Framework is the same set of GTK-based classes
that Nokia used with Maemo.

%package        libs
Summary:        Libraries for %{name}
Group:          System Environment/Libraries
Requires:       pkgconfig

%description    libs
The %{name}-libs package contains shared libraries of %{name}.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n hildon-desktop
sed -i 's/-Werror/-Wno-format-security -Wno-int-conversion -Wno-implicit-function-declaration -Wno-incompatible-pointer-types -lXrender -lesd/' configure.ac
sed -i -e 's/dbus_g_proxy_begin_call_with_timeout/dbus_g_proxy_begin_call/' -e 's/g_free, 120000, /g_free, /' background-manager/Makefile.am
sed -i '11d' libhildondesktop/Makefile.am
sed -i 's|glib/gkeyfile.h|glib.h|' src/hd-plugin-loader-legacy.c
sed -i 's|glib/gtypes.h|glib.h|' src/hn-app-sound.c

%build
./autogen.sh
%configure
%__make

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

%files
%doc AUTHORS ChangeLog COPYING desktop-safe-mode.txt
%{_bindir}/*
%{_sysconfdir}/xdg/*
%{_libdir}/pkgconfig/hildon-desktop.pc
%{_datadir}/applications/*
%{_datadir}/dbus-1/services/*

%files libs
%{_libdir}/libhildondesktop.so.0*
%{_libdir}/libhildonwm.so.0*

%files devel
%{_includedir}/hildon-desktop
%{_includedir}/libhildondesktop
%{_includedir}/libhildonwm
%{_libdir}/hildon-desktop
%{_libdir}/libhildondesktop.a
#{_libdir}/libhildondesktop.la
%{_libdir}/libhildondesktop.so
%{_libdir}/libhildonwm.a
#{_libdir}/libhildonwm.la
%{_libdir}/libhildonwm.so
%{_libdir}/pkgconfig/libhildon*.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.43
- Rebuilt for Fedora
