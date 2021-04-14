%undefine _debugsource_packages

Name:         libbls
Summary:      Efficient Data Manipulation Library
URL:          http://libbls.hellug.gr/
Group:        Libraries
License:      LGPL
Version:      0.3.0
Release:      12.2
Source0:      http://libbls.hellug.gr/libbls-%{version}.tar.gz
Patch:        libbls.patch
BuildRequires: python2-scons

%description
libbls is a highly efficient, flexible and robust data manipulation
library in the form of an editable buffer. An editable buffer
is a data structure which stores data and allows for efficient
insert, replace, delete, copy, multiple undo and redo editing
operations. libbls does all these in a fast and memory efficient
manner, combining data from both memory and arbitrary sized chunks
from files.

%package devel
Summary: Development files for %{name}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q
%patch -p0

%build
scons \
    lfs=0 \
    destdir=$RPM_BUILD_ROOT \
    prefix=%{_prefix} \
    includedir=%{_includedir} \
    libdir=%{_libdir} \
    lib

%install
rm -rf $RPM_BUILD_ROOT
scons \
    lfs=0 \
    destdir=$RPM_BUILD_ROOT \
    prefix=%{_prefix} \
    includedir=%{_includedir} \
    libdir=%{_libdir} \
    install-links=no \
    install

%files devel
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuilt for Fedora
