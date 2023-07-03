Name:           tennebon-dynamic-wallpaper
License:        CC-BY-SA-2.5
Group:          System/GUI/GNOME
Summary:        Tennebon Dynamic wallpaper for GNOME
Version:        1
Release:        5.1
Source0:        tennebon-wallpaper.tar.bz2
# Note: the license was discussed by mail with jimmac
Source1:        %name.COPYING
BuildArch:      noarch

%description
This package contains a dynamic wallpaper based on the Tennebon wallpaper.

A dynamic wallpaper changes depending on the time of the day: it is
generally bright during the day, and dark during the night.

%prep
%setup -q -c
cp %{SOURCE1} COPYING

%build

%install
install -d %{buildroot}%{_datadir}/backgrounds
cp -a tennebon %{buildroot}%{_datadir}/backgrounds/
install -Dm644 tennebon-dynamic-wallpaper.xml %{buildroot}%{_datadir}/gnome-background-properties/tennebon-dynamic-wallpaper.xml
install -Dm644 tennebon-dynamic-wallpaper.xml %{buildroot}%{_datadir}/mate-background-properties/tennebon-dynamic-wallpaper.xml

%clean
rm -rf %{buildroot}

%files
%doc COPYING
%{_datadir}/backgrounds/tennebon
%{_datadir}/gnome-background-properties/tennebon-dynamic-wallpaper.xml
%{_datadir}/mate-background-properties/tennebon-dynamic-wallpaper.xml

%changelog
* Wed Aug 01 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuilt for Fedora
* Wed Feb  9 2011 vuntz@opensuse.org
- New package, containing a dynamic wallpaper based on the Tennebon
  set of wallpapers (see bnc#358461).
