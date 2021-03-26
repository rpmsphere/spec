%global debug_package %{nil}
Summary:	A simple Python interface to GLPK
Name:		python-glpk
Version:	0.4.43
Release:	6.1
Epoch:		1
Source0:    http://www.dcc.fc.up.pt/~jpp/code/python-glpk/%{name}-%{version}.tar.gz
Patch0:		Makefile.patch
License:	GPLv2
Group:		Development/Python
URL:		http://www.dcc.fc.up.pt/~jpp/code/python-glpk/
BuildRequires:	python-devel
BuildRequires:	glpk-devel, swig
BuildRequires:  atlas

%description
This requires GLPK to be installed, and uses the SWIG package for
producing the API. Notice that the glpk's C keyword 'in' is renamed
'_in' in Python, for avoiding conflict.

%prep
%setup -q
%patch0 -p1 

%build
make -C src all

%install
cd src
python2 setup.py install --root=%{buildroot}

%files
%doc COPYING ChangeLog readme.txt examples
%{python2_sitearch}/*

%changelog
* Thu Feb 06 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.43
- Rebuild for Fedora
* Sun Nov 21 2010 Funda Wang <fwang@mandriva.org> 1:0.4.43-2mdv2011.0
+ Revision: 599397
- rebuild for py 2.7
* Tue Jul 13 2010 Lev Givon <lev@mandriva.org> 1:0.4.43-1mdv2011.0
+ Revision: 551465
- Update to 0.4.43.
- Update to 0.3.43.
- Update to 0.1.36.
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
* Sat Jan 10 2009 Funda Wang <fwang@mandriva.org> 1:0.1.16-2mdv2009.1
+ Revision: 328010
- llink against py ver
* Fri Jul 25 2008 Lev Givon <lev@mandriva.org> 1:0.1.16-1mdv2009.0
+ Revision: 249838
- Since this package no longer builds, switch to the python-glpk
  software included in Debian.
  Update epoch to account for different version numbers.
- Tweak to rebuild with Python 2.5.
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.4-2mdk
- Rebuild for new python
* Mon Sep 06 2004 Yoshinori Okuji <yo@nexedi.com> 0.4-1mdk
- updated to use libglpk4.7
* Fri Feb 27 2004 Sebastien Robin <seb@nexedi.com> 0.3-1mdk
- updated to use libglpk4.4
* Tue Oct 21 2003 Yoshinori OKUJI <yo@nexedi.com> 0.2-1nxd
- new upstream release
* Mon Oct 20 2003 Yoshinori OKUJI <yo@nexedi.com> 0.1-1nxd
- initial version
