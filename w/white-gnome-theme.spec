%define theme_name White

Summary: %{theme_name} GTK and Metacity theme
Name: white-gnome-theme
Version: 3.18.feb16
Release: 6.1
License: GPL
Group: User Interface/Desktops
Source0: 173840-White-Feb2016.tar.gz
URL: https://gnome-look.org/content/show.php/White?content=173840
BuildArch: noarch
Requires: numix-icon-theme-circle
Requires: win9-backgrounds

%description
White theme is a simple theme built to mimic OS x Yosemite and El Capitan
clean interface.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
echo IconTheme=Numix-Circle >> $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme
echo BackgroundImage=/usr/share/backgrounds/win9/flower.png >> $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme
chmod -x $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Wed Mar 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.18.feb16
- Rebuilt for Fedora
