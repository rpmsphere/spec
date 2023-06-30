%define theme_name Antique

Summary: %{theme_name} GTK and Icon theme
Name: antique-theme
Version: 20100906
Release: 7.1
License: GPL
Group: User Interface/Desktops
Source0: https://www.deviantart.com/download/178319784/antique_theme_by_andrewtheshort-d2y60fc.zip
Source1: %{theme_name}-index.theme
URL: https://www.gnome-look.org/p/1079047/
BuildArch: noarch
Requires: steampunk-cursor-theme

%description
This GTK theme is not my work at all! Credit goes to: Uknown author Sebco,
who created the Woodbuntech theme (gtk, emerald, woodbuntu icons),
I only changed the color of the text to make it readable!
As I said, the theme contains emerald theme, I highly reccomend to use it,
it looks pretty good (check the screens).
Gnome-look.org user migedith - I´ve used his window border \"Slickness brown\"
(only changed a window title color a little).

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
tar xf Gtk/%{theme_name}.tar.gz -C $RPM_BUILD_ROOT%{_datadir}/themes
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
tar xf Icons/Woodbuntu.tar.gz -C $RPM_BUILD_ROOT%{_datadir}/icons
rm $RPM_BUILD_ROOT%{_datadir}/icons/Woodbuntu/icon-theme.cache
mkdir -p $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}
tar xf emerald/Classtech.emerald -C $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc *.png *.txt
%{_datadir}/themes/%{theme_name}
%{_datadir}/icons/Woodbuntu
%{_datadir}/emerald/themes/%{theme_name}

%changelog
* Tue Oct 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20100906
- Rebuilt for Fedora
