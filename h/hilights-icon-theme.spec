%define theme_name Hi-Lights

Summary: %{theme_name} icon theme
Name: hilights-icon-theme
Version: 5.0
Release: 4.1
License: GPL
Group: User Interface/Desktops
URL: https://gnome-look.org/content/show.php/Hi-Lights?content=153771
Source: %{theme_name}_%{version}.tar.gz
BuildArch: noarch

%description
Taking into account the wishes of users post the updated version of a set of
icons. I'm developing icons for KDE and Gnome I have, so please send Gnome
user errors found. Whole set includes 10,300 icons.

%prep
%setup -q -c
sed -i 's|Example=start-here|Example=folder|' index.theme
sed -i 's|actions48|actions/48|' index.theme

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
* Sun Jun 16 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0
- Rebuilt for Fedora
