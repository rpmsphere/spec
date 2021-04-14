%define theme_name Windows7-Aero

Summary: %{theme_name} GTK and Metacity theme
Name: windows7aero-gnome-theme
Version: 2.0
Release: 4.1
License: GPL
Group: User Interface/Desktops
Source0: 162581-%{theme_name}.zip
URL: http://gnome-look.org/content/show.php/Windows7-Aero+%28Cinnamon%2B+GTK3%2B2%29?content=162581
BuildArch: noarch
Requires: win2-7-theme

%description
Theme by Brahim Salem inspired by Win2-7.

%prep
%setup -q -n %{theme_name}
sed -i 's|Win2-7|Win2-7Libre|' index.theme
sed -i '14,$d' index.theme
sed -i '$a BackgroundImage=/usr/share/backgrounds/Win2-7/Win2-7.jpg' index.theme

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
* Wed Mar 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
