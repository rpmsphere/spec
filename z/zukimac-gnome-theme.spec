%define theme_name Zukimac

Summary: %{theme_name} GTK and Metacity theme
Name: zukimac-gnome-theme
Version: 1.5
Release: 14.1
License: GPL
Group: User Interface/Desktops
Source0: 165450-zukimac-gtk-themes.7z
Source1: Sunrise_at_Pyramid_Lake.png
Source2: Mount_Fuji.jpg
URL: http://gnome-look.org/content/show.php/Zukimac?content=165450
BuildArch: noarch
BuildRequires: p7zip
Requires: gtk-murrine-engine
Requires: gtk2-engines
Requires: breathe-icon-theme

%description
This is a Mac-like theme that I made based on Zuki-themes.
With backgrounds by:
G. Donald Bain, http://360panos.com/Nevada/NorthAndCentralNevada/PyramidLake/
Sean MacDonald, http://sportsroadtrips.blogspot.tw/2012/04/hnd-cts-april-5-2012.html

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a %{theme_name}-3.14 $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a %{theme_name}-Com-3.14 $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}-Com
sed -i '$a IconTheme=Breathe' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}*/index.theme
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
sed -i '$a BackgroundImage=/usr/share/themes/%{theme_name}/Sunrise_at_Pyramid_Lake.png' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}-Com
sed -i '$a BackgroundImage=/usr/share/themes/%{theme_name}-Com/Mount_Fuji.jpg' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}-Com/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}*

%changelog
* Wed Mar 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuild for Fedora
