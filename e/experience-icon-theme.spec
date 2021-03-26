%define theme_name eXperience

Summary: %{theme_name} icon theme
Name: experience-icon-theme
Version: 20050723
Release: 1.1
License: CC BY-NC-ND
URL: http://benjamin.sipsolutions.net/Projects/eXperience
Group: User Interface/Desktops
Source: http://benjamin.sipsolutions.net/experience/%{theme_name}-icons.tar.gz
BuildArch: noarch

%description
eXperience Crystal made by David Christian Berg. The use of the Crystal icons
has been permitted by Everaldo, www.everaldo.com
The Crystal SVG For Gnome Theme - which this theme is based on - has been
converted by Tehmiller, Panic_69 (Infernux), Exdaix, and Chromakode,
all members of www.LinuxCult.com.

%prep
%setup -q -n %{theme_name}
rm *~

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' $RPM_BUILD_ROOT%{_datadir}/icons/eXperience/genindex.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Sun Mar 03 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 20050723
- Rebuild for Fedora
