%global __os_install_post %{nil}

Name:           winetools
URL:            https://www.von-thadden.de/Joachim/%{name}/
License:        GNU General Public License (GPL)
Group:          Applications/Emulator
Summary:        Easy WINE Setup and Program Installation
Version:        0.9jo
Release:        1
Source0:        %{name}-%{version}-III.tar.gz
Source1:        wt0.9-zh_TW.po
Patch0:         %{name}-suse.patch
BuildArch:      noarch
Requires:       wine wget xdialog gettext

%description
WineTools is a menu-driven installer for installing Windows programs
under the x86 (Athlon or Intel PC) processor architecture with the
Linux operatin system using Wine. This software lets you install the
following Windows software:
- DCOM98
- InternetExplorer 6
- Windows Core Fonts
- Windows System Software
- Office & Office Viewer
- Adobe Photoshop 7, Illustrator 9, Acrobat Reader 5.1
- Many other programs

Authors:
--------
    Joachim von Thadden <thadden@web.de>
    Frank Hendriksen <frank@franksworld.net>
    Mike Hearn <mike@navi.cx>

%prep
%setup -q -n %{name}-%{version}-III
%patch0 -p0
%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Name=WineTools
Name[zh_TW]=WINE 加值程式安裝
Comment=Easy WINE Setup and Program Installation
Comment[zh_TW]=簡單的 WINE 設定與加值程式安裝工具
Exec=wt
Terminal=false
Type=Application
Categories=Application;System;
Icon=%{name}
EOF

%install
%{__rm} -rf %{buildroot}
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%{__sed} -i 's/dlldump.com\/dllfiles\/M/gorzyk.tczew.net.pl\/pliki\/instalki\/ubuntu-dapper\/Wine\/winetools\/sys/' wt%{version}
%{__sed} -i 's/^root_test$/#root_test/' findwine
perl -pi -e 's#^. findwine#. /usr/share/winetools/findwine#;' scripts/*
%{__cp} -a 3rdParty doc icon scripts chopctrl.pl findwine gettext.sh.dummy %{buildroot}%{_datadir}/%{name}
%__install -D -m 755 wt%{version} %{buildroot}%{_bindir}/wt
%__install -D -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%__install -D -m 644 icon/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%{__cp} %{SOURCE1} po/zh_TW.po
mv po/de_DE@euro.po po/de_DE.po
cd po
for i in $(ls *.po|cut -f1 -d.) ; do
  mkdir -p %{buildroot}%{_datadir}/locale/$i/LC_MESSAGES
  msgfmt $i.po -o %{buildroot}%{_datadir}/locale/$i/LC_MESSAGES/wt0.9.mo
done
cd ..

%clean
%{__rm} -rf %{buildroot}

%files
%doc INSTALL.txt LICENSE.txt
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9jo
- Rebuilt for Fedora
* Thu Dec 08 2005 Joachim von Thadden <thadden@web.de>
- version 0.9 III
* Sat Nov 19 2005 Joachim von Thadden <thadden@web.de>
- version 0.9 II
* Thu Nov 08 2005 Joachim von Thadden <thadden@web.de>
- version for 0.9
* Wed May 25 2005 Gladiston Santana <gladiston.santana@gmail.com>
- Updated to 2.1.2 and CL10 package compatible
