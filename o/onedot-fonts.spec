%define fontdir %{_datadir}/fonts/onedot

Summary: One-dot Font Project
Name: onedot-fonts
Version: 8.10
Release: 1
License: GPLv2, GPLv3, IPA Open Font License v1.0
Group: User Interface/X
BuildArch: noarch
Source0: I.Ming-8.10.zip
Source1: https://input.foruto.com/ccc/1.font/font/I.Ngaan.zip
Source2: https://input.foruto.com/ccc/1.font/font/I.PenCrane.zip
URL: https://founder.acgvlyric.org/iu/doku.php
Requires(post): fontconfig

%description
Projects on Open Source Asian Fonts. Including:
I.Ming 8.00, I.Ming-CP 8.00, I.Ngaan 1.004, I.PenCrane 1.004

%prep
%setup -q -n I.Ming-%{version} -a 1
rm gpl-?.0.txt
unzip -q %{SOURCE2}

%build

%install
rm -rf %{buildroot}
install -d  %{buildroot}%{fontdir}
install -m644 *.ttf %{buildroot}%{fontdir}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%doc *.txt *.md
%{fontdir}/*

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 8.10
- Rebuilt for Fedora
