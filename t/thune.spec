Summary: Thune Scripting Language
Name: thune
Version: 0.0.5
Release: 12.1
License: LGPL-2.1
URL: http://urlan.sf.net/
Group: Development/Languages
Source: thune-%{version}.tgz
BuildRequires: cmake

%description
Thune is an experimental interpreted language mixing ideas from Forth and Rebol.

%prep
%setup -q
sed -i '101s|printf(|printf("%s",|' console.c

%build
cmake .
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/thune
mkdir -p $RPM_BUILD_ROOT%{_libdir}
install -m 755 thune $RPM_BUILD_ROOT%{_bindir}
install -m 644 urlan.h       $RPM_BUILD_ROOT%{_includedir}/thune
install -m 644 urlan_atoms.h $RPM_BUILD_ROOT%{_includedir}/thune
install -m 644 bignum.h      $RPM_BUILD_ROOT%{_includedir}/thune
install -m 755 libthune.so $RPM_BUILD_ROOT%{_libdir}/libthune.so.0
ln -s libthune.so.0 $RPM_BUILD_ROOT%{_libdir}/libthune.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE doc/*Manual
%{_bindir}/thune
%{_libdir}/libthune.so
%{_libdir}/libthune.so.0
%{_includedir}/thune/urlan.h
%{_includedir}/thune/urlan_atoms.h
%{_includedir}/thune/bignum.h

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.5
- Rebuilt for Fedora
* Fri Mar 21 2008 Karl Robillard <wickedsmoke@users.sf.net>
- Initial package release.
