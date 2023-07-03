%define theme_name oRainge

Summary: oRainge GNOME theme
Name: orainge-gnome-theme
Version: 0.alpha
Release: 15.1
License: GPLv2+
Group: User Interface/Desktops
Source0: %{theme_name}.tar.gz
Source1: %{theme_name}-index.theme
Source2: %{theme_name}-background.png
URL: https://mein-neues-blog.de/2008/01/03/orainge-gnome-theme-alpha-version/
BuildArch: noarch
Requires: polar-cursor-theme

%description
A flat and stylish Theme.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a gtk-2.0 metacity-1 $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/background.png
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a index.theme scalable $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}
%{_datadir}/icons/%{theme_name}

%changelog
* Fri Apr 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.alpha
- Rebuilt for Fedora
