Summary:	A flat theme with transparent elements
Name:		arc-theme
Version:	20160605
Release:	5.3
URL:		https://github.com/horst3180/arc-theme
License:	GPL3
Group:		User Interface/Desktops
Source0:	%{name}-%{version}.tar.gz
Source1:    glacier-869593_1920.jpg
BuildArch:	noarch
BuildRequires: gtk3-devel
Requires:	gtk-murrine-engine
Requires:   breeze-cursor-theme
Requires:   breeze-icon-theme

%description
Arc is a flat theme with transparent elements for GTK 3, GTK 2 and Gnome-Shell
which supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity,
Budgie, Pantheon, XFCE, Mate, etc.

%prep
%setup -q

%build
./autogen.sh --prefix=/usr
make

%install
%make_install
sed -i -e 's|gnome|breeze|' -e 's|DMZ-Black|breeze_cursors|' %{buildroot}%{_datadir}/themes/Arc/index.theme
sed -i -e 's|gnome|breeze-dark|' -e 's|DMZ-Black|Breeze_Snow|' %{buildroot}%{_datadir}/themes/Arc-Dark*/index.theme
install -m644 %{SOURCE1} %{buildroot}%{_datadir}/themes/Arc
sed -i '$a BackgroundImage=%{_datadir}/themes/Arc/glacier-869593_1920.jpg' %{buildroot}%{_datadir}/themes/Arc*/index.theme

%files
%doc AUTHORS README.md COPYING
%{_datadir}/themes/Arc*

%changelog
* Wed Jun 29 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20160605
- Rebuilt for Fedora
