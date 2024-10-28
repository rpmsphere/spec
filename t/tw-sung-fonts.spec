%define fontdir %{_datadir}/fonts/tw-sung

Summary: Taiwan TrueType Fonts -- Sung Face
Name: tw-sung-fonts
Version: 98.1
Release: 4
License: BSD-like
Group: User Interface/X
URL: https://data.gov.tw/node/5961
BuildArch: noarch
Source0: %{name}-%{version}.zip
Requires: fontconfig

%description
Chinese TTF Fonts applied by www.cns11643.gov.tw
License see: https://www.cns11643.gov.tw/AIDB/copyright.do

TW-Sung-98_1.ttf, TW-Sung-Ext-B-98_1.ttf, TW-Sung-Plus-98_1.ttf
are from https://www.cns11643.gov.tw/AIDB/Open_Data.zip with

%prep
%setup -q -c

%build

%install
install -d $RPM_BUILD_ROOT%{fontdir}
install -m644 *.ttf $RPM_BUILD_ROOT%{fontdir}

%post
fc-cache 2> /dev/null

%postun
fc-cache 2> /dev/null

%files
%doc *.txt
%{fontdir}

%changelog
* Mon Aug 10 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 98.1
- Initial package
