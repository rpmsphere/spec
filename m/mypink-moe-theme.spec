%define theme_name MyGTKPink2-moe
%define icon_name MyIpink-moe
%define gdm_name moegdm

Summary: MyPink theme for moebuntu
Name: mypink-moe-theme
Version: 3.0
Release: 11.1
License: Artistic 2.0
Group: User Interface/Desktops
Source0: %{theme_name}.tar.gz
Source1: %{icon_name}.tar.gz
Source2: %{gdm_name}.tar.gz
Source3: mypink-moe-index.theme
BuildArch: noarch
Requires: comixcursors-cursor-theme
URL: https://gnome-look.org/content/show.php/mypink-moebuntu?content=106584

%description
Mypink special edition, edited by moebuntu.

%prep
%setup -q -a 1 -a 2 -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a %{theme_name}/gtk-2.0 %{theme_name}/metacity-1 $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{icon_name}
cp -a %{icon_name}/index.theme %{icon_name}/128x128 $RPM_BUILD_ROOT%{_datadir}/icons/%{icon_name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gdm/%{gdm_name}
cp -a %{gdm_name}/* $RPM_BUILD_ROOT%{_datadir}/gdm/%{gdm_name}
cd %{theme_name}/pink
cp %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme
cp princesa-1ping.jpg $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/background.jpg

%files
%{_datadir}/themes/%{theme_name}
%{_datadir}/icons/%{icon_name}
%{_datadir}/gdm/%{gdm_name}

%changelog
* Tue Feb 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0
- Rebuilt for Fedora
