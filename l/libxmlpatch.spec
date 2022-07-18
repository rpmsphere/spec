%global __os_install_post %{nil}

Name:         libxmlpatch
Summary:      An XML Patch library
URL:          http://xmlpatch.sourceforge.net/
Group:        XML
License:      LGPL
Version:      0.4.0
Release:      10.1
Source0:      http://sourceforge.net/projects/xmlpatch/files/xmlpatch/%{version}/%{name}_%{version}.tar.gz
BuildRequires: glib2-devel
BuildRequires: libxml2-devel

%description
Extensible Markup Language (XML) documents are widely used as
containers for the exchange and storage of arbitrary data in today's
systems. Updates to this data requires exchanging of the entire
XML document between hosts, unless there's a mechanism that allows
exchanging only the updates of XML documents. This memo describes a
framework utilizing XML Path language (XPath) selectors with the aid
of which a set of patches can be applied to an existing initial XML
document.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q -n %{name}

%build
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --enable-shared
%{__make} %{_smp_mflags -O}

%install
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
rm %{buildroot}%{_libdir}/tests/xml_diff/test-diff

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_mandir}/man1/*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuilt for Fedora
