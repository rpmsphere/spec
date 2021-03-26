%global theme_name    Boomerang

Name:           boomerang-gnome-theme
Version:        5.0
Release:        9.1
Summary:        Boomerang Themes for GNOME
Group:          User Interface/Desktops
License:        GPLv3
URL:            http://ghogaru.deviantart.com/art/Boomerang-GTK3-189180645
Source0:        boomerang___gtk3_by_ghogaru-d34mspx.zip
Source1:        http://www.shoutot.net/stockimage/boomerang-nebula-hubble-wallpaper-heica.jpg
BuildArch:      noarch
Requires:       faience-icon-theme
Requires:       dmz-cursor-themes

%description
Boomerang is designed and developed by Muhammad Nabil
a.k.a ghogaru <ghogaru.deviantart.com>

%prep
%setup -q -n Boomerang_GTK_by\ ghogaru

%build

%install
mkdir -p -m755 %{buildroot}%{_datadir}/themes
tar xf %{theme_name}.tar.gz -C %{buildroot}%{_datadir}/themes
tar xf %{theme_name}-Deux.tar.gz -C %{buildroot}%{_datadir}/themes
rm %{buildroot}%{_datadir}/themes/Boomerang*/index.theme~
sed -i 's|Theme=Boomerang Deux|Theme=Boomerang-Deux|' %{buildroot}%{_datadir}/themes/Boomerang-Deux/index.theme
sed -i 's|CursorTheme=DMZ-White|CursorTheme=dmz|' %{buildroot}%{_datadir}/themes/Boomerang*/index.theme
cp %{SOURCE1} %{buildroot}%{_datadir}/themes/Boomerang
sed -i '$a BackgroundImage=/usr/share/themes/Boomerang/boomerang-nebula-hubble-wallpaper-heica.jpg' %{buildroot}%{_datadir}/themes/Boomerang*/index.theme

%files
%doc COPYING ChangeLog README
%{_datadir}/themes/%{theme_name}*

%changelog
* Mon Mar 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0
- Rebuild for Fedora
