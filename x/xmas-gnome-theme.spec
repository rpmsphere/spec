%define theme_name Xmas

Summary: %{theme_name} GNOME theme
Name: xmas-gnome-theme
Version: 1.5
Release: 21.1
License: GPL
Group: User Interface/Desktops
Source0: https://dl.dropboxusercontent.com/s/lhfm5g8tdnxglkv/XmasTheme.tar.gz
Source1: %{theme_name}-index.theme
Source2: hc.png
SOurce3: ny.png
URL: https://www.gnome-look.org/p/1014258/
BuildArch: noarch
Requires: kids-icon-theme
Requires: comicface-cursor-theme
Requires: angrybirds-backgrounds

%description
Every year I mean to write a Christmas theme but leave it to late well not this year!
This is just a bit of fun for the hols and is not meant to be a complete (or even very usable theme!)

%prep
%setup -q -n %{theme_name}Theme
cp %{SOURCE1} index.theme
cp %{SOURCE2} %{SOURCE3} metacity-1

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
* Wed Oct 05 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuilt for Fedora
