%undefine _debugsource_packages

Name:           qtweb
Version:        3.8.5.108
Release:        1
Summary:        Portable Qt-based web browser
Group:          Applications/Internet
License:        GPLv2
URL:            https://github.com/magist3r/QtWeb
Source0:        QtWeb-master.zip
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel
BuildRequires:  qtwebkit-devel

%description
QtWeb is a fast, lightweight and portable browser with some unique UI and
privacy features. QtWeb is an open source project based on Qt framework
and Apple's WebKit rendering engine (the same as being used in Apple
Safari and Google Chrome).

%prep
%setup -q -n QtWeb-master
#sed -i '/Q_IMPORT_PLUGIN/d' main.cpp
#sed -i 's|static|shared|' QtWeb.pro
#sed -i -e '/macx/d' -e '/else/,$d' QtWeb.pri

%build
qmake-qt4
make %{?_smp_mflags}

%install
install -Dm755 src/QtWeb %{buildroot}%{_bindir}/%{name}
install -Dm644 src/Resources/logo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Name=QtWeb
Comment=Portable Qt-based web browser
Exec=qtweb
Icon=qtweb
Terminal=false
Type=Application
StartupNotify=false
Categories=Network;WebBrowser;
EOF
install -d %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/qt4/plugins/codecs > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-qt4.conf
echo %{_libdir}/qt4/plugins/imageformats >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-qt4.conf

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_sysconfdir}/ld.so.conf.d/%{name}-qt4.conf

%changelog
* Mon Jan 13 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 3.8.5.108
- Rebuilt for Fedora
