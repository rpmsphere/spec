%global theme_name Color-UI

Name:           colorui-gnome-theme
Version:        1.5.1rc2.19
Release:        6.1
Summary:        The project behind the %{theme_name} theme
License:        GPL-3.0+
Group:          System/GUI/Other
URL:            https://github.com/MasicoreLord/%{theme_name}-theme-project
Source0:        https://github.com/MasicoreLord/%{theme_name}-theme-project/archive/1.5.1-RPF-2-Build-19.tar.gz#/%{theme_name}-theme-project-1.5.1-RPF-2-Build-19.tar.gz
Source1:        https://orig00.deviantart.net/8cef/f/2014/114/e/5/pen_tool_wallpaper_by_samuelfur-d7ftg5r.png
BuildArch:      noarch
Requires:       gtk-murrine-engine
Requires:	numix-icon-theme-circle

%description
Color UI was made with maximum usability in mind, from the window borders to
the color scheme, Color UI was made for the user who wants an elegant simple
theme that does not look broken. If any part of Color UI has any problems in
any of the things I listed as this theme supporting, please notify me and I
will try to fix it ASAP!

%prep
%setup -q -n %{theme_name}-theme-project-1.5.1-RPF-2-Build-19
cp %{SOURCE1} %{theme_name}

%build
sed -i 's|IconTheme=.*|IconTheme=Numix-Circle|' %{theme_name}/index.theme
sed -i '$a BackgroundImage=/usr/share/themes/%{theme_name}/pen_tool_wallpaper_by_samuelfur-d7ftg5r.png' %{theme_name}/index.theme
rm %{theme_name}/metacity-1/metacity-theme-1.xml %{theme_name}/metacity-1/metacity-theme-3.xml

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/themes
cp -a %{theme_name} %{buildroot}%{_datadir}/themes

%files
%doc LICENSE README.md
%{_datadir}/themes/%{theme_name}

%changelog
* Wed Aug 01 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.1rc2.19
- Rebuild for Fedora
