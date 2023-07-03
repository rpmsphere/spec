Name:           pangox-compat
Version:        0.0.2
Release:        2
Summary:        Compatibility library for pangox
License:        LGPLv2+
URL:            https://ftp.gnome.org/pub/GNOME/sources/pangox-compat/0.0/
Source0:        https://ftp.gnome.org/pub/GNOME/sources/pangox-compat/0.0/%{name}-%{version}.tar.xz 
BuildRequires:  pango-devel

%description
This is a compatibility library providing the obsolete pangox library
that is not shipped by Pango itself anymore.  

%package devel
Summary: Development files for pangox-compat
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
sed -i '/font_class->find_shaper/d' pangox.c

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc README COPYING NEWS AUTHORS
%{_libdir}/libpango*-*.so.*
%dir %{_sysconfdir}/pango
%config %{_sysconfdir}/pango/pangox.aliases

%files devel
%{_libdir}/libpango*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%changelog
* Sun Dec 4 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.2
- Rebuilt for Fedora
* Tue Feb 05 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.0.2-2
- Resolves:rh#907552 - unowned directory /etc/pango after pangox-compat installation
* Fri Nov 09 2012 Kalev Lember <kalevlember@gmail.com> - 0.0.2-1
- Update to 0.0.2
* Tue Aug 28 2012 Parag Nemade <pnemade AT redhat DOT com> - 0.0.1-1
- Initial package
