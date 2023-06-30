%undefine _debugsource_packages

Name: light-monitor
Summary: A transparent panel with calendar
Version: 1.7
Release: 26.1
Group: Amusements/Games
License: GPL
URL: https://freecode.com/projects/light-monitor
Source0: https://www.dixsous.org/media/download/%{name}-v%{version}.tgz
BuildRequires: libX11-devel
BuildRequires: libXft-devel
BuildRequires: libXpm-devel
BuildRequires: freetype-devel
BuildRequires: libvpx-devel

%description
light-monitor is a transparent panel that depends only on X and Xft.
It comes with light-calendar, a simple, transparent, and lightweight
calendar. These two programs are written to consume the lowest possible
amount of resources.

%prep
%setup -q -n %{name}-v%{version}
sed -i 's|xft-config|pkg-config freetype2 xft x11 vpx|' makefile
sed -i -e '/extern int max/d' -e 's|max|fmax|' light-monitor.c

%build
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -m755 light-monitor light-calendar %{buildroot}%{_bindir}
install -Dm644 light-monitor.conf %{buildroot}%{_sysconfdir}/light-monitor.conf

%files
%doc README TODO gpl.txt CHANGELOG
%{_bindir}/light-monitor
%{_bindir}/light-calendar
%{_sysconfdir}/light-monitor.conf

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7
- Rebuilt for Fedora
