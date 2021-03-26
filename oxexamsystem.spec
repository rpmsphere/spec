Name:           oxexamsystem
Version:        0.2
Release:        8
Summary:        Quiz create system develop by html and javascript.
Group:          Amusements/Eduactions
License:        Commercial
URL:            http://www.ossii.com.tw/
Source0:        exam.tar.gz
Requires:       zip mysql php-mysql php-gd ImageMagick httpd php-mbstring php-xml php-pdo mysql mysql-server
Requires:       %{name}-include = %{version}-%{release}

%description
Quiz create system develop by html and javascript..

%package include
Summary:        Include files.
Group:          System/Internationalization
License:        adobe(BSD,LGPL), iepngfix.htc(BSD,LGPL), jquerys (GPL,MIT), colorbox(MIT)
Requires:       %{name} = %{version}-%{release}


%description include
Include files.

%prep
%setup -q -c exam

%build
rm -rf $RPM_BUILD_ROOT
myPWD=$PWD
cd exam/shells
%{__make} TARGETFLAGS="" %{?_smp_mflags}
cd $myPWD

%install
mkdir -p $RPM_BUILD_ROOT%{_var}/www/html
cp -a exam $RPM_BUILD_ROOT%{_var}/www/html

# install 404 dummy.gif
mkdir -p $RPM_BUILD_ROOT%{_var}/www/error
cp -f exam/images/dummy.gif $RPM_BUILD_ROOT%{_var}/www/error/

