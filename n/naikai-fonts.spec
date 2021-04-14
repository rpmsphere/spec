Name: naikai-fonts
Summary: A free font family derived from setofont
Version: 1.31
Release: 1
Group: User Interface/X
License: Open Font License 1.1
URL: https://github.com/max32002/naikaifont
Source0: naikai-fonts-1.31.zip
BuildArch: noarch
Obsoletes: seto-fonts
Requires: fontconfig

%description
Naikai Fonts are open source chinese fonts based on Seto Fonts,
including 31933 characters and symbols.

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
* Tue Apr 28 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.31
- Rebuilt for Fedora
