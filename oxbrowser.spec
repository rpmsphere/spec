Name:           oxbrowser
Version:        0.2
Release:        2
Summary:        Light browser with Hand-Written by html and javascript.
Group:          Applications/Internet
License:        Commercial
URL:            http://www.ossii.com.tw/
Source0:        %{name}.tar.gz
Source1:        %{name}.png
Source2:	odokai@.ttf
BuildArch:      noarch
Requires:       oxzilla >= 0.1.1-17
Requires:       fineart >= 0.4-1
Requires:	fontconfig

%description
Light browser with Hand-Written by html and javascript.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/

mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}

cd $RPM_BUILD_ROOT%{_datadir}/
tar zxvf %{SOURCE0} 
cd -

# Bin
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat >$RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla index.htm
EOF

# Pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
%__cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/

# Desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=OX broswer
Name[zh_TW]=OX 網頁瀏覽器
Comment=Light browser with Hand-Written by html and javascript.
Comment[zh_TW]=輕巧的網頁瀏覽器，內含手寫輸入法
Categories=Network;Application;
Exec=%{name}
Terminal=false
Type=Application
Hidden=false
Icon=%{name}
EOF

# Fonts
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/opendesktop/TrueType/
%__cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/fonts/opendesktop/TrueType/

%post
%{_bindir}/fc-cache %{_datadir}/fonts 2> /dev/null

%postun
%{_bindir}/fc-cache %{_datadir}/fonts 2> /dev/null

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,root,root,0755)
%{_datadir}/%{name}/images
%{_datadir}/%{name}/inc/functions.js
%{_datadir}/%{name}/inc/include.js
%{_datadir}/%{name}/inc/config.js
%{_datadir}/%{name}/inc/drag.htm
%{_datadir}/%{name}/inc/default.js
%{_datadir}/%{name}/index.htm
%{_datadir}/%{name}/magic_hand.htm
%{_datadir}/%{name}/release.sh
%{_datadir}/%{name}/oxbrowser.css
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/inc/theme/icon/go-next.png
%{_datadir}/%{name}/inc/theme/icon/go-previous.png
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/fonts/opendesktop/TrueType/*

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Tue Nov 16 2010 Sean Lin <sean@ossii.com.tw> 0.2-2.ossii
- 增加自動高度調整
- 修正翻轉iframe的css語法錯誤
- 修正上下頁按鈕顯示問題
- 修正網址無法修改的bug

* Tue Nov 16 2010 Sean Lin <sean@ossii.com.tw> 0.2-1.ossii
- 修改外觀
- 增加上下頁按鈕
- 網址列同步顯示瀏覽頁面的網址
- 網址暫時無法修改

* Thu Aug 23 2010 Feather Mountain <john@ossii.com.tw> 0.1-3.ossii
- 增加翻轉的功能，但功能尚未完全
- 翻轉iframe
- 使用90度字型
- 圖片使用 canvas 翻轉

* Fri May 28 2010 Feather Mountain <john@ossii.com.tw> 0.1-2.ossii
- 啟動時不再全螢幕

* Wed May 19 2010 Feather Mountain <john@ossii.com.tw> 0.1-1.ossii
- Build for OSSII
