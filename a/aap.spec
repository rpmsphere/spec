%define __arch_install_post %{nil}

Summary:	Construction tool
Name:		aap
Version:	1.094
Release:	4.1
Source0:	https://belnet.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.zip
License:	GPLv2
Group:		Development/Other
BuildArch:	noarch
BuildRequires:	python2-devel
Requires:	python2
URL:		https://www.a-a-p.org/
Provides:	a-a-p

%description
A-A-P is an Open Source software construction tool--that is, a build
tool; an improved substitute for the classic Make utility; a better way
to build software. A-A-P "configuration files" are similar to makefile
but they can include Python.

A-A-P uses MD5 signatures to rebuild only when the contents of a file have
really changed, not just when the timestamp has been touched. A-A-P
supports side-by-side variant builds, and is easily extended with user-
defined Builder and/or Scanner objects.  Most of the a-a-p logic is object
oriented, including default build rules for many types of program,  they are
all overloadable also.

%prep
%setup -q -c
sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{name} *.py

%build

%install
rm -rf $RPM_BUILD_ROOT
export PYTHONOPTIMIZE=1
mkdir -p $RPM_BUILD_ROOT/usr
./%{name} PREFIX=$RPM_BUILD_ROOT/usr install

cd $RPM_BUILD_ROOT/%{_bindir}
rm %{name}
ln -s ../lib/aap/Exec-%{version}/%{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}

mkdir -p $RPM_BUILD_ROOT/%{_datadir}
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/%{_mandir}
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT/usr/lib/%{name}/Exec-%{version}/doc $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}

#sed -i 's|/usr/bin/env python|/usr/bin/python2|' $RPM_BUILD_ROOT/usr/lib/aap/Exec-%{version}/*.py $RPM_BUILD_ROOT/usr/lib/aap/Exec-%{version}/aap

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
/usr/lib/%{name}
%{_mandir}/man*/*
%{_docdir}/%{name}-%{version}

%changelog
* Mon Jun 04 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.094
- Rebuilt for Fedora
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.091-2mdv2011.0
+ Revision: 609899
- rebuild
* Fri Feb 26 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.091-1mdv2010.1
+ Revision: 511526
- Fix mix of spaces and tabs in spec
- Fix source0
- Fix license
- Update to 1.090
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - rebuild
* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.090-2mdv2008.1
+ Revision: 170695
- rebuild
- kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Tue Aug 21 2007 Gaëtan Lehmann <glehmann@mandriva.org> 1.090-1mdv2008.0
+ Revision: 68255
- 1.090
* Fri Feb 23 2007 Gaëtan Lehmann <glehmann@mandriva.org> 1.089-1mdv2007.0
+ Revision: 124900
- 1.089
- Import a-a-p
* Tue Jun 27 2006 Lenny Cartier <lenny@mandriva.com> 1.088-2mdv2007.0
- rebuild
* Sat Mar 04 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.088-1mdk
- New release 1.088
* Fri Feb 10 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.087-1mdk
- New release 1.087
* Wed Feb 08 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.086-1mdk
- New release 1.086
* Tue Jan 17 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.085-1mdk
- New release 1.085
* Tue Jan 10 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.084-1mdk
- New release 1.084
- fix extraction path (archive doesn't contains root dir this time)
* Wed Dec 21 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.083-1mdk
* Tue Dec 20 2005 Ian S. Nelson <nelsonis@earthlink.net> 1.083-1mdk
 - Updating to aap 1.083.  There are several minor fixes
* Sat Dec 17 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.080-1mdk
- Initial mdk RPM package from Ian S. Nelson <nelsonis@earthlink.net>
