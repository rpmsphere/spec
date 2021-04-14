Summary: Globalization Library
Name: g11n
Version: 0.9
Release: 1
License: GPL
Group: System/Libraries
URL: http://people.debian.org.tw/~chihchun/debian/g11n/
Source: %{name}-%{version}.tar.gz

%description
G11N Library is developed by Brian Lin for Software Globalization.
It is a better solution than i18n.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
make install ROOTDIR=%{buildroot}
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf %{buildroot}

%files
%doc docs/*
%{_libdir}/libg11n.a
%{_libdir}/libg11n.so
%{_libdir}/libg11n.so.0
%{_libdir}/libg11n.so.0.8
%{_includedir}/g11n.h
%{_includedir}/gcs.h
%{_includedir}/gcschar.h

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9
- Rebuilt for Fedora
* Wed Dec 15 1999 Brian Lin <foxman@xlinux.com>
- create an automatic build script
