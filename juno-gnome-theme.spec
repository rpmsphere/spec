%define theme_name Juno

Summary: Juno GNOME theme
Name: juno-gnome-theme
Version: 0.0.0git
Release: 1
License: GPLv3.0
Group: User Interface/Desktops
Source: %{theme_name}-master.zip
BuildArch: noarch
URL: https://github.com/EliverLara/Juno
Recommends: zafiro-icon-theme

%description
GTK themes inspired by epic vscode themes.

%prep
%setup -q -n %{theme_name}-master
sed -i 's|Zafiro-icons|Zafiro|' index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -R assets cinnamon gnome-shell gtk-2.0 gtk-3.0 Gulpfile.js index.theme metacity-1 xfwm4 $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.md LICENSE
%{_datadir}/themes/%{theme_name}

%changelog
* Thu Oct 22 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.0git
- Rebuild for Fedora
