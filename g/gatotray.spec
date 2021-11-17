Name: gatotray
Summary: Graphical CPU stats monitor in the system tray
Version: 4.0
Release: beta.4
Group: Accessories
License: Free Software
URL: https://bitbucket.org/gatopeich/gatotray
Source0: %{name}-%{version}-%{release}.tar.gz
BuildRequires: gtk2-devel

%description
gatotray is a tiny CPU monitor displaying several stats graphically (usage,
temperature, frequency) in small space, and tight on resources. Since version
3.0, It can also run as a screensaver.

%prep
%setup -q -n %{name}-%{version}-%{release}

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
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0-beta.4
- Rebuilt for Fedora
