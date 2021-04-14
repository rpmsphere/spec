Name: ccif
Summary: C library for handling CCIF files
Version: 0.3.20111209
Release: 6.1
License: LGPLv3
Group: System Environment/Libraries
URL: http://www.ccp4.ac.uk
Source0: ftp://ftp.ccp4.ac.uk/opensource/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Library for low level manipulation of CCIF files.
CCIF is a subset of the mmCIF format,
proposed as a replacement for the PDB format for holding coordinate data.

This library is written by Peter Keller and is a part of the CCP4 suite.

%package devel
Summary: Development files for ccif library
Requires: %{name} = %{version}-%{release}
Group: Development/Libraries

%description devel
Files needed for developing apps using ccif library.

ccif library provides access to CCIF files that contain macromolecular
coordinate data.

%prep
%setup -q

%build
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING* README
%{_libdir}/libccif.so.*
%dir %{_datadir}/ccif
%{_datadir}/ccif/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libccif.so

%changelog
* Tue Aug 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.20111209
- Rebuilt for Fedora
* Thu Dec 9 2011 Marcin Wojdyr <wojdyr@gmail.com> - 0.3.20111209-1
- updated tarball
