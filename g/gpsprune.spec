Name:           gpsprune
Summary:        Viewing, editing and converting coordinate data from GPS systems
Version:        19.2
Release:        1.bin
Group:          Productivity/Other 
License:        GPL
URL:            http://activityworkshop.net/software/prune/
Requires:       java-1.8.0-openjdk
##BuildRequires:  unzip
##BuildRequires:  java-devel-openjdk lua
##BuildRequires:  ant 
##BuildRequires:  ant-nodeps
##BuildRequires:  java3d
##BuildRequires:  jpackage-utils
##Source0:        http://activityworkshop.net/software/%{name}/%{name}_%{version}_source.tar.bz2
Source0:        https://activityworkshop.net/software/gpsprune/gpsprune_19.2.jar
Source1:	%{name}.desktop
Source2:        %{name}.png
BuildArch:      noarch

%description
Prune is an application for viewing, editing and converting coordinate data
from GPS systems. Basically it's a tool to let you play with your GPS data
after you get home from your trip. It can load data from arbitrary text-based
formats (for example, any tab-separated or comma-separated file) or Xml, or
directly from a GPS receiver. It can display the data (as map view using
openstreetmap images and as altitude profile), edit this data (for example
delete points and ranges, sort waypoints, compress tracks), and save the data
(in various text-based formats). It can also export data as a Gpx file, or as
Kml/Kmz for import into Google Earth, or send it to a GPS receiver.

%prep
##%setup -q -n %{name}_%{version}
%setup -T -c

%build
# Start building - set java3D lib path
##export CLASSPATH=$(build-classpath-directory /usr/share/java/java3d/)
# run build script
##sh build.sh

%install
##export NO_BRP_CHECK_BYTECODE_VERSION=true
# install jar
%__install -d -m 755 %{buildroot}%{_datadir}/%{name}
##%__install -m 755 dist/*.jar %{buildroot}%{_datadir}/%{name}/
%__install -m 755 %{SOURCE0} %{buildroot}%{_datadir}/%{name}/

# startscript
cat > %{name} << EOF
#!/bin/sh
echo Starting %{name} version %{version} ...
echo with options : \${@}
java -jar %{_datadir}/%{name}/%{name}_%{version}.jar \$@
EOF

%__install -d -m 755 %{buildroot}%{_bindir}
%__install -m 755 %{name} %{buildroot}%{_bindir}/

# Icon
%__install -D -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

# Desktop menu entry
%__install -d -m 755 %{buildroot}%{_datadir}/applications
%__install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
#%doc README.html LICENSE.txt ChangeLog 

%changelog
* Wed May 22 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 19.2
- Rebuilt for Fedora
* Fri Nov 30 2012 lumnis@opensuse.org
- updated to version 14
- New Features: Dragging points, nautical miles, deleting points inside a rectangle
* Sat Nov 12 2011 lumnis@opensuse.org
- renamed files in project to gpsprune
* Tue Feb  8 2011 lumnis@opensuse.org
- renamed obs project to prunegps (copypac + delete prune pkg)
- update to PruneGPS vers. 12.1
* Thu Sep 30 2010 lumnis@opensuse.org
- update to Prune vers. 11.2
* Thu Aug 12 2010 lumnis@opensue.org
- update to Prune vers. 11
* Thu May  6 2010 lumnis@opensuse.org
- update to Prune vers. 10
* Tue Feb 16 2010 lumnis@opensuse.org
- update to prune vers. 8
* Mon Oct  5 2009 lumnis@opensuse.org
- initial rpm build for prune 8
