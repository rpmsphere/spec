Name:         axl
Summary:      XML Parsing Library
URL:          http://xml.aspl.es/
Group:        XML
License:      LGPL
Version:      0.7.2
Release:      7.1
Source0:      http://www.aspl.es/xml/downloads/%{name}-%{version}.b3508.tar.gz

%description
AXL is a parser library for the XML 1.0 standard specification with
a very low memory footprint.

%package devel
Summary: Development files for package axl
Requires: %{name} = %{version}

%description devel
Header files and libraries of the XML Parsing Library.

%prep
%setup -q -n axl-%{version}.b3508
#sed -i '/new_size/d' knife/exarg.c
sed -i 's|node->type != node->type|node->type != node2->type|' src/axl_dtd.c

%build
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --disable-py-axl \
    --disable-axl-doc \
    --disable-axl-test \
    --enable-shared

%{__make} %{_smp_mflags}

%install
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%doc NEWS README AUTHORS ChangeLog COPYING
%{_bindir}/%{name}-knife
%{_libdir}/lib%{name}*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc
%exclude %{_libdir}/lib%{name}*.{a,la}

%changelog
* Mon Aug 29 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.2
- Rebuilt for Fedora
