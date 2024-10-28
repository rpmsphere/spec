Name:           openbox-themes
Version:        1.0.2
Release:        7.1
Summary:        Themes for Openbox
Group:          User Interface/Desktops
License:        GPLv3
Source0:        %{name}_%{version}.tar.gz
BuildArch:      noarch
Requires:           gtk-murrine-engine
Requires:           openbox
Requires:           industrial-gnome-theme

%description
Various themes for openbox window manager.

%prep
%setup -q
for i in Aubergine Generic Green Industrial Orange Red Slate
do
sed -i -e 's|=Mist|='Simple-$i'|' -e 's|IconTheme=.*|IconTheme=Industrial|' Simple-$i/index.theme
done

%build

%install
mkdir -p -m755 %{buildroot}%{_datadir}/themes
cp -a * %{buildroot}%{_datadir}/themes
rm -r %{buildroot}%{_datadir}/themes/debian

%files
%doc debian/copyright debian/changelog
%{_datadir}/themes/*

%changelog
* Mon Feb 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuilt for Fedora
