Name: hardinfo
Version: 0.5.1
Release: 15.1
Summary: System Profiler and Benchmark      
Group: Applications/System     
License: GPLv2        
URL: http://hardinfo.org/            
Source0:  http://download.berlios.de/hardinfo/%{name}-%{version}.tar.bz2
Patch0:  build-fix.diff
BuildRequires:  gtk2-devel
BuildRequires:  libsoup-devel
BuildRequires:  desktop-file-utils
BuildRequires:  pciutils
BuildRequires:  libtasn1-devel
BuildRequires:	libffi-devel
BuildRequires:	libselinux-devel
BuildRequires:	libmount-devel
Requires:  pciutils 
Requires:  glx-utils
Requires:  xorg-x11-utils
#Requires:  gcc
#Requires:  lm_sensors

%description
HardInfo can gather information about a system's hardware and operating system,
perform benchmarks, and generate printable reports either in HTML or in plain 
text formats.

%prep
%setup -q
%autopatch -p1
sed -i 's|/lib/|/%{_lib}/|' configure arch/linux/common/os.h

%build
export LIBDIR=%{_libdir}
%configure
make %{?_smp_mflags} ARCHOPTS="%{optflags} -std=gnu89"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir} 
desktop-file-install --vendor="" --delete-original  \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/hardinfo.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/hardinfo
%{_libdir}/hardinfo
%{_datadir}/hardinfo
%{_datadir}/applications/hardinfo.desktop
%doc LICENSE

%changelog
* Fri Jul 15 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.1
- Rebuilt for Fedora

* Mon Jan 12 2015 Nux <rpm@li.nux.ro> - 0.5.1-5
- build for EL7

* Mon Aug 06 2012 Scott Santos <halocaridina@gmail.com> - 0.5.1-4
- Rebuilt for EL6

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 10 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.5.1-1
- Update to 0.5.1

* Sun Mar 29 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.5c-1
- Update to 0.5c (bugfix release)

* Sat Mar 28 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.5b-1
- New upstream version
- Drop patches

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 04 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.3-8
- Apply the patch

* Sat Oct 04 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.3-7
- Fix build RH #465047

* Fri Jul 04 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.3-6
- Rebuild for new gnutls

* Thu Feb 14 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.3-5
- Rebuild for new libsoup

* Sat Feb 09 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.3-4
- Add libsoup-2.4 patch (RH#430960)

* Tue Jan 29 2008 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.3-3
- Rebuild for new libsoup

* Mon Nov 05 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.3-2
- Use --delete-original for desktopfile installation

* Sun Nov 04 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.3-1
- Update to new upstream version
- Drop obsolete patches

* Wed Sep 05 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-19
- Fix libz location (/lib(64) vs /usr/lib(64))

* Sun Sep 02 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-18
- Fix libz detection RH #274381

* Wed Aug 15 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-17
- Disable debug 

* Wed Aug 15 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-16
- New fix for RH #249794

* Wed Aug 15 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-15
- New fix for RH #249794

* Fri Aug 03 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-14
- Revert patch doesn't work 

* Fri Aug 03 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-13
- Update License tag

* Thu Aug 02 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-12
- Try again to fix RH #249794

* Tue Jul 31 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-11
- Enable debug output

* Mon Jul 30 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-10
- Fix changelog date ....

* Mon Jul 30 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-9
- Try to fix RH #249794 (upstream patch)

* Fri Jul 27 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-8
- Fix build

* Fri Jul 27 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-7
- bump release

* Fri Jul 27 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-6
- Specfile cleanups

* Fri Jul 27 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-5
- Add better sensors fix from upstream

* Thu Jul 26 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-4
- Fix and reenable sensor reading
- Remove zlib requires
- Fix group

* Wed Jul 25 2007 Jesse Keating <jkeating@redhat.com> - 0.4.2.2-3
- Rebuild for RH #249435

* Mon Jul 23 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-2
- In Fedora (human)uids start with 500 not 1000

* Mon Jul 23 2007 Adel Gadllah <adel.gadllah@gmail.com> 0.4.2.2-1
- Initial Build
