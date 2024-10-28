Summary:        An X Window System kernel parameter monitoring tool
Name:           xsysinfo
Version:        1.7
Release:        23
License:        MIT
Group:          Monitoring
Source0:        ftp://sunsite.unc.edu/pub/Linux/system/status/xstatus/xsysinfo-%{version}.tar.xz
Source1:        %{name}
Source11:       %{name}-16x16.png
Source12:       %{name}-32x32.png
Source13:       %{name}-48x48.png
Patch0:         xsysinfo-1.7-imake.patch
Patch1:         xsysinfo-1.7-xf4.patch
Patch2:         xsysinfo-1.7-includes.patch
BuildRequires:  imake
BuildRequires:  libX11-devel
BuildRequires:  Xaw3d-devel
BuildRequires:  libXt-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXp-devel

%description
Xsysinfo is a graphic kernel monitoring tool for the X Window System.
Xsysinfo displays vertical bars for certain kernel parameters:  CPU load
average, CPU load, memory and swap sizes.

Install the xsysinfo package if you'd like to use a graphical kernel
monitoring tool.

%prep
%setup -q
%patch 0 -p1
%patch 1 -p0
%patch 2 -p1 -b .includes
make clean

%build
xmkmf
make CDEBUGFLAGS="%optflags" EXTRA_LDOPTIONS="%optflags"

%install
rm -rf $RPM_BUILD_ROOT
%make_install

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Xsysinfo
Comment=System information
Exec=%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=System;Monitor;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

rm -f $RPM_BUILD_ROOT/%{_prefix}/lib/X11/app-defaults

%files
%doc README CHANGES
%{_bindir}/xsysinfo
%config(noreplace) %{_datadir}/X11/app-defaults/XSysinfo
%config(noreplace) %{_datadir}/X11/app-defaults/XSysinfo-color
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Sun May 9 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7
- Rebuilt for Fedora
* Sun May 02 2021 tex - 1.7-23pclos2021
- rebuild against updates
* Sun May 05 2019 tex - 1.7-22pclos2019
- rebuild against updates
* Sat May 14 2011 Texstar <texstar at gmail.com> 1.7-21pclos2011
- update for new xorg server
