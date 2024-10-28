Name:           ubuntu-backgrounds
Version:        0.35.1
Release:        7.1
Summary:        The default Wallpapers for Ubuntu
Group:          User Interface/Desktops
License:        CC SA 2.5
URL:            https://launchpad.net/ubuntu-wallpapers/
Source0:        https://launchpadlibrarian.net/114804769/ubuntu-wallpapers_%{version}.tar.gz
BuildRequires:  python2, intltool, python2-distutils-extra
BuildArch:      noarch

%description
ubuntu-wallpapers-karmic: Ubuntu 9.10 Wallpapers
ubuntu-wallpapers-lucid: Ubuntu 10.04 Wallpapers
ubuntu-wallpapers-maverick: Ubuntu 10.10 Wallpapers
ubuntu-wallpapers-natty: Ubuntu 11.04 Wallpapers
ubuntu-wallpapers-oneiric: Ubuntu 11.10 Wallpapers
ubuntu-wallpapers-precise: Ubuntu 12.04 Wallpapers
ubuntu-wallpapers-quantal: Ubuntu 12.10 Wallpapers

%prep
%setup -q -n ubuntu-wallpapers-%{version}

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --root $RPM_BUILD_ROOT --prefix /usr

rm $RPM_BUILD_ROOT%{_datadir}/backgrounds/warty-final-ubuntu.png
rm $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/ubuntu-wallpapers.xml
rm $RPM_BUILD_ROOT/usr/lib/python2.?/site-packages/ubuntu_wallpapers-%{version}-py2.?.egg-info
mkdir $RPM_BUILD_ROOT%{_datadir}/backgrounds/ubuntu
sed -i 's|share/backgrounds|share/backgrounds/ubuntu|' $RPM_BUILD_ROOT%{_datadir}/backgrounds/contest/*.xml
mv $RPM_BUILD_ROOT%{_datadir}/backgrounds/contest $RPM_BUILD_ROOT%{_datadir}/backgrounds/*.jpg $RPM_BUILD_ROOT%{_datadir}/backgrounds/ubuntu
sed -i 's|share/backgrounds|share/backgrounds/ubuntu|' $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/*.xml
cp -a $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties $RPM_BUILD_ROOT%{_datadir}/mate-background-properties

%files
%doc COPYING ChangeLog AUTHORS
%{_datadir}/backgrounds/ubuntu
%{_datadir}/*-background-properties/*.xml

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.35.1
- Rebuilt for Fedora
