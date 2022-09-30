Summary: Compat package with poppler 0.22 libraries
Name: compat-poppler022
Version: 0.22.5
Release: 4%{?dist}
License: (GPLv2 or GPLv3) and GPLv2+ and LGPLv2+ and MIT
Group: Development/Libraries
URL:     http://poppler.freedesktop.org/
Source0: http://poppler.freedesktop.org/poppler-%{version}.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=1024753
Patch0:  poppler-0.22.5-CVE-2013-4473.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1024762
Patch1:  poppler-0.22.5-CVE-2013-4474.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1053616
Patch2:  poppler-0.22.5-rotated-words-selection.patch

Requires: poppler-data >= 0.4.0
BuildRequires: automake libtool
BuildRequires: gettext-devel
BuildRequires: libjpeg-devel
BuildRequires: openjpeg-devel >= 1.3-5
BuildRequires: pkgconfig(cairo) >= 1.10.0
BuildRequires: pkgconfig(gobject-introspection-1.0) 
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(QtGui) pkgconfig(QtXml)
BuildRequires: pkgconfig(libtiff-4)

Conflicts:     poppler < 0.24

%description
Compatibility package with poppler 0.22 libraries.


%package glib
Summary:  Glib wrapper for poppler
Group:    Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

Conflicts: poppler-glib < 0.24

%description glib
%{summary}.


%package qt
Summary:  Qt4 wrapper for poppler
Group:    System Environment/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%{?_qt4:Requires: qt4%{?_isa} >= %{_qt4_version}}

Conflicts: poppler-qt < 0.24

%description qt
%{summary}.


%package cpp
Summary:   Pure C++ wrapper for poppler
Group:     Development/Libraries
Requires:  %{name}%{?_isa} = %{version}-%{release}

Conflicts: poppler-cpp < 0.24

%description cpp
%{summary}.


%prep
%setup -q -n poppler-%{version}
%patch0 -p1 -b .CVE-2013-4473
%patch1 -p1 -b .CVE-2013-4474
%patch2 -p1 -b .rotated-word-selection

# hammer to nuke rpaths, recheck on new releases
autoreconf -i -f

%build

# Hack around borkage, http://cgit.freedesktop.org/poppler/poppler/commit/configure.ac?id=9250449aaa279840d789b3a7cef75d06a0fd88e7
PATH=%{_qt4_bindir}:$PATH; export PATH

%configure \
  --disable-static \
  --disable-gtk-test \
  --enable-cairo-output \
  --enable-libjpeg \
  --enable-libopenjpeg \
  --enable-poppler-qt4 \
  --enable-xpdf-headers \
  --disable-zlib \
  --enable-introspection=yes

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -fv $RPM_BUILD_ROOT%{_libdir}/lib*.la

rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/girepository-1.0/Poppler-0.18.typelib
rm -rf $RPM_BUILD_ROOT%{_libdir}/libpoppler-cpp.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/libpoppler-glib.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/libpoppler-qt4.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/libpoppler.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
rm -rf $RPM_BUILD_ROOT%{_datadir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post glib -p /sbin/ldconfig

%postun glib -p /sbin/ldconfig

%post qt -p /sbin/ldconfig

%postun qt -p /sbin/ldconfig

%post cpp -p /sbin/ldconfig

%postun cpp -p /sbin/ldconfig


%files
%doc COPYING
%{_libdir}/libpoppler.so.37*

%files glib
%{_libdir}/libpoppler-glib.so.8*

%files qt
%{_libdir}/libpoppler-qt4.so.4*

%files cpp
%{_libdir}/libpoppler-cpp.so.0*


%changelog
* Fri Apr 24 2015 Marek Kasik <mkasik@redhat.com> - 0.22.5-4
- Add back glib, cpp and qt frontends so that existing applications
- loads correct libpoppler.so.*.
- Resolves: #1184215

* Tue Apr 21 2015 Marek Kasik <mkasik@redhat.com> - 0.22.5-3
- Don't convert utils/pdftohtml.1 to UTF-8, it is already UTF-8
- Resolves: #1184215

* Mon Apr 20 2015 Marek Kasik <mkasik@redhat.com> - 0.22.5-2
- Initial import of compat-poppler022 package
- Resolves: #1184215

* Wed Nov 12 2014 Kalev Lember <kalevlember@gmail.com> - 0.22.5-1
- Poppler 0.22 compat package for el7-gnome-3-14 copr
