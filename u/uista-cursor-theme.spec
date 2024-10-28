%define theme_name UISTA

Summary:        UISTA cursor theme
Name:           uista-cursor-theme
Version:        20100410
Release:        3.1
License:        freeware
Group:          User Interface/Desktops
URL:            https://grynays.deviantart.com/art/UISTA-160216742?q=1&qo=1
Source0:        https://www.deviantart.com/download/160216742/UISTA_by_GrynayS.gz
BuildArch:      noarch

%description
Original theme By VovanR:
https://www.deviantart.com/users/outgoing?https://users.wincustomize.com/2168068/
As requested, I convert this pointer of VovanR.
For the conversion I used the program perl sd2xc-2.5.pl adds KDE4 Compatibility,
and adjusts the individual pointer animations with GIMP and XMC plugin.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%files 
%{_datadir}/icons/%{theme_name}

%changelog
* Thu Dec 08 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20100410
- Rebuilt for Fedora
