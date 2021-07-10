Name:           eekboard
Version:        1.0.8
Release:        1
Summary:        An easy to use virtual keyboard toolkit
License:        GPL-3.0+
Group:          System/GUI/Other
URL:            http://github.com/ueno/eekboard
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  libvala-devel
BuildRequires:  at-spi2-core-devel
BuildRequires:  cairo-devel
BuildRequires:  gtk3-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libcroco-devel
BuildRequires:  libxklavier-devel
BuildRequires:  pango-devel
BuildRequires:  libXtst-devel
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  python2-devel

#glib2_gsettings_schema_requires

%description
eekboard is a virtual keyboard software package, including a set of
tools to implement desktop virtual keyboards.

%package devel
Summary:        Development Files for libskk
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
The eekboard-devel package contains the header files.

%prep
%setup -q

%build
# ./autogen.sh
%configure --enable-introspection \
           --enable-vala \
           --enable-atspi \
           --enable-xtest \
           --disable-schemas-compile \
           --enable-libcanberra=yes

make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install 
rm -rf %{buildroot}%{_libdir}/*.la
%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README AUTHORS
%{_bindir}/eekboard
%{_bindir}/eekboard-server
%{_libdir}/libeek*.so.*
%{_libexecdir}/eekboard-setup
%{_datadir}/applications/eekboard.desktop
%{_datadir}/dbus-1
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas
%config %{_sysconfdir}/xdg/autostart/eekboard-autostart.desktop
%{_datadir}/icons/hicolor

%files devel
%{_includedir}/eek-0.90/
%{_includedir}/%{name}-0.90/
%{_libdir}/pkgconfig/eek*.pc
%{_libdir}/libeek*.so
%{_libdir}/girepository-1.0/
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/*
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/eek*.vapi
%{_datadir}/vala/vapi/eek*.deps

%changelog
* Sun Jul 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.8
- Rebuilt for Fedora
* Thu Jan 31 2013 mlin@suse.com
- makes more flexible for pkgconfig with vala
* Tue Sep 25 2012 hillwood@linuxfans.org
- move girepository files to typelib-1_0-Eek-0_90 package.
* Mon Sep 24 2012 hillwood@linuxfans.org
- Initial package.
