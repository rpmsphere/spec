Summary: Buffer manager abstraction library
Name:    libwsbm       
Version: 1.1.0
Release: 5.11
Group:   Development/Libraries       
License: MIT
Source: libwsbm-src.1.1.0.tar.bz2
Patch0: libwsbm.patch
URL:  http://www.x.org/wiki/libwsbm
BuildRequires: autoconf libdrm-devel psb-headers
   
%description
The libwsbm (wsbm stands for Window System Buffer Manager) library previously lived as
a dri buffer manager within mesa. 

%package devel
Summary: Development headers for libwsbm
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development headers (Graphics) for libwsbm

%prep
%setup -q -n libwsbm

#libswbm.patch 
%patch0 -p1  

%build
./autogen.sh
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=${RPM_BUILD_ROOT} make install

find ${RPM_BUILD_ROOT} -name "*.la" -delete

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root,-)
%{_libdir}/libwsbm.so.1
%{_libdir}/libwsbm.so.1.1.0


%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/libwsbm.pc
%{_libdir}/libwsbm.so
%{_includedir}/wsbm/*.h





%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Wed Jun 30 2010 chris.e.ferron@linux.intel.com
- added patch to fix memory leak for EXA under gnome for powerVR driver sharebuffer issue.
* Thu Apr 29 2010 Anas Nashif <anas.nashif@intel.com> - 1.1.0
- Make it exclusive to %%ix86
* Mon Aug 24 2009 Priya Vijayan <priya.vijayan@intel.com> 1.1.0
- Update to 1.1.0 beta
* Sun Aug 16 2009 Anas Nashif <anas.nashif@intel.com> - 1.1.0_20090609
- Use _ instead of ~ in version
* Tue Jun 16 2009 Priya Vijayan <priya.vijayan@intel.com> 1.1.0~20090318
- Update to 1.1.0-1.0.7.20090609
* Tue Apr 14 2009 Anas Nashif <anas.nashif@intel.com> 1.1.0~20090318
- Added missing required packagein -devel
* Fri Mar 27 2009 Anas Nashif <anas.nashif@intel.com> 1.1.0~20090318
- Fixed BuildRequires, now use psb-headers
* Fri Mar 27 2009 Anas Nashif <anas.nashif@intel.com> 1.1.0~20090318
- Fixed Requires
* Wed Feb 25 2009 bjhueni <bret.j.hueni@intel.com> 1.0.5
- request package merge to MRST. Build & install testing completed
* Fri Jan 16 2009 Priya Vijayan <priya.vijayan@intel.com> 1.0.2
- Updating source
* Tue Jan  6 2009 Priya Vijayan <priya.vijayan@intel.com> 1.0.1
- fixed spec
* Tue Jan  6 2009 Priya Vijayan <priya.vijayan@intel.com> 1.0.0
- Update to 1.0.1-working combination with X Server
* Thu Nov 27 2008 Yin Kangkai <kangkai.yin@intel.com>
- actually compress the tar ball to bz2 format
  * Nov 2008 Priya Vijayan <Initial import to MRST>
- Version 0.28
