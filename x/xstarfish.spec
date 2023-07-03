Name: xstarfish
Summary: X wallpaper generator
Version: 1.1
Release: 10.1
Group: Amusements/Games
License: GPL
URL: https://www.redplanetsw.com/starfish/
Source0: https://ftp.de.debian.org/debian/pool/main/x/xstarfish/%{name}_%{version}.orig.tar.gz
BuildRequires: libpng12-devel
BuildRequires: libX11-devel
BuildRequires: xorg-x11-xbitmaps

%description
XStarfish generates colourful, tiled images for your background using random
numbers fed through mathematical functions. It does not use source image
files, so it can generate its images nearly forever without running out of
material.

%prep
%setup -q -n starfish-%{version}
sed -i 's|png\.h|libpng12/png.h|' unix/makepng.c
sed -i 's|-lpng|-lpng12|' Makefile

%build
make

%install
install -Dm755 starfish %{buildroot}%{_bindir}/%{name}

%files
%doc COPYING README TODO
%{_bindir}/%{name}

%changelog
* Sun Jul 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
