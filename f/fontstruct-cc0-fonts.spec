%define fontdir %{_datadir}/fonts/fontstruct-cc0

Name:           fontstruct-cc0-fonts
Version:        2021.11
Release:        1
Summary:        Public Domain Fonts from fontstruct.com
License:        CC0
Group:          System/X11/Fonts
URL:            https://fontstruct.com
Source0:        %{name}.zip
BuildArch:      noarch

%description
https://fontstruct.com/fontstructions/show/617978/mandrill_2
https://fontstruct.com/fontstructions/show/1989435/tekmedia
https://fontstruct.com/fontstructions/show/1046703/gothic_fractura_simplex
https://fontstruct.com/fontstructions/show/1758288/masoneer
https://fontstruct.com/fontstructions/show/1599681/marrada-1
https://fontstruct.com/fontstructions/show/1619775/black-butterfly
https://fontstruct.com/fontstructions/show/1917126/baardusan
https://fontstruct.com/fontstructions/show/1611040/laconica

%prep
%setup -q -c

%build

%install
install -d %{buildroot}%{fontdir}
install -m644 *.ttf %{buildroot}%{fontdir}

%files
%doc *.txt
%{fontdir}/*

%changelog
* Sun Nov 7 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2021.11
- Rebuilt for Fedora
