%define theme_name CountryOak

Summary:        Country Oak GTK theme
Name:           countryoak-gtk-theme
Version:        20100719
Release:        29.1
License:        GPL
Group:          User Interface/Desktops
URL:            http://gnome-look.org/content/show.php/Country+Oak?content=127617
Source0:        http://gnome-look.org/CONTENT/content-files/127617-Country_Oak.tar.bz2
Source1:        %{theme_name}-index.theme
BuildArch:	    noarch
Requires:       tierrauim-wood-metacity-theme
Requires:       ubo-icon-theme
Requires:       knotvista-cursor-theme

%description
This is a lighter variation on the "WoodenHead" GTK theme. This is also
an attempt to emulate the color of the wood in Mozilla Firefox's "Walnut"
or "Walnut 2" themes and apply them to the rest of your GNOME or Xfce desktop.

%prep
%setup -q -n "Country Oak"
cp %{SOURCE1} index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%{_datadir}/themes/%{theme_name}

%changelog
* Fri Jun 17 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20100719
- Rebuilt for Fedora
