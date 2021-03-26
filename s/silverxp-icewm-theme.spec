Name: silverxp-icewm-theme
Version: 1.2.17
Release: 5.1
License: GPL
Group: Graphical desktop/Icewm
URL: http://sourceforge.net/projects/icewmsilverxp/
Summary: A theme for IceWM inspired by the Silver theme of WindowsXP
BuildArch: noarch
Requires: icewm
Source: http://prdownloads.sourceforge.net/icewmsilverxp/SilverXP-1.2.17-single-1.tar.bz2

%description
A theme for IceWM window manager inspired by the Silver theme of WindowsXP.
The theme have a very nice look based on gradients and shaped windows
decorations.

%prep
%setup -q -c

%build

%install
mkdir -p %buildroot%_datadir/icewm/themes
cp -a icewm/themes/SilverXP-1.2.17-single-1 %buildroot%_datadir/icewm/themes/SilverXP

# fix font name
/bin/sed -i 's,-koi8-r,-*-*,g' %buildroot%_datadir/icewm/themes/*/default.theme
# do not paint buttons border
/bin/sed -i 's,^#  $,ShowButtonBorder=0,' %buildroot%_datadir/icewm/themes/*/default.theme

find %buildroot%_datadir/icewm/themes -type f -print0 | 
	xargs -r0 chmod 0444
find %buildroot%_datadir/icewm/themes -type d -print0 | 
	xargs -r0 chmod 0755

%files
%_datadir/icewm/themes/SilverXP

%changelog
* Thu Mar 31 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.17
- Rebuild for Fedora
* Mon Jan 07 2013 Dmitriy Khanzhin <jinn@altlinux.org> 1.2.17-alt5
- updated some .xpm's for fix breaks themes with xorg 1.12.3.902 and later
  (bfo#54168)
* Sun Mar 20 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 1.2.17-alt4
- now depends of design-icewm
* Sun Nov 01 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 1.2.17-alt3
- internal RPM macros are replaced by real commands
* Sat Jan 20 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 1.2.17-alt2
- rebuild (fix bug #10391)
* Mon Sep 26 2005 Kachalov Anton <mouse@altlinux.ru> 1.2.17-alt1
- first build
