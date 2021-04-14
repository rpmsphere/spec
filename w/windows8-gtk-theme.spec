%define theme_name Windows8

Summary:        Windows8 GTK theme
Name:           windows8-gtk-theme
Version:        1.3
Release:        5.1
License:        GPL
Group:          User Interface/Desktops
URL:            http://gnome-look.org/content/show.php?content=158721
Source0:        http://gnome-look.org/CONTENT/content-files/158721-Windows8-gtk-%{version}.tar.gz
BuildArch:	    noarch
Requires:       win2-7-theme
Requires:       win8-cursor-theme
Requires:       win9-backgrounds

%description
Windows 8 modern UI (metro) gtk3 (+gtk2) theme.

%prep
%setup -q -n %{theme_name}
sed -i -e 's|ubuntu-mono-dark|Win2-7Libre|' -e 's|DMZ-White|Win8|' index.theme
echo BackgroundImage=/usr/share/backgrounds/win9/color.png >> index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/themes/%{theme_name}

%changelog
* Mon Apr 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
