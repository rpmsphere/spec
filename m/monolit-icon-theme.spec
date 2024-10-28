%define theme_name Monolit

Summary: %{theme_name} icon theme
Name: monolit-icon-theme
Version: 0.4.1
Release: 7.1
License: CC 3.0 BY-NC-SA
Group: User Interface/Desktops
URL: https://www.gnome-look.org/content/show.php/?content=119813
Source: https://dl.opendesktop.org/api/files/download/id/1466436815/%{theme_name}_%{version}.tar.bz2
BuildArch: noarch

%description
Icons theme for linux. This iconset contains mimetypes icons, places icons
(folder, trash, etc.) and partly devices icons. My own handmade in GIMP.
No collection, no use of other themes. Icons that I have not yet created,
there simply are not included.

%prep
%setup -q -n %{theme_name}_%{version}
sed -i 's|Example=exec|Example=folder|' index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%files
%{_datadir}/icons/%{theme_name}*

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuilt for Fedora
