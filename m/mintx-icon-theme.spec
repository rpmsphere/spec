%global theme_name Mint-X

Name:		mintx-icon-theme
Version:	1.3.7
Release:	2.1
Summary:	%{theme_name} icon theme
Group:		System/GUI/GNOME
License:	GPLv3+
URL:		https://www.gnome-look.org/content/show.php/Mint+X+Colors+Icon+Theme?content=165531
Source0:	https://packages.linuxmint.com/pool/main/m/mint-x-icons/mint-x-icons_1.3.7.tar.xz
BuildArch:      noarch

%description
Brings You The Linux Mint Default Icon Theme in 8 Awesome New Colors!

%prep
%setup -q -n mint-x-icons/usr/share/icons

%build

%install
install -d %{buildroot}%{_datadir}/icons
cp -a * %{buildroot}%{_datadir}/icons

%files
%{_datadir}/icons/%{theme_name}*

%changelog
* Wed Aug 10 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.7
- Rebuilt for Fedora
