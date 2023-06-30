Summary:	Aurora engine for Gtk 2.x
Group:		Graphical desktop/Other
Name:		gtk-aurora-engine
Version:	1.5.1
Release:	21.1
License:	GPLv2+
URL:		https://gnome-look.org/content/show.php/Aurora+Gtk+Engine?content=56438
Source0:	https://gnome-look.org/CONTENT/content-files/56438-aurora-%{version}.tar.bz2
Source1:    Aurora-index.theme
Source2:    aurora_by_paolorotolo-1920x1200.png
Patch0:		animation.diff
BuildRequires:	pkgconfig(gtk+-2.0)
Requires: awoken-icon-theme
Requires: uista-cursor-theme

%description
The goal of this theme is to provide a complete and consistent look
for Gtk. The theme aims to be very flexible in color choice, but
provide few other options otherwise. The theme includes some features
that do not seem to be available in other Gtk engines; it also allows
the theming of Gnome panel widgets.

%prep
%setup -qc
tar xf *.tar.bz2
tar xf *.tar.gz
%patch0 -p1

# Fix bug 56215:
sed -i 's/\(^.*odd_row_color.*\)/\#\1/' Aurora/gtk-2.0/gtkrc
cp %{SOURCE1} Aurora/index.theme
cp %{SOURCE2} Aurora

%build
cd aurora-1.5
export LDFLAGS="-lm"
%configure --enable-animation
make

%install
%makeinstall -C aurora-1.5
mkdir -p %{buildroot}%{_datadir}/themes
cp -fr Aurora %{buildroot}%{_datadir}/themes

%files
%doc aurora-1.5/README aurora-1.5/ChangeLog
%{_datadir}/themes/*
%{_libdir}/gtk-2.0/*/engines/*.*

%changelog
* Mon Mar 07 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.1
- Rebuilt for Fedora
* Sun Jul 19 2015 Bernhard Rosenkraenzer <bero@bero.eu> 1.5.1-11
+ Revision: 9fc0332
- MassBuild#774: Increase release tag
