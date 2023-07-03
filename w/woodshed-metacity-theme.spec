%define theme_name WoodShed

Summary: %{theme_name} metacity theme
Name: woodshed-metacity-theme
Version: 20160317
Release: 6.1
License: CC by
Group: User Interface/Desktops
Source: Wood Shed.tar.gz
URL: https://gnome-look.org/content/show.php/Wood+Shed?content=175520
BuildArch: noarch

%description
Simulated wood-grain Cinnamon & Metacity themes for those who like
skeuomorphic design.

%prep
%setup -q -n "Wood Shed"
sed -i 's|"left_titlebar_edge" value="10"|"left_titlebar_edge" value="0"|' metacity-1/metacity-theme-1.xml
sed -i 's|"right_titlebar_edge" value="10"|"right_titlebar_edge" value="14"|' metacity-1/metacity-theme-1.xml

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -R * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Wed Mar 23 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20160317
- Rebuilt for Fedora
