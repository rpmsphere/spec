%global __spec_install_post %{nil}
%undefine _debugsource_packages

Name:         libsrs2
Summary:      Mail Sender Rewriting Scheme (SRS) Library
URL:          https://www.libsrs2.org/
Group:        Mail
License:      GPL/BSD
Version:      1.0.18
Release:      11.1
Source0:      https://www.libsrs2.org/srs/libsrs2-%{version}.tar.gz

%description
Libsrs2 implements the Sender Rewriting Scheme (SRS), a part of the
SPF/SRS protocol pair. Libsrs2 has been written from an entirely
clean codebase with compliance, speed and versatility in mind.
It is platform independent and has no external dependencies. It
is thread-safe and heap-safe, and is suitable for large scale
applications and embedded systems and can operate without many
standard system facilities.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q

%build
%configure
#./configure \
#    --prefix=%{_prefix} \
#    --libdir=%{_libdir} \
#    --enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_libdir}/lib*.so.*
%{_bindir}/*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Apr 2 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.18
- Rebuilt for Fedora
