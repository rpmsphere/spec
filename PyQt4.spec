
# Fedora review: http://bugzilla.redhat.com/190189

%global with_python3 1

Summary: Python bindings for Qt4
Name: 	 PyQt4
Version: 4.7.4
Release: 2%{?dist}

# GPLv2 exceptions(see GPL_EXCEPTIONS*.txt)
License: GPLv3 or GPLv2 with exceptions
Group: 	 Development/Languages
Url:     http://www.riverbankcomputing.com/software/pyqt/
Source0: http://www.riverbankcomputing.com/static/Downloads/PyQt4/PyQt-x11-gpl-%{version}%{?snap:-snapshot-%{snap}}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch1:  PyQt-x11-gpl-4.4.4-64bit.patch
# HACK! FIXME: ping upstream why this isn't working right. -- Rex
Patch2:  PyQt-x11-gpl-4.5.2-QT_SHARED.patch
Patch4:  PyQt-x11-gpl-4.5.1-pyuic_shebang.patch
# fix multilib conflict because of timestamp
Patch5:  PyQt-x11-gpl-4.6.2-timestamp-multilib.patch
# fix implicit linking when checking for QtAssistant, QtHelp
Patch6:  PyQt-x11-gpl-4.7.2-fix-implicit-linking.patch

BuildRequires: chrpath
BuildRequires: dbus-devel dbus-python-devel
BuildRequires: findutils
BuildRequires: phonon-devel
# beware of PyQt4/qscintilla bootstap issues
%if 0%{?fedora}
BuildRequires: qscintilla
%endif
BuildRequires: qt4-devel >= 4.5.0-7
BuildRequires: qt4-webkit-devel
BuildRequires: qt-assistant-adp-devel

BuildRequires: python-devel
%global python_sitelib  %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")
%global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")

BuildRequires: sip-devel >= 4.10.3

%if 0%{?with_python3}
BuildRequires: python3-devel
BuildRequires: python3-sip-devel >= 4.10.3
%endif # with_python3

Requires: dbus-python
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}
%{?_sip_api:Requires: sip-api(%{_sip_api_major}) >= %{_sip_api}}

%description
These are Python bindings for Qt4.

%package devel
Summary: Files needed to build other bindings based on Qt4
Group:	 Development/Languages
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt4-devel
Requires: sip-devel
%description devel
Files needed to build other bindings for C++ classes that inherit from any
of the Qt4 classes (e.g. KDE or your own).

# The bindings are imported as "PyQt4", hence it's reasonable to name the
# Python 3 subpackage "python3-PyQt4", despite the apparent tautology
%package -n python3-PyQt4
Summary: Python 3 bindings for Qt4
Group:   Development/Languages
# The dbus Python bindings have not yet been ported to Python 3:
# Requires: dbus-python
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}
%{?_sip_api:Requires: python3-sip-api(%{_sip_api_major}) >= %{_sip_api}}
%description -n python3-PyQt4
These are Python 3 bindings for Qt4.

%package -n python3-PyQt4-devel
Summary: Python 3 bindings for Qt4
Group:   Development/Languages
Requires: python3-PyQt4%{?_isa} = %{version}-%{release}
Requires: python3-sip-devel
%description -n python3-PyQt4-devel
Files needed to build other Python 3 bindings for C++ classes that inherit
from any of the Qt4 classes (e.g. KDE or your own).


%prep
%setup -q -n PyQt-x11-gpl-%{version}%{?snap:-snapshot-%{snap}}

%patch1 -p1 -b .64bit
%patch2 -p1 -b .QT_SHARED
%patch4 -p1 
%patch5 -p1 -b .timestamp
%patch6 -p1 -b .fix-implicit-linking

## permissions
# mark examples non-executable
find examples/ -name "*.py" | xargs chmod a-x
chmod a+rx pyuic/uic/pyuic.py

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3

%build

QT4DIR=%{_qt4_prefix}
PATH=%{_qt4_bindir}:$PATH ; export PATH

