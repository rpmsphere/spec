%global with_python3 1

%if 0%{?with_python3}
%{!?python3_inc:%global python3_inc %(%{__python3} -c "from distutils.sysconfig import get_python_inc; print(get_python_inc(1))")}
%endif
%{!?python_sitearch:%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%{!?python_inc:%global python_inc %(%{__python} -c "from distutils.sysconfig import get_python_inc; print get_python_inc(1)")}

Summary: SIP - Python/C++ Bindings Generator
Name: sip
Version: 4.10.3
Release: 1%{?dist}
License: GPLv2 or GPLv3
Group: Development/Tools
Url: http://www.riverbankcomputing.com/software/sip/intro 
Source0: http://www.riverbankcomputing.com/static/Downloads/sip4/sip-%{version}%{?snap:-snapshot-%{snap}}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# extracted from sip.h, SIP_API_MAJOR_NR SIP_API_MINOR_NR defines
Source1: macros.sip
%global _sip_api_major 7
%global _sip_api_minor 1 
%global _sip_api %{_sip_api_major}.%{_sip_api_minor}

Provides: sip-api(%{_sip_api_major}) = %{_sip_api}

BuildRequires: python-devel
BuildRequires: sed

%if 0%{?with_python3}
BuildRequires:  python3-devel
%endif

%description
SIP is a tool for generating bindings for C++ classes so that they can be
accessed as normal Python classes. SIP takes many of its ideas from SWIG but,
because it is specifically designed for C++ and Python, is able to generate
tighter bindings. SIP is so called because it is a small SWIG.

SIP was originally designed to generate Python bindings for KDE and so has
explicit support for the signal slot mechanism used by the Qt/KDE class
libraries. However, SIP can be used to generate Python bindings for any C++
class library.


%package devel
Summary: Files needed to generate Python bindings for any C++ class library
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-macros = %{version}-%{release}
Requires: python-devel 
%description devel
This package contains files needed to generate Python bindings for any C++
classes library.


%package macros
Summary: RPM macros for use when working with SIP
Group: Development/Tools
Requires: rpm
%description macros
This package contains RPM macros for use when working with SIP.
%if 0%{?with_python3}
It is used by both the sip-devel (python 2) and python3-sip-devel subpackages.
%endif


%if 0%{?with_python3}
%package -n python3-sip
Summary: SIP - Python 3/C++ Bindings Generator
Group: Development/Tools
Provides: python3-sip-api(%{_sip_api_major}) = %{_sip_api}
%description -n python3-sip
This is the Python 3 build of SIP.

SIP is a tool for generating bindings for C++ classes so that they can be
accessed as normal Python 3 classes. SIP takes many of its ideas from SWIG but,
because it is specifically designed for C++ and Python, is able to generate
tighter bindings. SIP is so called because it is a small SWIG.

SIP was originally designed to generate Python bindings for KDE and so has
explicit support for the signal slot mechanism used by the Qt/KDE class
libraries. However, SIP can be used to generate Python 3 bindings for any C++
class library.

%package -n python3-sip-devel
Summary: Files needed to generate Python 3 bindings for any C++ class library
Group: Development/Libraries
Requires: %{name}-macros = %{version}-%{release}
Requires: python3-sip%{?_isa} = %{version}-%{release}
Requires: python3-devel
%description -n python3-sip-devel
This package contains files needed to generate Python 3 bindings for any C++
classes library.
%endif


%prep

%setup -q -n %{name}-%{version}%{?snap:-snapshot-%{snap}}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
%{__python} configure.py -d %{python_sitearch} CXXFLAGS="%{optflags}" CFLAGS="%{optflags}"

make %{?_smp_mflags} 

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} configure.py -d %{python3_sitearch} CXXFLAGS="%{optflags}" CFLAGS="%{optflags}" --sipdir=%{_datadir}/python3-sip

make %{?_smp_mflags} 
popd
%endif


%install
rm -rf %{buildroot}

# Perform the Python 3 installation first, to avoid stomping over the Python 2
# /usr/bin/sip:
%if 0%{?with_python3}
pushd %{py3dir}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/python3-sip
mv %{buildroot}%{_bindir}/sip %{buildroot}%{_bindir}/python3-sip
popd
%endif

# Python 2 installation:
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/sip

