%global debug_package %{nil}

Summary: New Standard C Library
Name:	 musl
Version: 1.1.24
Release: 1
Source0: http://www.musl-libc.org/releases/%{name}-%{version}.tar.gz
License: LGPLv2+
Group:	 Development/C
URL:	 http://www.musl-libc.org/
BuildRequires: zlib-devel

%description
musl is a new standard library to power Linux-based devices.  It is
lightweight, fast, simple, free, and strives to be correct in the sense of
standards-conformance and safety.

%package devel
Summary:	Development files for %{name}
Group:		Development/C
License:	LGPLv2+
Conflicts:  glibc, glibc-headers

%description devel
musl is a new standard library to power Linux-based devices.  It is
lightweight, fast, simple, free, and strives to be correct in the sense of
standards-conformance and safety.

%prep
%setup -q
sed -i '/__tls_get_new/d' src/ldso/*/tlsdesc.s

%build
sed 's!/usr/local!/usr/lib!' dist/config.mak > config.mak
# set arch:
%ifnarch %ix86
sed -i "s/i386/%_arch/" config.mak
%endif
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%doc INSTALL README WHATSNEW 
%{_libdir}/lib*.so
%{_libdir}/*.o
%{_libdir}/lib*.a
%{_libdir}/musl-gcc.specs
%{_includedir}/*
%{_bindir}/*

%changelog
* Mon Oct 14 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.24
- Rebuilt for Fedora
* Thu Jan 12 2012 tv <tv> 0.8.3-0.1.mga2
+ Revision: 195390
- imported package musl
