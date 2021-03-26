%define theme_name MeliaeSVG

Summary: %{theme_name} icon theme
Name: meliaesvg-icon-theme
Version: 1.2
Release: 1.1
License: GPL
Group: User Interface/Desktops
URL: http://sora-meliae.deviantart.com/art/Meliae-SVG-Icon-Theme-v-1-2-151155215
Source: http://fc04.deviantart.net/fs70/f/2010/065/9/1/Meliae_SVG_Icon_Theme_v__1_2_by_sora_meliae.zip
BuildArch: noarch
Obsoletes: meliae-icon-theme

%description
MeliaeSVG icon theme for dark panels.

%prep
%setup -q -c
tar xf %{theme_name}.tar.gz
rm %{theme_name}/index.theme~

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
cp -a %{theme_name} $RPM_BUILD_ROOT%{_datadir}/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Sun May 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuild for Fedora
