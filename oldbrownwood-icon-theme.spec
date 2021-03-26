%define theme_name OldBrownWood

Summary: %{theme_name} Icon theme
Name: oldbrownwood-icon-theme
Version: 0.0.2
Release: 3.1
License: GPL
Group: User Interface/Desktops
Source0: https://dl.dropboxusercontent.com/s/z3vpwn7pemlf94n/OldBrownWoodIcons.tar.gz
URL: https://www.gnome-look.org/p/1015823/
BuildArch: noarch

%description
An Old wood icon set based off of nouveGnomeGray available here:
http://tsujan.deviantart.com/art/nouveGnomeGray-300365158
This is the brown version.

%prep
%setup -q -n %{theme_name}Icons
echo -e '[256x256/filesystems]\nSize=256\nContext=Filesystems\nType=Scalable' >> index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a index.theme 256x256 $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README GPL AUTHORS
%{_datadir}/icons/%{theme_name}

%changelog
* Wed Oct 05 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.2
- Rebuild for Fedora
