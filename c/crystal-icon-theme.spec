%define theme_name crystalsvg

Summary:        %{theme_name} icon theme
Name:           crystal-icon-theme
Version:        2.6
Release:        4.1
License:        GPL
Group:          User Interface/Desktops
URL:            https://gnome-look.org/content/show.php/Crystal?content=108398
Source0:        Crystal.tar.bz2
BuildArch:      noarch
Obsoletes:      crystal-svg-icon-theme

%description
FOR KDE 3.5 LOVERS!!! These icons are from Everaldo:
https://www.everaldo.com/crystal/ and I just revived the old icon theme:
https://www.gnome-look.org/content/show.php/Crystal+SVG+Icons?content=24758
because a lot of icons were not working properly, I edited a couple of icons,
but the credits design is for Everaldo and his project.

%prep
%setup -q -n Crystal
rm index.theme~

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
* Fri Apr 08 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6
- Rebuilt for Fedora
