%global debug_package %{nil}
%global _name QtPaint

Name: qtpaint
Summary: MS Paint clone using Qt
Version: 0.20170726
Release: 4.1
Group: Graphics
License: LGPLv3
URL: https://github.com/SillyLossy/QtPaint
Source0: %{_name}-master.zip
BuildRequires: qt5-qtbase-devel

%description
Simple graphics editor using Qt 5 library.
Supports image loading and saving, basic drawing, etc.

%prep
%setup -q -n %{_name}-master
sed -i 's|L#IBS|#LIBS|' QtPaint.pro
sed -i 's|setWindowFlag(|setWindowFlags(|' layerslist.cpp

%build
qmake-qt5
make %{?_smp_mflags}

%install
install -Dm755 %{_name} %{buildroot}%{_bindir}/%{name}
install -Dm644 icons/app.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
DEncoding=UTF-8
Name=QtPaint
Exec=%{name}
Terminal=false
Comment=MS Paint clone using Qt
Type=Application
Categories=Application;Graphics;
Icon=%{name}
EOF

%files
%doc README.md LICENSE
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Sep 08 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20170726
- Rebuild for Fedora
