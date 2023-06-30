%define theme_name lxice

Name: lxice-icewm-theme
Version: 0.1.0
Release: 2.1
License: GPL
Group: User Interface/Desktops
Source: https://downloads.sourceforge.net/lxde/%{theme_name}.tar.bz2
URL: https://lxde.sourceforge.net/
Summary: A theme for IceWM for a lightweight X11 desktop
BuildArch: noarch
Requires: icewm

%description
This is a new theme for IceWM window manager. Its author is
PCMan (Hong Jen Yee), and some parts of it are inspired by 
OpenBox.

%prep
%setup -q -n %{theme_name}

%install
rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_datadir}/icewm/themes/%{theme_name}
%__cp -a * %{buildroot}%{_datadir}/icewm/themes/%{theme_name}

%clean
rm -rf %{buildroot}

%files
%{_datadir}/icewm/themes/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0
- Rebuilt for Fedora
