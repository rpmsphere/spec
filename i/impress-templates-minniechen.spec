Name: impress-templates-minniechen
License: Public Domain
Group: Applications/Productivity
Summary: Templates by minniechen for Impress 
Version: 2007
Release: 1
URL: https://tw.class.urlifelinks.com/class/?csid=css000000017834&id=model4&cl=1157539248-7034-2912
Source: %{name}.zip
BuildArch: noarch
Requires: libreoffice-impress

%description
崇文國小陳桂美老師
提供五種簡報範本，希望對大家有助益。

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/template/zh-TW/presnt
cp *.otp $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/template/zh-TW/presnt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/libreoffice/share/template/zh-TW/presnt/*.otp

%changelog
* Mon Mar 05 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2007
- Rebuilt for Fedora
