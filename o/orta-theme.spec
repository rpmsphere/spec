%define theme_name Orta

Summary: %{theme_name} GTK and Metacity theme
Name: orta-theme
Version: 1.4.1
Release: 15.1
License: GPL for codes, CC-NC-SA for pixmaps
Group: User Interface/Desktops
Source0: %{name}-%{version}.zip
Source1: raindrops.jpg
Source2: %{theme_name}-index.theme
URL: https://skiesofazel.deviantart.com/art/Orta-184118297
Requires: dalisha-icon-theme
Requires: oxygen-cursor-themes
BuildArch: noarch

%description
%{theme_name} is a new take on Azel theme by SkiesOfAzel.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
tar zxf %{theme_name}.tar.gz -C $RPM_BUILD_ROOT%{_datadir}/themes
tar zxf %{theme_name}-Squared.tar.gz -C $RPM_BUILD_ROOT%{_datadir}/themes
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp CHANGELOG *.py %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/%{name}
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme
sed -e 's|Name=Orta|Name=Orta Squared|' -e 's|MetacityTheme=Orta|MetacityTheme=Orta-Squared|' %{SOURCE2} > $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}-Squared/index.theme

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%files
%{_datadir}/themes/%{theme_name}*
%{_datadir}/%{name}

%changelog
* Mon May 09 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.1
- Rebuilt for Fedora
