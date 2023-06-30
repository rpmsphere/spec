%undefine _debugsource_packages

Summary:	Easy to use text mode editor
Name:		efte
Version:	1.1git
Release:	1
Source0:	https://github.com/lanurmi/efte/archive/master.zip#/efte-master.zip
License:	GPL
Group:		Editors
URL:		https://github.com/lanurmi/efte/
BuildRequires:	gpm-devel
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(slang)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	cmake ninja-build

%description
eFTE is a Text Mode text editor for xterm sessions.  Color syntax highlighting
for C/C++, REXX, HTML, IPF, PERL, Ada, Pascal, TEX.  Multiple file/window
editing, Column blocks, configurable menus and keyboard bindings, mouse
support, undo/redo, regular expression search and replace, folding, background
compiler execution.

%package x11
Summary:	X11 version of the eFTE editor
Group:		Editors
Requires:	%{name}

%description x11
X11 version of the eFTE editor

%prep
%autosetup -p1 -n efte-master
sed -i 's|-Wall|-Wall -fPIE|' src/CMakeLists.txt
cmake -DCMAKE_INSTALL_PREFIX=/usr -G Ninja

%build
%ninja_build 
#-C *-linux-build

%install
%ninja_install 
#-C *-linux-build

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/org.openmandriva.%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=eFTE Text Editor
Exec=%{name}
Icon=editors_section
Terminal=false
Type=Application
Categories=Utility;TextEditor;
EOF

%files 
%doc README COPYING AUTHORS HISTORY Artistic
%{_bindir}/nefte
%{_bindir}/vefte
%{_datadir}/efte

%files x11
%{_bindir}/efte
%{_datadir}/applications/*
%{_datadir}/pixmaps/efte*.xpm

%changelog
* Sun May 9 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1git
- Rebuilt for Fedora
