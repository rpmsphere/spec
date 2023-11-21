%undefine _debugsource_packages

Summary: Screensaver with flying gopher
Name: gophersaver
Version: 0.20191126
Release: 1
License: MIT
Group: X11/Utilities
Source: %{name}-master.zip
URL: https://github.com/vasyahuyasa/gophersaver
BuildRequires: SDL2_image-devel

%description
Gophersaver is screensaver programm with flying gophers in space.

%prep
%setup -q -n %{name}-master
sed -i 's|-Werror ||' Makefile

%build
make

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc LICENSE README.md
%{_bindir}/%{name}

%changelog
* Thu Dec 19 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20191126
- Rebuilt for Fedora
