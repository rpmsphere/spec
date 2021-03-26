%define __spec_install_post %{nil}

Summary: 	Sync your files online and across computers
Name: 		dropbox
Version: 	3.0.5
Release: 	1%{?dist}.bin
License: 	Commercial, freeware
Group:		Networking/Remote access
Source0:	https://dl.dropboxusercontent.com/u/17/%{name}-lnx.x86_64-%{version}.tar.gz
Source1:	https://dl.dropboxusercontent.com/u/17/%{name}-lnx.x86-%{version}.tar.gz
URL:		http://www.dropbox.com/

%description
Dropbox is software that syncs your files online and across your computers
and also allows one to share files with other dropbox users.

%prep

%build -T -c
%ifarch x86_64
tar xf %{SOURCE0}
%else
tar xf %{SOURCE1}
%endif

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/%{name}
cp -R .dropbox-dist/VERSION .dropbox-dist/dropbox-lnx.*-%{version} .dropbox-dist/dropboxd %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_bindir}
ln -s ../..%{_libdir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}d
%{_libdir}/%{name}

%changelog
* Fri Jan 30 2015 Wei-Lun Chao <bluebat@member.fsf.org> 3.0.5
- Updated

* Mon Dec 23 2013 Pinoc <vogtpet at gmail.com> 2.4.10-1pclos2014
- 2.4.10

* Thu Oct 17 2013 Pinoc <vogtpet at gmail.com> 2.4.3-1pclos2013
- 2.4.3

* Thu Oct 17 2013 Pinoc <vogtpet at gmail.com> 2.4.2-1pclos2013
- 2.4.2

* Sun Oct 06 2013 Pinoc <vogtpet at gmail.com> 2.4.1-1pclos2013
- 2.4.1

* Sat Sep 14 2013 Pinoc <vogtpet at gmail.com> 2.2.13-1pclos2013
- 2.2.13

* Fri Jul 19 2013 Pinoc <vogtpet at gmail.com> 2.2.9-1pclos2013
- 2.2.9

* Sat Jun 22 2013 Pinoc <vogtpet at gmail.com> 2.2.3-1pclos2013
- 2.2.3
- combined setup for 32/64

* Tue Mar 19 2013 Pinoc <vogtpet at gmail.com> 2.0.0-1pclos2013
- 2.0.0

* Sat Dec 22 2012 Pinoc <vogtpet at gmail.com> 1.6.10-1pclos2012
- 1.6.10

* Sat Dec 15 2012 Pinoc <vogtpet at gmail.com> 1.6.5-1pclos2012
- 1.6.5

* Tue Nov 20 2012 Pinoc <vogtpet at gmail.com> 1.6.0-1pclos2012
- 1.6.0

* Mon Jun 18 2012 Pinoc <vogtpet at gmail.com> 1.4.9-1pclos2012
- 1.4.9
- add Require for sqlite3-tools

* Sat May 26 2012 Pinoc <vogtpet at gmail.com> 1.4.7-1pclos2012
- 1.4.7

* Wed May 02 2012 Pinoc <vogtpet at gmail.com> 1.4.0-1pclos2012
- 1.4.0

* Sun Jan 29 2012 Pinoc <vogtpet at gmail.com> 1.2.51-1pclos2012
- 1.2.51
- changed compression to xz

* Fri May 27 2011 Pinoc <vogtpet at gmail.com> 1.1.35-1pclos2011
- 1.1.35

* Wed Apr 27 2011 Texstar <texstar at gmail.com> 1.1.28-1pclos2011
- 1.1.28

* Thu Mar 31 2011 Texstar <texstar at gmail.com> 1.0.28-1pclos2011
- 1.0.28

* Sat Feb 27 2010 Texstar <texstar at gmail.com> 0.7.110-1pclos2010
- update

* Sun Nov 08 2009 Texstar <texstar at gmail.com> 0.6.557-1pclos2010
- add provide exceptions per mdawkins

* Sat Sep 12 2009 Texstar <texstar at gmail.com> 0.6.557-1pclos2009
- create package
