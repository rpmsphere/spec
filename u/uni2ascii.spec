Name:         uni2ascii
Summary:      Convert between Unicode and ASCII
URL:          http://billposer.org/Software/uni2ascii.html
Group:        Charset
License:      GPL
Version:      4.18
Release:      3.1
Source0:      http://billposer.org/Software/Downloads/uni2ascii-%{version}.tar.gz

%description
This package provides conversion in both directions between UTF-8
Unicode and a variety of 7-bit ASCII equivalents.

%prep
%setup -q

%build
echo "ac_cv_header_libintl_h=no" > config.cache
./configure \
    --cache-file=./config.cache \
    --prefix=%{_prefix}
%{__make} %{_smp_mflags -O}

%install
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
rm -rf $RPM_BUILD_ROOT%{_prefix}/bin/u2a

%files
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 4.18
- Rebuilt for Fedora
