Name: dcmtk
Summary: Offis DICOM Toolkit (DCMTK)
Version: 3.6.0
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
Source:  ftp://dicom.offis.de/pub/dicom/offis/software/dcmtk/dcmtk360/%{name}-%{version}.tar.gz
Patch1: dcmtk-3.6.0_shared.patch
Patch2: dcmtk-3.6.0_dcmjpls.patch
URL: http://dicom.offis.de/dcmtk.php.en
BuildRoot: %{_tmppath}/%{name}-%{version}-root

BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libxml2-devel
BuildRequires: openssl-devel
BuildRequires: tcp_wrappers-devel
BuildRequires: zlib-devel
BuildRequires: dos2unix

%description
DCMTK is a collection of libraries and applications implementing large
parts the DICOM standard. It includes software for examining,
constructing and converting DICOM image files, handling offline media,
sending and receiving images over a network connection, as well as
demonstrative image storage and worklist servers. DCMTK is is written
in a mixture of ANSI C and C++.  It comes in complete source code and
is made available as "open source" software. This package includes
multiple fixes taken from the "patched DCMTK" project.

Install DCMTK if you are working with DICOM format medical image files.

%package devel
Summary: Development Libraries and Headers for dcmtk
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development Libraries and Headers for dcmtk.  You only need to install
this if you are developing programs that use the dcmtk libraries.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%configure --with-private-tags
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
make install-lib DESTDIR=$RPM_BUILD_ROOT

#make sure libraries are executable
chmod 755 $RPM_BUILD_ROOT/usr/%{_lib}/*.so

#Move configuration file from /etc to /etc/dcmtk/
mv $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/%{name}
mkdir $RPM_BUILD_ROOT/etc
mv $RPM_BUILD_ROOT/%{name} $RPM_BUILD_ROOT/etc/


#Move doc files and man pages from /usr/share to temporary positions
mv $RPM_BUILD_ROOT/usr/share/doc/%{name} $RPM_BUILD_ROOT/usr/doc
mv $RPM_BUILD_ROOT/usr/share/man $RPM_BUILD_ROOT/usr/man

#Move remaining stuff in /usr/share (arch independent data) to /usr/share/dcmtk
mv $RPM_BUILD_ROOT/usr/share $RPM_BUILD_ROOT/usr/arch_independent
mkdir $RPM_BUILD_ROOT/usr/share/
mv $RPM_BUILD_ROOT/usr/arch_independent $RPM_BUILD_ROOT/usr/share/%{name}
#mv $RPM_BUILD_ROOT/usr/%{_lib}/dicom.dic $RPM_BUILD_ROOT/usr/share/%{name}/


#Move doc files and man pages from temporary positions to /usr/share/doc/dcmtk-name-version/
mkdir $RPM_BUILD_ROOT/usr/share/doc
mv $RPM_BUILD_ROOT/usr/doc $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/usr/share/man

#mkdir -p %{buildroot}/usr/%{_lib}/%{name}/
##mv %{buildroot}/usr/%{_lib}/*.so* %{buildroot}/usr/%{_lib}/%{name}/


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%docdir %{_docdir}/%{name}-%{version}/*
%{_docdir}/%{name}-%{version}/*
%{_bindir}/*
%{_libdir}/lib*.so
%config(noreplace) %{_sysconfdir}/%{name}/dcmpstat.cfg
%config(noreplace) %{_sysconfdir}/%{name}/dcmqrscp.cfg
%config(noreplace) %{_sysconfdir}/%{name}/filelog.cfg
%config(noreplace) %{_sysconfdir}/%{name}/logger.cfg
%config(noreplace) %{_sysconfdir}/%{name}/printers.cfg
%config(noreplace) %{_sysconfdir}/%{name}/storescp.cfg
%config(noreplace) %{_sysconfdir}/%{name}/storescu.cfg
%{_datadir}/%{name}/*
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%{_includedir}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Wed Mar 02 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 3.6.0-1.ossii
- Rebuild for OSSII

* Tue Jan 18 2011 Andy Loening <loening@alum dot mit dot edu> 3.6.0-1
- updates for 3.6.0

* Mon Mar 15 2010 Andy Loening <loening@alum dot mit dot edu> 3.5.4-3
- updates for packaging with fedora core
- multiple fixes/enhancements from pdcmtk version 48

* Sat Jan 02 2010 Andy Loening <loening@ alum dot mit dot edu> 3.5.4-2
- tlslayer.cc patch for openssl 1.0 

* Thu Feb 02 2006 Andy Loening <loening @ alum dot mit dot edu> 3.5.4-1
- initial build
