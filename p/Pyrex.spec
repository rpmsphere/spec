%if %($(pkg-config emacs) ; echo $?)
%define emacs_version 22.1
%define emacs_lispdir %{_datadir}/emacs/site-lisp
%define emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d
%else
%define emacs_version %(pkg-config emacs --modversion)
%define emacs_lispdir %(pkg-config emacs --variable sitepkglispdir)
%define emacs_startdir %(pkg-config emacs --variable sitestartdir)
%endif

Name:           Pyrex
Version:        0.9.9
Release:        18
Epoch:          0
BuildArch:      noarch
Summary:        A compiler/language for writing Python extension modules
Group:          Development/Languages
License:        Public Domain
URL:            http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/
Source0:        http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/Pyrex-%{version}.tar.gz
Source1:        pyrex-mode-init.el
BuildRequires:  pkgconfig
BuildRequires:  python2-devel
BuildRequires:  dos2unix
BuildRequires:  findutils
BuildRequires:  emacs emacs-el
Requires:       python2-devel
Obsoletes:      emacs-pyrex <= 0.9.9-12
Provides:       emacs-pyrex <= 0.9.9-12

%description
Pyrex is Python with C types.  It is specially designed to allow you to
write extension modules for Python that have the speed of C and the
simplicity and readability of Python.  You write your code in a Python-like
language with C-typed variables, then use the pyrexc compiler to transform
it into a C representation.  This is useful for speeding up critical sections
of your Python code or wrapping an external library.

Please see the documentation for how to get the best performance from your
code.

%prep
%setup -q

%build
%{__python2} setup.py build

