Name:		faba-icon-theme
Version:	4.1.2
Release:	5.1
Summary:	Faba icon theme
Group:		System/GUI/GNOME
License:	GPL-3.0+
URL:		https://github.com/moka-project/faba-icon-theme
Source0:	https://raw.githubusercontent.com/moka-project/faba-icon-theme/master/%{name}-%{version}.tar.gz
Source1:    faba-mono-icons.tar.gz
Requires:	gtk3
BuildArch:  noarch

%description
This package contains the Faba icon theme and
the monochromatic panel icon sets for Faba.

%prep
%setup -q -a 1

%build

%install
install -d %{buildroot}%{_datadir}/icons
cp -a Faba* %{buildroot}%{_datadir}/icons

%files
%doc LICENSE AUTHORS COPYING
%{_datadir}/icons/Faba*

%changelog
* Wed Jul 20 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1.2
- Rebuilt for Fedora
