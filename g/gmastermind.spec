Name:          gmastermind
Version:       0.01
Release:       1
Summary:       A simple GTK clone of the classic board game, MasterMind
Group:         Graphical Desktop/Applications/Educational
URL:           https://www.linuxsoft.cz/en/sw_detail.php?id_item=4085
Source:        https://rsynnott.f2g.net/gmastermind/%{name}-%{version}.tar.gz
Source1:       %{name}.png
License:       GPL
BuildRequires: glib-devel
BuildRequires: gtk+-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel

%description
GMasterMind is a simple GTK clone of the classic board game, MasterMind.

%prep
%setup -q -n %{name}
sed -i 's| -g | -g -Wl,--allow-multiple-definition |' Makefile

%build
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
install -m 755 gmastermind %{buildroot}/usr/bin

#Icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Create the system menu entry
mkdir -p %{buildroot}%{_datadir}/applnk/Edutainment/Miscellaneous
cat > %{buildroot}%{_datadir}/applnk/Edutainment/Miscellaneous/%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=A simple GTK clone of the classic board game, MasterMind
Exec=gmastermind
Icon=%{name}
Terminal=0
Type=Application
Categories=GNOME;Application;Education;
EOF

%files
%{_bindir}/gmastermind
%{_datadir}/applnk/Edutainment/Miscellaneous/gmastermind.desktop
%{_datadir}/pixmaps/gmastermind.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.01
- Rebuilt for Fedora
* Wed Apr 08 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.01-2mamba
- specfile updated and rebuilt
* Wed Jul 20 2005 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 0.01-1qilnx
- package created by autospec
