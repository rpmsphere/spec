%define	fontdir	%{_datadir}/fonts/rixing

Summary: RiXing TrueType Fonts
Name: rixing-fonts
Version: 1.0
Release: 2
License: free, no commercial
Group: User Interface/X
URL: https://typography.ascdc.sinica.edu.tw/
BuildArch: noarch
Source0: rx_kt0_linux.ttf
Source1: release_note.txt
Requires: fontconfig

%description
Fonts from Ri Xing Type Foundry, digitalized by 
Academia Sinica Center for Digital Cultures.
https://ascdc.sinica.edu.tw/single_news_page.jsp?newsId=1705
rx_kt0_linux.ttf is derived from v1.0 only with Kai Face,
adapted for Linux platform.

%prep
%setup -T -c

%build

%install
install -d $RPM_BUILD_ROOT%{fontdir}
install -m644 %{SOURCE0} %{SOURCE1} $RPM_BUILD_ROOT%{fontdir}

%post
fc-cache 2> /dev/null

%postun
fc-cache 2> /dev/null

%files
%{fontdir}/release_note.txt
%{fontdir}/rx_kt0_linux.ttf

%changelog
* Tue Oct 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Initial package
