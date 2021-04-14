%undefine _debugsource_packages

Summary:	Minimal X display lock program
Name:		xtrlock
Version:	2.13
Release:	1
Group:		Graphical desktop/Other
BuildRequires:	libX11-devel
BuildRequires:	imake
License:	GPLv2+
URL:		https://salsa.debian.org/debian/xtrlock
Source0:	%{name}_%{version}.tar.xz

%description
xtrlock is a very minimal X display lock program, which uses nothing
except the Xlib library. It doesn't obscure the screen, it is
completely idle while the display is locked and you don't type at it,
and it doesn't do funny things to the X access control lists. 

%prep
%setup -q

%build
xmkmf -a
make CFLAGS="%{optflags} -DSHADOW_PWD" xtrlock

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 xtrlock %{buildroot}%{_bindir}/%{name}
install -m 644 xtrlock.man %{buildroot}%{_mandir}/man1/%{name}.1x

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Xtrlock
Comment=X terminal lock
Exec=%{name} 
Icon=gnome-lockscreen
Terminal=false
Type=Application
StartupNotify=true
Categories=System;
EOF

%clean
rm -rf %{buildroot}

%files
%doc debian/README.Debian GPL-3.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Jul 23 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2.13
- Rebuilt for Fedora
* Mon Sep 21 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.0-2mdv2010.0
+ Revision: 446272
- rebuild
* Wed Dec 24 2008 Adam Williamson <awilliamson@mandriva.org> 2.0-1mdv2009.1
+ Revision: 318409
- buildrequires imake
- import xtrlock
