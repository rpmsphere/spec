%define theme_name Leopard

Summary: Leopard for GNOME environment
Name: leopard-theme
Version: 20091012
Release: 16.1
License: GPL
Group: User Interface/Desktops
Source0: Leopard-For-Gnome.tar.gz
Source1: Leopard-Wallpaper.png
Source2: Leopard-index.theme
Source3: Leopard-missing.tgz
BuildArch: noarch
URL: http://gekos.no/themes/gtk.html
Requires: aquanukex-cursor-theme

%description
Make Your Linux GNOME Desktop Look Like A Mac.

%prep
%setup -q -n Leopard-For-Gnome
tar xf ToyBox/Leopardish-GDM.tar.gz
sed -i '/evolution-tweaks.rc/d' gtk-2.0/gtkrc
tar xf %{SOURCE3} -C gtk-2.0

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gdm/%{theme_name}ish
cp -a Leopardish-GDM/* $RPM_BUILD_ROOT%{_datadir}/gdm/%{theme_name}ish
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -a metacity-1 gtk-2.0 xfwm4 $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}
cp -f %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/wallpaper.png
cp -f %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/themes/%{theme_name}/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}
%{_datadir}/gdm/%{theme_name}ish

%changelog
* Fri May 27 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20091012
- Rebuild for Fedora
