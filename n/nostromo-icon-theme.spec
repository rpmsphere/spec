%define theme_name Nostromo

Summary: %{theme_name} icon theme
Name: nostromo-icon-theme
Version: 1.03
Release: 5.1
License: GPL
Group: User Interface/Desktops
URL: http://gnome-look.org/content/show.php/?content=101422
Source: http://voyager.legtux.org/icones/%{theme_name}-%{version}.tar.gz
BuildArch: noarch

%description
Nostramo icons from gnome-look, made by rodofr.

%prep
%setup -q -n %{theme_name}-%{version}
sed -i '8i Example=folder' index.theme
rm index.theme~

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}*

%changelog
* Thu May 19 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.03
- Rebuilt for Fedora
