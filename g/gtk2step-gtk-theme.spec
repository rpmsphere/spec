%define theme_name GTK2-Step

Name: gtk2step-gtk-theme
Version: 1.2
Release: 12.1
Summary: The NeXT look of GTK2
License: GPL
Group: Graphical desktop/GNOME
BuildArch: noarch
Source0: %theme_name-%version.tar.gz
Source1: http://sid.ethz.ch/gnustep/root/etc/skel/Backgrounds/gnustep.png
Requires: nouvegnome-icon-theme
Requires: openzone-cursor-theme

%description
%theme_name theme is the NeXT look of GTK2.

%prep
%setup -n %theme_name
sed -i 's|IconTheme=Gorilla|IconTheme=nouveGnome|' index.theme
sed -i '$a BackgroundImage=/usr/share/themes/%{theme_name}/gnustep.png' index.theme
sed -i '$a CursorTheme=OpenZone_White' index.theme
chmod -R a-rwx,u+rwX,a+rX *
find . -name '*~' -delete

%install
mkdir -p %buildroot%_datadir/themes/%theme_name
cp -r index.theme gtk-2.0 %{SOURCE1} %buildroot%_datadir/themes/%theme_name

%files
%_datadir/themes/%theme_name

%changelog
* Thu Sep 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuild for Fedora
* Fri Apr 09 2004 Sir Raorn <raorn@altlinux.ru> 1.2-alt1
- [1.2]
* Thu Mar 25 2004 Sir Raorn <raorn@altlinux.ru> 1.1-alt1
- Built for Sisyphus
