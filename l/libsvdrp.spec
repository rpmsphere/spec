Summary: 	An interface to VDR via SVDRP protocol
Name: 		libsvdrp
Version: 	0.0.1r35
Release: 	1
License: 	LGPL
Group: 		Application/Multimedia
URL:		http://hg.geexbox.org/libsvdrp
Source0: 	http://sources.openbricks.org/devel/libsvdrp-r35.tar.bz2

%description
libsvdrp is an interface library to allow C programs to interact
with the Linux Video Disc Recorder VDR using the SVDRP protocol.

%package devel
Summary: Development files for libsvdrp
Requires: %{name} = %{version}

%description devel
libsvdrp is an interface library to allow C programs to interact
with the Linux Video Disc Recorder VDR using the SVDRP protocol.
This package contains the development files.

%prep
%setup -q -n %{name}-r35

%build
%configure
make

%install
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS COPYING README
%{_bindir}/getwakeup
%{_libdir}/libsvdrp.so.*

%files devel
%{_includedir}/*
%{_libdir}/libsvdrp.a
%{_libdir}/libsvdrp.la
%{_libdir}/libsvdrp.so
%{_libdir}/pkgconfig/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1r35
- Rebuild for Fedora
