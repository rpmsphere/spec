%define		oname  burrGui

Name:		burrtools		
Version:	0.6.3
Release:	1
Summary:	Burr Tools	
Group:		Applications/System
License:	GPL	
URL: 		https://burrtools.sourceforge.net		
Source0:	https://sourceforge.net/projects/burrtools/files/%{name}/%{version}/%{name}-%{version}.tar.gz	
Source1:        %{name}.png
BuildRequires:  fltk-devel
BuildRequires:  boost-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXi-devel

%description
This (set of) program(s) will help you solve a certain kind of puzzle.
Namely puzzles that are made out "glued" together basic units. As basic units
the program currently supports: square or dice shaped units, spheres,
prisms with an equilateral triangle as base or 2 grids that use tetrahedra.

%prep
%setup -q 
sed -i "s/examples\/README//g" Makefile.in
sed -i "s/boost_test_exec_monitor/boost_unit_test_framework/g" configure
#sed -i '1i #define BOOST_TEST_DYN_LINK' src/lib/main_test.cpp
sed -i 's|.*openGL is needed for burrtools.*|:|' configure
sed -i 's|.*Could not find a version of the library.*|:|' configure
sed -i 's|struct face f;|faceList_c::face f;|' src/halfedge/modifiers.cpp

%build
autoreconf -ifv
./configure --prefix=/usr
sed -i 's|-Werror=format-security|-Wno-error -shared -fPIC|' Makefile */Makefile
make %{?_smp_mflags}

cat > %{name}.desktop <<EOF
[Desktop Entry]
Name=%oname
Comment=%summary
Exec=%oname
Icon=%{name}
Type=Application
StartupNotify=false
Categories=Game;LogicGame;
Terminal=false
EOF

%install
%makeinstall INSTALL_ROOT=$RPM_BUILD_ROOT
install -Dm644 %{name}.desktop $RPM_BUILD_ROOT/%_datadir/applications/%{name}.desktop
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT/%_datadir/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%_bindir/%oname
%_bindir/burrTxt
%_bindir/burrTxt2
%_datadir/applications/%{name}.desktop
%_datadir/pixmaps/%{name}.png
%_datadir/doc/*

%changelog
* Sun Mar 19 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.3
- Rebuilt for Fedora
