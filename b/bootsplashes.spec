Name:           bootsplashes
Version:        20070602
Release:        3.1
Summary:        A few GRUB bootsplashes
Group:          User Interface/Desktops
License:        GPL
URL:            http://gnome-look.org/content/show.php/GRUB+Splashes?content=59322
Source0:        http://gnome-look.org/CONTENT/content-files/59322-Bootsplashes.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       grub

%description
What you get:
(Color) Great F.H. picture of B-17s
(Color) Good lookin' shot of 3 soldiers in Iraq
(Color) Shot of golden, rolling, California hills
(Grayscale) Shot of Asian waterway and mountains. (Windows Vista Wallpaper)
(Color) Great painting made by Ecsdesign, a member of the F.H. Developer team, of German troops moving through a North African city.
(Color) Another great painting by Ecsdesign, of a British North-African charge.
(Grayscale) Antelope in desert (Vista Wallpaper)
(Grayscale) Explosion
(Color) Vista grass

%prep
%setup -q -n Bootsplashes

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/boot/grub/%{name}
cp * $RPM_BUILD_ROOT/boot/grub/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/boot/grub/%{name}

%changelog
* Sun Jan 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 20070602
- Rebuild for Fedora
