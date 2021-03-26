Summary: A library to read Paradox DB files
Name: pxlib
Version: 0.6.5
Release: 8.1
License: GPL
Group: System/Libraries
URL: http://pxlib.sourceforge.net/
Source: http://prdownloads.sourceforge.net/pxlib/%{name}-%{version}.tar.gz
BuildRequires: autoconf
BuildRequires: sqlite-devel
BuildRequires: libgsf-devel
BuildRequires: intltool
BuildRequires: docbook2X docbook-utils
BuildRequires: glib2-devel
BuildRequires: w3m

%description
pxlib is a simply and still small C library to read Paradox DB files. It
supports all versions starting from 3.0. It currently has a very limited set of
functions like to open a DB file, read its header and read every single record.

%package devel
Summary: A library to read Paradox DB files (Development)
Group: Development/C
Requires: %name = %{version}

%description devel
pxlib is a simply and still small C library to read Paradox DB files. It
supports all versions starting from 3.0. It currently has a very limited set of
functions like to open a DB file, read its header and read every single record.

%prep
%setup -q

%build
export CPPFLAGS=`pkg-config --cflags glib-2.0`
%configure  --with-sqlite --with-gsf
make LIBS=-lm

%install
rm -rf %{buildroot}
%makeinstall
rm %{buildroot}%{_libdir}/*.la
%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%doc README AUTHORS ChangeLog
%_libdir/libpx.so.*

%files devel
%_libdir/lib*.so
%_libdir/*.a
%_libdir/pkgconfig/*
%_includedir/*

%changelog
* Sat Apr 20 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.5
- Rebuild for Fedora
* Thu Oct 18 2012 Mandriva
- Initial package
