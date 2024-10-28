%define fontdir %{_datadir}/fonts/monlam-bodyig

Name:           monlam-bodyig-fonts
Version:        3
Release:        5.1
Summary:        Tibetan fonts by Lobsang Monlam
License:        GPL
Group:          System/X11/Fonts
URL:            https://www.tibetangeeks.com/geeks/lobsang_monlam/
Source0:        https://www.tibetangeeks.com/downloads/bodyig/Monlam-lobsangmonlam/Monlam_bodyig-v.%{version}_fonts_only.zip
Source1:        https://www.tibetangeeks.com/downloads/bodyig/Monlam-lobsangmonlam/monlam-info.txt
BuildArch:      noarch

%description
Lobsang Monlam, a monk from Sera Mey monastery in southern India,
has created a large set of beautiful Tibetan fonts.
Version 3 is all Unicode; previous versions are not.

%prep
%setup -q -n Monlam_bodyig-v.%{version}-fonts_only
cp %{SOURCE1} .

%build

%install
install -d %{buildroot}%{fontdir}
install -m644 *.ttf %{buildroot}%{fontdir}

%files
%doc monlam-info.txt
%{fontdir}/*

%changelog
* Fri Oct 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3
- Rebuilt for Fedora
