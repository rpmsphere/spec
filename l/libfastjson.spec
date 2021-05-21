Name:           libfastjson
Version:        0.99.2
Release:        3.1
Summary:        Fast JSON parsing library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/rsyslog/libfastjson
Source:         http://download.rsyslog.com/libfastjson/%{name}-%{version}.tar.gz

%description
A fast JSON parsing library, a fork of json-c, developed by the rsyslog team
and used for rsyslog and liblognorm.

%package devel
Summary:        Development headers and libraries for libfastjson
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
A fast JSON parsing library, a fork of json-c, developed by the rsyslog team
and used for rsyslog and liblognorm.

This package includes header files and scripts needed for developers
using the libfastjson library

%prep
%setup -q

%build
%configure --disable-static --with-pic
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING
%{_libdir}/libfastjson.so.*

%files devel
%{_libdir}/libfastjson.so
%{_includedir}/libfastjson
%{_libdir}/pkgconfig/libfastjson.pc

%changelog
* Tue Jun 21 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.99.2
- Rebuilt for Fedora
* Sun Mar 13 2016 astieger@suse.com
- update to 0.99.2
  * new API: json_object_get_member_count()
  * make comaptible with autoconf < 2.64
  * 0.99.1 was not released
* Sat Jan  2 2016 astieger@suse.com
- initial package
