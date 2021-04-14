%define theme_name G6

Summary: G6 for GNOME environment
Name: g6-theme
Version: 20110221
Release: 22.1
License: GPL
Group: User Interface/Desktops
Source0: https://dl.opendesktop.org/api/files/download/id/1460968136/138556-G6.tar.bz2
Source1: G6-index.theme
BuildArch: noarch
URL: http://gnome-look.org/content/show.php/%22G6%22+for+GNOME+%26+Xfce4?content=138556
Requires: silver3d-cursor-theme
Requires: inx-icon-theme
Requires: ios4mac-backgrounds

%description
G6 - neutral colors, easy for tired eyes (especially - my).
G6 is a heavy modified "Smooth" theme, that I created long time ago (now obsolete...).
All images attached to this "G6" Theme set are hand drawn from scratch - nothing remixed or copied.

%prep
%setup -q -n %{theme_name}
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
* Fri May 27 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20110221
- Rebuilt for Fedora
