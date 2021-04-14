%define	fontdir	%{_datadir}/fonts/wsl-tps

Summary: WSL Taiwan Phonetic Fonts
Name: wsl-tps-fonts
Version: 1.00
Release: 5.1
License: opensource
Group: User Interface/X
BuildArch: noarch
Source0: http://xiaoxue.iis.sinica.edu.tw/download/files/WSL_TPS_Font.zip
URL: http://xiaoxue.iis.sinica.edu.tw/download/WSL_TPS_Font.htm
Requires(post): fontconfig

%description
WSL Kai TPS: CC-BY-ND 3.0 Taiwan
WSL Ming TPS: Arphic Public License
WSL TPS: CC0 1.0

%prep
%setup -q -n WSL_TPS_Font

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{fontdir}
install -m 0644 */*.ttf %{buildroot}%{fontdir}

%clean
rm -rf %{buildroot}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%doc *.pdf */*.txt
%{fontdir}/*

%changelog
* Sun May 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.00
- Rebuilt for Fedora
