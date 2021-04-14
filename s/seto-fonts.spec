Name: seto-fonts
Summary: Handwriting Japanese font including JIS X 0213 kanji
Version: 6.20
Release: 7.1
Group: User Interface/X
License: Open Font License 1.1
URL: https://osdn.net/projects/setofont/
Source0: http://nchc.dl.osdn.jp/setofont/61995/setofont_v_6_20.zip
BuildArch: noarch
Requires: fontconfig

%description
Seto font is a handwriting Japanese monospaced font.
It includes JIS X 0213 kanji and also Unicode SIP (Supplementary Ideographic
Plane) kanji.

%prep
%setup -q -n setofont

%build

%install
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
iconv -f SHIFT-JIS -t utf8 readme.txt > %{buildroot}%{_datadir}/doc/%{name}/readme.txt
mkdir -p %{buildroot}%{_datadir}/fonts/seto
install -m644 *.ttf %{buildroot}%{_datadir}/fonts/seto

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%{_datadir}/doc/%{name}
%{_datadir}/fonts/seto

%changelog
* Mon Oct 24 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 6.20
- Rebuilt for Fedora
