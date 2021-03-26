Name: impress-templates-gp
License: free software
Group: Applications/Productivity
Summary: Templates from Gold-Penguin for Impress 
Version: 2008
Release: 1
URL: http://taiwan-linux.tca.org.tw/GP-prize/
Source: %{name}.zip
BuildArch: noarch
Requires: libreoffice-impress

%description
第六屆 Linux 黃金企鵝簡報範本設計得獎作品：
第一名 洪晉敬 藍天白雲
第二名 孫賜萍 熱氣球
第三名 陳智群 海鷗

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
* Mon Mar 05 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2008
- Rebuild for Fedora
