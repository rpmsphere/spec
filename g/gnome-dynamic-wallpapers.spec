Name:           gnome-dynamic-wallpapers
URL:            https://gitorious.org/opensuse/art/trees/master/wallpaper/wallpaper-gnome?p=opensuse:art.git;a=tree;f=wallpaper/wallpaper-gnome
Summary:        Dynamic wallpapers for GNOME
License:        GPL-3.0 and CC-BY-SA-2.5
Group:          System/GUI/GNOME
Version:        11.4
Release:        4.1
Source0:        gnome-wallpaper-11.0.2.tar.bz2
Source1:        gnome-wallpaper-11.1.tar.bz2
Source2:        gnome-wallpaper-11.2.tar.bz2
Source3:        gnome-wallpaper-11.3.tar.bz2
Source4:        gnome-wallpaper-11.4.tar.bz2
Source10:       COPYING
Source11:       COPYING.CCBYSA
Source12:       COPYING.GPLv3
BuildArch:      noarch

%description
This package contains dynamic wallpapers from previous versions of
openSUSE.

A dynamic wallpaper changes depending on the time of the day: it is
generally bright during the day, and dark during the night.

%prep
%setup -q -T -a0 -a1 -a2 -a3 -a4 -c %{name}-%{version}
cp %{SOURCE10} %{SOURCE11} %{SOURCE12} .

%build

%install
install -d %{buildroot}%{_datadir}/backgrounds %{buildroot}%{_datadir}/gnome-background-properties

cp -a grass %{buildroot}%{_datadir}/backgrounds/
install -m0644 desktop-backgrounds-grass.xml %{buildroot}%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.0.xml
cp -a glass %{buildroot}%{_datadir}/backgrounds/
install -m0644 desktop-backgrounds-glass.xml %{buildroot}%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.1.xml
cp -a daft %{buildroot}%{_datadir}/backgrounds/
install -m0644 desktop-backgrounds-daft.xml %{buildroot}%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.2.xml
cp -a gnome-wallpaper-11.3/IK %{buildroot}%{_datadir}/backgrounds/
install -m0644 gnome-wallpaper-11.3/desktop-backgrounds-IK.xml %{buildroot}%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.3.xml
cp -a stripes %{buildroot}%{_datadir}/backgrounds/
install -m0644 desktop-backgrounds-stripes.xml %{buildroot}%{_datadir}/gnome-background-properties/dynamic-wallpaper-openSUSE-11.4.xml
cp -a %{buildroot}%{_datadir}/gnome-background-properties %{buildroot}%{_datadir}/mate-background-properties

%files
%doc COPYING COPYING.CCBYSA COPYING.GPLv3
%{_datadir}/backgrounds/*
%{_datadir}/gnome-background-properties/*.xml
%{_datadir}/mate-background-properties/*.xml

%changelog
* Wed Aug 01 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 11.4
- Rebuilt for Fedora
* Fri Mar  1 2013 coolo@suse.com
- Update license to new format.
* Wed Oct 12 2011 cdenicolo@suse.com
- Fix license tag: license is "GPL-3; CC-BY-SA-2.5", not BSD.
* Wed Oct  5 2011 vuntz@opensuse.org
- New package to contain dynamic wallpapers from the openSUSE 11.x
  releases. This is split from the old gconf2-branding-openSUSE
  package.
