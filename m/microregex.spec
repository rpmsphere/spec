Name:         microregex
Summary:      Micro Regular Expression Library
URL:          https://trac.kite-language.org/wiki/Microregex
Group:        RegExp
License:      MIT-style
Version:      1.0b7
Release:      6.1
Source0:      https://www.kite-language.org/files/microregex-%{version}.tar.gz

%description
microregex is a lightweight regular expression library written in C.
It uses Perl syntax with some exceptions: "(?...)" construct and
some escapes are not supported.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

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

%files
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
#{_libdir}/lib*.la
%{_libdir}/lib*.so

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0b7
- Rebuilt for Fedora
