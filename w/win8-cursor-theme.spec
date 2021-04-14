%define theme_name Win8

Summary:        Win8 cursor theme
Name:           win8-cursor-theme
Version:        1.01
Release:        4.1
License:        GPL
Group:          User Interface/Desktops
URL:            http://gnome-look.org/content/show.php/Windows+8+cursors?content=155025
Source0:        http://gnome-look.org/CONTENT/content-files/155025-win8.tar.gz
BuildArch:      noarch

%description
Windows 8 cursors.

%prep
%setup -q -n win8

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/icons/%{theme_name}

%changelog
* Sun Mar 24 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.01
- Rebuilt for Fedora
