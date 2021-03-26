%define theme_name Moblin

Summary: %{theme_name} Unofficial Icons
Name: moblin-icon-theme
Version: 20110122
Release: 5.1
License: GPL
Group: User Interface/Desktops
Source0: https://dl.opendesktop.org/api/files/download/id/1460758503/137740-Moblin.tar.gz
Source1: moblin-energy-blue-1024x600.png
URL: https://www.gnome-look.org/p/1012137/
BuildArch: noarch
BuildRequires: ghostscript-core ImageMagick

%description
These are the Moblin Netbook Icons - Kudos the the Original Creator.

%prep
%setup -q -n %{theme_name}
convert -resize 24x24 48x48/places/user-trash-full.png 24x24/places/user-trash-full.png
mogrify -resize 48x48 48x48/places/user-trash-full.png
mogrify -resize 48x48 48x48/places/user-trash.png
mogrify -resize 48x48 48x48/places/edittrash.png

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a index.theme *x* %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Thu Oct 06 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20110122
- Rebuild for Fedora
