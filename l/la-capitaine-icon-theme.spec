%global theme_name LaCapitaine

Summary:	La Capitaine icon theme
Name:		la-capitaine-icon-theme
Version:	0.5.0
Release:	3.1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		https://krourke.org/projects/art/la-capitaine-icon-theme
Source0:	https://krourke.org/files/%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
Icon theme inspired by macOS and Google's Material Design.

%prep
%setup -q
rm -rf .github .product .gitignore

%build
#./configure

%install
install -d %{buildroot}%{_datadir}/doc/la-capitaine-icon-theme
mv *.md COPYING LICENSE %{buildroot}%{_datadir}/doc/la-capitaine-icon-theme
install -d %{buildroot}%{_datadir}/icons/%{theme_name}
cp -R * %{buildroot}%{_datadir}/icons/%{theme_name}

%files
%{_datadir}/doc/%{name}
%{_datadir}/icons/%{theme_name}

%changelog
* Tue Sep 19 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuilt for Fedora
* Sat Feb 04 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.4.0-2
- (383782a) MassBuild#1230: Increase release tag


