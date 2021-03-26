%define theme_name RaveH20-Classic

Summary: %{theme_name} icon theme
Name: raveh20-classic-icon-theme
Version: 4
Release: 3.1
License: GPL/LGPL
Group: User Interface/Desktops
URL: http://gnome-look.org/content/show.php?content=119776
Source: RaveH20-4-Classic-GTK-IconTheme.tar.gz
BuildArch: noarch

%description
The RaveH20 4 Theme Aims to be an Original (As in Originality and Uniqueness)
Shiny and beautiful Theme. RaveH20 4 doesn't try to mimic,copy or by any means
ripoff other Themes or Operating System GUIs. It only tries to be a unique
beautiful first class version of it's self. Its also aims to a 100% Free and
Legal Icon Theme For Linux,BSD and any other OpenSource desktops, useing GTK,
Gnome , XFCE , LXDE or other desktops, It does its best to not use Icons Taken
from unauthorized sources, RaveH20 4 Only trys to include Icons Licensed Under
the GPL/LGPL (v.2) Created by Us or others!

%prep
%setup -q -n RaveH20-4-Classic

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 4
- Rebuild for Fedora
