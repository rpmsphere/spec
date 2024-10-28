%define theme_name OneStepBack

Summary:        One Step Back GTK theme
Name:           onestepback-gtk-theme
Version:        0.91
Release:        5.1
License:        GPLv3
Group:          User Interface/Desktops
URL:            https://www.gnome-look.org/p/1013663/
Source0:        https://dl.opendesktop.org/api/files/download/id/1472928821/1472928821-OneStepBack.zip
Source1:        next_wallpaper.jpg
BuildArch:              noarch
Requires:       baku-icon-theme
Requires:       albatross-metacity-theme
Requires:       openzone-cursor-theme

%description
OneStepBack is a Gtk 2 and 3 theme with some colors and embossed widgets
inspired by the good old NextStep look. I'm old. It is developed from scratch,
is light and minimal, uses only three shades of grays and one color.
That was the challenge.

%prep
%setup -q -n %{theme_name}

%build
echo IconTheme=Baku >> index.theme
echo MetacityTheme=Albatross >> index.theme
echo BackgroundImage=/usr/share/themes/%{theme_name}/next_wallpaper.jpg >> index.theme
echo CursorTheme=OpenZone_White_Slim >> index.theme

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a gtk-2.0 gtk-3.0 img index.theme %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%files
%doc README LICENSE
%{_datadir}/themes/%{theme_name}

%changelog
* Thu Sep 29 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.91
- Rebuilt for Fedora
