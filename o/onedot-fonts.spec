%define	fontdir	%{_datadir}/fonts/onedot

Summary: One-dot Font Project
Name: onedot-fonts
Version: 2022
Release: 1
License: GPLv2, GPLv3, IPA Open Font License v1.0
Group: User Interface/X
BuildArch: noarch
Source0: https://github.com/ichitenfont/I.Ming/raw/master/8.00/I.Ming-8.00.ttf
Source1: https://github.com/ichitenfont/I.Ming/raw/master/8.00/I.MingCP-8.00.ttf
Source2: https://input.foruto.com/ccc/1.font/font/I.Ngaan.zip
Source3: https://input.foruto.com/ccc/1.font/font/I.PenCrane.zip
Source4: https://github.com/ichitenfont/I.Ming/raw/master/8.00/IPA_Font_License_Agreement_v1.0.md
Source5: https://github.com/ichitenfont/I.Ming/raw/master/8.00/readme.md
URL: https://founder.acgvlyric.org/iu/doku.php
Requires(post): fontconfig

%description
Projects on Open Source Asian Fonts. Including:
I.Ming 8.00, I.Ming-CP 8.00, I.Ngaan 1.004, I.PenCrane 1.004

%prep
%setup -q -T -c -a 2
rm gpl-*.txt
unzip -q %{SOURCE3}
cp %{SOURCE4} %{SOURCE5} .

%build

%install
rm -rf %{buildroot}
install -Dm644 %{SOURCE0} %{buildroot}%{fontdir}/I.Ming.ttf
install -Dm644 %{SOURCE1} %{buildroot}%{fontdir}/I.MingCP.ttf
install -m644 I.PenCrane-B.ttf I.Ngaan.ttf %{buildroot}%{fontdir}

%clean
rm -rf %{buildroot}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%doc *.txt *.md
%{fontdir}/*

%changelog
* Sun Nov 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2022
- Rebuilt for Fedora
