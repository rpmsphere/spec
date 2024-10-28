%undefine _debugsource_packages

Name:           x9wm
Summary:        Single file version of w9wm
Version:        2013.05.13
Release:        4.1
License:        MIT
Group:          User Interface/Desktops
Source0:        %{name}-master.zip
Source1:        x9wm.desktop
URL:            https://github.com/ggprotech/x9wm
BuildRequires:  libX11-devel, libXext-devel

%description
x9wm is enhanced w9wm based on 9wm - providing small bug fixes / small binary
an easier modification and fastest remote desktop for VNC / RDP desktop
sessions for multi-admin remote administration for Windows / Linux and Mac
systems from a single remote location / interface.

%prep
%setup -q -n %{name}-master

%build
gcc -O3 x9wm.c -lX11 -lXext -o x9wm

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/xsessions/x9wm.desktop

%files
%doc README
%{_bindir}/%{name}
%{_datadir}/xsessions/%{name}.desktop

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2013.05.13
- Rebuilt for Fedora
