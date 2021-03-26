%global theme_name Capitaine

Name:           capitaine-cursor-theme
Version:        2.1
Release:        4.1
Summary:        %{theme_name} Cursor theme
Group:          System/X11/Icons
License:        LGPLv3
URL:            https://krourke.org/projects/art/capitaine-cursors
Source0:        capitaine-cursors-r%{version}.tar.gz
BuildArch:      noarch

%description
This is an x-cursor theme inspired by macOS and based on KDE Breeze.
All cursor images were designed in Inkscape, before being generated
by xcursorgen. This cursor pack was designed to pair well with my
icon theme, La Capitaine.

%prep
%setup -q -n capitaine-cursors-r%{version}

%build
./build.sh

%install
install -d %{buildroot}%{_datadir}/icons/%{theme_name}
cp -a dist/* %{buildroot}%{_datadir}/icons/%{theme_name}

%clean
rm -rf %{buildroot}

%files
%doc README.md COPYING
%{_datadir}/icons/%{theme_name}

%changelog
* Sat Dec 02 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuild for Fedora
