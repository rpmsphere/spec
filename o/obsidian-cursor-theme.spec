%define theme_name Obsidian

Summary:        Obsidian cursor theme
Name:           obsidian-cursor-theme
Version:        1.0
Release:        2.1
License:        GPL
Group:          User Interface/Desktops
URL:            https://www.gnome-look.org/content/show.php/Obsidian+Cursors?content=73135
Source0:        https://dl.opendesktop.org/api/files/download/id/1460735403/73135-Obsidian.tar.bz2
BuildArch:      noarch

%description
Obsidian Cursors is a shiny and clean cursor set created in Inkscape
based upon my previous Polar Cursor Theme.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a index.theme cursors $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/icons/%{theme_name}

%changelog
* Thu Aug 11 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
