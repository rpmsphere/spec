Name:		epdf
Version:	0.1
Release:	1
Summary:	Epdf is PDF Library

Group:		User Interface/X
License:	BSD
URL:		http://www.enlightenment.org/pages/efl.html
Source:		%{name}-%{version}.tar.bz2
Patch0:		epdf-0.1-pdfver.patch
Patch1:         epdf-0.1-psoutputdev.patch

BuildRequires:	libtool-ltdl-devel, evas-devel, ecore-devel, libeina-devel
BuildRequires:	poppler-devel >= 0.10, doxygen
#Requires:

%description
Enlightenment PDF library.

%package devel
Summary: 	Epdf headers and development libraries.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Epdf development headers and libraries.


%prep
%setup -q
if [ $(rpm -q --qf "%%{version}" poppler|cut -d. -f2) -ge 12 ] ; then
%patch0 -p0
%patch1 -p0
fi


%build
export LDFLAGS=-leina
%configure --disable-static --disable-ewl
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
find $RPM_BUILD_ROOT -name '*.la' -delete


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING INSTALL NEWS README ChangeLog
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, -)
%{_bindir}/epdf*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%dir %{_includedir}/epdf
%{_includedir}/epdf/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Tue Oct 06 2009 Chelban Vasile <vchelban@fedoramd.org> 0.1-1
- first release
