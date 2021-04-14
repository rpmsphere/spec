%define theme_name A-New-Hope

Summary: %{theme_name} GTK and Metacity theme
Name: anewhope-gnome-theme
Version: 0.7.9
Release: 24.1
License: GPL for codes, CC-NC-SA for pixmaps
Group: User Interface/Desktops
Source0: %{theme_name}.zip
Source1: %{theme_name}-index.theme
Source2: http://awesomewallpaper.files.wordpress.com/2011/02/see-the-world.jpg
URL: http://jurialmunkey.deviantart.com/art/Divergence-IV-quot-A-New-Hope-quot-183377193
BuildArch: noarch
Requires: gtk-murrine-engine
Requires: nitrux-icon-theme
Requires: ecliz-cursor-theme

%description
A New Hope is the Divergence IV theme by jurialmunkey.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}
tar xf %{theme_name}.tar.gz -C $RPM_BUILD_ROOT%{_datadir}/themes
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
rm -f $RPM_BUILD_ROOT%{_datadir}/themes/A-New-Hope/Configure\ A\ New\ Hope
rm -f $RPM_BUILD_ROOT%{_datadir}/themes/A-New-Hope/customise.py
rm -rf $RPM_BUILD_ROOT%{_datadir}/themes/A-New-Hope/RES
tar xf EMERALD/%{theme_name}.emerald -C $RPM_BUILD_ROOT%{_datadir}/emerald/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%{_datadir}/themes/%{theme_name}
%{_datadir}/emerald/themes/%{theme_name}

%changelog
* Mon May 09 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.9
- Rebuilt for Fedora
