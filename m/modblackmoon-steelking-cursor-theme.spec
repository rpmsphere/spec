%define theme_name ModBlackmoon-SteelKing

Summary:        %{theme_name} cursor theme
Name:           modblackmoon-steelking-cursor-theme
Version:        1.0
Release:        2.1
License:        GPLv2+
URL:            http://xfce-look.org/content/show.php/ModBlackmoon-SteelKing?content=106338
Group:          User Interface/Desktops
Source0:        106338-ModBlackmoon-SteelKing.tar.gz
BuildArch:      noarch

%description
MB-SteelKing By ModBlackmoon http://users.wincustomize.com/2501323/
MB-SteelKing X11 Mouse theme converted with sd2xc-2.5.pl and refined with GIMP+xmc plugin.

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
* Thu Mar 31 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
* Wed Aug 01 2012 Motsyo Gennadi <drool@altlinux.ru> 0.1-alt1
- initial build for ALT Linux
