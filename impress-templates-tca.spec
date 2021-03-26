Name: impress-templates-tca
License: free software
Group: Applications/Productivity
Summary: Templates from TCA for Impress 
Version: 2007
Release: 1
URL: http://taiwan-linux.tca.org.tw/news1.php?id=13
Source: %{name}.zip
BuildArch: noarch
Requires: libreoffice-impress

%description
第一屆簡報範本設計大賽社會組得獎作品：
資訊未來大自由(孫賜萍)、蒲公英(蔡凱如)、綠色圓圈(鐘祥仁)

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
- Rebuild for Fedora
