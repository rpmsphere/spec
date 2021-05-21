Name:           oxquiz
Version:        0.8
Release:        4
Summary:        Test system develop by html and javascript.
Group:          Amusements/Eduactions
License:        Commercial
URL:            http://www.ossii.com.tw/
Source0:        %{name}.tar.gz
Source1:        %{name}.png
Source2:        %{name}.xml
Source3:        %{name}-icon.png
BuildArch:      noarch
Requires:       oxzilla >= 0.1.1-17
Requires:		oxzilla-jscollections
Requires:		oxzilla-mysql
Requires:       oxim >= 1.3.1
Requires:       fuse, fuse-zip
Requires:       fineart >= 0.4-1
#Requires:	    penpower >= 0.1-4
Requires:		thai-scalable-purisa-fonts

%description
Test system develop by html and javascript.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/

mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}

cd $RPM_BUILD_ROOT%{_datadir}/
tar zxvf %{SOURCE0} 
cd -

# Mime type
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mime/packages/
%__cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/mime/packages/

# Bin
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat >$RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
oxzilla -f "full_exam.htm?quiz_path=\$1&rounds=\$2&show_ans=true"
EOF

# oxquiz_client.sh

%__cat >$RPM_BUILD_ROOT%{_bindir}/%{name}_client <<EOF
#!/bin/bash
cd %{_datadir}/%{name}
while true;
do
oxzilla -f client.htm;
sleep 1;
done
EOF

# Pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
%__cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/
%__cp %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/pixmaps/

# Desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=OX Quiz
Name[zh_TW]=OX 測驗程式
Comment=OXquiz written in OXZilla
Comment[zh_TW]=利用 OXZilla 編寫的測驗程式
Categories=Application;Education;
Exec=%{name}
Terminal=false
Type=Application
MimeType=application/x-quiz;
Hidden=false
Icon=%{name}
EOF

