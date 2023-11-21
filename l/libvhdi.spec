Name:		libvhdi
Version:	20160424
Release:	4.1
Summary:	Library to access the Virtual Hard Disk (VHD) image format
Group:		System Environment/Libraries
License:	LGPL
Source:		%{name}-alpha-%{version}.tar.gz
URL:		https://code.google.com/p/libvhdi/

%description
libvhdi is a library to access the Virtual Hard Disk (VHD) image format.

%package devel
Summary:	Header files and libraries for developing applications for libvhdi
Group:		Development/Libraries
Requires:	libvhdi = %{version}-%{release}

%description devel
Header files and libraries for developing applications for libvhdi.

%package tools
Summary:	Several tools for reading Virtual Hard Disk (VHD) image files
Group:		Applications/System
Requires:	libvhdi = %{version}-%{release}  fuse-libs
BuildRequires:	fuse-devel

%description tools
Several tools for reading Virtual Hard Disk (VHD) image files

%package python
Summary:	Python bindings for libvhdi
Group:		System Environment/Libraries
Requires:	libvhdi = %{version}-%{release} python
BuildRequires:	python-devel

%description python
Python bindings for libvhdi

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir} --enable-python
make %{?_smp_mflags}

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install

%clean
rm -rf ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%doc AUTHORS COPYING NEWS README ChangeLog
%{_libdir}/*.a
#{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvhdi.pc
%{_includedir}/*
%{_mandir}/man3/*

%files tools
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_bindir}/vhdiinfo
%attr(755,root,root) %{_bindir}/vhdimount
%{_mandir}/man1/*

%files python
%doc AUTHORS COPYING NEWS README
%{_libdir}/python*/site-packages/*.a
#{_libdir}/python*/site-packages/*.la
%{_libdir}/python*/site-packages/*.so

%changelog
* Wed May 18 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20160424
- Rebuilt for Fedora

* Fri Jan  8 2016 Lawrence R. Rogers <lrr@cmu.edu> 20160108-1
* Release 20160108-1
	20160108
	* 2016 update
	* worked on Python 3 support

* Sun Dec 20 2015 Lawrence R. Rogers <lrr@cmu.edu> 20151220-1
* Release 20151220-1
	20151220
	* updated dependencies
	* changes for deployment

* Sat Dec  5 2015 Lawrence R. Rogers <lrr@cmu.edu> 20151205-1
* Release 20151205-1
	20151205
	* worked on Python bindings

* Sat Sep  5 2015 Lawrence R. Rogers <lrr@cmu.edu> 20150905-1
* Release 20150905-1
	20150905
	* updated dependencies

	20150125
	* vhdiinfo: fix for handling missing parent filename

* Sat Jan 10 2015 Lawrence R. Rogers <lrr@cmu.edu> 20150110-1
* Release 20150110-1
	20150110
	* updated version for release

* Mon Jan  5 2015 Lawrence R. Rogers <lrr@cmu.edu> 20150105-1
* Release 20150105-1
	20150105
	* 2015 update

	20141229
	* updated dpkg files
	* updated dependencies
	* updated .gitignore

	20141221
	* worked on Python 3 support
	* worked on tests

	20141205
	* worked on test scripts

	20141129
	* code clean up

	20141114
	* code clean up

	20141105
	* worked on multi-threading support
	* removed deprecated functions
	  - libvhdi_file_read_random
	  - pyvhdi file.read_random

	20141029
	* bug fix in Python-bindings

	20141027
	* changes for deployment

* Tue Oct 21 2014 Lawrence R. Rogers <lrr@cmu.edu> 20141021-1
* Release 20141021-1
	20141021
	* changes for deployment

	20140929
	* removed README.macosx
	* changes for project site move

	20140803
	* bug fix in Python-bindings
	* updated dependencies

* Sun Mar 30 2014 Joachim Metz <joachim.metz@gmail.com> 20140330-1
- Auto-generated
