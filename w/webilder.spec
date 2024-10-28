Summary: complete solution for Webshots users who use Linux
Name: webilder
Version: 0.7.3
Release: 1
Source0: %{name}-master.zip
Source1: %{name}-0.6.7.zh_TW.po
License: GPLv2+
Group: Desktop/User Interface
BuildArch: noarch
Requires: python-imaging, pygtk2, pygtk2-libglade
URL: https://www.webilder.org/
BuildRequires: python2-setuptools
BuildRequires: gnome-python2-gnome
#BuildRequires: python2-appindicator

%description
Webilder enables you to download photos from Webshots website into your photo
collection. The package includes a GNOME panel applet that can notify you
whenever new daily photos are ready to be downloaded.
Webilder now also downloads picturesd from flickr based on interestingness and tags.

%prep
%setup -q -n %{name}-master
mkdir -p src/%{name}/locale/zh_TW/LC_MESSAGES
cp %{SOURCE1} src/%{name}/locale/zh_TW/LC_MESSAGES/%{name}.po
sed -i "s|, 'appindicator'||" setup.py

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --root=$RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%{_bindir}/*
%{_datadir}/pixmaps/*
%{python2_sitelib}/*
/usr/lib/bonobo/servers/GNOME_WebilderApplet.server
%{_datadir}/applications/webilder_desktop.desktop
%{_datadir}/applications/webilder_indicator.desktop
%{_datadir}/gnome/autostart/webilder_indicator.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.3
- Rebuilt for Fedora
