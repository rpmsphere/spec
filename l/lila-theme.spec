%define theme_name Lila

Summary: Lila theme for GNOME
Name: lila-theme
Version: 20071027
Release: 13.1
License: GPL
Group: User Interface/Desktops
Source0: lila-backgrounds-0.3.4.tar.bz2
Source1: lila-cursors-0.5.tar.bz2
Source2: lila-gdm-0.3.4.tar.bz2
Source3: lila-gnome_0.6.4.tar.bz2
Source4: lila-gtk-0.5.5.tar.bz2
Source5: lila-gtk-extras-0.4.5.tar.bz2
URL: https://www.lila-center.info/
BuildArch: noarch
Requires: gtk-smooth-engine
Requires: gtk-xfce-engine

%description
A theme I started for Gentoo Linux based on purple and green,
now maintained by Gentoo community members.

%prep
%setup -q -c -a 1 -a 2 -a 3 -a 4 -a 5
sed -i 's/Name=Lila/Name=LilaCursor/' lila-cursors/Lila/index.theme
mv lila-cursors/Lila lila-cursors/LilaCursor

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a lila-gtk/* $RPM_BUILD_ROOT%{_datadir}/themes
cp -a lila-gtk-extras/* $RPM_BUILD_ROOT%{_datadir}/themes
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gdm/themes
cp -a lila-gdm/* $RPM_BUILD_ROOT%{_datadir}/gdm/themes
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
cp -a Lila $RPM_BUILD_ROOT%{_datadir}/icons
cp -a lila-cursors/* $RPM_BUILD_ROOT%{_datadir}/icons
mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/%{theme_name}
cp -a lila-backgrounds/* $RPM_BUILD_ROOT%{_datadir}/backgrounds/%{theme_name}
echo CursorTheme=Lila-white >> $RPM_BUILD_ROOT%{_datadir}/themes/SimpLila/index.theme
echo CursorTheme=LilaCursor >> $RPM_BUILD_ROOT%{_datadir}/themes/GorLila/index.theme
echo BackgroundImage=%{_datadir}/backgrounds/%{theme_name}/lila-messy.svg >> $RPM_BUILD_ROOT%{_datadir}/themes/SimpLila/index.theme
echo BackgroundImage=%{_datadir}/backgrounds/%{theme_name}/lila-penguin.svg >> $RPM_BUILD_ROOT%{_datadir}/themes/GorLila/index.theme

cd $RPM_BUILD_ROOT%{_datadir}/icons/Lila/scalable/stock
for i in *-ltr.svg
do
ln -s $i ${i/-ltr/}
done

%files
%doc LICENSE COPYRIGHT CREDITS
%{_datadir}/themes/*
%{_datadir}/gdm/themes/*
%{_datadir}/icons/*
%{_datadir}/backgrounds/*

%changelog
* Fri Apr 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20071027
- Rebuilt for Fedora
