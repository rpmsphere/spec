%define _name ZThread

Name: zthread
Version: 2.3.2
Release: 15.1
Summary: Cross-platform c++ multi-threading framework
License: MIT
Group: Development/Libraries
URL: http://zthread.sourceforge.net/
Source: ftp://download.sourceforge.net/pub/sourceforge/zthread/%_name-%version.tar.gz

%description
ZThreads is an advanced platform-independant, Object-Oriented threading and
synchronization library. It has been designed and tested under POSIX & Win32
systems. It is not just another thread wrapper. 

%package devel
Summary: Development tools for ZThread
Group: Development/Libraries
Requires: %name = %version

%description devel
The %name-devel package contains the static libraries and header files
needed for development with %name.

%prep
%setup -q -n %_name-%version
sed -i 's|:space:|[:space:]|g' configure

%build
%configure
sed -i -e 's| $(bindir)| $(DESTDIR)$(bindir)|' -e 's| $(datadir)/aclocal| $(DESTDIR)$(datadir)/aclocal|' Makefile
sed -i 's|-DNDEBUG|-DNDEBUG -fpermissive|' src/Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/lib*.so.*
%doc AUTHORS COPYING INSTALL NEWS README LICENSE MIT.TXT TODO ChangeLog
%doc doc/*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.*a
%{_datadir}/aclocal/*.m4
%{_bindir}/zthread-config

%changelog
* Tue Mar 10 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.2
- Rebuilt for Fedora
* Sun Mar 13 2005 Bastiaan Bakker <bastiaan.bakker@lifeline.nl>
- Initial package
