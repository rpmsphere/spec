%define theme_name Iris

Summary: %{theme_name} GTK and Metacity theme
Name: iris-gnome-theme
Version: 2016
Release: 16.1
License: GPL
Group: User Interface/Desktops
Source0: iris_dark_gtk_theme__v1_10_by_thevirtualdragon-d73sf8i.tgz
Source1: iris_light_gtk_theme__v1_75_by_thevirtualdragon-d73dv3h.tgz
Source2: https://pixabay.com/get/e03db50e2afc1c22d2524518a33219c8b66ae3d11eb5144595f9c278/matterhorn-984128_1280.jpg
Source3: zune_by_hellishere_12-1920x1200.jpg
URL: https://github.com/xyl0n
BuildArch: noarch
Requires: gtk-murrine-engine
Requires: faba-icon-theme
Requires: metacity-themes-compat
BuildRequires: ghostscript-core ImageMagick

%description
Iris Dark 1.10 is a flat theme that uses varying shades and tones to create
distinction and a modern experience. It supports Gtk 3.18 and Gtk 2
(using the Murrine engine).

Iris Light 1.75 supports Gtk 3.14, Gtk 2 (using the Murrine engine), Granite
Widgets and also includes a Metacity window decoration theme.

%prep
%setup -q -c -a 1
mogrify -gamma 2 "Iris Light"/gtk-2.0/Panel/panel-bg.png

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a "Iris Dark" $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}Dark
sed -i 's|Iris$|IrisDark|' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}Dark/index.theme
cp -a "Iris Light" $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}Light
sed -i '10i IconTheme=Faba' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}Dark/index.theme
sed -i '10i IconTheme=Faba-Mono' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}Light/index.theme
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}Dark
sed -i '$a BackgroundImage=/usr/share/themes/%{theme_name}Dark/matterhorn-984128_1280.jpg' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}Dark/index.theme
cp %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}Light
sed -i '$a BackgroundImage=/usr/share/themes/%{theme_name}Light/zune_by_hellishere_12-1920x1200.jpg' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}Light/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}*

%changelog
* Wed Mar 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2016
- Rebuild for Fedora
