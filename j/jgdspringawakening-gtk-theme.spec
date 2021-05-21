%define theme_name JGD-SpringAwakening

Summary:        JGD Spring Awakening GTK theme
Name:           jgdspringawakening-gtk-theme
Version:        1.0
Release:        1
License:        GPL
Group:          User Interface/Desktops
URL:            https://www.gnome-look.org/p/1015172/
Source0:        https://dl.opendesktop.org/api/files/download/id/1460764340/170371-JGD-SpringAwakening-01ObGtk2.tar.gz
Source1:        %{theme_name}-index.theme
BuildArch:      noarch
Requires:       fitts-natural-metacity-theme
Requires:       gartoonredux-icon-theme

%description
The JGD-Spring Awakening GTK+ 2 theme to go with its Openbox theme, which is
included in this package. It requires the Murrine theme engine.

%prep
%setup -q -n %{theme_name}
cp %{SOURCE1} index.theme

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
* Mon Sep 26 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
