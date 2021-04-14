Name: gatotray
Summary: Graphical CPU stats monitor in the system tray
Version: 3.3
Release: 2.1
Group: Accessories
License: Free Software
URL: https://bitbucket.org/gatopeich/gatotray
Source0: %{name}-v%{version}.tar.bz2
BuildRequires: gtk2-devel

%description
gatotray is a tiny CPU monitor displaying several stats graphically (usage,
temperature, frequency) in small space, and tight on resources. Since version
3.0, It can also run as a screensaver.

%prep
%setup -q -n %{name}

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
install -Dm644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Mon Jul 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.3
- Rebuilt for Fedora
