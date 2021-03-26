Name: page
Summary: Python Automatic GUI Generator
Version: 4.6
Release: 8.1
Group: Development/Tools
License: GPLv2
URL: http://page.sourceforge.net/
Source0: http://sourceforge.net/projects/page/files/%{name}/%{version}/%{name}-%{version}.tgz
Requires: tkinter
BuildRequires: ghostscript-core ImageMagick
BuildArch: noarch

%description
PAGE is a tool which helps to create Tkinter GUI interfaces for use within
Python programs.  It is a rework or extension of the program Visual Tcl (Vtcl)
so that Vtcl now produces Python code. Faced with the problem of building an
application driven by a single GUI window, PAGE will facilitate designing the
GUI and building a working skeletal Python program emphasizing the ttk widgets.
As other windows are required, they are designed with PAGE and incorporated into
the application by importing the generated python module.

%prep
%setup -q -n %{name}
sed -i '1s|/bin|/usr/bin|' page.tcl

%build
convert WIN_INSTALL/page.ico page.png

%install
install -d %{buildroot}%{_datadir}/%{name}
cp -a images lib page.tcl version %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=PAGE
Comment=Python Automatic GUI Generator
Exec=PAGE
Icon=%{name}
Terminal=false
Type=Application
Categories=Utility;TextEditor;
StartupNotify=true
EOF
install -Dm644 page.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/PAGE <<EOF
#!/usr/bin/sh
cd %{_datadir}/%{name}
exec ./%{name}.tcl
EOF
chmod +x %{buildroot}%{_bindir}/PAGE

%files
%doc docs/*
%{_bindir}/PAGE
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Feb 17 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 4.6
- Rebuild for Fedora
