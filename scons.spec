#global posttag .final.0

# SCons 3.0.1 does not run under (3.0.0) < Python3 < (3,5,0) or
# Python < (2,7,0).
# Epel7 provides Python3.4

%if 0%{?fedora}
%global with_python3 1
%global with_python2 1
%endif

%if 0%{?rhel}
%global with_python3 0
%global with_python2 1
%endif

Name:		    scons
Version:	    3.0.1
Release:	    6.1
Summary:	    An Open Source software construction tool

License:	    MIT
URL:		    http://www.scons.org
Source:		    http://prdownloads.sourceforge.net/scons/scons-%{version}.tar.gz
BuildArch:	    noarch

%description
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines. SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.

%if 0%{?with_python2}
%package -n     python2-%{name}
Summary:        An Open Source software construction tool

BuildRequires:  python2-devel
Provides:       scons = %{version}-%{release}
Obsoletes:      scons < %{version}-4
%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines. SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.
%endif

%if 0%{?with_python3}
%package -n     python3-%{name}
Summary:        An Open Source software construction tool

BuildRequires:  python3-devel
Provides:       scons-python3 = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
SCons is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. SCons is based on the design which won the Software
Carpentry build tool design competition in August 2000.

SCons "configuration files" are Python scripts, eliminating the need
to learn a new build tool syntax. SCons maintains a global view of
all dependencies in a tree, and can scan source (or other) files for
implicit dependencies, such as files specified on #include lines. SCons
uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. SCons
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.
%endif

%prep
%setup -qc

