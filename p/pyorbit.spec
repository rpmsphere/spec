%define __python /usr/bin/python2

Name: pyorbit
Version: 2.24.0
Release: 15
License: LGPLv2+
Group: Development/Languages
Summary: Python bindings for ORBit2
Source0: https://ftp.gnome.org/pub/GNOME/sources/pyorbit/2.24/%{name}-%{version}.tar.bz2
Requires: ORBit2
Requires: glib2
Requires: libIDL
Requires: python2
BuildRequires: ORBit2-devel
BuildRequires: glib2-devel
BuildRequires: libIDL-devel
BuildRequires: libtool
BuildRequires: python2-devel

# We don't want to provide private python extension libs.
%{?filter_setup:
%filter_provides_in %{python2_sitearch}/.*\.so$
%filter_setup
}

%description
pyorbit is an extension module for python that gives you access
to the ORBit2 CORBA ORB.

%package devel
Summary: Files needed to build wrappers for ORBit2 addon libraries
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description devel
This package contains files required to build wrappers for ORBit2 addon
libraries so that they interoperate with pyorbit

%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name "*.la" -exec rm -f {} ';'

%files
%doc AUTHORS NEWS README ChangeLog
%{python_sitearch}/*.so
%{python_sitearch}/*.py*

%files devel
%{_includedir}/pyorbit-2
%{_libdir}/pkgconfig/*.pc

%changelog
* Sun May 9 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.24.0
- Rebuilt for Fedora
* Tue Jan 28 2014 Daniel Mach <dmach@redhat.com> - 2.24.0-15
- Mass rebuild 2014-01-24
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.24.0-14
- Mass rebuild 2013-12-27
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Wed Nov 07 2012 Matthew Barnes <mbarnes@redhat.com> - 2.24.0-12
- Remove unused multilib patch.
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Sun Mar  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 2.24.0-10
- Bump NVR to be higher than F-16
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Fri Sep 24 2010 Parag Nemade <paragn@fedoraproject.org> - 2.24.0-7
- Merge-review cleanup (#226336)
* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.24.0-6
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild
* Fri Jan 08 2010 Matthew Barnes <mbarnes@redhat.com> - 2.24.0-5
- Fix the major version number in the Source URI.
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.24.0-2
- Rebuild for Python 2.6
* Tue Sep 23 2008 Matthew Barnes <mbarnes@redhat.com> - 2.24.0-1.fc10
- Update to 2.24.0
* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.14.3-3
- fix license tag
* Sun Feb 17 2008 Matthew Barnes <mbarnes@redhat.com> - 2.14.3-2.fc8
- Rebuild with GCC 4.3
* Wed Oct 10 2007 Matthew Barnes <mbarnes@redhat.com> - 2.14.3-1.fc8
- Update to 2.14.3
* Tue Apr 17 2007 Matthew Barnes <mbarnes@redhat.com> - 2.14.2-2.fc7
- Fix some file permissions (RH bug #236738).
- Spec file cleanups.
* Sun Feb 25 2007 Matthew Barnes <mbarnes@redhat.com> - 2.14.2-1.fc7
- Update to 2.14.2
* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.14.1-2
- rebuild for python 2.5
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.14.1-1.1
- rebuild
* Tue Jun 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-1
- Update to 2.14.1
* Mon Mar 13 2006 Ray Strode <rstrode@redhat.com> - 2.14.0-1
- Update to 2.14.0
* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.0.1-4.2.1
- bump again for double-long bug on ppc(64)
* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.0.1-4.2
- rebuilt for new gcc4.1 snapshot and glibc changes
* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt
* Sat Apr 16 2005 Florian La Roche <laroche@redhat.com>
- Copyright: -> License:
* Fri Nov 26 2004 Florian La Roche <laroche@redhat.com>
- add %%clean target
* Sun Nov  7 2004 Jeremy Katz <katzj@redhat.com> - 2.0.1-2
- rebuild for python 2.4
* Tue Sep 28 2004 Mark McLoughlin <markmc@redhat.com> 2.0.0-5
- Remove linc requires
- Fix multilib issue
* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Thu Nov  6 2003 Jeremy Katz <katzj@redhat.com> 2.0.0-2
- rebuild for python 2.3
* Thu Sep  4 2003 Jeremy Katz <katzj@redhat.com> 2.0.0-1
- 2.0.0
* Wed Aug 20 2003 Jeremy Katz <katzj@redhat.com> 1.99.6-1
- 1.99.6
* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Thu Feb  6 2003 Matt Wilson <msw@redhat.com> 1.99.3-5
- rebuild against new python
* Tue Jan 28 2003 Jeremy Katz <katzj@redhat.com> 1.99.3-4
- libdir-ify
* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt
* Sat Dec 28 2002 Jeremy Katz <katzj@redhat.com> 1.99.3-2
- fix defattr
* Fri Dec 27 2002 Jeremy Katz <katzj@redhat.com> 1.99.3-1
- update to pyorbit 1.99.3, obsolete orbit-python
* Thu Oct 31 2002 Matt Wilson <msw@redhat.com>
- use %%configure and %%makeinstall
- don't install .la files
- use %%_libdir for pkgconfig files
* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild
* Wed Feb 27 2002 Matt Wilson <msw@redhat.com>
- initial package
