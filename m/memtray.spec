Name:           memtray
Version:        1.4
Release:        1
Summary:        Show your system memory usage on an icon in the system tray
License:        GPL3
Group:          User Interface/X
URL:            https://sourceforge.net/projects/systray-memory-display/
Source0:        systray-memory-display-%{version}.zip
BuildRequires:  qt5-qtbase-devel

%description
Do you ever need to know how much memory your system is using, but you don't
want to open an application to know? Then this tool is for you!

While running, you'll see an icon in the system tray (notification area).
The icon displays a number, representing the %% of memory you're currently using.

Right click on the icon to open the settings window, in which you can configure
the colors of text and background, and how often the displayed value is updated.

%prep
%setup -q -n systray-memory-display-%{version}

%build
%qmake_qt5 PREFIX=/usr
make

%install
mkdir -p %{buildroot}%{_bindir}
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 appicon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Categories=Utility;
Name=MemTray       
Comment=Show your system memory usage on an icon in the system tray
Exec=%{name}        
Icon=%{name}
EOF

%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Jan 02 2020 Wei-Lun Chao <blubat@member.fsf.org> - 1.4
- Rebuilt for Fedora
