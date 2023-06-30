%define theme_name Brushed

Summary: %{theme_name} GTK2 & GTK3 & Metacity theme
Name: brushed-gnome-theme
Version: 2011
Release: 18.1
License: GPL3
Group: User Interface/Desktops
Source0: https://orig13.deviantart.net/e16d/f/2011/345/5/4/brushed___gtk3_by_rvc_2011-d4iocrp.zip
Source1: %{theme_name}-index.theme
Source2: RealSteel.jpg
URL: https://rvc-2011.deviantart.com/art/Brushed-GTK3-273234085
BuildArch: noarch
Requires: nouvegnome-icon-theme
Requires: modblackmoon-steelking-cursor-theme

%description
Theme created with an intention to have a matching gtk / metacity for brushed
metal gnome shell theme. This theme is a mod and re-mix of 2 different themes.
Full credit to the original authors:
a) Metacity is a mod from SLAVE-gtk3 by half-left
https://half-left.deviantart.com/art/SLAVE-GTK3-256366787
b) gtk3 is a mod from Luminiare created by sauravzone1
https://gnome-look.org/content/show.php/Luminaire?content=146615
Wallpaper "Real Steel" by ilnanny.

%prep
%setup -q -n %{theme_name}-GTK3
cp %{SOURCE1} index.theme
cp %{SOURCE2} .

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
* Wed Jun 15 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2011
- Rebuilt for Fedora
