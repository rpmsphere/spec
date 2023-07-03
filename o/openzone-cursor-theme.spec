Name:           openzone-cursor-theme
License:        X11
Group:          User Interface/Desktops
Summary:        OpenZone Cursors
Version:        1.2.6
Release:        5.1
URL:            https://gnome-look.org/content/show.php/OpenZone?content=111343
Source0:        https://gnome-look.org/CONTENT/content-files/OpenZone-%{version}.tar.xz
BuildArch:      noarch

%description
Cursor themes: Black Black_Slim White White_Slim Ice Ice_Slim Fire Fire_Slim.

%prep
%setup -q -n openzone-cursors

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
for i in *.tar.xz
do
tar xf $i -C $RPM_BUILD_ROOT%{_datadir}/icons
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/OpenZone_*
%doc ChangeLog COPYING

%changelog
* Wed Jan 10 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.6
- Rebuilt for Fedora
