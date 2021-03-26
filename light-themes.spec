Name:           light-themes
Version:        0.1.8.6
Release:        4.1
License:        CC-BY-SA ; Canonical Trademark Policy ; Others
Summary:        Ubuntu light themes (Ambiance, Radiance)
URL:            http://launchpad.net/light-themes
Group:          System/GUI/GNOME
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Patch0:         %{name}-icontheme.patch

%description
This package provides Ubuntu's Light Themes:
 * Ambiance - a light-on-dark theme
 * Radiance - a dark-on-light theme

%prep
%setup -q
%patch0 -p1

%build

%install
%{__mkdir} -p $RPM_BUILD_ROOT%{_datadir}/themes
%{__cp} -a Ambiance $RPM_BUILD_ROOT%{_datadir}/themes/Ambiance
%{__cp} -a Ambiance-CSD $RPM_BUILD_ROOT%{_datadir}/themes/Ambiance-CSD
%{__cp} -a Radiance $RPM_BUILD_ROOT%{_datadir}/themes/Radiance

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc debian/copyright debian/changelog
%{_datadir}/themes/Ambiance
%{_datadir}/themes/Ambiance-CSD
%{_datadir}/themes/Radiance

%changelog
* Tue May 17 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.8.6
- Rebuild for Fedora

* Tue Feb 15 2011 nmarques@opensuse.org
- Initial package from release 0.1.8.6
