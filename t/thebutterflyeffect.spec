%global _name TheButterflyEffect

Name:		thebutterflyeffect
# sed -n '/APPRELEASE/s/.*"\(.*\)".*/\1/p' src/tbe_global.h
Version:	0.8.2
Release:	1
License:	GPL
Group:		Games/Puzzles
Summary:	Combine mechanical elements to achieve a simple goal in the most complex way
Source:		http://dl.sourceforge.net/project/tbe/Milestone%%208.2/%_name-m8.2.src.tgz
Patch:		%_name-qt4.patch
URL:		http://sourceforge.net/apps/trac/tbe/wiki/WikiStart
BuildRequires: gcc-c++ qt4-devel unzip

%description
The Butterfly Effect uses realistic physics simulations to combine lots of simple
mechanical elements to achieve a simple goal in the most complex way possible.

%prep
%setup -q -n %_name-m%version
%patch

%build
./configure --datadir=%_datadir/%name
echo "QQQ"
#( cd 3rdParty; #make_build )
#qmake-qt4
%make_build
cat > %name <<@@@
#!/bin/sh
cd %_datadir/%name
%_bindir/tbe
@@@

%install
mkdir -p %buildroot%_datadir/%name
cp -a images i18n levels %buildroot%_datadir/%name
install -D tbe %buildroot%_bindir/tbe
install -D -m755 %name %buildroot%_bindir/%name

%files
%doc README
%_bindir/*
%_datadir/%name

%changelog
* Mon Jan 26 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.2
- Rebuilt for Fedora
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 8.2-alt1.qa1
- NMU: rebuilt for debuginfo.
* Mon Dec 06 2010 Fr. Br. George <george@altlinux.ru> 8.2-alt1
- Version up
- Milestone based versioning used
* Fri Jul 02 2010 Fr. Br. George <george@altlinux.ru> 0.0.3-alt1
- Initial build for ALT
