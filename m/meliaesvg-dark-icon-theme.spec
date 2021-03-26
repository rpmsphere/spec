%define theme_name MeliaeSVG-Dark

Summary: %{theme_name} icon theme
Name: meliaesvg-dark-icon-theme
Version: 1.2
Release: 2.1
License: GPL
Group: User Interface/Desktops
URL: http://sora-meliae.deviantart.com/art/Meliae-SVG-Dark-v-1-2-155756091
Source: http://fc06.deviantart.net/fs71/f/2010/065/1/7/Meliae_SVG_Dark_v__1_2_by_sora_meliae.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
MeliaeSVG-Dark icon theme for light panels.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
cp -a %{theme_name} $RPM_BUILD_ROOT%{_datadir}/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/icons/%{theme_name}*

%changelog
* Sun May 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuild for Fedora
