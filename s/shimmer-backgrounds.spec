Name:           shimmer-backgrounds
Version:        1.6.2
Release:        8.1
Summary:        Backgrounds from Shimmer Project
Group:          User Interface/Desktop
License:        GPLv3
URL:            https://github.com/shimmerproject/Wallpapers
Source0:        Wallpapers-master.zip
Source1:        %{name}.xml
BuildArch:      noarch

%description
This package contains desktop backgrounds accompanied our themes from Shimmer Project.

%prep
%setup -q -n Wallpapers-master

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/backgrounds/shimmer
cp Albatross/albatross-2009-10.png Bluebird/bluebird-2010-08-1920x1440-notext.png Greybird/greybird-wall-1920x1200.png $RPM_BUILD_ROOT/%{_datadir}/backgrounds/shimmer
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/%{name}.xml
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/mate-background-properties/%{name}.xml

%files
%{_datadir}/backgrounds/shimmer
%{_datadir}/*-background-properties/%{name}.xml

%changelog
* Fri Oct 18 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.2
- Rebuilt for Fedora
