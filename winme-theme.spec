%define theme_name WinMe

Summary: %{theme_name} GTK and Metacity theme
Name: winme-theme
Version: 3.11
Release: 11.1
License: GPL
Group: User Interface/Desktops
Source0: http://matsusoft.com.ar/uploads/perberos/%{theme_name}.tar.gz
Source1: windows_me.jpg
BuildArch: noarch
URL: http://gnome-look.org/content/show.php/WinMe?content=123613
Requires: gtk-murrine-engine
Requires: classic95-icon-theme

%description
This metacity is a fork of W2k metacity. Based on the classic style of the NT serie.
The GTK Theme requires murrine engine and redmond95 engine.
Wallpaper modified from http://www.deviantart.com/art/Windows-ME-361282419

%prep
%setup -q -n %{theme_name}
sed -i 's|IconTheme=gnome|IconTheme=Classic95|' index.theme
sed -i '$a BackgroundImage=/usr/share/themes/WinMe/windows_me.jpg' index.theme
sed -i '/Font/d' index.theme
sed -i '/notification-area/d' gtk-2.0/gtkrc

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Wed Jun 01 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 3.11
- Rebuild for Fedora
