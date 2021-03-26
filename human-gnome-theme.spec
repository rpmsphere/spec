%global _name human-theme

Name: human-gnome-theme
License: GPL
Group: User Interface/Desktops
Summary: Ubuntu Human theme
Version: 0.39.2
Release: 12.1
Source0: https://launchpad.net/ubuntu/+archive/primary/+files/%{_name}_%{version}.tar.gz
Source1: HumanLogin-index.theme
URL: https://launchpad.net/human-theme
BuildRequires: intltool, python, python-setuptools, python-distutils-extra
BuildArch: noarch
Requires: humanity-icon-theme
Requires: gtk-ubuntulooks-engine
Requires: ubuntu-backgrounds

%description
The default Human theme. At the moment the package contains
  - the theme definitions
  - metacity theme elements.
It pulls in the Cursor theme, the GTK+ theme and the Icon theme which gives
the Human look.

%prep
%setup -q -n %{_name}-%{version}

%build
python setup.py build

%install
%__rm -rf %{buildroot}
python setup.py install --root=%{buildroot}
sed -i '$a BackgroundImage=/usr/share/backgrounds/ubuntu/contest/maverick.xml' %{buildroot}%{_datadir}/themes/DarkRoom/index.theme
sed -i '$a BackgroundImage=/usr/share/backgrounds/ubuntu/contest/oneiric.xml' %{buildroot}%{_datadir}/themes/Human/index.theme
sed -i '$a BackgroundImage=/usr/share/backgrounds/ubuntu/contest/lucid.xml' %{buildroot}%{_datadir}/themes/Human-Clearlooks/index.theme
install -m644 %{SOURCE1} %{buildroot}%{_datadir}/themes/HumanLogin/index.theme
mv %{buildroot}%{_datadir}/icons/HumanLoginIcons/apps/64/computer.png %{buildroot}%{_datadir}/icons/HumanLoginIcons/apps/64/ubuntu.png

%clean
%__rm -rf %{buildroot}

%files
%doc ChangeLog COPYING AUTHORS
%{python_sitelib}/*
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/icons/*
%{_datadir}/themes/*

%changelog
* Tue Sep 06 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.39.2
- Rebuild for Fedora
