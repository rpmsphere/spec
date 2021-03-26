Name: elementary
Version: 0.8.0.65643
Release: 1%{?dist}
Summary: Widget set based on the Enlightenment Foundation Libraries
Group: Graphical desktop/Enlightenment
License: LGPLv2
URL: http://www.enlightenment.org
Source: http://download.enlightenment.org/snapshots/LATEST/%name-%version.tar.bz2
BuildRequires: ecore-devel libeina-devel eet-devel edje-devel evas-devel embryo-devel
Requires: libelementary

%description
Elementary is a widget set based on the Enlightenment Foundation
Libraries, primarily aimed at creating graphical user interfaces for mobile and embedded devices.
This package contains binary helpers and data.

%package -n libelementary
Summary: Libraries for %name
Group: Development/C

%description -n libelementary
Elementary is a widget set based on the Enlightenment Foundation
Libraries, primarily aimed at creating graphical user interfaces for mobile and embedded devices.
This package contains shared libraries.

%package -n libelementary-devel
Summary: Development files for %name
Group: Development/C
Requires: libelementary = %version-%release

%description -n libelementary-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q

%build
%configure --disable-static
make %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=%{buildroot} INSTALL='install -p'
find %buildroot -name "*.la" -delete

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING INSTALL NEWS README ChangeLog
%dir %{_datadir}/elementary/
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/elementary/images/*
%{_datadir}/elementary/objects/*
%{_datadir}/elementary/themes/*
%{_datadir}/elementary/config/*
%{_datadir}/elementary/edje_externals/*
%{_datadir}/icons/elementary.png

%files -n libelementary
%doc COPYING
%{_libdir}/libelementary*.so.*
%{_libdir}/elementary/*
%{_libdir}/edje/*

%files -n libelementary-devel
%defattr(-, root, root, -)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Fri Mar 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> 0.8.0
- Update to r65643

* Sat Dec 4 2010 Firefly <firefly@opendesktop.org.tw> 0.7.0.55225
- Initial
