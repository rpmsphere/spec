Summary:        Music/rhythm game : Songs files
Name:           stepmania-songs
Version:        4.0
Release:        1
License:        MIT
URL:            https://www.stepmania.com/browse.php
Group:          Amusements/Games/Arcade
Source0:        %{name}-%{version}.tar.bz2
Requires:       stepmania
BuildArch:      noarch

%description
StepMania is a free dance and rhythm game for Linux. It features 3D 
graphics, keyboard and "dance pad" support, and an editor for creating 
your own steps.

%prep
%setup -q

%install
rm -rf %buildroot
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/stepmania/Songs/
cp -a * $RPM_BUILD_ROOT%{_datadir}/stepmania/Songs/

%files
%{_datadir}/stepmania/Songs/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0
- Rebuilt for Fedora
* Thu Dec 23 2010 Chrin Lin <chris.lin@ossii.com.tw> 4.0-0 OX
- Stepmania : Songs
