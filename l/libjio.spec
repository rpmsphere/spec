Name:         libjio
Summary:      Journaled Transactional I/O Library
URL:          http://blitiri.com.ar/p/libjio/
Group:        Libraries
License:      OSL
Version:      1.02
Release:      12.1
Source0:      http://blitiri.com.ar/p/libjio/files/%{version}/libjio-%{version}.tar.gz

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%description
Libjio is a user-space C library to do journaled,
transaction-oriented I/O. It provides a very simple API to commit
and rollback transactions, and on top of that a UNIX-alike set of
functions to perform most regular operations (i.e. open(), read(),
write()) in a non-intrusive threadsafe and atomic way, with safe
and fast crash recovery. This allows the library to guarantee file
integrity even after unexpected crashes, never leaving your files in
an inconsistent state. On the disk, the file you work on is exactly
like a regular one, but a special directory is created to store
in-flight transactions.

%prep
%setup -q

%build
cd libjio
%{__make} %{_smp_mflags} \
      CC="%{__cc}" \
      CFLAGS="%{optflags -O} -std=c99" \
      build/libjio.a build/libjio.pc build/jiofsck

%install
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_bindir} \
    $RPM_BUILD_ROOT%{_includedir} \
    $RPM_BUILD_ROOT%{_libdir} \
    $RPM_BUILD_ROOT%{_libdir}/pkgconfig
cd libjio
install -c -m 755 \
      build/jiofsck $RPM_BUILD_ROOT%{_bindir}/
install -c -m 644 \
      libjio.h $RPM_BUILD_ROOT%{_includedir}/
install -c -m 644 \
      build/libjio.a $RPM_BUILD_ROOT%{_libdir}/
install -c -m 644 \
      build/libjio.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/

%files
%doc doc/*
%{_bindir}/*

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.02
- Rebuilt for Fedora