%post
groupadd students
chown root:root %{_var}/www/html/exam/shells/user_add %{_var}/www/html/exam/shells/user_del
chmod 4755 %{_var}/www/html/exam/shells/user_add %{_var}/www/html/exam/shells/user_del
mysql -u root < %{_var}/www/html/exam/db/oxquiz.sql
# 清空使用者的紀錄
mysql -u root < %{_var}/www/html/exam/db/delete.sql

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0777,apache,apache,0777)
%{_var}/www/error/dummy.gif
%{_var}/www/html/exam/*.php
%{_var}/www/html/exam/allpoweroff.htm
%{_var}/www/html/exam/db
%{_var}/www/html/exam/images
%{_var}/www/html/exam/teacher_mark_files
%attr(4755,root,root) %{_var}/www/html/exam/shells
%{_var}/www/html/exam/release.sh
%{_var}/www/html/exam/*.csv
%{_var}/www/html/exam/doc

%attr(0777,apache,apache) %{_var}/www/html/exam/.htaccess
%attr(0777,apache,apache) %{_var}/www/html/exam/uploads
%attr(0777,apache,apache) %{_var}/www/html/exam/pdf_convert
%attr(0777,apache,apache) %{_var}/www/html/exam/download_tmp

%files include
%defattr(0777,apache,apache,0777)
%{_var}/www/html/exam/inc

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Fri Jun 11 2010 Feather Mountain <john@ossii.com.tw> 0.2-8.ossii
- Update to 0.2-8
- 加入 gettime.php
- 文件更新為 sopv4

* Tue Jun 1 2010 Feather Mountain <john@ossii.com.tw> 0.2-7.ossii
- Update to 0.2-7
- 增加玉田吳老師指定的統計計算資料表

* Tue May 21 2010 Feather Mountain <john@ossii.com.tw> 0.2-6.ossii
- Update to 0.2-6
- 增加老師批改功能

* Tue May 04 2010 Feather Mountain <john@ossii.com.tw> 0.2-5.ossii
- Update to 0.2-5
- 增加 Kami 出的最新題目測驗
- 修正組填裡迴圈使用的值
- 修正連連看的顯示問題

* Tue Apr 27 2010 Feather Mountain <john@ossii.com.tw> 0.2-4.ossii
- Update to 0.2-4
- 修改 student.php 將shell 指令分成二部分
- 增加集體關機 shell script 檔於 shells 裡(shutdown-allclients.sh)
- 增加給 oxzilla 用的 allpoweroff.htm
- 增加考卷批改功能(未完成)

* Tue Apr 13 2010 Feather Mountain <john@ossii.com.tw> 0.2-3.ossii
- Update to 0.2-3
- 增加玉田老師出的一份考卷

* Thu Apr 01 2010 Feather Mountain <john@ossii.com.tw> 0.2-2.ossii
- Update to 0.2-2
- 修正目錄讀取權限的問題
- shells/useradd.c﹑user_del.c 加上 pxe YP (Rickz的環境)

* Tue Mar 30 2010 Feather Mountain <john@ossii.com.tw> 0.2-1.ossii
- Update to 0.2-1
- package全部加上分頁的功能
- 統計資料，加上瀏覽學生的成績的功能
- 表格顏色分列加上顏色
- 測驗卷各回問答設定左邊題目列表加上題目類型
- 統計資料加上「匯出」﹑「列印」功能
- 統計資料列表內容值最後一欄輸出資料修正
- 將每份考卷的權限分離，各老師自己出題只能看到自己的考卷
- 「填充題」﹑「連連看」答案分格符號改用較特殊的分格雙線取代原本的半型逗號
- 畫面美觀調整
- 頁面連結頁數增加至 5 頁
- 必填欄位顏色﹑符號醒目提醒
- 圖片增加框線
- 測驗時間增加選項
- 可以瀏覽成績，並有列印的功能  
- package.php﹑舉辦考試﹑統計資料加上創建人的名字
- 統計資料也只能顯示自己舉辦考試的結果
- 統計資料﹑資料統計表格修改
- 瀏覽成績時，還可以看正確答案
- 刪除測驗卷修改成直接刪除
- 將灰階的效果加回去
- 修正 package_dump 多人使用時的bug，也減少容量的浪費，將自動回收不需要的空間
- 修正package_info.php輸入重覆名稱的問題
- 舉辦考試時，只能看到自己建立的考卷
- 連連看的題型修正
- 列印的功能將表頭字體變小
- 列印改成tiffany新製的小圖
- 填充答案支援|分格功能
- 填充說明修改
- 移除本測驗系統所有非使用的套件﹑檔案

* Tue Mar 09 2010 Feather Mountain <john@ossii.com.tw> 0.1-10.ossii
- Update to 0.1-10
- 增加 瀏覽器造訪限制
- 增加 .htaccess 檔﹑dummy.gif 修正 ie 404 bug
- 增加 sop.pdf 操作說明檔

* Mon Feb 23 2010 Feather Mountain <john@ossii.com.tw> 0.1-9.ossii
- Update to 0.1-9
- 修正 delete.sql
- 修正 oxexamsystem.spec 增加 groupadd students
- 統計資料的欄位互調

* Sun Feb 07 2010 Feather Mountain <john@ossii.com.tw> 0.1-8.ossii
- Update to 0.1-8
- 統計資料完成
- 增加一個將秒數轉成時間的function

* Wed Feb 05 2010 Feather Mountain <john@ossii.com.tw> 0.1-7.ossii
- Update to 0.1-7
- 增加移除使用者記錄的 sql 檔

* Wed Feb 05 2010 Feather Mountain <john@ossii.com.tw> 0.1-6.ossii
- Update to 0.1-6
- 移所考試資料，使資料庫乾淨，僅留一份可以測到 2017 年的考卷

* Wed Feb 05 2010 Feather Mountain <john@ossii.com.tw> 0.1-5.ossii
- Update to 0.1-5

* Wed Feb 03 2010 Feather Mountain <john@ossii.com.tw> 0.1-4.ossii
- Update to 0.1-4

* Mon Jan 28 2010 Feather Mountain <john@ossii.com.tw> 0.1-3.ossii
- Update to 0.1-3

* Mon Jan 28 2010 Feather Mountain <john@ossii.com.tw> 0.1-2.ossii
- Update to 0.1-2
- Remove alerts
- Add pkill in students.php
- Build for OSSII

* Mon Jan 27 2010 Feather Mountain <john@ossii.com.tw> 0.1-1.ossii
- Build for OSSII


