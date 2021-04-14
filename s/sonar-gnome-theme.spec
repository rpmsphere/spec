%define theme_name Sonar

Summary: %{theme_name} GTK2 & GTK3 & Metacity theme
Name: sonar-gnome-theme
Version: 3.2
Release: 12.1
License: GPL3
Group: User Interface/Desktops
Source0: %{theme_name}-%{version}.tar.bz2
Source1: %{theme_name}-index.theme
URL: http://half-left.deviantart.com/art/Sonar-GTK3-254801661
BuildArch: noarch
Requires: sonar-icon-theme
Requires: harmony-cursor-theme
Requires: gnome-backgrounds

%description
This is a GTK3 port of Sonar used by default in openSUSE.

%prep
%setup -q -n %{theme_name}-%{version}
cp %{SOURCE1} index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a index.theme mozilla gtk-2.0 metacity-1 gtk-3.0 $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING AUTHORS
%{_datadir}/themes/%{theme_name}

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2
- Rebuilt for Fedora
* Fri Dec 16 2011 malcolmlewis@opensuse.org
- Update on 2nd November 2011:
  + Fixed rubberband selection looking solid white in the
    filemanager.
  + Added DnD lines.
- Updates from 25th October 2011:
  + Improved tabs.
  + Added dark border on menus.
  + Lighter selection.
  + Don't use dark Adwaita theme for image viewer.
- Add fdupes BuildRequires and call %%fdupes: there are now some
  duplicate svg images and css files.
* Thu Oct 20 2011 vuntz@opensuse.org
- Update to version 3.2:
  + Works fine with GTK+ 3.2.
- Remove unzip BuildRequires: the source is not compressed with zip
  anymore.
* Tue Sep 13 2011 vuntz@opensuse.org
- Initial import of GTK+ 3 port of Sonar (version 1.3).
