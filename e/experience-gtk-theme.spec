%define theme_name eXperience

Summary:        eXperience GTK theme
Name:           experience-gtk-theme
Version:        3.02
Release:        1.1
License:        GPL
Group:          User Interface/Desktops
URL:            http://art.gnome.org/themes/gtk2/1058
Source0:        http://art.gnome.org/download/themes/gtk2/1058/GTK2-EXperience.tar.gz
BuildArch:	noarch
Requires:	gtk-experience-engine, experience-icon-theme

%description
eXperience GTK theme by David Christian Berg.

%prep
%setup -q -c
sed -i -e 's|-my||' -e 's| - |-|' */index.theme
mv "%{theme_name} - ice" %{theme_name}-ice
mv "%{theme_name} - olive" %{theme_name}-olive
cp -a %{theme_name}/gtk-2.0/tweaks %{theme_name}-ice/gtk-2.0/
cp -a %{theme_name}/gtk-2.0/tweaks %{theme_name}-olive/gtk-2.0/

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a %{theme_name}* $RPM_BUILD_ROOT%{_datadir}/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/themes/%{theme_name}*

%changelog
* Sun Mar 03 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.02
- Rebuild for Fedora
