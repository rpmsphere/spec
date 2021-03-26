Name:          libbraille
Version:       0.19.0
Release:       4.1
Summary:       A library which makes it possible to easily develop for Braille displays
Group:         System/Libraries
URL:           http://libbraille.org/
Source:        http://prdownloads.sourceforge.net/libbraille/libbraille-%{version}.tar.gz
License:       LGPL
BuildRequires: libusb-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

%description
Libbraille is a computer shared library which makes it possible to easily develop
for Braille displays. It provides a simple API to write text on the display,
directly draw dots, or get the value of keys pressed on the Braille keyboard.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
Libbraille is a computer shared library which makes it possible to easily develop
for Braille displays. It provides a simple API to write text on the display,
directly draw dots, or get the value of keys pressed on the Braille keyboard.

This package contains static libraries and header files need for development.

%prep
%setup -q
sed -i 's/libusb-config/pkg-config libusb/' configure

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/libbraille.conf
%{_bindir}/test_libbraille
%{_libdir}/libbraille-0.so.*
%dir %{_libdir}/libbraille
%{_libdir}/libbraille/*
%dir %{_datadir}/libbraille
%{_datadir}/libbraille/*
%doc AUTHORS COPYING ChangeLog README TODO

%files devel
%defattr(-,root,root)
%dir %{_includedir}
%{_libdir}/libbraille.a
%{_libdir}/libbraille.la
%{_libdir}/libbraille.so
%{_includedir}/*.h

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.19.0
- Rebuild for Fedora

* Wed Sep 16 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.19.0-1mamba
- package created by autospec
