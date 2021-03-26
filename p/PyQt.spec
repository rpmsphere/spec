%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%define qt3 qt3
%define qt3version 3.3.8

Summary: Python bindings for Qt3
Name: PyQt
Version: 3.18.1
Release: 6%{?dist}

License: GPLv2
Group: Development/Languages
Url: http://www.riverbankcomputing.com/pyqt/
Source0: http://www.riverbankcomputing.com/static/Downloads/PyQt3/PyQt-x11-gpl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libXmu-devel
BuildRequires: python-devel
%if 0%{?qscintilla}
BuildRequires: qscintilla-devel
%else
Obsoletes: %{name}-qscintilla < %{version}-%{release}
%endif
BuildRequires: %{qt3}-devel >= %{qt3version}
BuildRequires: %{qt3}-MySQL %{qt3}-ODBC %{qt3}-PostgreSQL
BuildRequires: libXmu-devel

Provides: PyQt3 = %{version}-%{release}
%{?_isa:Provides: PyQt3%{?_isa} = %{version}-%{release}}

BuildRequires: sip-devel >= 4.9.1

Requires: %{qt3} >= %{qt3version}
%{?_sip_api:Requires: sip-api(%{_sip_api_major}) >= %{_sip_api}}


%description
These are Python bindings for Qt3.

%package devel
Summary: Files needed to build other bindings based on Qt3
Group: Development/Languages
Provides: PyQt3-devel = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
Requires: sip-devel
%if ! 0%{?qscintilla}
Obsoletes: %{name}-qscintilla-devel < %{version}-%{release}
%endif

%description devel
Files needed to build other bindings for C++ classes that inherit from any
of the Qt3 classes (e.g. KDE or your own).

%package examples
Summary: Examples for %{name} 
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description examples
Example code demonstrating how to use the Python bindings for Qt3.

%if 0%{?qscintilla}
%package qscintilla
Summary: %{name} qscintilla extentions
Group:   Development/Languages
Requires: %{name} = %{version}-%{release}

%description qscintilla 
%{summary}.

%package qscintilla-devel
Summary: Libraries and header files for %{name} development
Group:   Development/Libraries
Requires: %{name}-qscintilla = %{version}-%{release}
Requires: %{name}-devel

%description qscintilla-devel
%{summary}.
%endif


%prep
%setup -q -n %{name}-x11-gpl-%{version}%{?snap:-snapshot-%{snap}}


%build
QTDIR="" && . /etc/profile.d/qt.sh

echo yes | python configure.py -d %{python_sitearch} CXXFLAGS="%{optflags}" CFLAGS="%{optflags}"

# Makefiles are broken, workaround
make -C qt %{?_smp_mflags}
make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

