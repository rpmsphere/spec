%define theme_name Woody

Summary: %{theme_name} GNOME theme
Name: woody-gnome-theme
Version: 20091104
Release: 26.1
License: GPL
Group: User Interface/Desktops
Source0: https://www.deviantart.com/download/140869176/woody_by_nale12.zip
Source1: %{theme_name}-index.theme
Source2: motionwood3_by_neodesktop.jpg
URL: https://nale12.deviantart.com/art/Woody-140869176
BuildArch: noarch
Requires: britanzan-icon-theme

%description
Gtk,two metacity,xwvm4 and emerald themes included. Enjoy!

%prep
%setup -q -c
tar xf %{theme_name}.tar.gz
cp %{SOURCE1} %{theme_name}/index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name} $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}
cp -a %{theme_name}/gtk-2.0 %{theme_name}/metacity-1 %{theme_name}/xfwm4 %{theme_name}/index.theme $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
tar xf %{theme_name}.emerald -C $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%files
%{_datadir}/themes/%{theme_name}
%{_datadir}/emerald/themes/%{theme_name}

%changelog
* Fri Sep 23 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20091104
- Rebuilt for Fedora
