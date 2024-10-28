%define theme_name Lemnos-UI

Summary: %{theme_name} metacity theme
Name: lemnosui-metacity-theme
Version: 0.1
Release: 2.1
License: GPL
Group: User Interface/Desktops
Source: https://dl.opendesktop.org/api/files/download/id/1460749420/94532-Lemnos-UI-Metacity.tar.gz
URL: https://www.gnome-look.org/p/1007141/ 
BuildArch: noarch

%description
Wood background for this theme.
Based on Tierra-UI Metacity-wood theme.

%prep
%setup -q -n %{theme_name}-Metacity

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Wed Oct 05 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
