%define	fontdir	%{_datadir}/fonts/onedot

Summary: One-dot Font Project
Name: onedot-fonts
Version: 2021
Release: 1
License: GPLv2, GPLv3, IPA Open Font License v1.0
Group: User Interface/X
BuildArch: noarch
Source0: https://github.com/ichitenfont/I.Ming/raw/master/7.01/I.Ming-7.01.ttf
Source1: http://input.foruto.com/ccc/1.font/font/I.Ngaan.zip
Source2: http://input.foruto.com/ccc/1.font/font/I.PenCrane.zip
Source3: https://github.com/ichitenfont/I.Ming/raw/master/7.01/I.MingCP-7.01.ttf
Source4: https://github.com/ichitenfont/I.Ming/raw/master/7.01/IPA_Font_License_Agreement_v1.0.md
Source5: https://github.com/ichitenfont/I.Ming/raw/master/7.01/readme.md
URL: http://founder.acgvlyric.org/iu/doku.php
Requires(post): fontconfig

%description
Projects on Open Source Asian Fonts. Including:
I.Ming 7.01, I.Ming-CP 7.01, I.Ngaan 1.004, I.PenCrane 1.004

%prep
%setup -q -T -c -a 1
rm gpl-*.txt
unzip -q %{SOURCE2}
cp %{SOURCE4} %{SOURCE5} .

%build

%install
rm -rf %{buildroot}
install -Dm644 %{SOURCE0} %{buildroot}%{fontdir}/I.Ming.ttf
install -Dm644 %{SOURCE3} %{buildroot}%{fontdir}/I.MingCP.ttf
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
* Thu Feb 25 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2021
- Rebuilt for Fedora
