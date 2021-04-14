%define theme_name Overglossed

Name:           overglossed-gnome-theme
Version:        0.4
Release:        3.1
Summary:        Overglossed GTK 2.x Theme/Style
Group:          User Interface/Desktops
License:        GPL
URL:            http://www.gnome-look.org/p/1080229/
Source0:        74813-Overglossed.tar.gz
BuildArch:      noarch
Requires:       blackwhite2-icon-theme

%description
This theme is the default in Ubuntu Ultimate 1.8 ,info and download:
http://ultimateedition.info/Ultimate_Edition_1.8/
package contains gtk and metacity themes (controls and window borders).

%prep
%setup -q -n %{theme_name}
sed -i 's|black-white_2-Style|black-white-2|' index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/themes/%{theme_name}
cp -a * %{buildroot}%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
