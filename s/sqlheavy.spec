Name:           sqlheavy
Version:        0.2.0git
Release:        16.1
License:        LGPL-2.1 and LGPL-3.0
Summary:        GObject SQLite wrapper
URL:            http://gitorious.org/sqlheavy
Group:          System/Libraries
Source0:        http://sqlheavy.googlecode.com/files/%{name}-master.tar.gz
BuildRequires:  libtool
BuildRequires:  vala-compat-devel vala-compat vala-compat-tools
BuildRequires:  glib2-devel
BuildRequires:  sqlite-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtk2-devel

%description
SQLHeavy is a convenience wrapper on top of SQLite. Though its primary
purpose is to provide an easy to use Vala interface, it also provides
a very nice C interface and GObject Introspection support, and may be
easier to use from other languages than the standard SQLite interface.
This package contains the executables.

%package devel
Summary:        SQLheavy Shared Library
Group:          Development/Libraries/Other
Requires:       sqlheavy = %{version}

%description devel
SQLHeavy is a convenience wrapper on top of SQLite. Though its primary
purpose is to provide an easy to use Vala interface, it also provides
a very nice C interface and GObject Introspection support, and may be
easier to use from other languages than the standard SQLite interface.
This package contains the executables.

%package -n sqlheavygtk-devel
Summary:        SQLheavyGTK Shared Library
Group:          Development/Libraries/Other
Requires:       sqlheavygtk = %{version}

%description -n sqlheavygtk-devel
SQLHeavy is a convenience wrapper on top of SQLite. Though its primary
purpose is to provide an easy to use Vala interface, it also provides
a very nice C interface and GObject Introspection support, and may be
easier to use from other languages than the standard SQLite interface.
This package contains the executables.

%package -n sqlheavygtk
Summary:        SQLheavyGTK Shared Library
Group:          System/Libraries
Requires:       sqlheavy = %{version}

%description -n sqlheavygtk
SQLHeavy is a convenience wrapper on top of SQLite. Though its primary
purpose is to provide an easy to use Vala interface, it also provides
a very nice C interface and GObject Introspection support, and may be
easier to use from other languages than the standard SQLite interface.
This package contains the executables.

%prep
%setup -q -n %{name}-0.2.0
sed -i 's|libvala-0\.16|libvala-0.18|' configure.ac

%build
touch ChangeLog
autoreconf -iv
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc NEWS README
%{_mandir}/man1/*
%{_libdir}/libsqlheavy0*.so.*
%{_datadir}/sqlheavy
%{_libdir}/girepository-1.0/SQLHeavy-0.2.typelib

%files devel
%{_includedir}/sqlheavy
%{_libdir}/libsqlheavy0*.a
%{_libdir}/libsqlheavy0*.so
%{_libdir}/pkgconfig/sqlheavy-*.pc
%{_datadir}/vala/vapi/sqlheavy-*.*
%{_datadir}/gir-1.0/SQLHeavy-0.2.gir

%files -n sqlheavygtk
%{_libdir}/libsqlheavygtk0*.so.*

%files -n sqlheavygtk-devel
%{_includedir}/sqlheavy/sqlheavy-*/SQLHeavyGTK.h
%{_libdir}/libsqlheavygtk0*.so
%{_libdir}/libsqlheavygtk0*.a
%{_libdir}/pkgconfig/sqlheavygtk-*.pc
%{_datadir}/vala/vapi/sqlheavygtk-*.*

%changelog
* Tue Jul 17 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0git
- Rebuilt for Fedora
* Fri May 18 2012 whats_up@tut.by
- initial release 0.1.1
