%define theme_name DAnup

Summary: %{theme_name} GNOME theme
Name: danup-gnome-theme
Version: 1.0
#Version: 2
Release: 14.1
License: GPL
Group: User Interface/Desktops
Source0: wood-theme_1.0.tar.gz
Source1: %{theme_name}-index.theme
Source2: http://cdn.wallpapersafari.com/3/91/sTmXdb.jpg
URL: https://www.gnome-look.org/content/show.php?content=153114
BuildArch: noarch
Requires: wood-theme

%description
Another GTK3 Wood Theme by paudelanup.
Credits: All GTK2 Wood Themes, Swar-blue Theme.

%prep
%setup -q -n theme/wood-theme
cp %{SOURCE1} index.theme
cp %{SOURCE2} .
rm .icon-theme.cache

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
* Fri Sep 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
