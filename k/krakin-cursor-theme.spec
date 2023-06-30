%define theme_name Krakin

Summary:        Krakin cursor theme
Name:           krakin-cursor-theme
Version:        20100221
Release:        3.1
License:        freeware
Group:          User Interface/Desktops
URL:            https://grynays.deviantart.com/art/krakin-154925900?q=1&qo=1
Source0:        https://www.deviantart.com/download/154925900/krakin_by_GrynayS.gz
BuildArch:      noarch

%description
As requested, I converted this pointer of Brett Zenor.
Thank to Brett Zenor "theCasualties" for having authorized to distribute Krakin.
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
%{_datadir}/icons/%{theme_name}

%changelog
* Thu Dec 08 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20100221
- Rebuilt for Fedora
