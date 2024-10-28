%define theme_name Chi

Summary:        Chi GTK theme
Name:           chi-gtk-theme
Version:        20131031
Release:        11.1
License:        GPL
Group:          User Interface/Desktops
URL:            https://gnome-look.org/content/show.php/Chi+?content=143387
Source0:        https://gnome-look.org/CONTENT/content-files/143387-Chi.tar.bz2
BuildArch:          noarch
Requires:       feelofjapan-icon-theme
Requires:       woodshed-metacity-theme

%description
Used interior deco of local chain restaurant, as a idea, melded an exterior
1947 Chrysler Town and Country as a toolbar, panel, etc.

%prep
%setup -q -n %{theme_name}
sed -i 's|#IconTheme=|IconTheme=Feel-of-Japan|' index.theme
sed -i '10i MetacityTheme=WoodShed' index.theme
sed -i '$a BackgroundImage=/usr/share/icons/Feel-of-Japan/158335-Japanese_Room.jpg' index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%files 
%{_datadir}/themes/%{theme_name}

%changelog
* Thu Jan 02 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 20131031
- Rebuilt for Fedora
