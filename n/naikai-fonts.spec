Name: naikai-fonts
Summary: A free font family derived from setofont
Version: 1.89
Release: 1
Group: User Interface/X
License: Open Font License 1.1
URL: https://github.com/max32002/naikaifont
Source0: naikai-fonts-%{version}.tar.xz
BuildArch: noarch
Obsoletes: seto-fonts
Requires: fontconfig

%description
Naikai Fonts are open source chinese fonts based on Seto Fonts,
including 47417 characters and symbols.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/naikai
install -m644 *.ttf %{buildroot}%{_datadir}/fonts/naikai

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%doc README.md SIL_Open_Font_License_1.1.txt naikaifont_history.md
%{_datadir}/fonts/naikai

%changelog
* Sun Jan 15 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.89
- Rebuilt for Fedora
