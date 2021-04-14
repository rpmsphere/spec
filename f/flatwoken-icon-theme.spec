%global theme_name FlatWoken

Name:		flatwoken-icon-theme
Version:	20160321
Release:	1.1
Summary:	%{theme_name} icon theme
Group:		System/GUI/GNOME
License:	CC by SA
URL:		https://github.com/alecive/FlatWoken
Source0:	%{theme_name}-master.zip
BuildArch:  noarch

%description
This package contains the %{theme_name} icon theme.

%prep
%setup -q -n %{theme_name}-master
sed -i 's|Example=logo|Example=folder|' %{theme_name}/index.theme
sed -i 's|Example=google-maps|Example=folder|' %{theme_name}Min/index.theme

%build

%install
install -d %{buildroot}%{_datadir}/icons
cp -a %{theme_name} %{theme_name}Min %{buildroot}%{_datadir}/icons

%files
%doc LICENSE README.md
%{_datadir}/icons/%{theme_name}*

%changelog
* Thu Sep 29 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20160321
- Rebuilt for Fedora
