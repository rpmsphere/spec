%define theme_name CrystalClear

Summary: %{theme_name} icon theme
Name: crystalclear-icon-theme
Version: 1.0.0
Release: 3.1
License: GPL
URL: https://www.gnome-look.org/content/show.php?content=26331
Group: User Interface/Desktops
Source: %{theme_name}-GNOME-%{version}.tar.bz2
BuildArch: noarch

%description
Crystal Clear icon theme for GNOME.

%prep
%setup -q -n %{theme_name}-GNOME-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/%{theme_name}
rm -rf index.theme~ .DS_Store
cp -R * %{buildroot}%{_datadir}/icons/%{theme_name}

%clean
rm -rf %{buildroot}

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuild for Fedora
