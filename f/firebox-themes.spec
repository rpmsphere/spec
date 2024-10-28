Name:           firebox-themes
Version:        0.5.0
Release:        2.1
Summary:        Themes for the Firebox Window Manager
Group:          User Interface/Desktops
License:        GPLv2+
URL:            https://firebox.intuxication.org/
Source:         https://download.gna.org/firebox/tarballs/%{name}-%{version}.tar.gz
Requires:       firebox
BuildArch:      noarch

%description
Themes for the Firebox Window Manager.

%prep
%setup -q

%build
%configure

%install
rm -rf %{buildroot}
%makeinstall

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_datadir}/firebox/themes

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuilt for Fedora
