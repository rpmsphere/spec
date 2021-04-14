%define theme_name XPRoyale

Summary: XPRoyale gnome theme
Name: xproyale-gnome-theme
Version: 2.0
Release: 6.1
License: GPL
URL: https://www.gnome-look.org/p/1014658/
Group: User Interface/Desktops
Source0: %{theme_name}.tar.gz
Source1: xp_bliss.jpg
BuildArch: noarch
Requires: gnomexp-icon-theme
Requires: xp-cursor-theme

%description
This is my first theme made from original Microsoft's theme "Luna" for WinXP.
The Metacity theme is Lunacity Blue.
I recommend GnomeXP icon theme for this GTK&Metacity theme.

%prep
%setup -q -n %{theme_name}
cp %{SOURCE1} Bliss_XP.jpg
sed -i '$a CursorTheme=XP' index.theme

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/themes/%{theme_name}
cp -a * %{buildroot}%{_datadir}/themes/%{theme_name}

%clean
rm -rf %{buildroot}

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
