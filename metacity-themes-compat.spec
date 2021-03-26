Name: metacity-themes-compat
Version: 20160921
Release: 1.1
Summary: Compatible Metacity Themes
License: GPL
Group: Graphical desktop/MATE
Source0: %{name}.tar.gz
Buildarch: noarch

%description
This package contains compatible metacity themes for:
Adwaita, Sato, IrisDark, IrisLight.

%prep
%setup -q -c

%build

%install
install -d $RPM_BUILD_ROOT%_datadir/icons/hicolor/16x16/status
mv gtk-missing-image.png $RPM_BUILD_ROOT%_datadir/icons/hicolor/16x16/status
install -d $RPM_BUILD_ROOT%_datadir/themes
cp -a * $RPM_BUILD_ROOT%_datadir/themes

%files
%_datadir/themes/*/metacity-1/*
%_datadir/icons/hicolor/16x16/status/gtk-missing-image.png

%changelog
* Wed Sep 21 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20160921
- Rebuild for Fedora
