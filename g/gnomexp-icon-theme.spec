%define theme_name GnomeXP

Summary: %{theme_name} icon theme
Name: gnomexp-icon-theme
Version: 1.0
Release: 2.1
License: GPL
Group: User Interface/Desktops
Source: %{theme_name}.tar.gz
BuildArch: noarch

%description
Windows XP Luna Theme for Gnome.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/%{theme_name}
cp -a * %{buildroot}%{_datadir}/icons/%{theme_name}

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
