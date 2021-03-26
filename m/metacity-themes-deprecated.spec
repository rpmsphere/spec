Name: metacity-themes-deprecated
Version: 3.18.7
Release: 2.1
Summary: Deprecated Metacity Themes
License: GPL
Group: Graphical desktop/MATE
Source0: https://download.gnome.org/sources/metacity/3.18/metacity-%{version}.tar.xz
Conflicts: metacity < 3.20
Buildarch: noarch

%description
This package contains deprecated metacity themes from version < 3.20:
Adwaita, AgingGorilla, Bright, Crux, Esco, HighContrast, Metabox, Simple.

%prep
%setup -q -n metacity-%{version}

%build

%install
install -d $RPM_BUILD_ROOT%{_datadir}/themes
cd src/themes
for theme in Adwaita AgingGorilla Bright Crux Esco HighContrast Metabox Simple ; do
  mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/$theme/metacity-1
  cp $theme/* $RPM_BUILD_ROOT%{_datadir}/themes/$theme/metacity-1
done

%files
%{_datadir}/themes/*/metacity-1/*

%changelog
* Thu Aug 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.18.7
- Rebuild for Fedora
