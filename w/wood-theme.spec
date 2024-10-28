%define theme_name Wood

Summary: %{theme_name} GTK and Icon theme
Name: wood-theme
Version: 1.6
Release: 3.1
License: free
Group: User Interface/Desktops
Source0: https://dl.dropboxusercontent.com/s/cveht2sx9b31k5o/WoodIcons.tar.gz
Source1: https://dl.dropboxusercontent.com/s/ktimb3jbo9zc9xo/WoodThemeSmooth.tar.gz
Source2: https://dl.dropboxusercontent.com/s/hwulukcjtq76060/WoodThemeRustic.tar.gz
Source3: https://dl.opendesktop.org/api/files/download/id/1460833420/106805-revitalized-wood-1280x800.jpg
Source4: %{theme_name}Smooth-index.theme
Source5: %{theme_name}Rustic-index.theme
URL: https://www.gnome-look.org/content/show.php/Wood+Theme?content=91601
BuildArch: noarch
Requires: oldbrownwood-icon-theme

%description
This theme has two flavours - Rustic and Smooth, also included is a set of
gnome desktop icons. Updated to now include Xfce4 window manager decorations.
By Keith Hedger at https://khapplications.darktech.org/pages/themes/wood.html

%prep
%setup -q -c -a 1 -a 2
cp %{SOURCE3} %{theme_name}Icons
cp %{SOURCE4} %{theme_name}ThemeSmooth/index.theme
cp %{SOURCE5} %{theme_name}ThemeRustic/index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes $RPM_BUILD_ROOT%{_datadir}/icons
cp -a %{theme_name}ThemeSmooth $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}Smooth
cp -a %{theme_name}ThemeRustic $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}Rustic
cp -a %{theme_name}Icons $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%files
%{_datadir}/themes/%{theme_name}*
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Jun 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6
- Rebuilt for Fedora
