%global theme_name    ZukiBlues

Name:           zukiblues-gnome-theme
Version:        0.1.1
Release:        13.1
Summary:        Zuki Blues Theme for Gtk, Metacity and Openbox
Group:          User Interface/Desktops
License:        GPL
Source0:        %{name}.tgz
Source1:        %{theme_name}-index.theme
BuildArch:      noarch      
Requires:	    gtk-equinox-engine, gtk-murrine-engine
Requires:       raveh20-classic-icon-theme
Requires:       blueglass3d-cursor-theme
Requires:       shimmer-backgrounds

%description
Zuki Blues GTK by lassekongo83 from https://lassekongo83.deviantart.com/art/Zuki-Blues-175190463
Zuki Blues openbox by nale dany from https://box-look.org/content/show.php/Zuki+Blues?content=128931
Zuki Blues Metacity by na12 from https://gnome-look.org/content/show.php/Zuki%20Blues?content=129575

%prep
%setup -q -c
cp %{SOURCE1} "Zuki Blues"/index.theme

%build

%install
mkdir -p -m755 %{buildroot}%{_datadir}/themes
cp -pr "Zuki Blues" %{buildroot}%{_datadir}/themes/%{theme_name}

%files
%{_datadir}/themes/*

%changelog
* Mon Feb 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuilt for Fedora