# Python 2 build:
%{__python} configure.py \
  --confirm-license \
  --qmake=%{_qt4_qmake} \
  --verbose 

make %{?_smp_mflags}

# Python 3 build:
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} configure.py \
  --confirm-license \
  --qmake=%{_qt4_qmake} \
  --verbose 

make %{?_smp_mflags}
popd
%endif # with_python3


%install
rm -rf %{buildroot}

InstallPyQt4() {
  PySiteArch=$1

  make install DESTDIR=%{buildroot} INSTALL_ROOT=%{buildroot}

  # fix/remove rpaths
  chrpath --list   %{buildroot}$PySiteArch/PyQt4/QtCore.so && \
  chrpath --delete %{buildroot}$PySiteArch/PyQt4/QtCore.so ||:

  chrpath --list   %{buildroot}$PySiteArch/PyQt4/QtGui.so && \
  chrpath --delete %{buildroot}$PySiteArch/PyQt4/QtGui.so ||:

  chrpath --list   %{buildroot}$PySiteArch/PyQt4/QtDesigner.so && \
  chrpath --delete %{buildroot}$PySiteArch/PyQt4/QtDesigner.so ||:
}


# Install Python 3 first, and move aside any executables, to avoid clobbering
# the Python 2 installation:
%if 0%{?with_python3}
pushd %{py3dir}
InstallPyQt4 %{python3_sitearch}
popd
%endif # with_python3

InstallPyQt4 %{python_sitearch}

# DBus bindings only work for Python 2 so far:
chrpath --list   %{buildroot}%{python_sitelib}/dbus/mainloop/qt.so && \
chrpath --delete %{buildroot}%{python_sitelib}/dbus/mainloop/qt.so ||:

# HACK: fix multilb conflict, http://bugzilla.redhat.com/509415
rm -fv %{buildroot}%{_bindir}/pyuic4
mv %{buildroot}%{python_sitearch}/PyQt4/uic/pyuic.py \
   %{buildroot}%{_bindir}/pyuic4
ln -s %{_bindir}/pyuic4 \
      %{buildroot}%{python_sitearch}/PyQt4/uic/pyuic.py

# remove Python 3 code from Python 2.6 directory, fixes FTBFS (#564633)
rm -rf %{buildroot}%{python_sitearch}/PyQt4/uic/port_v3/

# likewise, remove Python 2 code from the Python 3.1 directory:
rm -rf %{buildroot}%{python3_sitearch}/PyQt4/uic/port_v2/


%check
# verify phonon built ok
test -f %{buildroot}%{python_sitearch}/PyQt4/phonon.so
test -d %{buildroot}%{_datadir}/sip/PyQt4/phonon

