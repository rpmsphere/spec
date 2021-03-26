%define theme_name Classic95

Summary: %{theme_name} icon theme
Name: classic95-icon-theme
Version: 0.8p1
Release: 2.1
License: GPL
Group: User Interface/Desktops
URL: http://gnome-look.org/content/show.php/Classic95?content=157298
Source: %{theme_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
Classic icons for GNOME/MATE based on Windows 95.

%prep
%setup -q -n %{theme_name}
rm findsymbolic icon-theme.cache x

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
mv COPYING README $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/icons/%{theme_name}
%{_datadir}/doc/%{name}-%{version}

%changelog
* Sun Jun 16 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8p1
- Rebuild for Fedora
