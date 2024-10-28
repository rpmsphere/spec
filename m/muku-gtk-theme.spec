%define theme_name Muku

Summary: %{theme_name} GNOME theme
Name: muku-gtk-theme
Version: 1.2
Release: 17.1
License: freeware
Group: User Interface/Desktops
Source0: https://www.deviantart.com/download/56137684/muku_gtk_by_thrynk.zip
Source1: %{theme_name}-index.theme
Source2: https://alxboss.free.fr/wallpapers/background-japan1.jpg
URL: https://thrynk.deviantart.com/art/Muku-GTK-56137684
BuildArch: noarch
Requires: mintx-icon-theme
Requires: lemnosui-metacity-theme

%description
This is a port of Mac OS X theme, Muku v1.2 by Daisuke Yamashita.
Special thanks for his permission. Emerald theme is included.
Known problem: a minor glitch with a progressbar. Probably just a GTK2 problem.
Finally, thanks to beckyhorse30 for suggesting a Muku theme which inspired me to make it.

%prep
%setup -q -n %{theme_name}
tar xf %{theme_name}-gtk.tar.gz
cp %{SOURCE1} %{theme_name}/index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}
cp -a %{theme_name} $RPM_BUILD_ROOT%{_datadir}/themes
tar xf %{theme_name}.emerald -C $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%files
%{_datadir}/themes/%{theme_name}
%{_datadir}/emerald/themes/%{theme_name}

%changelog
* Fri Sep 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