# Remove some Macintosh-isms
find . -name '.DS_Store' -exec rm -f \{\} \;
dos2unix -k -c mac CHANGES.txt ToDo.txt  Demos/Makefile.nodistutils Tools/*
find Doc -type f | xargs dos2unix -k -c mac

# Compile emacs module
emacs -batch -f batch-byte-compile Tools/*.el

%install
rm -rf $RPM_BUILD_ROOT
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{emacs_lispdir}
mkdir -p $RPM_BUILD_ROOT/%{emacs_startdir}
cp -p Tools/pyrex-mode.* $RPM_BUILD_ROOT/%{emacs_lispdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT/%{emacs_startdir}

%files
%doc USAGE.txt README.txt CHANGES.txt ToDo.txt Demos Doc
%{python2_sitelib}/Pyrex*
%exclude %{python2_sitelib}/Pyrex/Mac
%{_bindir}/pyrexc
%{emacs_lispdir}/*

%changelog
* Thu Oct 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.9
- Rebuilt for Fedora
* Thu Jul 26 2018 My Karlsson <mk@acc.umu.se> - 0:0.9.9-18
- Build with python as /usr/bin/python2 (rhbz#1603306)
* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.9.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.9.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0:0.9.9-15
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.9.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Wed Jun 28 2017 My Karlsson <mk@acc.umu.se> - 0:0.9.9-13
- Removed emacs-pyrex subpackage (RHBZ#1234561)
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.9.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.9.9-11
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:0.9.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.9.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.9.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.9.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.9.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.9.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 0:0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild
* Tue Apr 13 2010 Matthew Barnes <mbarnes@redhat.com> - 0:0.9.9-1
- Update to 0.9.9
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.9.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:0.9.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0:0.9.8.4-2
- Rebuild for Python 2.6
* Thu Jun 12 2008 Matthew Barnes <mbarnes@redhat.com> - 0:0.9.8.4-1
- Update to 0.9.8.4
* Tue Jun  3 2008 Kyle VanderBeek <kylev@kylev.com> - 0:0.9.8.2-2
- Fix several rpmlint complaints
- Remove errant egg packaging (there is no egg)
* Tue Jun  3 2008 Matthew Barnes <mbarnes@redhat.com> - 0:0.9.8.2-1
- Update to 0.9.8.2
* Mon Jun  2 2008 Kyle VanderBeek <kylev@kylev.com> - 0:0.9.6.4-3
- rpmlint cleanup
* Mon May  6 2008 Matthew Barnes <mbarnes@redhat.com> - 0:0.9.6.4-2
- Require pkgconfig for building.
* Mon May  5 2008 Kyle VanderBeek <kylev@kylev.com> - 0:0.9.6.4-1
- Update to 0.9.6.4
- Add sub-package for emacs mode.
* Tue Jun 26 2007 Matthew Barnes <mbarnes@redhat.com> - 0:0.9.5.1a-1.fc8
- Update to 0.9.5.1a
- Remove Pyrex-0.9.4-fix-indent.patch (fixed upstream).
- Remove pyrex-python-2.5.patch (fixed upstream).
* Wed Jan  3 2007 David Zeuthen <davidz@redhat.com> - 0:0.9.4-4
- include a patch so Pyrex works with python 2.5
* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 0:0.9.4-2
- rebuild against python 2.5
* Fri Sep 22 2006 Matthew Barnes <mbarnes@redhat.com> - 0.8.4-2.fc6
- Don't %%ghost .pyo files (bug #205445).
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.9.4-1.1
- rebuild
* Wed Apr 19 2006 John (J5) Palmieri <johnp@redhat.com> - 0.9.4-1
- Upgrade to upstream 0.9.4
* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt
* Wed Oct 26 2005 John (J5) Palmieri <johnp@redhat.com> - 0.9.3.1-2
- Remove lib64 hack since this is a noarch package  
- use python_sitelib script for determining where to install to 
* Fri Sep 30 2005 John (J5) Palmieri <johnp@redhat.com> - 0.9.3.1-1
- update to 0.9.3.1
- remove gcc4 patch which is incorporated in this release
* Tue Mar 22 2005 Jeremy Katz <katzj@redhat.com> - 0.9.3-0
- update to 0.9.3
- add patch to fix generated code to build with gcc4
- require python-abi and python-devel instead of conflicting with 
  newer python-devel
* Mon Nov  8 2004 Jeremy Katz <katzj@redhat.com> - 0:0.9.2.1-3
- rebuild against python 2.4
* Wed Aug 18 2004 John (J5) Palmieri <johnp@redhat.com> - 0:0.9.2.1-2
- Added Steve Grubb's spec file patch (RH Bug #130200)
* Fri Jun 25 2004 John (J5) Palmieri <johnp@redhat.com> - 0:0.9.2.1-1
- New upstream version
- Pyrex-0.9-split-base-types.patch synced for new version
* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt
* Fri Jun 03 2004 John (J5) Palmieri <johnp@redhat.com> - 0:0.9-5
- Built to rawhide
* Wed May 19 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- use rpm macros to determine lib64 usage
* Fri Apr 23 2004 John (J5) Palmieri <johnp@redhat.com> - 0:0.9-3
- Added Pyrex-0.9-split-base-types.patch which fixes 
  long unsigned int bug showing up in dbus python binding
  builds for the x86_64 arch
- Added regex hack to spec to work around a bug in python's
  distutils which would install files into /usr/lib instead of
  /usr/lib64 on 64 bit archs
  * Mon Apr 19 2004 John (J5) Palmieri <johnp@redhat.com> - 0:0.9-2
- Was informed that the epoch change was not needed so the epoch 
  was reverted back to 0  
* Mon Apr 19 2004 John (J5) Palmieri <johnp@redhat.com> - 1:0.9-1
- Upped the epoch so as to avoid clashes with the Fedora extra package
* Mon Apr 19 2004 John (J5) Palmieri <johnp@redhat.com> - 0:0.9-1
- Transfered to Red Hat Fedora's main tree
- Removed need for LONG_LONG patch 
* Mon Feb 02 2004 Toshio Kuratomi <toshio@tiki-lounge.com> - 0:0.9-0.fdr.4
- Removed the site-packages directory from the directories owned by the
  package
* Mon Feb 02 2004 Toshio Kuratomi <toshio@tiki-lounge.com> - 0:0.9-0.fdr.3
- My mistake: rpm automatically removes %%ghost files, no need to script
  it manually.
- python distutils --record=FILE option doesn't record directories so include
  the site-packages/[directories] manually
* Thu Jan 15 2003 Toshio Kuratomi <toshio@tiki-lounge.com> - 0:0.9-0.fdr.2
- Merge changes from Michel Alexandre Salim <salimma[AT]users.sf.net>
  + Require build system's python version because directories are named
    pythonX.Y
  + Create *.pyo files and %%ghost them (Privleged user with python optimize
    turned on may generate them, but they aren't needed for operation.
  + Do not include the Mac Pyrex compiler stuff
  + Change license to Public Domain
- Script to remove any %%ghost files on package removal
- Patch around an incompatible change between python 2.2 and python 2.3's
  definition of LONG_LONG being renamed to PY_LONG_LONG
  * Fri Jan 09 2003 Toshio Kuratomi <toshio@tiki-lounge.com> - 0:0.9-0.fdr.1
- Initial RPM release.
