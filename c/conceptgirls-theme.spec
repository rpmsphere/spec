%define theme_name ConceptGirls

Summary: %{theme_name} GTK and Icon theme
Name: conceptgirls-theme
Version: 0.3.3
Release: 24.1
License: CC-BY-NC-SA
Group: User Interface/Desktops
Source0: http://sites.google.com/site/conceptgirls/fa-bu-yu-xia-zai/gnome-theme/概念少女GnomeTheme_Mark%{version}.tar.gz
Source1: https://sites.google.com/site/conceptgirls/_/rsrc/1287296769457/xi-tong-zhuang/Apartment_1.jpg
Source2: %{theme_name}-index.theme
URL: http://sites.google.com/site/conceptgirls/
BuildArch: noarch
Requires: tux-cursor-theme
Requires: industrial-gnome-theme

%description
%{theme_name} is the GTK/Icon-Theme of the Concept Girls Moe Project.
One character represent one main computer concept. Include "Confirm",
"No", Filesystem", "Info", "Secure"...etc.

%prep
%setup -q -c
cp %{SOURCE1} %{theme_name}
cp %{SOURCE2} %{theme_name}/index.theme
sed -i 's|Example=dialog-ok|Example=folder|' %{theme_name}Icon/index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes $RPM_BUILD_ROOT%{_datadir}/icons
cp -a %{theme_name} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a %{theme_name}Icon $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}
%{_datadir}/icons/%{theme_name}

%changelog
* Mon May 16 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.3
- Rebuilt for Fedora
