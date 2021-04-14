%define theme_name sketch

Summary:        Sketch cursor theme
Name:           sketch-cursor-theme
Version:        2008.10.11
Release:        2.1
License:        Creative Commons by
Group:          User Interface/Desktops
URL:            http://kde-look.org/content/show.php/sketch?content=91087
Source0:        http://kde-look.org/CONTENT/content-files/91087-sketch.tar.gz
BuildArch:      noarch

%description
original work of cibiboi
http://cibiboi.deviantart.com/art/Sketch-CursorXP-76819267

%prep
%setup -q -n sketch

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
* Thu Feb 18 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2008.10.11
- Rebuilt for Fedora
