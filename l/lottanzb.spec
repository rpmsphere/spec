%global debug_package %{nil}
Summary: Automated Usenet Client
Name: lottanzb
Version: 0.6
Release: 8.1
Source0: http://launchpad.net/lottanzb/0.6/%{version}/+download/%{name}-%{version}.tar.gz
License: GPL
Group: Networking/News
BuildArch: noarch
BuildRequires: python2-devel
BuildRequires: intltool
Requires: python-kiwi
Requires: python2
Requires: hellanzb
Requires: pygtk2
Requires: pygtk2-libglade
URL: http://www.lottanzb.org/

%description
LottaNZB is a Usenet client that automates the download of Usenet files with
the help of NZB files. It uses HellaNZB as its backend and PyGTK for its user
interface.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --packaging-mode --root=$RPM_BUILD_ROOT
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

%find_lang %{name} --with-gnome
#for omf in %buildroot%_datadir/omf/*/*[_-]??.omf;do 
#echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
#done
rm -fr %buildroot%_datadir/doc

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
#{_sysconfdir}/apport/crashdb.conf.d/lottanzb-crashdb.conf
#{_datadir}/apport
%{_bindir}/*
%{python2_sitelib}/%{name}*
%{_datadir}/%{name}/*
%{_datadir}/icons/*
%{_mandir}/man1/*
%{_datadir}/application-registry/lottanzb.applications
%{_datadir}/applications/lottanzb.desktop
%{_datadir}/mime-info/%{name}.*
%{_datadir}/mime/packages/*
%dir %{_datadir}/omf/lottanzb/
#{_datadir}/omf/lottanzb/*-C.omf

%changelog
* Sun Jun 09 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuild for Fedora
* Sat Jan 12 2013 umeabot <umeabot> 0.5.3-3.mga3
+ Revision: 358948
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Wed Apr 13 2011 ennael <ennael> 0.5.3-2.mga1
+ Revision: 84049
- clean spec file
- imported package lottanzb
