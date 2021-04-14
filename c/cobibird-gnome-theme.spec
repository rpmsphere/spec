%define theme_name CobiBird

Summary: %{theme_name} GTK and Metacity theme
Name: cobibird-gnome-theme
Version: 1.6
Release: 2.1
License: GPL
Group: User Interface/Desktops
Source0: https://dl.opendesktop.org/api/files/download/id/1471871179/%{theme_name}.zip
BuildArch: noarch
URL: http://gnome-look.org/content/show.php/CobiBird?content=157985
Requires: rosa-icon-theme
Requires: dmz-cursor-themes
Requires: shimmer-backgrounds

%description
A Gtk theme based on Greybird, with dark menus as Greybird was until its
version 0.8.2.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a gtk-2.0 gtk-3.0 metacity-1 index.theme $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
sed -i 's|CursorTheme=DMZ-White|CursorTheme=dmz|' %{buildroot}%{_datadir}/themes/%{theme_name}/index.theme
sed -i 's|elementary-xfce-dark|Rosa|' %{buildroot}%{_datadir}/themes/%{theme_name}/index.theme
sed -i '$a BackgroundImage=/usr/share/backgrounds/shimmer/greybird-wall-1920x1200.png' %{buildroot}%{_datadir}/themes/%{theme_name}/index.theme
mkdir -p $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}
tar zxf %{theme_name}.emerald -C $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README LICENSE.*
%{_datadir}/themes/%{theme_name}
%{_datadir}/emerald/themes/%{theme_name}

%changelog
* Wed Oct 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6
- Rebuilt for Fedora
