%define theme_name BigMint

Summary: %{theme_name} GTK & Metacity theme
Name: bigmint-gnome-theme
Version: 1.2
Release: 13.1
License: free 
Group: User Interface/Desktops
Source0: https://dl.opendesktop.org/api/files/download/id/1460759481/163179-%{theme_name}_2014-05-16.zip
URL: https://www.cinnamon-look.org/p/1012607/
BuildArch: noarch
Requires: comixcursors-cursor-theme
Requires: mintx-icon-theme
BuildRequires: ghostscript-core ImageMagick
Source1: http://www.hartwork.org/public/zwopper/Zwopper-Green-Dew-CC-BY-SA-30-2560x1600.png

%description
A tribute to Linux Mint :)
With background by zwopper.

%prep
%setup -q -c
cp %{theme_name}/metacity-1/titlebar-focused-middle.png %{theme_name}/metacity-1/titlebar-unfocused-middle.png
convert -resize 1920x1200 %{SOURCE1} %{theme_name}/Zwopper-Green-Dew-CC-BY-SA-30-1920x1200.png
sed -i '$a BackgroundImage=/usr/share/themes/%{theme_name}/Zwopper-Green-Dew-CC-BY-SA-30-1920x1200.png' %{theme_name}/index.theme
sed -i 's|CursorTheme=.*|CursorTheme=ComixCursors-Green|' %{theme_name}/index.theme
sed -i 's|rounded_top_left="true" rounded_top_right="true" rounded_bottom_left="false"|rounded_top_left="false" rounded_top_right="true" rounded_bottom_left="true"|' %{theme_name}/metacity-1/metacity-theme-1.xml
sed -i 's|x="6" y="0" width="width - 6"|x="3" y="0" width="width - 3"|' %{theme_name}/metacity-1/metacity-theme-1.xml

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a %{theme_name} $RPM_BUILD_ROOT%{_datadir}/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Thu Aug 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
