Summary:        Zinnia Handwriting Recognition Models for Tegaki
Name:           tegaki-models
Version:        0.3
Release:        1
License:        GPLv2+
Group:          System/Internationalization
Source0:        https://www.tegaki.org/releases/0.3/models/tegaki-zinnia-japanese-0.3.zip
Source1:        https://www.tegaki.org/releases/0.3/models/tegaki-zinnia-simplified-chinese-0.3.zip
Source2:        https://www.tegaki.org/releases/0.3/models/tegaki-zinnia-traditional-chinese-0.3.zip
URL:            https://www.tegaki.org/
BuildArch:      noarch
Requires:       tegaki

%description
Zinnia Handwriting Recognition Models for Tegaki.
Including Japanese, Simplified Chinese, Traditional Chinese.

%prep
%setup -q -c -a 1 -a 2
sed -i 's|/usr/local|%{buildroot}/usr|' */Makefile
sed -i 's/繁/繁中/' tegaki-zinnia-traditional-chinese-0.3/handwriting-zh_TW.meta
sed -i 's/中/簡中/' tegaki-zinnia-simplified-chinese-0.3/handwriting-zh_CN.meta
sed -i 's/日/日文/' tegaki-zinnia-japanese-0.3/handwriting-ja.meta

%build

%install
rm -rf %{buildroot}
make install -C tegaki-zinnia-japanese-0.3
make install -C tegaki-zinnia-simplified-chinese-0.3
make install -C tegaki-zinnia-traditional-chinese-0.3

%files
%{_datadir}/tegaki/models

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Tue Feb 09 2010 Feather Mountain <john@ossii.com.tw> 0.2-3.git20090918.ossii
- Fix tegaki requires tegaki-models
* Tue Nov 17 2009 Feather Mountain <john@ossii.com.tw> 0.2-2.git20090918.ossii
- Add patch for support Fineart model
- Add meta for Fineart model zh_TW
* Fri Sep 25 2009 Feather Mountain <john@ossii.com.tw> 0.2-1.git20090918.ossii
- Update to 20090918
* Mon Apr 20 2009 Feather Mountain <john@ossii.com.tw> 0.1-2.git20090421.ossii
- Rebuild for OSSII
- Add patch for support Penpower model
- Add meta for Penpower model zh_TW
- Update to 20090421
* Tue Mar 24 2009 Wei-Lun Chao <bluebat@member.fsf.org> 0.1-1.git20090324.ossii
- Rebuild for OSSII
* Sun Feb 15 2009 Funda Wang <fundawang@mandriva.org> 0.1-1mdv2009.1
+ Revision: 340630
- BR python
- import tegaki