mv examples3 examples


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README LICENSE NEWS
%{_bindir}/*
%{python_sitearch}/*
%{?qscintilla:%exclude %{python_sitearch}/qtext*.so}

%files devel
%defattr(-,root,root,-)
%{_datadir}/sip/*
%{?qscintilla:%exclude %{_datadir}/sip/qtext/}
%doc doc/PyQt.html

%files examples
%defattr(-,root,root,-)
%doc examples/README examples/*.py
%doc examples/*.png examples/*.gif examples/*.bmp

%if 0%{?qscintilla}
%files qscintilla
%defattr(-,root,root,-)
%{python_sitearch}/qtext*.so

%files qscintilla-devel
%defattr(-,root,root,-)
%{_datadir}/sip/qtext/
%endif


%changelog
* Thu Jan 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 3.18.1-6
- rebuild (sip)

* Mon Nov 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.18.1-5 
- Requires: sip-api(%%_sip_api_major) >= %%_sip_api

* Mon Nov 16 2009 Rex Dieter <rdieter@fedoraproject.org> 3.18.1-4
- rebuild for sip-4.9 (#537760)

* Thu Sep 10 2009 Than Ngo <than@redhat.com> - 3.18.1-3
- drop support fedora < 10

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.18.1-1
- PyQt-3.18.1

* Fri Jun 05 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.18-1
- PyQt-3.18

* Thu May 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.18-0.1.20090323
- PyQt-3.18-snapshot-20090323

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.17.6-2
- Rebuild for Python 2.6

* Mon Nov 17 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.17.6-1
- PyQt-3.17.6

* Mon Nov 10 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.17.5-1
- PyQt-3.17.5

* Wed Jun 18 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.17.4-5
- Provides: PyQt3(-devel)

* Tue Mar 25 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.17.4-4
- qt -> qt3 references

* Fri Feb 15 2008 Than Ngo <than@redhat.com> 3.17.4-3
- rebuilt against gcc-4.3

* Tue Jan 29 2008 Rex Dieter <rdieter@fedoraproject.org> - 3.17.4-2
- drop qscintilla support (f9+)

* Thu Dec 06 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.17.4-1
- 3.17.4

* Mon Nov 12 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.17.3-3
- Requires: sip >= %%{sip_version_used_to_build}

* Mon Nov 12 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.17.3-2
- -qscintilla(-devel) subpkgs
- License: GPLv2
- fix %%qtversion
- don't own %%_datadir/sip (sip-devel owns it)

* Mon Oct 22 2007 Than Ngo <than@redhat.com> - 3.17.3-1
- 3.17.3

* Thu Apr 12 2007 Than Ngo <than@redhat.com> - 3.17.1-1.fc7
- 3.17.1

* Thu Jan 18 2007 Than Ngo <than@redhat.com> - 3.17-3
- rebuilt

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 3.17-2
- rebuild for python 2.5

* Mon Nov 06 2006 Than Ngo <than@redhat.com> 3.17-1
- 3.17

* Wed Jul 19 2006 Than Ngo <than@redhat.com> 3.16-4
- rebuid against sip-4.4.5

* Tue Jul 18 2006 Than Ngo <than@redhat.com> 3.16-3
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.16-2.1
- rebuild

* Tue May 16 2006 Karsten Hopp <karsten@redhat.de> 3.16-2
- add some buildrequirements.

* Thu Apr 27 2006 Than Ngo <than@redhat.com> 3.16-1
- update to 3.16
- built with %%{optflags}

* Mon Feb 13 2006 Jesse Keating <jkeating@redhat.com> - 3.15-1.2.2
- rebump for build order issues during double-long bump

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.15-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.15-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Sep 12 2005 Than Ngo <than@redhat.com> 3.15-1
- update to 3.15

* Wed Mar 23 2005 Than Ngo <than@redhat.com> 3.14.1-1
- 3.14.1

* Fri Mar 04 2005 Than Ngo <than@redhat.com> 3.14-1
- 3.14

* Fri Jan 21 2005 Than Ngo <than@redhat.com> 3.13-3
- Add missing sip dependency

* Sat Nov 13 2004 Than Ngo <than@redhat.com> 3.13-2
- rebuilt against python 2.4

* Fri Sep 24 2004 Than Ngo <than@redhat.com> 3.13-1
- update to 3.13

* Fri Jun 18 2004 Than Ngo <than@redhat.com> 3.12-3
- rebuilt against gcc 3.4

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 27 2004 Than Ngo <than@redhat.com> 3.12-1
- update to 3.12
- add BuildRequires on python-devel sip-devel , bug #124417

* Fri Mar 12 2004 Than Ngo <than@redhat.com> 3.11-1
- 3.11

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 12 2004 Than Ngo <than@redhat.com> 3.10-3
- add some patch files from CVS, which supports Qt 3.3.0

* Thu Feb 12 2004 Than Ngo <than@redhat.com> 3.10-2
- use new methode of building SIP

* Wed Feb 11 2004 Than Ngo <than@redhat.com> 3.10-1
- 3.10 release
- build against qt 3.3.0

* Thu Nov 27 2003 Than Ngo <than@redhat.com> 3.8.1-3
- rebuild against python 2.3/ Qt 3.2.3

* Mon Sep 29 2003 Than Ngo <than@redhat.com> 3.8.1-2
- added sip_version

* Sat Sep 27 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- 3.8.1

* Mon Jul 21 2003 Than Ngo <than@redhat.com> 3.7-1
- 3.7

* Tue Jun 24 2003 Than Ngo <than@redhat.com> 3.6-4
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 6 2003 Than Ngo <than@redhat.com> 3.6-2.1
- fix search path problem (bug #87476)

* Mon Apr 28 2003 Than Ngo <than@redhat.com> 3.6-1
- 3.6
- remove unneeded patch file

* Mon Apr 21 2003 Elliot Lee <sopwith@redhat.com> 3.5.1-0.20030303.1
- Fix build for smp_mflags

* Tue Mar  4 2003 Than Ngo <than@redhat.com> 3.5.1-0.20030303.0
- snapshot 20030303, support qt 3.1.2

* Thu Feb  6 2003 Mihai Ibanescu <misa@redhat.com> 3.5-5
- rebuilt against new python

* Thu Jan 30 2003 Than Ngo <than@redhat.com> 3.5-4
- excludearch alpha
- disable smp_flag on s390

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 08 2003 Elliot Lee <sopwith@redhat.com> 3.5-3
- Don't exclude alpha

* Tue Dec 11 2002 Than Ngo <than@redhat.com> 3.5-2
- fix typo

* Tue Dec 11 2002 Than Ngo <than@redhat.com> 3.5-1
- 3.5 release

* Mon Nov 18 2002 Than Ngo <than@redhat.com> 3.5-0.20021114.1
- Release Candidate, which supports qt 3.1.0
- fix dependency problem with python

* Thu Nov  7 2002 Than Ngo <than@redhat.com> 3.4-1
- 3.4

* Sat Aug 24 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- to not enable parallel make
- specfile cleanups
- again excludearch alpha

* Mon Aug 12 2002 Than Ngo <than@redhat.com> 3.3.2-3
- rebuild using new gcc-3.2-0.3
- remove excludearch alpha

* Tue Jul 23 2002 Than Ngo <than@redhat.com> 3.3.2-2
- rebuild to get rid of deps

* Tue Jul 23 2002 Than Ngo <than@redhat.com> 3.3.2-1
- 3.3.2 release for qt 3.0.5

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 22 2002 Harald Hoyer <harald@redhat.de>
- updated to version 3.2.4

* Thu May 02 2002 Than Ngo <than@redhat.com> 3.2-0.rc4.1
- 3.2rc4
- build against python 2

* Tue Apr 16 2002 Than Ngo <than@redhat.com> 3.1-2
- rebuild

* Fri Mar 29 2002 Than Ngo <than@redhat.com> 3.1-1
- update 3.1 for qt 3.0.3

* Fri Mar  8 2002 Than Ngo <than@redhat.com> 3.0-4
- rebuild against qt-3
- fix Url

* Fri Feb 22 2002 Than Ngo <than@redhat.com> 3.0-3
- rebuild against python 1.5.2 and qt 2.3.2

* Wed Jan 16 2002 Than Ngo <than@redhat.com> 3.0-1
- update to 3.0
- add 4 official patches
- build against qt 3

* Tue Aug 14 2001 Than Ngo <than@redhat.com> 2.5-1
- update to 2.5
- add patch from alane@geeksrus.net (bug #54627)

* Mon Apr 23 2001 Than Ngo <than@redhat.com>
- update to 2.4
- remove a g++ patch, since the bug is fixed in current gcc-2.96-81

* Wed Feb 28 2001 Tim Powers <timp@redhat.com>
- rebuilt against new libmng

* Fri Feb 23 2001 Than Ngo <than@redhat.com>
- rebuild against sip-2.3-2

* Thu Feb 22 2001 Than Ngo <than@redhat.com>
- update to 2.3
- use python 1.5

* Fri Feb 02 2001 Than Ngo <than@redhat.com>
- fixed to build against gcc-2.96-72

* Wed Jan 10 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Don't require a package we aren't shipping (python2 >= 2.0,
  not python >= 2.0)

* Tue Dec 26 2000 Than Ngo <than@redhat.com>
- rebuild against the new qt-2.2.3
- fixed to build with python 2.0
- add missing PyQt docs

* Mon Nov 20 2000 Tim Powers <timp@redhat.com>
- rebuilt to fix bad dir perms

* Wed Nov 8 2000 Than Ngo <than@redhat.com>
- update to 2.2
- fixed BuildPrereq

* Tue Oct 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- remove bogus requirement on python-%%{pythonver}, there's no such
  thing as a python-1.5 package and we actually use version 1.5.2
  Than: I take this VERY seriously... "It compiles, therefore it
  works!" is a registered trademark of myself. ;)
- some fixes to spec file
- update URL

* Mon Oct 23 2000 Than Ngo <than@redhat.com>
- update to 2.1
- add requires python

* Thu Jul 27 2000 Than Ngo <than@redhat.de>
- don't hardcode Qt version
- add defattr

* Mon Jul 17 2000 Tim Powers <timp@redhat.com>
- added defattr

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- rebuilt with the new qt

* Sat May 27 2000 Ngo Than <than@redhat.de>
- update 0.12 for 7.0

* Mon May  8 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.11.1
- Qt 2.1.0

* Wed Feb  2 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 0.10.1
- Qt 1.45
- handle RPM_OPT_FLAGS
- fix download URL
- -devel and -examples require base package

* Tue Dec 21 1999 Ngo Than <than@redhat.de>
- updated 0.10

* Tue Dec 14 1999 Ngo Than <than@redhat.de>
- 0.10pre5

* Sun Nov 28 1999 Ngo Than <than@redhat.de>
- adapted for powertools-6.2

* Fri Aug 13 1998 Pieter Nagel <pnagel@e.co.za>
- Initial packaging as RPM
