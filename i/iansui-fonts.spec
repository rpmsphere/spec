%global _name iansui
%define fontdir %{_datadir}/fonts/%{_name}

Name:           %{_name}-fonts
Version:        1.020
Release:        1
Summary:        An open source Chinese font derived from Klee One (Fontworks)
Source0:        https://github.com/ButTaiwan/iansui/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/ButTaiwan/iansui
BuildArch:      noarch

%description
An open source Chinese font derived from Klee One (Fontworks).

%prep
%setup -q -n %{_name}-%{version}

%build

%install
install -d %{buildroot}%{fontdir}
install -m644 fonts/ttf/*.ttf %{buildroot}%{fontdir}

%files
%doc *.txt *.md img/*
%{fontdir}/*

%changelog
* Sun Oct 12 2025 Wei-Lun Chao <bluebat@member.fsf.org> - 1.020
- Rebuilt for Fedora
