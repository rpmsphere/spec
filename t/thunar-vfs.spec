%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define api 1

Name:		thunar-vfs
Version:	1.2.0
Release:	7
Summary:	Virtual filesystem shipped with Thunar 1.0 and earlier releases
Group:		Graphical desktop/Xfce
License:	LGPLv2+
URL:		https://thunar.xfce.org
Source0:	https://archive.xfce.org/src/xfce/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	pkgconfig(gamin)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	intltool

%description
Thunar-vfs contains the virtual filesystem shipped with Thunar 1.0 and
earlier releases. It provides compatibility for applications that still
use thunar-vfs while Thunar was ported to GVFS.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
Thunar-vfs contains the virtual filesystem shipped with Thunar 1.0 and
earlier releases. It provides compatibility for applications that still
use thunar-vfs while Thunar was ported to GVFS.

This package contains the libraries and header files for developing
applications that use %{name}.

%prep
%setup -q
sed -i 's|exo-1|exo-2|' configure thunar-vfs/thunar-vfs-1.pc.in
sed -i 's|window->window|gtk_widget_get_window(window)|' thunar-vfs/thunar-vfs-volume.c

%build
%configure --disable-static
%make_build

%install
%make_install

#we don't want these
find %{buildroot} -name '*.la' -delete

%find_lang %{name}

# remove duplicate docs
rm -rf %{buildroot}%{_datadir}/doc

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README 
%doc docs/ThumbnailersCacheFormat.txt docs/README.volumes
%{_datadir}/thumbnailers/thunar-vfs-font-thumbnailer-1.desktop
%{_libdir}/lib%{name}-%{api}.so.*
%{_libdir}/thunar-vfs-*

%files devel
%doc HACKING TODO
%doc %{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}-%{api}
%{_libdir}/lib%{name}-%{api}.so
%{_libdir}/pkgconfig/thunar-vfs-%{api}.pc

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.0
- Rebuilt for Fedora
