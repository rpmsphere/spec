%global theme_name GlassyBleu

Summary: GlassyBleu GNOME theme
Name: glassybleu-gnome-theme
Version: 21
Release: 4.1
License: GPL
Group: User Interface/Desktops
Source0: https://hpmini.archive.canonical.com/mie/dists/hardy-hpmini/universe/source/glassy-bleu-theme_%{version}.tar.gz
Source1: Pattern-Paisley-l.jpg
BuildArch: noarch

%description
This package contains the GlassyBleu GTK+, Metacity and icon theme.

%prep
%setup -q -n glassy-bleu-theme-%{version}
cp %{SOURCE1} icons
sed -i '$a BackgroundImage=/usr/share/icons/GlassyBleu/Pattern-Paisley-l.jpg' index.theme

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/themes/GlassyBleu
cp -R index.theme gtk-2.0 metacity-1 %{buildroot}%{_datadir}/themes/GlassyBleu
mkdir -p %{buildroot}%{_datadir}/icons/GlassyBleu
cp -R icons/* %{buildroot}%{_datadir}/icons/GlassyBleu

%files
%{_datadir}/themes/GlassyBleu
%{_datadir}/icons/GlassyBleu

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 21
- Rebuilt for Fedora
