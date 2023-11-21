Name:         libtpl
Summary:      Data Serialization C Library
URL:          https://tpl.sourceforge.net/
Group:        Libraries
License:      MIT
Version:      1.5
Release:      7.1
Source0:      https://switch.dl.sourceforge.net/tpl/libtpl-%{version}.tar.bz2

%description
Tpl is a library for serializing C data. The data is stored in its
natural binary form. The API is small and tries to stay "out of the
way". Tpl can serialize many C data types, including structures.

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
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/lib*.a
#{_libdir}/lib*.la
%{_libdir}/lib*.so

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuilt for Fedora
