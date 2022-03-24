%define theme_name Orchis

Summary:        Orchis and Orchis-Dark GTK theme
Name:           orchis-gtk-theme
Version:        2022.03.12
Release:        1
License:        GPL
Group:          User Interface/Desktops
#URL:            https://github.com/vinceliuice/Orchis-theme
URL:            https://www.gnome-look.org/p/1357889/
Source0:        Orchis.tar.xz
Source1:	orchis-purpurea-purpur-knabenkraut-3.jpg
BuildArch:	noarch
Requires:       moka-icon-theme

%description
Orchis is an elegant, modern desktop theme for Linux. Is has semi-flat style
and eschewing some of the traditional design patterns, it creates an elegant
desktop experience.

%prep
%setup -q -c
cp %{SOURCE1} %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a %{theme_name}* $RPM_BUILD_ROOT%{_datadir}/themes
#sed -i 's|GtkTheme=Orchis-Dark|GtkTheme=Orchis|' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}-Dark/index.theme
sed -i '$a BackgroundImage=/usr/share/themes/%{theme_name}/orchis-purpurea-purpur-knabenkraut-3.jpg' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}*/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files 
#doc AUTHORS LICENSE
%{_datadir}/themes/%{theme_name}*

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2022.03.12
- Rebuilt for Fedora
