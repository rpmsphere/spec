%define theme_name Ecliz

Summary:        Ecliz cursor theme
Name:           ecliz-cursor-theme
Version:        20090211
Release:        3.1
License:        freeware
Group:          User Interface/Desktops
URL:            https://gnome-look.org/content/show.php/Ecliz?content=110340
Source0:        110340-Ecliz.tar.gz
BuildArch:      noarch

%description
Original Ecliz Cursors theme By JJ Ying https://users.wincustomize.com/691873/

For the conversion I used the program perl sd2xc-2.5.pl adds KDE4 Compatibility,
and adjusts the individual pointer animations with GIMP and XMC plugin.

%prep
%setup -q -n %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%files 
%{_datadir}/icons/%{theme_name}

%changelog
* Fri Dec 02 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20090211
- Rebuilt for Fedora
