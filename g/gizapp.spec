Name: 		gizapp
Summary: 	GIZA++ and mkcls
Version: 	1.0.7
Release: 	4.1
License: 	GNU GPL v2
Source: 	giza-pp-v%{version}.tar.gz
BuildRequires: 	glibc-devel, glibc-headers
BuildRequires:  libstdc++-devel
Requires:	tcsh, libstdc++
URL:		http://code.google.com/p/giza-pp/

%description
GIZA++ is a statical machine translation toolkit that is used to train IBM
Models 1-5 and an HMM word alignment model. This package also contains the
source for the mkcls tool which generates the word classes necessary for
training some of the alignment models.

%prep
%setup -q -n giza-pp

%build
export CC=clang CXX=clang++
make

%install
rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 GIZA++-v2/GIZA++ %{buildroot}%{_bindir}/%{name}
install -m 755 GIZA++-v2/*.out %{buildroot}%{_bindir}
install -m 755 GIZA++-v2/*.sh %{buildroot}%{_bindir}
install -m 755 mkcls-v2/mkcls %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*

%changelog
* Sun Jun 30 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.7
- Rebuilt for Fedora
* Tue May 08 2012 Leo Jiang - 1.0.7-5
- add moses-suite-base as dependence
* Tue May 01 2012 Leo Jiang - 1.0.7-4
- rename the package and add the moses-suite-devel as build requires
* Sun Apr 29 2012 Leo Jiang - 1.0.7-3.fc16
- remove the macro tag and replace the installation path with macro _datadir
* Wed Apr 25 2012 Leo Jiang - v1.0.7-2.MosesSuite
- build for Fedora16
* Thu Apr 12 2012 Leo Jiang <leo.jiang.dev@gmail.com>
- we don't need the patch file now since upstream had removed the static flag in makefile
* Wed Feb 22 2012 Leo Jiang <leo.jiang.dev@gmail.com>
- update the source code to giza-pp.tgz from upstream, and patch the makefile because there is no 64bit static library on CentOS6
* Tue Aug 09 2011 Moses <leo.jiang.dev@gmail.com>
- remove the relocatable
* Mon Aug 08 2011 Moses <leo.jiang.dev@gmail.com>
- make the package relocatable
* Wed Aug 03 2011 Leo Jiang <leo.jiang.dev@gmail.com>
- add the patch0
* Wed Apr 20 2011 Leo Jiang <leo.jiang.dev@gmail.com>
- update the rpm spec
* Mon Apr 18 2011 Leo Jiang <leo.jiang.dev@gmail.com>
- create the rpm spec
