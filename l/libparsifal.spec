Name:         libparsifal
Summary:      XML Parser C library
URL:          https://www.saunalahti.fi/~samiuus/toni/xmlproc/
Group:        XML
License:      Public Domain
Version:      1.1.0
Release:      7.1
Source0:      https://www.saunalahti.fi/~samiuus/toni/xmlproc/libparsifal-%{version}.tar.gz

%description
Parsifal is a validating XML 1.0 parser written in ANSI C. Parsifal
API is based on SAX2 but it also offers progressive parsing feature
which can be used to implement pull parser on top of it.

%package devel
Summary: Development files for %{name}
#Requires: %{name}=%{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q

%build
autoreconf -ifv

./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --enable-shared
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_prefix}/bin
install -c -m 755 \
    parsifal-config $RPM_BUILD_ROOT%{_prefix}/bin/

%files devel
%{_bindir}/*
%{_includedir}/%{name}
%{_libdir}/lib*.a
#{_libdir}/lib*.la
%{_libdir}/lib*.so

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuilt for Fedora
