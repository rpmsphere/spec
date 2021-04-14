%define theme_name GartoonRedux

Summary: %{theme_name} icon theme
Name: gartoonredux-icon-theme
Version: 1.11
Release: 12.1
License: GPL
URL: https://www.gnome-look.org/p/1012491/
Group: User Interface/Desktops
Source0: https://launchpad.net/gartoon-redux/1.x/1.11/+download/gartoon-redux-%{version}.tar.gz
BuildRequires: librsvg2-tools
BuildRequires: perl-Switch
BuildRequires: redhat-lsb-core
BuildArch: noarch

%description
This is a massively improved variant of the well-known Gartoon theme, used by
e.g. Edubuntu. Some work may also be based on the Gnutoon/Ubuntoon variant by
reassuringlyoffensive.

%prep
%setup -q -n gartoon-redux-%{version}
#sed -i 's|rsvg -x \$zoom_factor -y \$zoom_factor \$source \$target|rsvg-convert -x $zoom_factor -y $zoom_factor $source -o $target|' configure

%build
#./configure --prefix=/usr
#make

%install
rm -rf %{buildroot}
make install PREFIX=%{buildroot}/usr
sed -i 's|Example=audacity|Example=folder|' %{buildroot}%{_datadir}/icons/%{theme_name}/index.theme

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS changelog README GPLv2.txt TODO
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.11
- Rebuilt for Fedora
