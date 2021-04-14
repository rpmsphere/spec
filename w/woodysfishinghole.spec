Name:          woodysfishinghole
Version:       0.9.0
Release:       1
Summary:       A fishing game for young children
Group:         Graphical Desktop/Applications/Educational
URL:           http://sourceforge.net/projects/wfh/
Source:        http://kent.dl.sourceforge.net/sourceforge/wfh/WoodysFishingHole-%{version}-src.tar.gz
Source1:       fish.png
License:       GPL
BuildRequires: java-1.8.0-openjdk-devel, ant
BuildArch:     noarch
Requires:      jre

%description
A fishing game for young children. A simple educational game for kids up to 6
years old. Young toddlers can match colors then move up to letters and numbers.
Older kids can practice the names of colors and/or simple objects and practice
math.

%prep
%setup -q -n WoodysFishingHole

%build
ant

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/lib
install -m 755 WoodysFishingHole.jar %{buildroot}/usr/lib

#Icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/fish.png

# Create the system menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Woodys Fishing Hole
Comment=A fishing game for young children
Exec=java -jar /usr/lib/WoodysFishingHole.jar
Icon=%{_datadir}/pixmaps/fish.png
Terminal=0
Type=Application
Category=Game;KidsGame;
EOF

%clean
rm -rf %{buildroot}

%files
%doc README
/usr/lib/WoodysFishingHole.jar
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/fish.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.0
- Rebuilt for Fedora
* Mon May 21 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 0.9.0-2mamba
- entry group fixed
- desktop menu file fixed
* Fri Jul 22 2005 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 0.9.0-1qilnx
- package created by autospec
