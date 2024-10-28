%define theme_name Wood

Summary: %{theme_name} Metacity theme
Name: wood-metacity-theme
Version: 0.1
Release: 4.1
License: GPL
Group: User Interface/Desktops
Source0: https://www.deviantart.com/download/212672302/wooden_desktop_by_ekylypse-d3imazy.zip
Source2: https://content.wallpapers-room.com/resolutions/1024x768/T/Wallpapers-room_com___The_Wood_Experiment_by_Delta909_1024x768.jpg
URL: https://ekylypse.deviantart.com/art/Wooden-Desktop-212672302
BuildArch: noarch

%description
Wood Metacity. WIP, serious.

%prep
%setup -q -c
tar xf %{theme_name}.tar.gz

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name} $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}
cp -a %{theme_name}/metacity-1 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Fri Sep 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
