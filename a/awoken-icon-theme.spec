%global theme_name AwOken

Name:		awoken-icon-theme
Version:	2.5
Release:	4.1
Summary:	%{theme_name} icon theme
Group:		System/GUI/GNOME
License:	CC by SA
URL:		http://alecive.deviantart.com/art/AwOken-163570862
Source0:	%{theme_name}-%{version}.zip
BuildArch:  noarch

%description
This package contains the %{theme_name} icon theme.

%prep
%setup -q -n %{theme_name}-%{version}
tar xf %{theme_name}.tar.gz
tar xf %{theme_name}Dark.tar.gz
tar xf %{theme_name}White.tar.gz

%build

%install
install -d %{buildroot}%{_datadir}/icons
cp -a %{theme_name} %{theme_name}Dark %{theme_name}White %{buildroot}%{_datadir}/icons
sed -i 's|Example=python|Example=folder|' %{buildroot}%{_datadir}/icons/%{theme_name}*/index.theme

%files
%{_datadir}/icons/%{theme_name}*

%changelog
* Tue Mar 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5
- Rebuilt for Fedora
