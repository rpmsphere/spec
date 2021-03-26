%define theme_name area.o43

Summary: %{theme_name} icon theme
Name: areao43-icon-theme
Version: 20090401
Release: 3.1
License: GPL2+
Group: User Interface/Desktops
Source: https://dl.opendesktop.org/api/files/download/id/1460759243/101979-areao43.tar.bz2
URL: https://www.gnome-look.org/content/show.php/area.o43+SVG+Icon+theme?content=101979
BuildArch: noarch

%description
This is an icon set meant to be used with dark themes.
It's based on servechilled's area.o42 icons (I found them awesome).

%prep
%setup -q -n areao43

%build

%install
install -d $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a index.theme scalable $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Mon Jul 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20090401
- Rebuild for Fedora
