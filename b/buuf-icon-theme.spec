%define theme_name Buuf

Summary:        Buuf icon theme
Name:           buuf-icon-theme
Version:        3.42
Release:        1
License:        CC-BY-NC-SA
Group:          User Interface/Desktops
URL:            https://gnome-look.org/content/show.php/Buuf?content=81153
Source0:        https://buuficontheme.free.fr/buuf%{version}.tar.xz
BuildArch:      noarch

%description
Based on the buuf theme by fana-m
(https://gnome-look.org/content/show.php/buuf+icon+theme?content=44539).
A very few icons come Buuf-Deuce theme by djaany
(https://gnome-look.org/content/show.php/BuuF-Deuce-iconset?content=46201).
His theme has been really helpful to get the right icons name !
All icons were made by mattahan (https://mattahan.deviantart.com/),
thanks a lot to him for his great work !!

%prep
%setup -q -n buuf%{version}
sed -i 's|Example=gnome-main-menu|Example=folder|' index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/icons/%{theme_name}

%changelog
* Sun May 21 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 3.42
- Rebuilt for Fedora
