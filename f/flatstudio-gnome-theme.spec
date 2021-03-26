%define theme_name FlatStudio

Summary: %{theme_name} GTK and Metacity theme
Name: flatstudio-gnome-theme
Version: 1.03
Release: 33.1
License: GPL
Group: User Interface/Desktops
Source0: 154296-%{theme_name}-%{version}.tar.gz
Source1: %{theme_name}-index.theme
Source2: %{theme_name}Light-index.theme
Source3: %{theme_name}Gray-index.theme
Source4: %{theme_name}Dark-index.theme
Source5: Chairs.png
URL: http://gnome-look.org/content/show.php/FlatStudio?content=154296
BuildArch: noarch
Requires: gtk-murrine-engine
Requires: flatwoken-icon-theme
Requires: apparatus-cursor-theme

%description
There are four themes:
FlatStudio: based on the color of my other theme MediterraneanNight
FlatStudioLight: found a mockup that I really liked and in which I based for
FlatStudioLight, the mockup is of Tobias Bernard\'s (minimal GTK theme mockup),
found in http://tobiasbernard.com/floss/minimal-gtk-theme/
FlatStudioGray: soft gray frame
FlatStudioDark: flat dark theme :)
With Wallpaper from http://www.icanbecreative.com/simple-desktop-wallpapers-for-minimalist-lovers.html

%prep
%setup -q -c
rm %{theme_name}/*.gz
cp %{SOURCE1} %{theme_name}/index.theme
cp %{SOURCE2} %{theme_name}Light/index.theme
cp %{SOURCE3} %{theme_name}Gray/index.theme
cp %{SOURCE4} %{theme_name}Dark/index.theme
cp %{SOURCE5} %{theme_name}

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
* Wed Mar 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.03
- Rebuild for Fedora
