%define theme_name Orchis

Summary:        Orchis and Orchis-Dark GTK theme
Name:           orchis-gtk-theme
Version:        3.0
Release:        6.1
License:        GPL
Group:          User Interface/Desktops
URL:            https://github.com/moka-project/orchis-gtk-theme
Source0:        https://raw.githubusercontent.com/moka-project/orchis-gtk-theme/master/%{name}-%{version}.tar.gz
Source1:        http://www.pflanzenportraits.com/blog/files/orchis-purpurea-purpur-knabenkraut-3.jpg
BuildArch:	    noarch
Requires:       moka-icon-theme

%description
Orchis is an elegant, modern desktop theme for Linux. Is has semi-flat style
and eschewing some of the traditional design patterns, it creates an elegant
desktop experience.

%prep
%setup -q
cp %{SOURCE1} %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a %{theme_name}* $RPM_BUILD_ROOT%{_datadir}/themes
sed -i 's|GtkTheme=Orchis-Dark|GtkTheme=Orchis|' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}-Dark/index.theme
sed -i '$a BackgroundImage=/usr/share/themes/%{theme_name}/orchis-purpurea-purpur-knabenkraut-3.jpg' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}*/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%doc AUTHORS LICENSE
%{_datadir}/themes/%{theme_name}*

%changelog
* Wed May 20 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0
- Rebuilt for Fedora
