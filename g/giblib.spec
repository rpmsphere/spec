Summary: Simple library and a wrapper for imlib2
Name: giblib
Version: 1.2.4
Release: 28
License: MIT
Group: System Environment/Libraries
# It looks like this project has been abandoned...
URL: http://linuxbrit.co.uk/giblib/
Source: http://linuxbrit.co.uk/downloads/giblib-%{version}.tar.gz
Patch0: giblib-1.2.4-multilib.patch
BuildRequires: imlib2-devel

%description
giblib is a utility library used by many of the applications from
linuxbrit.co.uk. It incorporates doubly linked lists, some string
functions, and a wrapper for imlib2. The wrapper does two things.
It gives you access to fontstyles, which can be loaded from files,
saved to files or defined dynamically through the API. It also,
and more importantly, wraps imlib2's context API.

%package devel
Summary: Static library and header files for giblib
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: imlib2-devel, pkgconfig

%description devel
Install this package if you intend to develop using the giblib library.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_prefix}/doc/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING ChangeLog
%{_libdir}/*.so.*

%files devel
%{_bindir}/*-config
%{_includedir}/*
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Dec 27 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.4
- Rebuilt for Fedora
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 24 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.4-21
- Append dist tag

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Matthias Saou <http://freshrpms.net/> 1.2.4-12
- Fix multilib conflict in the config script.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 1.2.4-10
- Rebuild for new BuildID feature.

* Sat Aug  4 2007 Matthias Saou <http://freshrpms.net/> 1.2.4-9
- Fix License field, it's "MIT" not "GPL".

* Fri Jun 22 2007 Matthias Saou <http://freshrpms.net/> 1.2.4-8
- Use DESTDIR install method.
- Disable building static library and remove it from the devel package.
- Remove dist, as it might be a while before the next rebuild.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.2.4-7
- FC6 rebuild.
- Require exact release in the devel sub-package.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.2.4-6
- FC5 rebuild.

* Wed Feb  8 2006 Matthias Saou <http://freshrpms.net/> 1.2.4-5
- Rebuild for new gcc/glibc.

* Mon Jan 23 2006 Matthias Saou <http://freshrpms.net/> 1.2.4-4
- Rebuilt for FC5.
- Switch back /sbin/ldconfig calls to use -p.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 1.2.4-2
- Bump release to provide Extras upgrade path.

* Mon Sep  6 2004 Matthias Saou <http://freshrpms.net/> 1.2.4-1
- Update to 1.2.4.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 1.2.3-4
- Rebuilt for Fedora Core 2.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.2.3-3
- Rebuilt for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Feb 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.3.

* Wed Nov 13 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.
