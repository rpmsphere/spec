Summary: 	Startup feedback monitor for the Matchbox Desktop
Name: 		mb-applet-startup-monitor
Version: 	0.1
Release: 	1
URL: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source0: 	http://matchbox-project.org/sources/%name/%version/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRequires:	gtk2-devel libmatchbox-devel startup-notification-devel

%description
Startup feedback monitor for the Matchbox Desktop.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install
##install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc INSTALL COPYING
%_bindir/%{name}
##%_datadir/applications/*
%_datadir/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
