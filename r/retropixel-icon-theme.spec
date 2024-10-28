%define theme_name RetroPixel

Summary: %{theme_name} icon theme
Name: retropixel-icon-theme
Version: 0.74
Release: 2.1
License: CC by-na-sa
Group: User Interface/Desktops
Source: https://www.deviantart.com/download/176033573/retropixel_v0_74_by_therealpadster-d2wt0dh.zip
URL: https://therealpadster.deviantart.com/art/RetroPixel-v0-74-176033573
BuildArch: noarch

%description
A retro theme made to go with my Digital pack
(https://gnome-look.org/content/show.php?content=127764)
Icons from:
https://icondock.com/free/mini-pixel-icons
https://www.scoutshonour.com/digital/
https://pichaus.com/art-font-bit-opentype-@afad45a09b7db1cb92cccac0944048e8/
and me, of course. Many icons were modified by me in some way.

%prep
%setup -q -n %{theme_name}

%build

%install
install -d $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}
cp -a index.theme scalable $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%files
%{_datadir}/icons/%{theme_name}

%changelog
* Mon Sep 26 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.74
- Rebuilt for Fedora
