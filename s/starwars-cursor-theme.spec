%define theme_name StarWars

Summary:        Star Wars cursor theme
Name:           starwars-cursor-theme
Version:        20090602
Release:        2.1
License:        Artistic 2.0
URL:            https://gnome-look.org/content/show.php/StarWars?content=106118
Group:          User Interface/Desktops
Source0:        106118-StarWars.tar.gz
BuildArch:      noarch

%description
Star Wars Cursors By JJ Ying https://users.wincustomize.com/691873/
StarWars X11 Mouse theme converted from StarWars.CurXPTheme with sd2xc-2.4.pl
and refined with GIMP.

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
* Wed Mar 30 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20090602
- Rebuilt for Fedora