%if 0%{?with_python3}
test -f %{buildroot}%{python3_sitearch}/PyQt4/phonon.so
test -d %{buildroot}%{_datadir}/python3-sip/PyQt4/phonon
%endif # with_python3

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc NEWS README
%doc OPENSOURCE-NOTICE.TXT
%doc LICENSE.GPL2 GPL_EXCEPTION*.TXT
%doc LICENSE.GPL3
%{python_sitearch}/PyQt4/
%exclude %{python_sitearch}/PyQt4/uic/pyuic.py*
# fixme?  -> sitearch?  -- Rex
%{python_sitelib}/dbus/mainloop/qt.so
%{_qt4_plugindir}/designer/*

%files devel
%defattr(-,root,root,-)
%doc doc/*
%doc examples/
%{_bindir}/pylupdate4
%{_bindir}/pyrcc4
%{_bindir}/pyuic4
%{python_sitearch}/PyQt4/uic/pyuic.py*
%{_datadir}/sip/PyQt4/
%if 0%{?fedora}
%{_qt4_prefix}/qsci/api/python/PyQt4.api
%endif

%if 0%{?with_python3}
%files -n python3-PyQt4
%defattr(-,root,root,-)
%doc NEWS README
%doc OPENSOURCE-NOTICE.TXT
%doc LICENSE.GPL2 GPL_EXCEPTION*.TXT
%doc LICENSE.GPL3
%{python3_sitearch}/PyQt4/
%exclude %{python3_sitearch}/PyQt4/uic/pyuic.py*

%files -n python3-PyQt4-devel
%defattr(-,root,root,-)
%doc doc/*
%doc examples/
%{python3_sitearch}/PyQt4/uic/pyuic.py*
%{_datadir}/python3-sip/PyQt4/
%if 0%{?fedora}
%{_qt4_prefix}/qsci/api/python/PyQt4.api
%endif
%endif


%changelog
* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 4.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jul 14 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7.4-1
- PyQt-x11-gpl-4.7.4

* Sat May 08 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7.3-3
- BR: qt4-webkit-devel

* Mon Apr 26 2010 David Malcolm <dmalcolm@redhat.com> - 4.7.3-2
- add python 3 subpackages (#586196)

* Sat Apr 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7.3-1
- PyQt-x11-gpl-4.7.3

* Sun Mar 21 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.7.2-2
- rebuild against fixed qt to get QtMultimedia detected properly

* Thu Mar 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7.2-1
- PyQt-x11-gpl-4.7.2

* Sun Mar 14 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.7-5
- fix implicit linking when checking for QtHelp and QtAssistant
- remove Python 3 code from Python 2.6 directory, fixes FTBFS (#564633)

* Sat Mar 13 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.7-4
- BR qt-assistant-adp-devel

* Tue Feb 23 2010 Than Ngo <than@redhat.com> - 4.7-3
- fix multilib conflict because of timestamp

* Sun Feb 14 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7-2
- rebuild

* Fri Jan 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7-1
- PyQt-x11-gpl-4.7 (final)

* Thu Jan 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.7-0.1.20091231
- PyQt-x11-gpl-4.7-snapshot-20091231

* Fri Nov 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.2-5
- phonon bindings missing (#541685)

* Wed Nov 25 2009 Than Ngo <than@redhat.com> - 4.6.2-4
- fix conditional for RHEL

* Wed Nov 25 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.2-3
- PyQt4-4.6.2 breaks QStringList in QVariant, rebuild with sip-4.9.3 (#541211)

* Wed Nov 25 2009 Than Ngo <than@redhat.com> - 4.6.2-2
- fix conditional for RHEL

* Fri Nov 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.2-1
- PyQt4-4.6.2

* Thu Nov 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.1-2.1
- rebuild (for qt-4.6.0-rc1, f13+)

* Mon Nov 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.1-2
- Requires: sip-api(%%_sip_api_major) >= %%_sip_api

* Fri Oct 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.1-1
- PyQt4-4.6.1

* Thu Oct 15 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.6.1-0.1.20091014
- PyQt4-4.6.1-snapshot-20091014 (#529192)

* Tue Jul 28 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5.4-1
- PyQt4-4.5.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-1
- PyQt4-4.5.2

* Thu Jul 02 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-2
- fix build with qt-4.5.2
- PyQt4-devel multilib conflict (#509415)

* Tue Jun 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-1
- PyQt-4.5.1

* Fri Jun 05 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5-1
- PyQt-4.5

* Thu May 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5-0.2.20090520
- fix generation of sip_ver

* Thu May 21 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.5-0.1.20090520
- PyQt-4.5-snapshot-20090520

* Sun Apr 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.4.4-6
- rebuild for phonon bindings (#497680)

* Wed Mar 05 2009 Rex Dieter <rdieter@fedorproject.org> - 4.4.4-5
- move designer plugins to main/runtime (#487622)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Than Ngo <than@redhat.com> - 4.4.4-3
- rebuild against qt-4.5rc1

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 4.4.4-2
- Rebuild for Python 2.6

* Mon Nov 10 2008 Rex Dieter <rdieter@fedoraproject.org> 4.4.4-1
- PyQt-4.4.4

* Tue Aug 26 2008 Rex Dieter <rdieter@fedoraproject.org> 4.4.3-1
- PyQt-4.4.3

* Sat Jun 14 2008 Rex Dieter <rdieter@fedoraproject.org> 4.4.2-2
- PyQt4 is built without QtWebKit support (#451490)

* Wed May 21 2008 Rex Dieter <rdieter@fedoraproject.org> 4.4.2-1
- PyQt-4.4.2

* Wed May 14 2008 Rex Dieter <rdieter@fedoraproject.org> 4.4-1
- PyQt-4.4
- License: GPLv3 or GPLv2 with exceptions

* Mon Feb 11 2008 Rex Dieter <rdieter@fedoraproject.org> 4.3.3-2 
- respin (gcc43)

* Wed Dec 05 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 4.3.3-1
- PyQt-4.3.3

* Thu Nov 22 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 4.3.1-3
- dbus support (#395741)

* Mon Nov 12 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 4.3.1-1
- PyQt-4.3.1

* Thu Oct 04 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 4.2-8
- drop ExcludeArch: ppc64 , qt4 bug is (hopefully) fixed.

* Thu Oct 04 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 4.2-7
- fix QtDesigner plugin install

* Wed Oct 03 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 4.2-6
- 64bit QtDesigner patch

* Mon Aug 27 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 4.2-5
- -devel: Requires: qt4-devel

* Sun Aug 26 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 4.2-4
- use %%python_sitearch
- License: GPLv2

* Thu Aug 02 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 4.2-3
- fix python_sitelib typo (wrt chrpath call)
- move %%_bindir stuff to -devel
- mark %%doc examples non-executable
- add shebang to %%_bindir/pyuic4

* Tue Jul 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 4.2-2
- remove rpath from QtDesigner.so
- BR: qt4-devel > 4.3.0-8

* Wed Apr 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 4.2-1
- PyQt4-4.2

* Wed Feb 28 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 4.1.1-2
- fix build against multilib'd qt4

* Mon Dec 11 2006 Rex Dieter <rexdieter[AT]usres.sf.net> 4.1.1-1
- PyQt4-4.1.1
- BR: sip-devel >= 4.5.1

* Mon Nov 06 2006 Rex Dieter <rexdieter[AT]users.sf.net> 4.1-1
- PyQt4-4.1

* Wed Oct 04 2006 Rex Dieter <rexdieter[AT]users.sf.net> 4.0.1-4
- don't own %%_datadir/sip (bug #206633)

* Mon Aug 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 4.0.1-3
- BR: qt4-devel < 4.2

* Sat Jul 29 2006 Rex Dieter <rexdieter[AT]users.sf.net> 4.0.1-2
- fix reference(s) to qmake(4)

* Sun Jul 16 2006 Rex Dieter <rexdieter[AT]users.sf.net> 4.0.1-1
- PyQt-4.0.1

* Mon Jun 12 2006 Rex Dieter <rexdieter[AT]users.sf.net> 4.0-1
- PyQt-4.0(final)
- BR: sip-devel >= 4.4.4 (see bug #199430)

* Fri May 12 2006 Rex Dieter <rexdieter[AT]users.sf.net> 4.0-0.6.beta1
- drop BR: qt4-MySQL qt4-ODBC qt4-PostgreSQL
- drop usage of (undefined) %%sip_min

* Fri Apr 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 4.0-0.5.beta1
- cleanup for Extras

* Fri Apr 28 2006 Rex Dieter <rexdieter[AT]users.sf.net> 4.0-0.4.beta1
- 4.0beta1

* Thu Apr 27 2006 Rex Dieter <rexdieter[AT]users.sf.net> 4.0-0.3.20060421 
- respin for sip-4.4.3
- use sip-abi, sip-abi-min

* Mon Apr 24 2006 Rex Dieter <rexdieter[AT]users.sf.net> 4.0-0.2.20060421
- 20060421 snapshot

* Wed Apr 19 2006 Rex Dieter <rexdieter[AT]users.sf.net> 0.0-0.1.20060417
- first try, using 20060417 snapshot

