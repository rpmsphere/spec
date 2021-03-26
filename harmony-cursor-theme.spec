%define theme_name Harmony

Summary:        Harmony cursor theme
Name:           harmony-cursor-theme
Version:        20100213
Release:        2.1
License:        freeware
Group:          User Interface/Desktops
URL:            http://grynays.deviantart.com/art/Harmony-154041068?q=1&qo=1
Source0:        http://www.deviantart.com/download/154041068/Harmony_by_GrynayS.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch

%description
Original theme By J. Aroche: http://fav.me/d14hpr8
For the conversion I used the program perl sd2xc-2.5.pl adds KDE4 Compatibility,
and adjusts the individual pointer animations with GIMP and XMC plugin.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,-)
%{_datadir}/icons/%{theme_name}

%changelog
* Thu Dec 08 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20100213
- Rebuild for Fedora
