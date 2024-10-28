%define theme_name TechniX

Summary: %{theme_name} gnome theme
Name: technix-gnome-theme
Version: 0.1
Release: 5.1
License: GPL
Group: User Interface/Desktops
URL: https://www.gnome-look.org/content/show.php/TechniX?content=79463
Source0: technix-theme.zip
Source1: https://dl.opendesktop.org/api/files/download/id/1460931636/78226-DRM-X.jpg
BuildArch: noarch
Requires: titanium-icon-theme
Requires: defenderblack-cursor-theme

%description
Contains the %{theme_name} theme for gtk and metacity.

%prep
%setup -q -n %{theme_name}
sed -i '/colorize_scrollbar/d' gtk-2.0/gtkrc
sed -i 's|CursorTheme=artwiz|CursorTheme=DefenderBlack|' index.theme
sed -i '$a BackgroundImage=/usr/share/themes/%{theme_name}/78226-DRM-X.jpg' index.theme

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/themes/%{theme_name}
cp -a * %{SOURCE1} %{buildroot}%{_datadir}/themes/%{theme_name}

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
