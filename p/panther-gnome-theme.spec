%define theme_name Panther

Summary: Panther for GNOME environment
Name: panther-gnome-theme
Version: 20090311
Release: 6.1
License: GPL
Group: User Interface/Desktops
Source0: https://dl.opendesktop.org/api/files/download/id/1460762503/100808-Panther.tar.gz
Source1: http://www.crossfitpanthercity.com/wp-content/uploads/2013/12/black-panther-animal-hd-wallpaper-1920x1200-5511.jpg
BuildArch: noarch
URL: https://www.gnome-look.org/p/1014213/
Requires: appleart-icon-theme
Requires: aquanukex-cursor-theme

%description
Mac osx Panther include metacity already in use.

%prep
%setup -q -n %{theme_name}
sed -i 's|Lero_0.3|AppleArt|' index.theme
sed -i '$a CursorTheme=Aqua-NukeX' index.theme
sed -i '$a BackgroundImage=/usr/share/themes/%{theme_name}/black-panther-animal-hd-wallpaper-1920x1200-5511.jpg' index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a metacity-1 gtk-2.0 index.theme %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Thu Oct 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20090311
- Rebuilt for Fedora
