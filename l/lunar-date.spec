Name: lunar-date
Version: 2.4.0
Release: 7.1
Summary: Chinese Lunar calendar library
Group: User Interface/Desktops	
License: GPLv2	
URL: http://code.google.com/p/liblunar	
Source0: http://liblunar.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires: libpng-devel
BuildRequires: intltool, gtk2-devel, gtk-doc, python-devel
BuildRequires: pygobject2-devel, gobject-introspection-devel
BuildRequires: w3m
##BuildRequires: vala-devel
Obsoletes: liblunar

%description
Library to support date conversion from/to chinese lunar calendar.

%package devel
Summary: Chinese Lunar calendar library development files
Requires: %{name}

%description devel
Development files for Chinese Lunar calendar library.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/liblunar
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_libdir}/liblunar-date-*.so.*
%doc AUTHORS COPYING ChangeLog ChangeLog.pre-2-2 NEWS README

%files devel
%{_includedir}/liblunar-*/lunar-date
%{_libdir}/liblunar-date-*.so
%{_libdir}/liblunar-date-*.*a
%{_libdir}/pkgconfig/lunar-date-*.pc
##%{python_sitearch}/gtk-2.0/liblunar
%{_datadir}/gtk-doc/html/lunar-date
##%{_datadir}/vala/vapi/liblunar-1.vapi
%{_libdir}/girepository-1.0/LunarDate-*.typelib
%{_datadir}/gir-1.0/LunarDate-*.gir

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.0
- Rebuild for Fedora
* Tue Mar 30 2010 Gcell <ph.linfan@gmail.com> - 2.2.4-2
- Fix some spec file details
- This rpm cotained holiday.dat
* Tue Mar 30 2010 Gcell <ph.linfan@gmail.com> - 2.2.4-1
- Creat a spec file fo 2.2.4
