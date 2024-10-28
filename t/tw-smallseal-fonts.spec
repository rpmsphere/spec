%define fontdir %{_datadir}/fonts/tw-smallseal

Summary: Taiwan TrueType Fonts -- Small-Seal Face
Name: tw-smallseal-fonts
Version: 92.7
Release: 5
License: BSD-like
Group: User Interface/X
URL: https://www.cns11643.gov.tw/AIDB/download.do?name=%E5%AD%97%E5%9E%8B%E4%B8%8B%E8%BC%89
BuildArch: noarch
Source0: https://www.cns11643.gov.tw/AIDB/file.do?path=download/%E5%AD%97%E5%9E%8B%E4%B8%8B%E8%BC%89%601q%60%E8%AA%AA%E6%96%87%E8%A7%A3%E5%AD%97True%60w%60Type%E5%AD%97%E5%9E%8B/name/ebas927.ttf
Source1: %name.LICENSE
Requires: fontconfig

%description
Chinese TTF Fonts applied by www.cns11643.gov.tw
License see: https://www.cns11643.gov.tw/AIDB/copyright.do

%prep

%build

%install
%__install -d $RPM_BUILD_ROOT%{fontdir}
%__install -m644 %{SOURCE0} $RPM_BUILD_ROOT%{fontdir}
%__install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{fontdir}/LICENSE

%post
fc-cache 2> /dev/null

%postun
fc-cache 2> /dev/null

%files
%{fontdir}

%changelog
* Mon Feb 10 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 92.7
- initial package
