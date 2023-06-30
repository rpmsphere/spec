%undefine _debugsource_packages

Name:       	bstracer
Version:    	0.04
Release:    	24.1
Summary:    	Beesoft Tracer
License:    	GPLv2+
Group:      	File tools
URL:        	https://www.beesoft.org/index.php?id=tracer
Source:     	https://www.beesoft.org/download/%{name}_%{version}.tar.gz
BuildRequires:	qt4-devel
BuildRequires:	ghostscript-core ImageMagick

%description
Beesoft Tracer is a suite of tools for a remote real time debugging of running
program. Core elements are wrote in pure C++ with using STL library.
The communication between elements is via sockets: so called unix domain socket
and TCP/IP.

%prep
%setup -q -n tracer
sed -i '1i #include <cstring>\n#include <unistd.h>\n#include <algorithm>' shared/BT*.cpp trace_clr/Trace*.cpp
sed -i 's|-O2|-O2 -fPIC|' makefile

%build
make
cd trview
qmake-qt4 QMAKE_CXXFLAGS+="-fPIC"
make

%install
install -d %{buildroot}%{_bindir}
install -m755 tracesrv tracecli traceclr %{buildroot}%{_bindir}
install -m755 trview/trview %{buildroot}%{_bindir}

# menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Trace View
Comment=Beesoft Tracer Viewer
Exec=trview
Icon=trview
Terminal=false
Type=Application
Categories=Development;
EOF

# icon
install -Dm644 trview/img/TraceView.png %{buildroot}%{_datadir}/pixmaps/trview.png

%files
%doc manual.txt
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/trview.png

%changelog
* Thu Feb 06 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.04
- Rebuilt for Fedora
