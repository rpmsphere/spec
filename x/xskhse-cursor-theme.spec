%define theme_name XSKHSE

Summary:        XSKHSE cursor theme
Name:           xskhse-cursor-theme
Version:        20100213
Release:        4.1
License:        freeware
Group:          User Interface/Desktops
URL:            http://grynays.deviantart.com/art/XSKH-SE-153963206?q=1&qo=1
Source0:        http://www.deviantart.com/download/153963206/XSKH_SE_by_GrynayS.gz
BuildArch:      noarch

%description
X-SKH SE by JJ Ying: http://jjying.wincustomize.com/
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
* Thu Dec 08 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20100213
- Rebuilt for Fedora
