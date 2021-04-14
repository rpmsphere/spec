%define url_ver %(echo %{version}|cut -d. -f1,2)

%define gstapi	1
%define api	0.4
%define libname lib%{name}
%define girname lib%{name}-gir
%define devname lib%{name}-devel

Summary:	Glib/gobject based library implementing a Genicam interface
Name:		aravis
Version:	0.7.3
Release:	1
License:	GPLv2+
Group:		Development/GNOME and GTK+
URL:		https://github.com/AravisProject/aravis
Source0:	http://ftp.gnome.org/pub/GNOME/sources/aravis/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-%{gstapi}.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi}.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(gstreamer-app-1.0)
BuildRequires:	gtk-doc
BuildRequires:	w3m
BuildRequires:  python

%description
Aravis is a glib/gobject based library implementing a Genicam interface, 
which can be used for the acquisition of video streams coming from either
ethernet, firewire or USB cameras. It currently only implements an ethernet 
camera protocol used for industrial cameras.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
Aravis is a glib/gobject based library implementing a Genicam interface, 
which can be used for the acquisition of video streams coming from either
ethernet, firewire or USB cameras. It currently only implements an ethernet 
camera protocol used for industrial cameras.

This package contains the shared library for %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n gstreamer%{gstapi}-%{name}
Summary:	Gstreamer support for %{name}
Group:		Sound
Obsoletes:	%{name}-gstreamer%{gstapi}

%description -n gstreamer%{gstapi}-%{name}
This package contains the gstreamer plugin for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}

%description -n %{devname}
This package contains the development files for %{name}

%prep
%setup -q

%build
#configure \
#	--disable-static \
#	--enable-gst-plugin \
#	--enable-viewer
#make LIBS='-lm -lz'
mkdir build
meson --prefix=/usr build
ninja -C build

%install
%ninja_install -C build
#make_install
rm -fr %{buildroot}%{_prefix}/doc

%files
%{_bindir}/*
%{_datadir}/%{name}-*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_mandir}/man1/*

%files -n %{libname}
%doc AUTHORS COPYING *.md
%{_libdir}/libaravis-*.so.*
#exclude %{_libdir}/libaravis-*.la

%files -n %{girname}
%{_libdir}/girepository-1.0/Aravis-*.typelib

%files -n gstreamer%{gstapi}-%{name}
%{_libdir}/gstreamer-*/libgstaravis*.so
#exclude %{_libdir}/gstreamer-%{gstapi}.0/libgstaravis-%{api}.la
#{_libdir}/gstreamer-0.10/libgstaravis-*.la
#{_libdir}/gstreamer-0.10/libgstaravis-*.so

%files -n %{devname}
%{_includedir}/%{name}-*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Aravis-*.gir
%{_datadir}/gtk-doc/html/%{name}-*

%changelog
* Mon Jan 06 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.3
- Rebuilt for Fedora
* Sun Jan 11 2015 abfonly <abfonly@gmail.com> 0.3.5-1
+ Revision: 13deda8
- Log: Update to 0.3.5
