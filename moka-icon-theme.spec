Name:		moka-icon-theme
Version:	5.3.2
Release:	4.1
Summary:	Moka icon theme
Group:		System/GUI/GNOME
License:	GPL-3.0+
URL:		http://mokaproject.com/moka-icon-theme/
Source0:	https://raw.githubusercontent.com/moka-project/moka-icon-theme/master/%{name}-%{version}.tar.gz
Requires:	gtk3
BuildArch:  noarch

%description
This package contains the Moka icon theme.

%prep
%setup -q

%build

%install
install -d %{buildroot}%{_datadir}/icons
cp -a Moka %{buildroot}%{_datadir}/icons

%files
%doc AUTHORS COPYING LICENSE_* README.md
%{_datadir}/icons/Moka

%changelog
* Wed Jul 20 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 5.3.2
- Rebuild for Fedora
* Wed Oct 2 2013 arnaldo.coelho@gmail.com
- Initial release
