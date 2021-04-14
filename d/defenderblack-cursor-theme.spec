%define theme_name DefenderBlack

Summary:        DefenderBlack cursor theme
Name:           defenderblack-cursor-theme
Version:        20100612
Release:        4.1
License:        freeware
Group:          User Interface/Desktops
URL:            http://grynays.deviantart.com/art/Defender-Black-167463928?q=1&qo=1
Source0:        http://www.deviantart.com/download/167463928/Defender_Black_by_GrynayS.zip
BuildArch:      noarch

%description
Original CursorXPTheme by RPGuere
http://rpguere.deviantart.com/gallery/?offset=72#/dihfbn
Thank RPGuere, authorized me to share.
I Hope you like! :-£

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
* Thu Dec 08 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20100612
- Rebuilt for Fedora
