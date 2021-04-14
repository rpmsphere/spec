%define	fontdir	%{_datadir}/fonts/tcrc-bodyig

Name:          tcrc-bodyig-fonts
Version:       2010
Release:       4.1
Summary:       Tibetan fonts from TCRC
License:       freeware
Group:         System/X11/Fonts
URL:           https://www.tibetangeeks.com/downloads/bodyig/TCRC-BodYig-unicode-2010/
Source0:       %{name}.zip
BuildArch:     noarch

%description
These are the latest TCRC fonts, and the only fonts from TCRC that are fully Unicode.

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
* Tue Oct 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2010
- Rebuilt for Fedora
