Name:          librcps
Version:       0.3
Release:       2.1
Summary:       Resource constrained project scheduling library
Group:         System/Libraries
URL:           https://www.librcps.org
Source:        https://www.librcps.org/librcps-%{version}.tar.gz
License:       GPL
BuildRequires: glibc-devel

%description
LibRCPS aims to be a versatile, powerful and fast open source library for resource constrained project scheduling.

%package devel
Group:         Development/Libraries
Summary:       Static libraries and headers for %{name}
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
LibRCPS aims to be a versatile, powerful and fast open source library for resource constrained project scheduling.
This package contains static libraries and header files need for development.

%prep
%setup -q

%build
%configure
make

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall

%clean
rm -rf "$RPM_BUILD_ROOT"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/librcps.so.*
%doc AUTHORS COPYING ChangeLog NEWS README TODO

%files devel
%{_includedir}/librcps.h
%{_libdir}/librcps.a
#{_libdir}/librcps.la
%{_libdir}/librcps.so

%changelog
* Fri Jun 17 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
* Fri Jul 09 2010 Davide Madrisan <davide.madrisan@gmail.com> 0.3-1mamba
- package created by autospec
