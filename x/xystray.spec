%undefine _debugsource_packages

Name: 	 	xystray
Summary: 	A simple implementation of freedesktop.org systray specification
Version: 	1.0
Release: 	6.1
Source:		https://github.com/steelman/xystray/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL:		http://steelman.github.io/xystray/
License:	GPL
Group:		Graphical desktop/Other
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: libXaw-devel

%description
Xystray is a simple implementation of freedesktop.org systray
specification (a.k.a notification area) for XWindow system. It is meant
for use in simple desktop environments which does not provide such
facility by default eg. FVWM. It may also run under GNOME or KDE but
the default tray programme has to be disabled then.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE README
%{_bindir}/%name

%changelog
* Tue Mar 14 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