# Convert to UTF-8
for file in %{name}-%{version}%{?posttag}/*.txt; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done
%if 0%{?with_python3}
cp -a %{name}-%{version}%{?posttag} %{name}-%{version}%{?posttag}-py3
%endif
%if 0%{?with_python2}
sed -i 's|/usr/bin/env python|%{__python2}|' %{name}-%{version}%{?posttag}/script/*
%endif
%if 0%{?with_python3}
sed -i 's|/usr/bin/env python|%{__python3}|' %{name}-%{version}%{?posttag}-py3/script/*
%endif

%build
%if 0%{?with_python2}
pushd %{name}-%{version}%{?posttag}
%py2_build
popd
%endif
%if 0%{?with_python3}
pushd %{name}-%{version}%{?posttag}-py3
%py3_build
popd
%endif

%install
%if 0%{?with_python3}
cd %{name}-%{version}%{?posttag}-py3
%py3_install \
 --standard-lib \
 --no-install-bat \
 --no-version-script \
 --install-scripts=%{_bindir} \
 --install-data=%{_datadir}
cd ..

#Avoiding collisions between the python 2 and python 3 stacks
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-3
mv %{buildroot}%{_bindir}/%{name}-configure-cache %{buildroot}%{_bindir}/%{name}-configure-cache-3
mv %{buildroot}%{_bindir}/%{name}ign %{buildroot}%{_bindir}/%{name}ign-3
mv %{buildroot}%{_bindir}/%{name}-time %{buildroot}%{_bindir}/%{name}-time-3

pushd %{buildroot}%{_bindir} 
for i in %{name}-v%{version}-%{python3_version} %{name}-%{python3_version}; do
  ln -fs %{_bindir}/%{name}-3 %{buildroot}%{_bindir}/$i
done
for i in %{name}ign-v%{version}-%{python3_version} %{name}ign-%{python3_version}; do
  ln -fs %{_bindir}/%{name}ign-3 %{buildroot}%{_bindir}/$i
done
for i in %{name}-time-v%{version}-%{python3_version} %{name}-time-%{python3_version}; do
  ln -fs %{_bindir}/%{name}-time-3 %{buildroot}%{_bindir}/$i
done
for i in %{name}-configure-cache-v%{version}-%{python3_version} %{name}-configure-cache-%{python3_version}; do
  ln -fs %{_bindir}/%{name}-configure-cache-3 %{buildroot}%{_bindir}/$i
done
popd
%endif

%if 0%{?with_python2}
cd %{name}-%{version}%{?posttag}
%py2_install \
 --standard-lib \
 --no-install-bat \
 --no-version-script \
 --install-scripts=%{_bindir} \
 --install-data=%{_datadir}
cd ..

#Avoiding collisions between the python 2 and python 3 stacks
pushd %{buildroot}%{_bindir} 
for i in %{name}-2 %{name}-%{python2_version} %{name}-v%{version}-%{python2_version}; do
  ln -fs %{_bindir}/%{name} %{buildroot}%{_bindir}/$i
done
for i in %{name}ign-2 %{name}ign-%{python2_version} %{name}ign-v%{version}-%{python2_version}; do
  ln -fs %{_bindir}/%{name}ign %{buildroot}%{_bindir}/$i
done
for i in %{name}-time-2 %{name}-time-%{python2_version} %{name}-time-v%{version}-%{python2_version}; do
  ln -fs %{_bindir}/%{name}-time %{buildroot}%{_bindir}/$i
done
for i in %{name}-configure-cache-2 %{name}-configure-cache-%{python2_version} %{name}-configure-cache-v%{version}-%{python2_version}; do
  ln -fs %{_bindir}/%{name}-configure-cache %{buildroot}%{_bindir}/$i
done
popd
%endif

%if 0%{?with_python2}
%files -n python2-%{name}
%doc %{name}-%{version}%{?posttag}/CHANGES.txt %{name}-%{version}%{?posttag}/README.txt %{name}-%{version}%{?posttag}/RELEASE.txt
%license %{name}-%{version}%{?posttag}/LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/%{name}ign
%{_bindir}/%{name}-time
%{_bindir}/%{name}-configure-cache
%{_bindir}/%{name}*-2
%{_bindir}/%{name}*-%{python2_version}
%{python2_sitelib}/SCons/
%{python2_sitelib}/scons-%{version}*.egg-info
%{_mandir}/man?/*
%endif
%if 0%{?with_python3}
%files -n python3-%{name}
%doc %{name}-%{version}%{?posttag}-py3/CHANGES.txt %{name}-%{version}%{?posttag}-py3/README.txt %{name}-%{version}%{?posttag}-py3/RELEASE.txt
%license %{name}-%{version}%{?posttag}-py3/LICENSE.txt
%{_bindir}/%{name}*-3
%{_bindir}/%{name}*-%{python3_version}
%{python3_sitelib}/SCons/
%{python3_sitelib}/scons-%{version}*.egg-info
%{_mandir}/man?/*
%endif

%changelog
* Mon Dec 25 2017 Antonio Trande <sagitter at fedoraproject.org> - 3.0.1-5
- Remove 'Obsoletes scons' for scons-python3

* Mon Dec 25 2017 Antonio Trande <sagitter at fedoraproject.org> - 3.0.1-4
- Fix Provides tag

* Mon Dec 25 2017 Antonio Trande <sagitter at fedoraproject.org> - 3.0.1-3
- Set Obsoletes tag

* Mon Dec 25 2017 Antonio Trande <sagitter at fedoraproject.org> - 3.0.1-2
- Provide Python2 and Python3 scons
- Avoiding collisions between the python 2 and python 3 stacks

* Tue Nov 28 2017 Antonio Trande <sagitter at fedoraproject.org> - 3.0.1-1
- Update to 3.0.1
- Build with Python2 on epel7

* Tue Oct 03 2017 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.1-1
- Update to new upstream version 3.0.0 (rhbz#1497891)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.1-1
- Update to new upstream version 2.5.1 (rhbz#1391798)

* Mon Jun 13 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.5.0-1
- Update to new upstream version 2.5.0

* Sat May 07 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.4.1-1
- Update to new upstream version 2.4.1 (rhbz#1265037)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 01 2015 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.6-1
- Update to new upstream version 2.3.6 (rhbz#1234119)

* Wed Jul 22 2015 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.5-1
- Update to new upstream version 2.3.5 (rhbz#1234119)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 30 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.4-1
- Update to new upstream version 2.3.4 (rhbz#1147461)

* Mon Sep 01 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.3-1
- Update to new upstream version 2.3.3 (rhbz#1133527)

* Mon Jul 07 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.2-1
- Update to new upstream version 2.3.2 (rhbz#1116635)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 05 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.1-1
- Update to new upstream version 2.3.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 09 2013 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.0-1
- Update to new upstream version 2.3.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 29 2012 Fabian Affolter <mail@fabian-affolter.ch> - 2.2.0-1
- Update to new upstream version 2.2.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 10 2011 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.0-1
- Update to new upstream version 2.1.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 23 2010 Chen Lei <supercyper@163.com> - 2.0.1-1
- new release 2.0.1

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 2.0.0-2.final.0
- recompiling .py files against Python 2.7 (rhbz#623357)

* Thu Jul 08 2010 Chen Lei <supercyper@163.com> - 2.0.0-1.final.0
- new release 2.0.0.final.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 25 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 1.2.0-1
- Update to 1.2.0 to fix problems with Python 2.6 (#475903)
  (currently causing broken deps with other packages)

* Thu Dec 18 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.1.0-1
- new release 1.1.0

* Fri Sep  5 2008 Gerard Milmeister <gemi@bluewin.ch> - 1.0.0-1.d20080826
- new release 1.0.0

* Sun Aug  3 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.5-1
- new release 0.98.5

* Sun Jun  1 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.4-2
- added buildreq sed

* Sat May 31 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.4-1
- new release 0.98.4

* Sun May  4 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.3-2
- changed shebang line of scripts

* Sun May  4 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.3-1
- new release 0.98.3

* Sat Apr 19 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98.1-1
- new release 0.98.1

* Sat Apr  5 2008 Gerard Milmeister <gemi@bluewin.ch> - 0.98-1
- new release 0.98

* Mon May 21 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.97-1
- new version 0.97

* Thu May 10 2007 Gerard Milmeister <gemi@bluewin.ch> - 0.96.96-1
- new version 0.96.96

* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 0.96.1-3
- Rebuild for FE6

* Sat Jun 18 2005 Gerard Milmeister <gemi@bluewin.ch> - 0.96.1-1
- New Version 0.96.1

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Jan 25 2005 Thorsten Leemhuis <fedora[AT]leemhuis[DOT]info> 0.96-4
- Place libs in {_prefix}/lib/ and not in {libdir}; fixes x86_64 problems
- Adjust minor bits to be in sync with python-spec-template
