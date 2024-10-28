%define theme_name SGI

Summary: SGI for GNOME desktop
Name: sgi-theme
Version: 2023
Release: 1
License: open source
Group: User Interface/Desktops
Source0: https://gnome-look.org/CONTENT/content-files/150069-Iris.tar.gz
Source1: https://gnome-look.org/CONTENT/content-files/174207-sgi.tar.bz2
Source2: https://gnome-look.org/CONTENT/content-files/97906-SGI-IMD.tar.gz
Source3: sgi.png
Source4: Iris.tar.bz2
Source5: 49014-sgi.tar.gz
BuildArch: noarch

%description
With following IRIX 4DWM desktop components:
Iris 0.5 icon theme https://gnome-look.org/content/show.php/Iris++%28fixed%29?content=150069
sgi 1.1 cursor theme https://gnome-look.org/content/show.php/SGI+Irix+cursor?content=174207
SGI-IMD 0.5 gtk theme https://gnome-look.org/content/show.php/SGI-IMD?content=97906
Iris 1.0 metacity theme https://art.gnome.org
SGI xfwm4 theme

%prep

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes $RPM_BUILD_ROOT%{_datadir}/icons
tar xf %{SOURCE0} -C $RPM_BUILD_ROOT%{_datadir}/icons
tar xf %{SOURCE1} -C $RPM_BUILD_ROOT%{_datadir}/icons
tar xf %{SOURCE2} -C $RPM_BUILD_ROOT%{_datadir}/themes
cp %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/icons/sgi
tar xf %{SOURCE4} -C $RPM_BUILD_ROOT%{_datadir}/themes
tar xf %{SOURCE5} -C $RPM_BUILD_ROOT%{_datadir}/themes
sed -i 's|CursorTheme=default|CursorTheme=sgi|' $RPM_BUILD_ROOT%{_datadir}/themes/SGI-IMD/index.theme
sed -i '11i BackgroundImage=/usr/share/icons/sgi/sgi.png' $RPM_BUILD_ROOT%{_datadir}/themes/SGI-IMD/index.theme
sed -i 's|MetacityTheme=SGI-IMD|MetacityTheme=Iris|' $RPM_BUILD_ROOT%{_datadir}/themes/SGI-IMD/index.theme

%files
%{_datadir}/themes/*
%{_datadir}/icons/*

%changelog
* Sun May 21 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2023
- Rebuilt for Fedora
