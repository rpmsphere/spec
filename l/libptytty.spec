Name:         libptytty
Summary:      PTY/TTY/UTMP/WTMP/LastLog Management Library
URL:          http://software.schmorp.de/pkg/libptytty
Group:        System
License:      GPL
Version:      1.6
Release:      6.1
Source0:      http://dist.schmorp.de/libptytty/libptytty-%{version}.tar.gz

%description
libptytty is an offspring of RXVT-Unicode that handles
PTY/TTY/UTMP/WTMP/LastLog handling in OS-independent ways.

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
%{__make} %{_smp_mflags} install DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/lib*.so.*
%{_mandir}/man3/*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6
- Rebuilt for Fedora
