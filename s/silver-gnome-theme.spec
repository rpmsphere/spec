%define theme_name Silver

Summary: %{theme_name} GTK & Metacity theme
Name: silver-gnome-theme
Version: 20160510
Release: 16.1
License: free
Group: User Interface/Desktops
Source0: https://www.dropbox.com/s/h55hjv1a1cgnvva/Silver.tar.gz
Source1: %{theme_name}-index.theme
URL: https://gentoo-art.org/content/show.php/Silver?content=168800
BuildArch: noarch
Requires: gtk-ubuntulooks-engine
Requires: nouvegnome-icon-theme
#Requires: xirod-fonts

%description
GTK 2.0/3.0, Cinnamon, Metacity theme.

%prep
%setup -q -c
cp %{SOURCE1} index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a cinnamon gtk-2.0 gtk-3.0 metacity-1 index.theme $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp "Silver Wallpapers/Cubic texture.png" $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/CubicTexture.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
cp -a "Black Diamonds" $RPM_BUILD_ROOT%{_datadir}/icons

%files
%doc README
%{_datadir}/themes/%{theme_name}
%{_datadir}/icons/*

%changelog
* Mon Jun 20 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20160510
- Rebuilt for Fedora
