%undefine _debugsource_packages

Name: sqlitestudio
Version: 3.2.1
Release: 4.1
Summary:    A SQLite database manager
License:    GPLv2
Group:      System/Configuration/Other
URL:        http://sqlitestudio.one.pl/
Source0:    http://sqlitestudio.pl/files/sqlitestudio3/complete/tar/%{name}-%{version}.tar.gz
BuildRequires: sqlite-devel
BuildRequires: readline-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qttools-static

%description
* Single executable file
* Intuitive interface
* All SQLite3 and SQLite2 features wrapped within simple GUI
* Cross-platform
* Localizations
* Exporting to various formats
* Importing data from various formats
* Numerous small additions
* UTF-8 support
* Skinnable
* Configurable colors, fonts and shortcuts
* Open source and free

%prep
%setup -q -n SQLiteStudio3

%build
qmake-qt5 -recursive
make

%install
make INSTALL_ROOT=%{buildroot} install
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

install -Dm644 docs/sqlitestudio_logo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=SQLite Studio
Comment=A SQLite database manager
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;Database;
MimeType=application/x-sqlite3;
EOF

%files
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/lib*

%changelog
* Tue Jul 31 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.1
- Rebuilt for Fedora
