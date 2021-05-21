%define theme_name WoodExtra

Summary:        A Minimal Wooden Icon Set for GNOME and KDE
Name:           woodextra-icon-theme
Version:        0.0.3
Release:        1.1
License:        GPL
Group:          User Interface/Desktops
URL:            http://gnome-look.org/content/show.php/Wood+Icon+Theme?content=160199
Source0:        wood-icon-extra_0.0.3_all.deb
BuildArch:      noarch

%description
Credits goes to following icon packages:
wooden_icons_by_pakito77-d314t3z
apple-inc-themed-wooden-graphics-set
Made_Of_Wood_by_Thvg
Wood_icons_by_teroleg
WoodIcons by Fredbird (xfce icon theme)
glossy-waxed-wood-icon (icons.mysitemyway.com)
Gopher-Wood-png
Woodbuntu by Sebco
OldBrownWoodIcons by K.D.Hedger.

%prep
%setup -T -c
ar -x %{SOURCE0}

%build

%install
mkdir -p %{buildroot}
tar xf data.tar.gz -C %{buildroot}
rmdir %{buildroot}%{_datadir}/icons/Wood
mv %{buildroot}%{_datadir}/icons/Wood* %{buildroot}%{_datadir}/icons/%{theme_name}
mv %{buildroot}%{_datadir}/doc/wood-icon-extra %{buildroot}%{_datadir}/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/icons/%{theme_name}
%{_datadir}/doc/%{name}

%changelog
* Fri Apr 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.3
- Rebuilt for Fedora
