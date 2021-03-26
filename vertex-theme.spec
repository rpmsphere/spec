Summary:	A theme for GTK 3, GTK 2, Gnome-Shell and Cinnamon
Name:		vertex-theme
Version:	20170128
Release:	1
URL:		https://github.com/horst3180/vertex-theme
License:	GPL3
Group:		User Interface/Desktops
Source0:	%{name}-%{version}.tar.gz
Source1:        alone.jpg
BuildArch:	noarch
Requires:	gtk-murrine-engine
Requires:       dmz-cursor-themes
Requires:       vertex-icon-theme

%description
Vertex is a theme for GTK 3, GTK 2, Gnome-Shell and Cinnamon. It supports
GTK 3 and GTK 2 based desktop environments like Gnome, Cinnamon, Mate, XFCE,
Budgie, Pantheon, etc. Themes for the Browsers Chrome/Chromium and Firefox
are included, too.

The theme comes with three variants to choose from. The default variant with
dark header-bars, a light variant, and a dark variant.

With background by memovaslg:
http://memovaslg.deviantart.com/art/Alone-353235628

%prep
%setup -q
ln -s 3.20 common/gtk-3.0/3.24
ln -s 3.20 common/gnome-shell/3.24

%build
./autogen.sh --prefix=/usr
make

%install
%make_install
sed -i -e 's|gnome|Vertex|' -e 's|DMZ-Black|dmz-aa|' %{buildroot}%{_datadir}/themes/Vertex*/index.theme
cp %{SOURCE1} %{buildroot}%{_datadir}/themes/Vertex
sed -i '$a BackgroundImage=/usr/share/themes/Vertex/alone.jpg' %{buildroot}%{_datadir}/themes/Vertex*/index.theme

%files
%doc AUTHORS NEWS ChangeLog README.md COPYING
%{_datadir}/themes/*

%changelog
* Wed Sep 25 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 20170128
- Rebuild for Fedora