%post
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,root,root,0755)
%{_datadir}/%{name}/css
%{_datadir}/%{name}/images
%{_datadir}/%{name}/inc/functions.js
%{_datadir}/%{name}/inc/include.js
%{_datadir}/%{name}/inc/config.js
%{_datadir}/%{name}/inc/drag.htm
%{_datadir}/%{name}/client.htm
%{_datadir}/%{name}/dialog.htm
%{_datadir}/%{name}/draw_board.htm
%{_datadir}/%{name}/full_exam.htm
%{_datadir}/%{name}/magic_hand.htm
%{_datadir}/%{name}/for_input.htm
%{_datadir}/%{name}/release.sh
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}-icon.png
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}_client
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%attr(0777,root,root) %{_sharedstatedir}/%{name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Thu Jul 12 2010 Feather Mountain <john@ossii.com.tw> 0.8-4.ossii
- Update to 0.8-4
- 調整倒數記時的數值位置
- 最後一分鐘，顯示秒數
- 將倒數計時秒數基數獨立成總體變數，放到 config.js

* Thu Jul 12 2010 Feather Mountain <john@ossii.com.tw> 0.8-3.ossii
- Update to 0.8-3
- 修改 oxquiz-icon.png
- 增加 oxquiz/images/counts/0~9.gif﹑moo.gif 數位七段計數字型圖
- 將倒數計時秒數移除

* Thu Jul 12 2010 Feather Mountain <john@ossii.com.tw> 0.8-2.ossii
- Update to 0.8-2
- 將手寫辨識修改回 fineart

* Thu Jul 9 2010 Feather Mountain <john@ossii.com.tw> 0.8-1.ossii
- Update to 0.8-1
- 將手寫辨識修改為 penpower

* Thu Jul 8 2010 Feather Mountain <john@ossii.com.tw> 0.7-9.ossii
- Update to 0.7-9
- 將倒數計時器改回 monospace 字型
- 增加 quiz 檔格式 icon 小圖
- 手寫字型使用 purisa, 相依性增加 thai-scalable-purisa-fonts

* Wed Jun 21 2010 Feather Mountain <john@ossii.com.tw> 0.7-8.ossii
- Update to 0.7-8
- 預設讀入的顏色暫定為粉紅色 #ffbbbb

* Fri May 21 2010 Feather Mountain <john@ossii.com.tw> 0.7-7.ossii
- Update to 0.7-7
- 修正呼叫手寫板的 dom 使用方式
- 將輸入欄，英文﹑數字都改成手寫字型(因中文無手寫字型，所以中文未加入)

* Fri May 07 2010 Feather Mountain <john@ossii.com.tw> 0.7-6.ossii
- Update to 0.7-6
- 所有的 dialog button 增加onmouseover out的功能
- 修正 client 分頁錯誤
- 增加 client 分頁數提醒
- 結束交卷增加考卷張數提醒
- icon 圖套入 tiffany 製作的圖片
- 連連看，增加老師提的紅點提示

* Fri May 07 2010 Feather Mountain <john@ossii.com.tw> 0.7-5.ossii
- Update to 0.7-5
- 修正快速點二下，畫板會有bug的問題
- client 開始考試，若遇到滑鼠故障，畫面出現又消失的功能，修正
- 直式作答輸入框，功能修正

* Tue May 04 2010 Feather Mountain <john@ossii.com.tw> 0.7-4.ossii
- Update to 0.7-4
- 修正快速點二下，下一頁，會有bug的問題

* Thu Apr 27 2010 Feather Mountain <john@ossii.com.tw> 0.7-3.ossii
- Update to 0.7-3
- 查看成績全螢幕設定
- 修正點二下暫停測驗的問題

* Thu Apr 27 2010 Feather Mountain <john@ossii.com.tw> 0.7-2.ossii
- Update to 0.7-2
- 修正client開啟後，有時點選開始測驗，會出現未成型的視窗

* Thu Apr 21 2010 Feather Mountain <john@ossii.com.tw> 0.7-1.ossii
- Update to 0.7-1
- 手寫畫板﹑畫板加大
- 畫點畫筆出現一個點的問題修正
- 手寫辨識功能，畫筆按著移出視窗問題修正
- 修正 client.htm 框選畫面mask的問題
- 修正 再做一次 的內容顯示錯誤
- 修正組填的題型 作答背景色 與錯誤的圓框順序位置
- 修正離開試卷的圖示顯示錯誤
- 修正組填文字顯示，改成等寬字

* Thu Apr 07 2010 Feather Mountain <john@ossii.com.tw> 0.6-9.ossii
- Update to 0.6-9
- 離開的功能加上提示
- 連連看加上提示
- 重新測驗的功能加上提示
- 修正組填題型錯誤

* Thu Apr 01 2010 Feather Mountain <john@ossii.com.tw> 0.6-8.ossii
- Update to 0.6-8
- 資料庫無法連線自動中斷修正
- 將設錯的路徑全改寫成引用變數
- 將使用者資料設至總體變數

* Wed Mar 31 2010 Feather Mountain <john@ossii.com.tw> 0.6-7.ossii
- Update to 0.6-7
- 支援螢幕放大縮小的功能
- 修正 file selector 點開後按取消失靈

* Mon Mar 30 2010 Feather Mountain <john@ossii.com.tw> 0.6-6.ossii
- Update to 0.6-6
- 修正點二下 quiz 檔案，就可以測驗的功能
- 將 demo 檔分到 oxquiz-demos 
- 加入 file selector 功能
- 新的選單小icon
- 加入 shell script 使 oxquiz_client 被關閉後又會馬上開啟

* Fri Mar 26 2010 Feather Mountain <john@ossii.com.tw> 0.6-5.ossii
- Update to 0.6-5
- 加入了華麗的換頁效果
- 套用 Tiffany 新設計的版面
- 換頁的上一頁﹑下一頁顯示調整
- 增加一個 demo quiz 檔，羽山的國文測驗.quiz

* Thu Mar 25 2010 Feather Mountain <john@ossii.com.tw> 0.6-4.ossii
- Update to 0.6-4
- 增加直書 demo 羽山的直書考卷
- 修正畫板畫筆的粗細，全改成2px
- 增加直書功能
- 使用輔助對話框的功能完成
- 座號不使用直書功能
- 增加 for_input.htm (輔助輸入法)


* Wed Mar 24 2010 Feather Mountain <john@ossii.com.tw> 0.6-3.ossii
- Update to 0.6-3
- 修改使瀏覽答案的功能正常
- 移除忘記拿掉的 require include

* Mon Mar 22 2010 Feather Mountain <john@ossii.com.tw> 0.6-2.ossii
- Update to 0.6-2
- client.htm 的最後一次測驗成績將可以重新瀏覽測驗結果
- 支援中文路徑

* Mon Mar 22 2010 Feather Mountain <john@ossii.com.tw> 0.6-1.ossii
- Update to 0.6-1
- client.htm 套版
- client.htm 增加分頁功能
- 所有的include改使用oxzilla system_include
- 修正demo裡面舊版的demo資料，已從資料庫重匯
- 將 switch.htm 移到 gdm-init-oxquiz 套件
- 修正 client.htm 按下開始後文字的顏色
- 修正 浮動移動功能，使用jquery 無法畫畫的功能

* Thu Mar 18 2010 Feather Mountain <john@ossii.com.tw> 0.5-16.ossii
- Update to 0.5-16
- 增加答案用色塊選擇器

* Tue Mar 11 2010 Feather Mountain <john@ossii.com.tw> 0.5-15.ossii
- Update to 0.5-15
- 將IO的工作全移到 /dev/shm 操作
- 修正填充﹑連連看的題型，分格符號改成使用∥
- 瀏覽答案的功能，圖片寬度若小於350px，就設成350px

* Tue Mar 02 2010 Feather Mountain <john@ossii.com.tw> 0.5-14.ossii
- Update to 0.5-14
- 修正圈選的function
- ADD switch.htm, oxquiz_switch.sh, :0

* Tue Feb 23 2010 Feather Mountain <john@ossii.com.tw> 0.5-13.ossii
- Update to 0.5-13
- 修改 myQuery 的使用方式，使之穩定加速
- 增加Desktop給小朋友用
- 暫時先把看答案的功能啟用
- 顯示答案增加關閉的按鈕
- 將大部分的功能連結，加上滑鼠按鈕的手勢

* Sun Feb 07 2010 Feather Mountain <john@ossii.com.tw> 0.5-12.ossii
- Update to 0.5-12
- Fix upload to mysql etime bug.
- Fix class_name display.

* Fri Feb 05 2010 Feather Mountain <john@ossii.com.tw> 0.5-11.ossii
- Update to 0.5-11
- 修正 client.htm 列表的內容

* Fri Feb 05 2010 Feather Mountain <john@ossii.com.tw> 0.5-10.ossii
- Update to 0.5-10
- 修正結束交卷連點造成的重覆交卷
- 修正寫入 mysql 資料庫日期格式的錯誤

* Fri Feb 05 2010 Feather Mountain <john@ossii.com.tw> 0.5-9.ossii
- Update to 0.5-9

* Fri Feb 05 2010 Feather Mountain <john@ossii.com.tw> 0.5-8.ossii
- Update to 0.5-8
- client 裡抓取使用者 ID 的錯誤, again

* Fri Feb 05 2010 Feather Mountain <john@ossii.com.tw> 0.5-7.ossii
- Update to 0.5-7
- client 裡抓取使用者 ID 的錯誤

* Fri Feb 05 2010 Feather Mountain <john@ossii.com.tw> 0.5-6.ossii
- Update to 0.5-6
- 修正 oxquiz.sh 裡的 & 多了個 \

* Fri Feb 05 2010 Feather Mountain <john@ossii.com.tw> 0.5-5.ossii
- Update to 0.5-5
- 使用者可以在 client.htm 看到最後一次自己測驗的成績

* Fri Feb 05 2010 Feather Mountain <john@ossii.com.tw> 0.5-4.ossii
- Update to 0.5-4
- 若從 client.htm 進入測驗系統，增加資料上傳的功能
- 修正測驗系統 USER NAME 的問題

* Fri Feb 05 2010 Feather Mountain <john@ossii.com.tw> 0.5-3.ossii
- Update to 0.5-3
- Client.htm 重寫
- 修正連連看若無作答時只顯示一個錯誤圈的問題
- 增加解答的功能，參數為 show_ans=true, from_client
- 修改 desktop 內容
- 增加 function canvas_small, 分頁 function
- 修正 magic_hand.htm 裡面資料重載的功能，使程式可以加快一些速度，但未來若要引用，要記得加上不足的函式
- 將使用者儲存的資料統一全放到 /var/lib/oxquiz/

* Tue Feb 03 2010 Feather Mountain <john@ossii.com.tw> 0.5-2.ossii
- Update to 0.5-2
- Not finish yet

* Tue Feb 02 2010 Feather Mountain <john@ossii.com.tw> 0.5-1.ossii
- Support oxzilla-mysql plugins.
- Support switch (mysql or sqlite) design.

* Tue Feb 02 2010 Feather Mountain <john@ossii.com.tw> 0.4-13.ossii
- Fix file_get_contents
- Remove do agin button

* Wed Jan 28 2010 Feather Mountain <john@ossii.com.tw> 0.4-12.ossii
- Fix client logout when usin LXDE window manager.

* Wed Jan 28 2010 Feather Mountain <john@ossii.com.tw> 0.4-11.ossii
- Fix quit exam.

* Wed Jan 27 2010 Feather Mountain <john@ossii.com.tw> 0.4-10.ossii
- Update to 0.4-10
- Remove mysql password from /usr/share/oxquiz/shells/inc/conn.php.
- Fix desktop comment.

* Mon Jan 25 2010 Feather Mountain <john@ossii.com.tw> 0.4-9.ossii
- Update to 0.4-9
- Fix name,class,site_number field.

* Mon Jan 25 2010 Feather Mountain <john@ossii.com.tw> 0.4-8.ossii
- Update to 0.4-8
- Preset fullscreen (1024x768).
- Fix attribs.
- Fix import db slow problem.

* Mon Jan 25 2010 Feather Mountain <john@ossii.com.tw> 0.4-7.ossii
- Update to 0.4-7
- Add client.htm

* Mon Jan 18 2010 Feather Mountain <john@ossii.com.tw> 0.4-6.ossii
- Update jQuery to 1.4
- While exam pictures more than 1, prePage and nextPage images will display.

* Tue Jan 12 2010 Feather Mountain <john@ossii.com.tw> 0.4-5.ossii
- Fix quiz demos SQL injection problem.

* Fri Jan 08 2010 Feather Mountain <john@ossii.com.tw> 0.4-4.ossii
- Fix umount problem while exam quit.

* Wed Jan 06 2010 Feather Mountain <john@ossii.com.tw> 0.4-3.ossii
- Fix codereference bug.

* Tue Jan 05 2010 Feather Mountain <john@ossii.com.tw> 0.4-2.ossii
- Add quiz demos

- Build for OSSII
* Tue Jan 05 2010 Feather Mountain <john@ossii.com.tw> 0.4-1.ossii
- Complete "matching" and fixed codereference performance.
- Build for OSSII

* Fri Dec 21 2009 Feather Mountain <john@ossii.com.tw> 0.3-2.ossii
- Complete 80 percent exam templetes. 

* Mon Dec 21 2009 Feather Mountain <john@ossii.com.tw> 0.3-1.ossii
- Add USER Location DB,images place.

* Fri Dec 11 2009 Feather Mountain <john@ossii.com.tw> 0.2-1.ossii
- Add check exam in full_exam.htm

* Mon Dec 7 2009 Feather Mountain <john@ossii.com.tw> 0.1-1.ossii
- Build for OSSII
