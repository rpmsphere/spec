%global debug_package %{nil}

Summary:    BGI-compatible 2D graphics C library
Name:       xbgi
Version:    364
Release:    4.1
License:    Free software
Group:      Development/Libraries
Source:     http://www.garret.ru/%{name}-%{version}.tar.gz
URL:        http://www.garret.ru/lang.html
BuildRequires:   libX11-devel

%description
This package contains a Borland Graphics Interface (BGI) emulation
library for X11. This library strictly emulates most BGI functions,
making it possible to compile X11 versions of programs written for
Turbo/Borland C. RGB extensions and basic mouse support are also
implemented.

%prep
%setup -q

%build
make -C src

%install
install -Dm744 src/libXbgi.a $RPM_BUILD_ROOT/%{_libdir}/libXbgi.a
install -Dm644 src/graphics.h $RPM_BUILD_ROOT/%{_includedir}/graphics.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc *.txt README
%{_libdir}/libXbgi.a
%{_includedir}/graphics.h

%changelog
* Fri Jan 24 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 364
- Rebuild for Fedora
* Wed Nov 27 2012 Guido Gonzato <guido.gonzato at gmail.com>
This is a generic rpm, buildable on Ubuntu
