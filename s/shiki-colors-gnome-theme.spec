%define theme_name Shiki-Colors

Summary:        %{theme_name} GTK & metacity theme
Name:           shiki-colors-gnome-theme
Version:        4.6
Release:        15.1
License:        GPL
Group:          User Interface/Desktops
URL:            https://www.gnome-look.org/content/show.php/Shiki-Colors?content=86717
Source0:        https://gnome-colors.googlecode.com/files/shiki-colors-%{version}.tar.gz
Source1:        aurora1_by_pkarwowski.jpg
BuildArch:	    noarch
Requires:       gnome-colors-icon-theme
Conflicts:      shiki-colors-gnome-theme-murrine

%description
Shiki-Colors Themes for GNOME.

%prep
%setup -q -c
sed -i 's|IconTheme=gnome|IconTheme=gnome-colors|' */index.theme
cp %{SOURCE1} .
sed -i '$a BackgroundImage=/usr/share/doc/%{name}/aurora1_by_pkarwowski.jpg' */index.theme

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a Shiki-* $RPM_BUILD_ROOT%{_datadir}/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%doc AUTHORS ChangeLog COPYING README *.png *.css *.jpg
%{_datadir}/themes/*

%changelog
* Sun Mar 17 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 4.6
- Rebuilt for Fedora
