%define theme_name MurrinaCrystal

Summary: Murrina Crystal II GTK theme
Name: murrinacrystal2-gtk-theme
Version: 0.3.2
Release: 21.1
License: LGPL
Group: User Interface/Desktops
Source0: 116964-murrinacrystall2.tar.gz
Source1: %{theme_name}-index.theme
Source2: https://imgs.mi9.com/uploads/other/2683/aquamarine-blue-crystal_1280x1024_36540.jpg
URL: https://gnome-look.org/content/show.php/MurrinaCrystal%20II?content=116964
BuildArch: noarch
Requires: crystal-icon-theme
Requires: crispblue-metacity-theme
Requires: crystal-cursor-theme

%description
Requirement: Latest murrine engine from git.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a %{theme_name}* $RPM_BUILD_ROOT%{_datadir}/themes
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}Aqua/index.theme
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}Aqua

%files
%{_datadir}/themes/%{theme_name}*

%changelog
* Fri Apr 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2
- Rebuilt for Fedora
