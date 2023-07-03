%define theme_name Square-Beam

Summary:        %{theme_name} icon theme
Name:           squarebeam-icon-theme
Version:        1.0
Release:        2.1
License:        GPL
Group:          User Interface/Desktops
URL:            https://gnome-look.org/content/show.php/Square-Beam?content=165094
Source0:        %{theme_name}_1_0.tar.gz
BuildArch:      noarch

%description
Colorful icon set for Gnome, KDE, Unity, and Gnome smiliar DE.
Icons are redesigned* and developed by Eep Setiawan.

%prep
%setup -q -n %{theme_name}

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
* Fri Apr 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
