%undefine _debugsource_packages

Name:           xdiskusage
Version:        1.52
Release:        1
Summary:        Lightweight interface to visualize your detailed disk usage
Group:          File tools
License:        GPLv2+
URL:            http://xdiskusage.sourceforge.net
Source0:        http://xdiskusage.sourceforge.net/%{name}-%{version}.tgz
Source1:        %{name}.png
Patch0:         xdiskusage-1.51-mga-optflags.patch
Patch1:         xdiskusage-1.51-mga-nostrip.patch
BuildRequires:  fltk-devel

%description
xdiskusage is a user-friendly program to show you what is using up all
your disk space. It is based on the design of xdu written by Phillip C.
Dykstra. Changes have been made so it runs "du" for you, and can display
the free space left on the disk, and produce a PostScript version of
the display.

%prep
%setup -q
sed -i 's|-Wall|-Wall -fPIE|' configure* Makefile*

%build
autoreconf -vfi
%configure
%make_build

%install
%makeinstall
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=XDiskUsage
GenericName=Disk usage visualizer
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Categories=FileTools;Monitor;
Type=Application
EOF

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.52
- Rebuilt for Fedora
* Mon Nov 30 2015 akien <akien> 1.51-1.mga6
+ Revision: 907390
- Prevent debuginfo stripping
- imported package xdiskusage