# Macros used by -devel subpackages:
install -D -p -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.sip


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE LICENSE-GPL2 LICENSE-GPL3
%doc NEWS README
%{python_sitearch}/*

%files devel
%defattr(-,root,root,-)
%{_bindir}/sip
%{_datadir}/sip/
%{python_inc}/*

%files macros
%defattr(-,root,root,-)
%{_sysconfdir}/rpm/macros.sip

%if 0%{?with_python3}
%files -n python3-sip
%{python3_sitearch}/*

%files -n python3-sip-devel
# Note that the "sip" binary is invoked by name in a few places higher up
# in the KDE-Python stack; these will need changing to "python3-sip":
%{_bindir}/python3-sip
%{_datadir}/python3-sip/
%{python3_inc}/*
%endif


%changelog
* Wed Jul 14 2010 Rex Dieter <rdieter@fedoraproject.org> 4.10.3-1
- sip-4.10.3

* Fri Jun 25 2010 Karsten Hopp <karsten@redhat.com> 4.10.2-3
- bump and rebuild so that s390 will build the python3-sip packages

* Mon Apr 26 2010 David Malcolm <dmalcolm@redhat.com> - 4.10.2-2
- enable "with_python3" in the build
- use py3dir throughout, as provided by python3-devel
- name the python 3 sip binary "python3-sip"
- fix a typo in the name of the data dir: python-3sip -> python3-sip
- split out macros.sip into a new subpackage

* Sat Apr 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- sip-4.10.2

* Thu Mar 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-2
- _sip_api_minor 1

* Thu Mar 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-1
- sip-4.10.1

* Fri Jan 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.10-1
- sip-4.10 (final)

* Fri Jan 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.10-0.2.20100102
- RFE: Support python3 when building sip (#545124)
- drop old pre v4 changelog

* Thu Jan 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.10-0.1.20100102
- sip-4.10-snapshot-20100102

* Mon Nov 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.9.3-1
- sip-4.9.3

* Fri Nov 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- sip-4.9.2

* Tue Nov 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.9.1-3
- move sip binary to -devel 

* Mon Nov 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.9.1-2
- Provides: sip-api(%%_sip_api_major) = %%_sip_api
- devel: /etc/rpm/macros.sip helper

* Fri Oct 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.9.1-1
- sip-4.9.1

* Thu Oct 15 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.9.1-0.1.20091014
- sip-4.9.1-snapshot-20091014

* Thu Oct 15 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.9-1
- sip-4.9
- License: GPLv2 or GPLv3

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 4.8.2-2
- Convert specfile to UTF-8.

* Tue Jul 28 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.8.2-1
- sip-4.8.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.8.1-1
- sip-4.8.1

* Fri Jun 05 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.8-1
- sip-4.8

* Thu May 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.8-0.1.20090430
- sip-4.8-snapshot-20090430

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 4.7.9-2
- Rebuild for Python 2.6

* Mon Nov 17 2008 Rex Dieter <rdieter@fedoraproject.org> 4.7.9-1
- sip-4.7.9

* Mon Nov 10 2008 Rex Dieter <rdieter@fedoraproject.org> 4.7.8-1
- sip-4.7.8

* Thu Sep 04 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4.7.7-3
- fix license tag

* Tue Sep 02 2008 Than Ngo <than@redhat.com> 4.7.7-2
- get rid of BR on qt

* Tue Aug 26 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.7.7-1
- sip-4.7.7

* Wed May 21 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.7.6-1
- sip-4.7.6

* Wed May 14 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.7.5-1
- sip-4.7.5

* Tue Mar 25 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.7.4-3
- BR: qt3-devel (f9+)

* Tue Feb 12 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.7.4-2
- fix 64bit patch

* Tue Feb 12 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.7.4-1
- sip-4.7.4

* Thu Dec 06 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 4.7.3-1
- sip-4.7.3

* Wed Dec 05 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 4.7.2-1
- sip-4.7.2
- omit needless scriptlets

* Mon Nov 12 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 4.7.1-2
- License: Python Software Foundation License v2
- fix/cleanup some macro usage
- fix Source, Url. 

* Mon Oct 22 2007 Than Ngo <than@redhat.com> - 4.7.1-1
- 4.7.1

* Mon Oct 01 2007 Than Ngo <than@redhat.com> - 4.6-3
- fix rh#289321, sipconfig.py includes wrong py_lib_dir, thanks to Rex Dieter

* Thu Aug 30 2007 Than Ngo <than@redhat.com> - 4.6-2.fc7
- typo in description

* Thu Apr 12 2007 Than Ngo <than@redhat.com> - 4.6-1.fc7
- 4.6

* Thu Jan 18 2007 Than Ngo <than@redhat.com> - 4.5.2-1
- 4.5.2 

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 4.5-2
- rebuild against python 2.5
- cleanups for python packaging guidelines

* Mon Nov 06 2006 Than Ngo <than@redhat.com> 4.5-1
- 4.5

* Thu Sep 28 2006 Than Ngo <than@redhat.com> 4.4.5-3
- fix #207297, use qt qmake files

* Wed Sep 20 2006 Than Ngo <than@redhat.com> 4.4.5-2
- fix #206633, own %%_datadir/sip

* Wed Jul 19 2006 Than Ngo <than@redhat.com> 4.4.5-1
- update to 4.4.5

* Mon Jul 17 2006 Than Ngo <than@redhat.com> 4.4.3-2
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 4.4.3-1.1
- rebuild

* Thu Apr 27 2006 Than Ngo <than@redhat.com> 4.4.3-1
- update to 4.4.3
- built with %%{optflags}

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 4.3.1-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 4.3.1-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Sep 12 2005 Than Ngo <than@redhat.com> 4.3.1-1
- update to 4.3.1

* Wed Mar 23 2005 Than Ngo <than@redhat.com> 4.2.1-1
- 4.2.1

* Fri Mar 04 2005 Than Ngo <than@redhat.com> 4.2-1
- 4.2

* Thu Nov 11 2004 Than Ngo <than@redhat.com> 4.1-2
- rebuild against python 2.4

* Fri Sep 24 2004 Than Ngo <than@redhat.com> 4.1-1
- update to 4.1
