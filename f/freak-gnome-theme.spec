%define theme_name Freak

Summary: %{theme_name} GTK and Metacity theme
Name: freak-gnome-theme
Version: 1.1
Release: 10.1
License: CC-BY-NC-SA
Group: User Interface/Desktops
Source0: FREAK1.1.tar.gz
Requires: buuf-icon-theme
Requires: buuf-backgrounds
Requires: buuf-cursor-theme
Requires: gtk-aurora-engine
BuildArch: noarch
URL: https://gnome-look.org/content/show.php/FREAK+1.1?content=116383

%description
Improved theme for BUUF.
wall : https://hotiron.deviantart.com/art/macabre-series-110073622 by Hotiron
skydome : https://alexander-gg.deviantart.com/art/Firewall-143988510 by AlexanderGG

gtkrc :
https://gnome-look.org/content/show.php/Santay+theme+pack?content=88825 by Jecovier
https://gnome-look.org/content/show.php/Freak?content=105620
Aurora, Murrine and Pixmaps engine required

Emerald Title and Desktop Panel:
https://gnome-look.org/content/show.php/Gnome+Panel+Collection?content=112337 by PaperOnFire
https://gnome-look.org/content/show.php/Santay+theme+pack?content=88825 by Jecovier
Buttons: https://gnome-look.org/content/show.php/Buuf?content=81153 by OxayotlTheGreat

%prep
%setup -q -c
sed -i 's|BackgroundImage=.*|BackgroundImage=/usr/share/backgrounds/buuf/Some_clouds__sun.png|' FREAK1.1/index.theme
sed -i -e 's|buuf2.28|Buuf|' -e 's|FREAK1.1|Freak|' -e 's|Chameleon-Anthracite-Small-0.5|BuufCursor|' FREAK1.1/index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a FREAK1.1 $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}
tar zxf Smooth\ Grey\ BUUF.emerald -C $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}

%files
%doc readme
%{_datadir}/themes/%{theme_name}
%{_datadir}/emerald/themes/%{theme_name}

%changelog
* Tue Jul 12 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
