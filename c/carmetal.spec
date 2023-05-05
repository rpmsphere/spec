%global _name CaRMetal

Name:		carmetal
Version:	4.3
Release:	1.bin
BuildArch:	noarch
URL:		http://carmetal2.free.fr/site/telechargements.php
Source0:	%{_name}4-3.zip
Source1:	%{_name}.png
Summary:	Dynamic geometry software with highly ergonomic UI
License:	LGPLv3
Group:		Sciences/Mathematics
Requires:	jre

%description
Based on the C.a.R. (Compass and Ruler) project, CaRMetal includes
all of its functionalities - or almost. It propose a different approach
from the graphical interface point of view.

Here's the C.a.R. presentation:
 - Ruler and compass constructions can be changed by dragging one of the
basic construction points. The construction follows immediately. The
student can check the correctness of the construction and gain new
insight.
 - Tracks of points and animated constructions can help to understand
geometric relations. Tracks can be used as new objects to explore.
 - With the macros of C.a.R. very complicated constructions become
possible. Macros are also a way to organize the geometric thinking.
 - Hiding construction details and using colors make constructions
clearer to read. In C.a.R. lines and circles can also be reduced to the
relevant points.
 - Arithmetic computations, numerical solutions, curves and functions
go beyond classical constructions. It is even possible to construct in 3D
using advanced macros.
 - Other geometries, hyperbolic or elliptic, can be explored.

%prep
%setup -q -n %{_name}4-3

%install
%__rm -f uninstall
%__rm -f CaRMetalUninstall.png
%__rm -f CaRMetal.desktop

%__install -d %{buildroot}%{_bindir}
%__install -d %{buildroot}%{_datadir}/%{name}
%__install -d %{buildroot}%{_datadir}/pixmaps

cp -r * %{buildroot}%{_datadir}/%{name}
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/CaRMetal.png

# wrapper script
%__cat > %{buildroot}%{_bindir}/carmetal << EOF
#!/bin/sh
env AWT_TOOLKIT="MToolkit" java -jar -Xmx256m /usr/share/%{name}/CaRMetal.jar
EOF

%__chmod 0755 %{buildroot}%{_bindir}/carmetal

# xdg menu
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=CaRMetal
Comment=%{summary}
Icon=CaRMetal
Exec=carmetal
Categories=Math;Science;Education;
StartupNotify=false
Terminal=false
EOF

%files
%{_bindir}/carmetal
%{_datadir}/pixmaps/CaRMetal.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*

%changelog
* Sun Feb 05 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 4.3
- Rebuilt for Fedora
* Sun Feb 19 2012 Andrey Bondrov <abondrov@mandriva.org> 3.7.1-1
+ Revision: 777309
- imported package carmetal
