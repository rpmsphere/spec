%define theme_name Pulse-Glass

Summary:        Pulse-Glass cursor theme
Name:           pulseglass-cursor-theme
Version:        20100610
Release:        4.1
License:        freeware
Group:          User Interface/Desktops
URL:            http://grynays.deviantart.com/art/Pulse-Glass-167120696?q=1&qo=1
Source0:        http://www.deviantart.com/download/167120696/Pulse_Glass_by_GrynayS.zip
BuildArch:      noarch

%description
Original theme by Stamga:
http://stamga.deviantart.com/art/Pulse-Glass-122337588
I created this from .ani and .cur base cursor.
I hope you like it.

%prep
%setup -q -c
tar xf %{theme_name}.tar.gz

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a %{theme_name}/* $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/icons/%{theme_name}

%changelog
* Thu Dec 08 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20100610
- Rebuilt for Fedora
