Summary: C/Gobject based SVG/Mathml renderer and editor
Name: lasem
Version: 0.4.1
Release: 7.3
Group: Graphics
License: GPL
URL: http://blogs.gnome.org/emmanuel/category/lasem
Source: http://ftp.gnome.org/pub/GNOME/sources/lasem/0.4/%{name}-%{version}.tar.xz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: glib2-devel gvfs-devel gtk2-devel libxml2-devel 
BuildRequires: pango-devel cairo-devel intltool flex

%description
Lasem aims to be a C/Gobject based SVG/Mathml renderer and editor, supporting CSS
style sheets. It uses cairo and pango as it's rendering abstraction layer, and
then support numerous output formats: xlib, PNG, SVG, PDF, PS, EPS...

%package devel
Summary: C/Gobject based SVG/Mathml renderer and editor - development files
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for lasem.

%prep
%setup -q

%build
%configure --disable-static
make

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/doc

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%_bindir/*
%_libdir/lib*.so.*
%_datadir/locale/*/LC_MESSAGES/*.mo

%files devel
%_includedir/*
%_libdir/pkgconfig/*.pc
%_libdir/lib*.so
%_libdir/lib*.la
%_datadir/gtk-doc/html/*

%changelog
* Sun Jan 20 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuild for Fedora
* Mon Feb 15 2010 slick50 <lxgator@gmail.com> 0.13-1pclos2010
- initial pkg
