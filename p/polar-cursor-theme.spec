%define theme_name Polar

Summary:        Polar cursor theme
Name:           polar-cursor-theme
Version:        1.4
Release:        6.1
License:        GPL
Group:          User Interface/Desktops
URL:            http://gnome-look.org/content/show.php/Polar+Cursor+Theme?content=27913
Source0:        http://gnome-look.org/CONTENT/content-files/27913-PolarCursorThemes.tar.bz2
BuildArch:      noarch

%description
Polar Cursor Theme is a smooth and simple cursor set created primarily in Inkscape.

%prep
%setup -q -c
rm -rf */*~ */Source
sed -i 's|PolarCursorTheme|%{theme_name}|' */index.theme
rename PolarCursorTheme %{theme_name} *

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/icons/%{theme_name}*

%changelog
* Mon May 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
