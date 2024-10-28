%define theme_name FearAndMystery

Summary: %{theme_name} GTK and Icon theme
Name: fearandmystery-theme
Version: 20120331
Release: 7.1
License: free
Group: User Interface/Desktops
Source0: https://dl.dropboxusercontent.com/s/on99twphw2cc1kr/FearAndMystery.tar.gz
Source1: https://dl.dropboxusercontent.com/s/15qujrvgavmytwv/FearAndMysteryIcons.tar.gz
Source2: https://khapplications.darktech.org/pics/background4.jpg
Source3: %{theme_name}-index.theme
URL: https://khapplications.darktech.org/pages/themes/fear.html
BuildArch: noarch

%description
This theme and icon set is based on the fear theme for OSX and the murder mystery
icon set. Thanks to Joe Loy at https://www.fearutopia.com for permmision to use
and release this theme, the original icons were designed by Zachary Lutterman but
his web site is no longer around but a big thanks to him as well.

%prep
%setup -q -c -a 1
cp %{SOURCE2} %{theme_name}
cp %{SOURCE3} %{theme_name}/index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes $RPM_BUILD_ROOT%{_datadir}/icons
cp -a %{theme_name} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a %{theme_name}Icons $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%files
%{_datadir}/themes/%{theme_name}
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Jun 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20120331
- Rebuilt for Fedora
