%define theme_name Crisp-Blue

Summary: %{theme_name} metacity theme
Name: crispblue-metacity-theme
Version: 1.0.0
Release: 2.1
License: GPL
Group: User Interface/Desktops
Source: CrystalforGnomeCrispBlue1-0-0.tar.gz
URL: https://gnome-look.org/content/show.php/Crisp+Blue?content=24757
BuildArch: noarch

%description
A shiny and crisp metacity theme, created by member Chromakode, of the Crystal
for Gnome project.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -R * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%files
%{_datadir}/themes/%{theme_name}

%changelog
* Wed Mar 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuilt for Fedora
