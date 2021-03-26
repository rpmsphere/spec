%define	fontdir	%{_datadir}/fonts/yozfontkm

Summary: Hand-writing freeware unicode fonts
Name: yozfontkm-fonts
Version: 7.01
Release: 4.1
License: SIL Open Font License
Group: User Interface/X
BuildArch: noarch
Source0: http://yozvox.web.fc2.com/YOzFontKM-7.01.7z
URL: http://yozvox.web.fc2.com/
Requires(post): fontconfig
BuildRequires: util-linux, p7zip

%description
Y.OzFont(s) is hand-writing sans-serif type of freeware unicode fonts.
Developed by Y.OzVox.

Mouhitsu -- It seems to have written this with the brush.

%prep
%setup -q -n YOzFontKM
rename .TTC .ttc *.TTC

%build

%install
install -d %{buildroot}%{fontdir}
install -m 0644 *.ttc *.ttf %{buildroot}%{fontdir}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%doc *.txt
%{fontdir}/*

%changelog
* Wed Jan 08 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 7.01
- Rebuild for Fedora
