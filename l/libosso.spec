Name:           libosso
URL:            http://maemo.org/
License:        LGPL v2.1 only; LGPL v2.1 or later
Group:          System Environment/Libraries
Summary:        A wrapper library for D-Bus services
Version:        2.16
Release:        1
Source:         libosso-%{version}.tar.bz2
Patch1:         ecanuto-visibility.patch  
BuildRequires:  dbus-glib-devel mce-devel
Requires:       dbus-glib 

%description
Libosso is the basic library containing required and helpful functions
for maemo applications. One of Libosso's main features is RPC (Remote
Procedure Calls) services (as it "wraps" D-Bus). In addition, Libosso
provides access to low-level hardware functions, such as turning on (or
keeping on) the display, autosaving, state saving and system time.

All maemo-compliant applications must use Libosso to respond coherently
to system changes and signals, such as the battery low, pre-shutdown
and state saving signals.

This package contains the shared library.

%package devel
License:        LGPL v2.1 only; LGPL v2.1 or later
Group:          System Environment/Libraries
Summary:        Development files for libosso
Requires:       %{name} = %{version} dbus-glib-devel

%description devel
Libosso is the basic library containing required and helpful functions
for maemo applications. One of Libosso's main features is RPC (Remote
Procedure Calls) services (as it "wraps" D-Bus). In addition, Libosso
provides access to low-level hardware functions, such as turning on (or
keeping on) the display, autosaving, state saving and system time.

All maemo-compliant applications must use Libosso to respond coherently
to system changes and signals, such as the battery low, pre-shutdown
and state saving signals.

This package contains the development files.

%prep
%setup -q
%patch1 -p1  

%build
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%doc README INSTALL ChangeLog COPYING
%{_bindir}/*
%{_libdir}/libosso.so.1*
%{_sysconfdir}/dbus-1/system.d/libosso.conf
%{_sysconfdir}/libosso/sessionbus-libosso.conf

%files devel
%{_includedir}/*.h
%{_libdir}/libosso.a
%{_libdir}/libosso.la
%{_libdir}/libosso.so
%{_libdir}/pkgconfig/libosso.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.16
- Rebuilt for Fedora
* Thu Jul  3 2008 ecanuto@novell.com
- initial package based on 2.16
