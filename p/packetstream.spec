Name: packetstream
Summary: Thread-safe ring buffer library with shm support
Version: 0.1
Release: 14.1
License: GPL
Group: System/Libraries
Source: packetstream.tar.gz
URL: https://nullkey.ath.cx/packetstream/html/
BuildRequires: cmake gcc-c++

%description
This package contains the libraries of thread-safe ring buffer library with shm support.

%package devel
Summary: Thread-safe ring buffer library with shm support, development files
Group: System/Development

%description devel
This package contains header files of thread-safe ring buffer library with shm support.

%prep
%setup -q -n packetstream

%build
LIBDIR=lib
%ifarch x86_64 aarch64
LIBDIR=lib64
%endif

CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
cmake . \
         -DCMAKE_INSTALL_PREFIX:PATH="/usr" \
         -DCMAKE_BUILD_TYPE:STRING="Release" \
         -DCMAKE_C_FLAGS_RELEASE_RELEASE:STRING="${CFLAGS}"

make -j 2

%install
rm -rf $RPM_BUILD_ROOT
%ifarch x86_64 aarch64
make DESTDIR=$RPM_BUILD_ROOT LIBDIR=lib64 install
cd $RPM_BUILD_ROOT/usr
mv lib lib64
%else
make DESTDIR=$RPM_BUILD_ROOT LIBDIR=lib install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files 
%{_libdir}/libpacketstream.so.0
%{_libdir}/libpacketstream.so.0.1.4          

%files devel
/usr/include/packetstream.h
%{_libdir}/libpacketstream.so

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Thu Jun 25 2008 Mathias Homann <admin@eregion.de>
- initial import
