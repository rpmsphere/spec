%global debug_package %{nil}
Name:           tipp10
Summary:        Educational typing tutor
URL:            http://www.tipp10.de/
License:        GPLv2+
Group:          Amusements/Games
Version:        2.0.3
Release:        1
BuildRequires:  qt4-devel sqlite-devel libpng-devel unzip
Requires:	qt4-sqlite
Source:         tipp10_source_v2-0-3.zip
Source1:	%name.png
Source2:        tipp10.desktop

%description
TIPP10 is an educational typing tutor which automatically adapts the 
lesson to the typing failures of of the student.

%prep
%setup -q -n %{name}
find -name Thumbs.db |xargs rm -fv

%build
qmake-qt4
sed -i 's|-Wall|-Wall -fpermissive|' Makefile
make

%install
rm -rf %{buildroot}
mkdir -p %buildroot{%_bindir,%_datadir/%name}
cp -a license.txt help tipp10 tipp10v2.template wrong.wav %buildroot%_datadir/%name

cat > %buildroot%_bindir/%name << EOF
#!/bin/bash
cd %_datadir/%name
./tipp10 "\$@"
EOF

install -D -m644 %{SOURCE1} %buildroot/%_datadir/pixmaps/%name.png
install -D -m644 %{SOURCE2} %buildroot/%_datadir/applications/%name.desktop

%clean
rm -rf %buildroot

%files
%attr(755,root,root) %_bindir/%name
%_datadir/pixmaps/%name.png
%_datadir/applications/%name.desktop
%_datadir/%name

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.3
- Rebuild for Fedora
* Thu Sep 25 2008 lars@linux-schulserver.de
- moved to Education base repository
* Thu Sep 25 2008 lars@linux-schulserver.de
- moved to Education base repository
* Thu Jun  5 2008 lars@linux-schulserver.de
- fix type in install
* Sun May 18 2008 lars@linux-schulserver.de
- fix database problem (os-edu #0000036)
* Wed Mar 19 2008 lars@linux-schulserver.de
- initial version 2.0.1
