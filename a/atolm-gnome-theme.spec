%define theme_name Atolm

Name: atolm-gnome-theme
Version: 20150203
Release: 9.1
Summary: Atolm gnome theme
License: GPL
Group: Graphical desktop/GNOME
BuildArch: noarch
URL: https://github.com/Arakis/Atolm-gtk3
Source0: Atolm-gtk3-master.zip
Source1: %{theme_name}-index.theme
Source2: http://www.deviantart.com/download/152712508/surface_i_wallpaper_by_sword1ne.png
Requires: blackwhite2-icon-theme
Requires: dmz-cursor-themes

%description
Updated Atolm theme by Arakis, based on Atolm-gtk3 by TheDeviantMars:
http://thedeviantmars.deviantart.com/art/Atolm-gtk3-206663190
and again based on Atolm-gtk2 by SkiesOfAzel:
http://skiesofazel.deviantart.com/art/Atolm-191381339

%prep
%setup -q -n Atolm-gtk3-master
cp %{SOURCE1} theme/index.theme

%install
mkdir -p %buildroot%_datadir/themes/%theme_name
cp -a theme/* %{SOURCE2} %buildroot%_datadir/themes/%theme_name

%files
%doc README.md LICENSE
%_datadir/themes/%theme_name

%changelog
* Thu Sep 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20150203
- Rebuilt for Fedora
