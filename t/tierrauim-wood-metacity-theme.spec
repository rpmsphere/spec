%define theme_name Tierra-UI-M-wood

Summary: %{theme_name} metacity theme
Name: tierrauim-wood-metacity-theme
Version: 20081119
Release: 4.1
License: GPL
Group: User Interface/Desktops
Source: https://dl.opendesktop.org/api/files/download/id/1460749479/93542-Tierra-UI-M-wood.tar.gz
URL: https://gnome-look.org/content/show.php/Tierra-UI+Metacity-wood?content=93542
BuildArch: noarch

%description
Alternate Metacity theme to fit my Tierra-UI GTK2 theme.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Fri Apr 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20081119
- Rebuilt for Fedora
