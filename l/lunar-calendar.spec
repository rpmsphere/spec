%global __os_install_post %{nil}

Name: lunar-calendar
Version: 3.0.0
Release: 8.1
Summary: Chinese Lunar calendar Gtk widget
Group: User Interface/Desktops	
License: GPLv2	
URL: https://code.google.com/p/liblunar	
Source0: https://liblunar.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0: relative_libs.diff
BuildRequires: libpng-devel, intltool, gtk3-devel
BuildRequires: gtk-doc, pygtk2-devel
BuildRequires: pygobject2-devel, gobject-introspection-devel
BuildRequires: lunar-date-devel
BuildRequires: w3m
##BuildRequires: pygtksourceview-devel, vala-devel
Obsoletes: liblunar-gtk

%description
Gtk Widget which displays the Chinese Lunar calendar.

%package devel
Summary: Chinese Lunar calendar Gtk Widget development files
Requires: lunar-date-devel, %{name}

%description devel
Development files for Chinese Lunar calendar Gtk widget.

%prep
%setup -q
%patch0 -p1

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/liblunar-calendar-*.so.*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%doc AUTHORS COPYING ChangeLog NEWS README

%files devel
%{_includedir}/liblunar-*/lunar-calendar
%{_libdir}/liblunar-calendar-*.so
%{_libdir}/liblunar-calendar-*.*a
%{_libdir}/pkgconfig/lunar-calendar-*.pc
%{_datadir}/gtk-doc/html/lunar-calendar3
##%{_datadir}/vala/vapi/liblunar-gtk.deps
##%{_datadir}/vala/vapi/liblunar-gtk.vapi
%{_libdir}/girepository-1.0/LunarCalendar-*.typelib
%{_datadir}/gir-1.0/LunarCalendar-*.gir

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.0
- Rebuilt for Fedora
* Tue Mar 30 2010 Gcell <ph.linfan@gmail.com> - 2.2.4-2
- Add 99-liblunar-preload automatic loading
* Tue Mar 30 2010 Gcell <ph.linfan@gmail.com> - 2.2.4-1
- Creat a spec file fo 2.2.4
