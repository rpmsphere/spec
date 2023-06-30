%define theme_name Haiku

Summary: Haiku for GNOME environment
Name: haiku-gnome-theme
Version: 20110105
Release: 9.1
License: free
Group: User Interface/Desktops
Source0: https://dl.opendesktop.org/api/files/download/id/1460967677/106952-Haiku-5-1-11.tar.bz2
Source1: https://dl.opendesktop.org/api/files/download/id/1460735079/116169-HaikuHand-0.5.tar.bz2
Source2: https://dl.opendesktop.org/api/files/download/id/1460759082/114723-Haiku-0.7.tar.bz2
Source3: https://www.deviantart.com/download/137622183/haiku_os_wallpaper_by_cagwait.jpg
Source4: %{theme_name}-index.theme
BuildArch: noarch
URL: https://www.gnome-look.org/content/show.php/Haiku?content=106952

%description
Theme based on Haiku os gui:
-- GTK THEME --
https://www.gnome-look.org/content/show.php/Haiku?content=106952
-- CURSOR --
https://www.gnome-look.org/content/show.php/HaikuHand?content=116169 
-- ICON THEME --
https://www.gnome-look.org/content/show.php?content=114723
-- BACKGROUND --
https://cagwait.deviantart.com/art/Haiku-Os-wallpaper-137622183

%prep
%setup -q -c
cp %{SOURCE3} %{theme_name}
cp %{SOURCE4} %{theme_name}/index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
cp -a %{theme_name} $RPM_BUILD_ROOT%{_datadir}/themes
tar xf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/icons
tar xf %{SOURCE2} -C $RPM_BUILD_ROOT%{_datadir}/icons
rm $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}/index.theme~

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}
%{_datadir}/icons/%{theme_name}*

%changelog
* Thu Aug 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20110105
- Rebuilt for Fedora
