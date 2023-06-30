%define theme_name Genoid

Summary: Android for GNOME environment
Name: genoid-gnome-theme
Version: 1.0
Release: 5.1
License: GPLv2
Group: User Interface/Desktops
Source0: https://genoid.googlecode.com/files/%{theme_name}_%{version}.tar.bz2
Source1: %{theme_name}-index.theme
BuildArch: noarch
URL: https://code.google.com/p/genoid/

%description
It's the theme for android lovers who use Gnome Environment,it's called "Genoid",
not much to say, i just try replicated Android Theme to used on Gnome with
some modification.

%prep
%setup -q -n packages
tar jxf xsplash.tar.bz2

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/icons
tar jxf icons.tar.bz2 -C %{buildroot}%{_datadir}/icons
tar jxf cursor.tar.bz2 -C %{buildroot}%{_datadir}/icons
mkdir -p %{buildroot}%{_datadir}/gdm
tar jxf gdm.tar.bz2 -C %{buildroot}%{_datadir}/gdm
mkdir -p %{buildroot}%{_datadir}/backgrounds/%{theme_name}
cp -a xsplash/bg_*.jpg %{buildroot}%{_datadir}/backgrounds/%{theme_name}
mkdir -p %{buildroot}%{_datadir}/themes
tar jxf theme.tar.bz2 -C %{buildroot}%{_datadir}/themes
cd %{buildroot}%{_datadir}/themes/%{theme_name}
rm -f gtk-2.0/panel/*.png~ metacity-1/*.xml~
cp %{SOURCE1} %{buildroot}%{_datadir}/themes/%{theme_name}/index.theme

%clean
rm -rf %{buildroot}

%files
%{_datadir}/themes/%{theme_name}
%{_datadir}/icons/%{theme_name}
%{_datadir}/icons/%{theme_name}Cursor
%{_datadir}/gdm/%{theme_name}
%{_datadir}/backgrounds/%{theme_name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
