Name: elfhacks
Summary: Various ELF run-time hacks
Version: 0.1
Release: 13.1
License: GPL
Group: System/Libraries
Source: elfhacks.tar.gz
URL: https://nullkey.ath.cx/elfhacks/html/
BuildRequires: cmake gcc-c++

%description
This package contains the libraries of various ELF run-time hacks.

%package devel
Summary: Various ELF run-time hacks, development files
Group: System/Development

%description devel
various ELF run-time hacks
this package contains header files.

%prep
%setup -q -n elfhacks
%ifarch x86_64 aarch64
sed -i '47i #define __elf64' src/elfhacks.h
%endif

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

%ifnarch x86_64 aarch64
make DESTDIR=$RPM_BUILD_ROOT LIBDIR=lib
%else
make DESTDIR=$RPM_BUILD_ROOT LIBDIR=lib64
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ifnarch x86_64 aarch64
make DESTDIR=$RPM_BUILD_ROOT LIBDIR=lib install
%else
make DESTDIR=$RPM_BUILD_ROOT LIBDIR=lib64 install
cd $RPM_BUILD_ROOT/usr
mv lib lib64
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files 
%{_libdir}/libelfhacks.so.0
%{_libdir}/libelfhacks.so.0.4.1

%files devel
%{_includedir}/elfhacks.h
%{_libdir}/libelfhacks.so

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Thu Jun 25 2008 Mathias Homann <admin@eregion.de>
- initial import
