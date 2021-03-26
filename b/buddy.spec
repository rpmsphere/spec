Name: buddy
Summary: Binary decision-diagram library
Version: 2.4
Release: 2.1
Group: Development/Libraries
License: Public Domain
URL: http://buddy.sourceforge.net
Source0: https://sourceforge.net/projects/buddy/files/buddy/BuDDy%20%{version}/%{name}-%{version}.tar.gz

%description
Binary decision diagrams (BDDs) are space-efficient encodings of
boolean expressions or dynamic truth tables, used in eg. model
checking.  BuDDy is an efficient BDD library with all the standard
BDD operations, dynamic reordering of variables, automated garbage
collection, a C++ interface with automatic reference counting, and
more.

%package devel
Summary: Development files for BuDDy
Requires: %{name} = %{version}

%description devel
The BuDDy development package containing a static library and the
include files needed for building applications using BuDDy.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS NEWS README ChangeLog
%{_libdir}/libbdd.so.*

%files devel
%{_includedir}/bdd.h
%{_includedir}/bvec.h
%{_includedir}/fdd.h
%exclude %{_libdir}/libbdd.*a
%{_libdir}/libbdd.so

%changelog
* Fri Apr 13 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4
- Rebuild for Fedora
