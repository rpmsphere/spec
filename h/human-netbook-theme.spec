Name: human-netbook-theme
License: GPL
Group: User Interface/Desktops
Summary: Human with panel themeing
Version: 0.15
Release: 12.1
Source: https://launchpadlibrarian.net/23003154/%{name}-%{version}.tar.gz
URL: https://launchpad.net/netbook-remix
BuildArch: noarch
BuildRequires: python, python-setuptools, python-distutils-extra, intltool
Requires: human-gnome-theme

%description
This is the Human theme used as the default Ubuntu Remix theme.

%prep
%setup -q

%build
python setup.py build

%install
%__rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/locale
cp -a build/mo/* %{buildroot}%{_datadir}/locale
sed -i 's|IconTheme=Human|IconTheme=Humanity|' build/share/themes/Human-Murrine-Netbook/index.theme
install -m644 -D build/share/themes/Human-Murrine-Netbook/index.theme %{buildroot}%{_datadir}/themes/Human-Murrine-Netbook/index.theme
sed -i '$a BackgroundImage=/usr/share/backgrounds/ubuntu/contest/natty.xml' %{buildroot}%{_datadir}/themes/Human-Murrine-Netbook/index.theme
cp -a Human-Murrine-Netbook %{buildroot}%{_datadir}/themes

%clean
%__rm -rf %{buildroot}

%files
%doc ChangeLog COPYING AUTHORS
%{_datadir}/locale/*/LC_MESSAGES/human-netbook-theme.mo
%{_datadir}/themes/Human-Murrine-Netbook

%changelog
* Tue Sep 06 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.15
- Rebuilt for Fedora
