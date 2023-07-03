%define theme_name GTK2-notif2

Summary: %{theme_name} gtk theme
Name: notif2-gtk-theme
Version: 0.2
Release: 10.1
License: GPL
Group: User Interface/Desktops
Source0: %{theme_name}.tar.gz
Source1: https://www.custompc.plus.com/twm/walls/solaris.gif
URL: https://gnome-look.org/content/show.php?content=18886
BuildArch: noarch
Requires: solarcity-metacity-theme
Requires: oldgnome2-icon-theme

%description
%{theme_name} is a Motif-like theme for gtk.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -R * %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
chmod -x $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme
sed -i 's|gnome|OldGNOME2|' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme
sed -i '$a BackgroundImage=/usr/share/themes/%{theme_name}/solaris.gif' $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Thu Apr 21 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
