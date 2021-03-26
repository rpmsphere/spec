%define theme_name Neotif

Summary: Smooth appearance with a Amiga inspired appearance and older UNIX style color scheme
Name: neotif-gnome-theme
Version: 0.1.1
Release: 31.1
License: free
Group: User Interface/Desktops
Source0: https://dl.opendesktop.org/api/files/download/id/1460765369/137267-Neotif-GTK.tar.gz
Source1: https://dl.opendesktop.org/api/files/download/id/1460749283/137265-Neotif-Metacity.tar.gz
Source2: %{theme_name}-index.theme
Source3: 121759.png
Source4: LighthouseBlue-index.theme
URL: http://gnome-look.org/content/show.php?content=137267
BuildArch: noarch
Requires: gtk-lighthouseblue-engine
Requires: gnome-themes-extras
Requires: goglus-cursor-theme

%description
This is an original theme created by me from scratch, vaguely inspired by a
combination of pre-OSX Macintosh and the Amiga Workbench. I've been using it
for a few years now, but this is the first time i'm releasing it publically.

The GTK portion of the theme requires the LighthouseBlue theme engine.
Recommended Metacity button layout is Close on the left and Maximize and
Minimize or Shade on the right. I never made proper buttons for Menu or any
of the other Metacity 2.x buttons. If this is a problem, just drop me a line.

%prep
%setup -q -c -a 1
cp %{SOURCE2} %{theme_name}/index.theme
cp %{SOURCE3} %{theme_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes
cp -a %{theme_name} $RPM_BUILD_ROOT%{_datadir}/themes
install -Dm644 %{SOURCE4} %{buildroot}%{_datadir}/themes/LighthouseBlue/index.theme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/themes/%{theme_name}
%{_datadir}/themes/LighthouseBlue/index.theme

%changelog
* Wed Jul 06 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuild for Fedora
