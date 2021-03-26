%define theme_name "No-Title 2"

Name:           notitle2-metacity-theme
Version:        20090904
Release:        2.1
Summary:        No-Title 2 metacity theme
Group:          User Interface/Desktops
License:        GPL
URL:            https://www.gnome-look.org/p/1006993/
Source0:        https://dl.opendesktop.org/api/files/download/id/1460749161/111447-No-Title-2.tar.bz2
BuildArch:      noarch

%description
Another No-Title theme.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a * $RPM_BUILD_ROOT%{_datadir}/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/*

%changelog
* Mon Sep 12 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20090904
- Rebuild for Fedora
