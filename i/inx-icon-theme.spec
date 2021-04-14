%define theme_name iNX-GTK

Summary: %{theme_name} icon theme
Name: inx-icon-theme
Version: 0.6
Release: 4.1
License: CC BY-NC-ND 3.0
Group: User Interface/Desktops
URL: http://deviantn7k1.deviantart.com/art/iNX-Icon-set-344494902
Source: inx.zip
BuildArch: noarch

%description
iNX is an Icon set based on the look and feel of iOS. It's inspired by
elementary and Matrilineare. iNX contains a beautiful
set of Icons tailored for those that want a good looking workspace.

%prep
%setup -q -c
mv %{theme_name}/COPYING %{theme_name}/CREDITS .

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
cp -a %{theme_name} $RPM_BUILD_ROOT%{_datadir}/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README-Icons COPYING CREDITS
%{_datadir}/icons/%{theme_name}

%changelog
* Sun Jun 16 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
