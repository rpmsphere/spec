%define theme_name E17gtk

Summary: %{theme_name} GTK & Metacity theme
Name: e17gtk-gnome-theme
Version: 3.20.0
Release: 12.1
License: GPL3
Group: User Interface/Desktops
Source0: %{theme_name}-%{version}.tar.gz
Source1: %{theme_name}-index.theme
Source2: e17.jpg
URL: https://github.com/tsujan/E17gtk
BuildArch: noarch
Requires: awoken-icon-theme
Requires: krakin-cursor-theme

%description
E17gtk is a dark GTK2/GTK3 theme with sharp corners, which is designed for use
in Enlightenment and gives the elegant look of Enlightenment to GTK widgets.
Of course, it can be used in other environments too but it is not tuned to Gnome
or any of its apps.

%prep
%setup -q -n %{theme_name}-%{version}
cp %{SOURCE1} index.theme
cp %{SOURCE2} .

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a index.theme e17.jpg gtk-2.0 gtk-3.0 metacity-1 $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING NEWS README.md WORKAROUNDS
%{_datadir}/themes/%{theme_name}

%changelog
* Mon Jul 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.20.0
- Rebuilt for Fedora
