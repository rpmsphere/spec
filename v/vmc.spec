%undefine _debugsource_packages
%define realname vodafone-mobile-connect-card-driver-for-linux

Name: vmc
License: GPL
Group: Applications/Internet
Summary: Vodafone 3G devices Internet connection assistant
Version: 2.0.beta3
Release: 1
Source: vodafone-mobile-connect-card-driver-for-linux-2.0.beta3.tar.gz
URL: https://forge.vodafonebetavine.net/projects/vodafonemobilec/
BuildRequires: python-devel, python-setuptools, libusb-devel
BuildArch: noarch
Requires: lsb, wvdial
Requires: gnome-python2, pygtk2-libglade, pyserial, notify-python
Requires: python-twisted-core, dbus-python, gnome-python2-extras, pytz, pyxdg

%description
Vodafone Mobile Connect Card driver for Linux is a GPRS/UMTS/HSDPA
device manager written in Python, licensed under the GPL. Features:
Data call handling Send/Receive SMS SIM phone book management
Graphical user interface using GTK.

%prep
%setup -q -n %{realname}-%{version}

%build
python2 setup.py build

%install
%__rm -rf %{buildroot}
python2 setup.py install --root %{buildroot}
echo -e "Name[zh_TW]=VMC 驅動器\nComment[zh_TW]=Vodafone 行動連線卡驅動程式" >> %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%__rm -rf %{buildroot}

%files
%doc README LICENSE*
%{_bindir}/*
%{_datadir}/%{realname}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*.png
%{python2_sitelib}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.beta3
- Rebuilt for Fedora
