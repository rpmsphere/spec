%define theme_name OxygenRefit2-black

Summary: %{theme_name} icon theme
Name: oxygenrefit2-black-icon-theme
Version: 2.0.0
Release: 2.1
License: GPL
Group: User Interface/Desktops
Source: %{theme_name}-version.tar.bz2
BuildArch: noarch

%description
%{theme_name} icon theme for GNOME.

%prep
%setup -q -n %{theme_name}-version

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons/%{theme_name}
cp -a * %{buildroot}%{_datadir}/icons/%{theme_name}

%clean
rm -rf %{buildroot}

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.0
- Rebuild for Fedora
