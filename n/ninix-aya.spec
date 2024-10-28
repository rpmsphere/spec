Summary: DeskTop mascot for X
Name: ninix-aya
Version: 5.0.9
Release: 1
License: GPL2
Group: Amusements/Games
Source: https://downloads.sourceforge.jp/ninix-aya/36866/ninix-aya-%{version}.tgz
URL: https://ninix-aya.sourceforge.jp/
Vendor: NISHIJIMA Akira <nisshi@mb.infoweb.ne.jp>
Requires: rubypick ruby rubygem-gtk3
Obsoletes: ninix-dv ninix
Provides: ninix = 0.8
BuildArch: noarch

%description
DeskTop mascot for X.

%description -l ja
Windows用デスクトップマスコット「何か/伺か」のX Window System用互換環境
ninixの機能拡張版ninix-ayaの開発プロジェクトです. 
ninix-ayaはWindows環境の「何か/伺か」ベースウェア用に作られたゴースト
(キャラクターデータ)を動作させることを目的としたソフトウェアです.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=/usr localedir=%{buildroot}/usr/share/locale DESTDIR=$RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_datadir}
install -d ${RPM_BUILD_ROOT}%{_datadir}/doc
install -d ${RPM_BUILD_ROOT}%{_datadir}/doc/%{name}
mv ${RPM_BUILD_ROOT}/usr/doc/* ${RPM_BUILD_ROOT}%{_datadir}/doc/%{name}/
sed -i 's|%{buildroot}||g' %{buildroot}%{_bindir}/ninix

%files
%{_bindir}/ninix*
/usr/lib/ninix*
%{_datadir}/locale/*/LC_MESSAGES/*
%doc %{_datadir}/doc/%{name}

%changelog
* Thu Dec 19 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0.9
- Rebuilt for Fedora

* Mon Dec  1 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/niseshiori.py: 「ポータル」, 「おすすめ」用URLの取得を修正.
  - lib/ninix/sakura.py: フォントサイズの計算を調整.

* Sun Nov 30 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: 選択肢の処理を変更.

* Sun Nov 30 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.5.3リリース.

* Sat Nov 29 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/main.py: ゴースト交代後に古いポップアプメニュー関連の
    オブジェクトが廃棄される前にApplicationクラスのメニューアイテムを
    detachするよう修正.
  - lib/ninix/sakura.py: BalloonWindow.motion_notify()の表示範囲の
    チェック忘れを修正.
    
* Sat Nov 29 2003  Shun-ichi TAHARA <jado@flowernet.gr.jp>
                   Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: バルーンのフォントサイズの設定が実際の表示に反映される
    よう修正.(Patch#3380)
    
* Fri Nov 28 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: バルーンフォント設定の変更が即反映されるように修正.
  - lib/ninix/sakura.py: %%usernameの展開で最初にSHIORIで設定されている値を
    問い合わせるようにした.
  - lib/ninix/sakura.py: Ghost.get_event_response()がNoneを返してしまう問題を
    修正(空文字列を返すようにした).

* Wed Nov 26 2003  Shun-ichi TAHARA <jado@flowernet.gr.jp>
  - lib/ninix/sakura.py: Communicate Boxの入力後にSSTP COMMUNICATEが発生する時
    UnicodeErrorが起きるのを修正.(Patch#3377)
  - lib/ninix/sakura.py: Teach Boxからの入力でUnicodeErrorが発生するのを修正.
    (Patch#3377)
  - lib/ninix/sakura.py: Communicate Boxへの入力の際にXIMの変換確定のEnterで
    入力処理が呼ばれてしまい, 空文字列が入力されてしまうのを修正.(Patch#3377)
  - lib/ninix/main.py: デフォルトバルーン設定のバグを修正.(Patch#3379)

* Tue Nov 25 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/satori.py: 内部関数call, loopを実装.

* Mon Nov 24 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/satori.py: 内部関数remember, setを実装.

* Fri Nov 14 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/satori.py: 前回終了時サーフェスの取得をサポート.
  - lib/ninix/dll/satori.py: 辞書情報の取得をサポート.

* Thu Nov 13 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.5.2リリース.

* Wed Nov 12 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/satori.py: デフォルトサーフェスの設定が機能していなかったのを
    修正して, サーフェス戻しの実装方法を変更.

* Tue Nov 11 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/satori.py: アンカー辞書をサポート.
  - lib/ninix/dll/satori.py: タイマーと予約トークもセーブするようにした.
  - lib/ninix/dll/satori.py: 辞書フォルダをサポート.
  - lib/ninix/dll/satori.py: 予約トークをサポート.
  - lib/ninix/dll/satori.py: OnTalkイベントをサポート.
  - lib/ninix/dll/satori.py: 文の途中でコメント(＃)を使えるようにした.
  - lib/ninix/dll/satori.py: サーフェス加算値をサポート.
  - lib/ninix/dll/satori.py: 自動セーブ, 手動セーブをサポート.
  - lib/ninix/dll/satori.py: OnUpdateReadyの（Ｒ０）に1加算するようにした.

* Tue Nov 11 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.5.1リリース.

* Sun Nov 9 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/satori.py: 変数と文と単語群の存在確認をサポート.

* Fri Nov 7 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/satori.py: セーブデータの暗号保存をサポート.

* Thu Nov 6 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/satori.py: OnRecommandedSiteChoiceイベントをサポート.
  - lib/ninix/dll/satori.py: 「ポータル」, 「おすすめ」用のURLリスト取得の
    サポートを追加.
  - lib/ninix/sakura.py: 「ポータル」, 「おすすめ」の中の項目を選択した際に
    OnRecommandedSiteChoiceイベントを発生させるようにした.

* Tue Nov 4 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/satori.py: OnSatoriBoot, OnSatoriCloseのサポートを追加.
  - lib/ninix/dll/satori.py: 改行の挿入位置を調整.
  - lib/ninix/dll/satori.py: satori_conf.txtが暗号化されている場合に対応.
  - lib/ninix/dll/satori.py: 選択ＩＤ, 選択ラベル, 選択番号を取得可能に.
  - lib/ninix/sakura.py: OnChoiceSelectedとOnChoiceEnterのReferenceを勝手に
    拡張.
  - lib/ninix/sakura.py: OnChoiceEnterイベントのサポートを追加.

* Tue Nov 4 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.5リリース.

* Tue Nov 4 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.4リリース.

* Mon Nov 3 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/satori.py: 最終トークからの経過秒を取得可能に.
  - lib/ninix/dll/satori.py: OnSatoriLoad, OnSatoriUnloadをサポート.
  - lib/ninix/dll/satori.py: 自動挿入ウェイトの倍率をサポート.
  - lib/ninix/dll/satori.py: さくらスクリプトを自動挿入ウェイトの計算対象に
    しないよう修正.
  - lib/ninix/dll/satori.py: マウスホイール反応をサポート.
  - lib/ninix/dll/satori.py: なで反応の感度を調整.
  - lib/ninix/dll/satori.py: cantalkが0の場合の処理を追加. 自発喋りのカウントを
    行わないようにした. またタイマのカウントは実行するが発動は遅らせるように
    した.
  - lib/ninix/dll/satori.py: 選択肢(\qタグ)の形式を変更.
  - lib/ninix/dll/satori.py: スコープ切り換えの際に改行を追加するようにした.
  - lib/ninix/dll/satori.py: スコープ切り換えの際の改行の再配置を削除.

* Sun Oct 26 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.3.8リリース.

* Fri Oct 24 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - locale/ja.poを更新.
  - lib/ninix/main.py: サーフェス倍率の最小値を10%%から40%%に変更.
  - lib/ninix/sakura.py: サーフェスに合わせてバルーンも縮小できるように変更.

* Mon Oct 20 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/main.py: 本体設定にデフォルトバルーンの設定を追加.
    ポップアップメニューのバルーンの項目は起動中のゴーストのバルーンを
    一時的に変更するのみにした.

* Thu Oct 16 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.3.7リリース.

* Wed Oct 15 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: 起動時点ではサーフェスはファイルチェックのみ行ない,
    ファイルからのgtk.gdk.Pixbufの作成は必要になってから行うように変更.
    作成したPixbufはキャッシュに入れられ, 参照されない状態が続くと破棄される.
  - lib/ninix/pix.py: Segfaultを引き起こすためgtk.gdk.Pixbuf作成後に行なって
    いたガーベジコレクションの実行を削除.
  - 全ての画像読み込みをpix.py経由に変更.

* Wed Oct 15 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.3.6リリース.

* Tue Oct 14 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - メモリリークを起こすgtk.gdk.pixbuf_new_from_file()のかわりに
    gtk.gdk.PixbufLoaderを使用するよう変更.
    また, pixbufの作成の後にガーベジコレクションを実行するようにした.

* Fri Oct 10 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.3.5リリース.

* Thu Oct 9 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: passivemode中にSSTPを受信した場合にはpassivemodeを
    抜けるまで再生を始めないよう修正.

* Wed Oct 8 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: サーフェス移動中にゴーストの動作を停止させないよう
    変更.
  - lib/ninix/dll/wmove.py: wmove.dll互換モジュール追加.

* Tue Oct 7 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sstp.py: UNIXドメインソケット版のSSTPサーバを追加した際に
    入ったバグを修正.
  - lib/ninix/dll/aya.py: SAORIの戻り値(Value*)の処理を修正.
  - lib/ninix/dll/aya.py: 四則演算の際の型変換のルールを修正.

* Sat Oct 4 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: ポップアップメニューの「ポータル」, 「おすすめ」を
    実装.
  - lib/ninix/dll/kawari.py: SHIORI判定の戻り値を修正.

* Fri Oct 3 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.3.4リリース.

* Thu Oct 2 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: ポップアップメニューに項目を追加.(機能自体は未実装.)
    それに伴ないlocale/ja.poを更新.
  - lib/ninix/sakura.py: Shellのdescript.txtのseriko.alignmenttodesktopに対応.
  - lib/ninix/sakura.py: 全てのデスクトップに居座るようにする設定をポップアップ
    メニューに追加.(ウインドウマネージャによっては正しく機能しないことがある.)

* Tue Sep 30 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.3.3リリース.

* Mon Sep 29 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/main.py, lib/ninix/sakura.py:
    ポップアップメニューのサーフェス倍率と表示ウェイトの項目をApplication
    クラスで管理するよう変更.
  - lib/ninix/main.py, lib/ninix/sakura.py, lib/ninix/dll/bln.py:
    起動後に本体設定で画面下端からの距離を調整できるようにした.
    (従来通り-Rオプションも使用可能で, オプションを指定した場合はそれが
     優先される.)
    また画面上部に移動するゴースト向けに画面上端からの距離も指定できるように
    した.
    easyballoon互換モジュールの位置計算もこの設定の影響を受ける.

* Mon Sep 29 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.3.2リリース.

* Fri Sep 26 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: 前回の修正で問題があったためその部分は元に戻した.
    (Python2.3で出る警告は無視しても問題無し.)
  - lib/ninix/sakura.py, lib/ninix/dll/hanayu.py:
    gtk.Window.begin_move_drag()の引数の型を修正.
  - lib/ninix/dll/satori.py: Python2.3の仕様変更(Boolean型の追加)で動作に
    問題が発生していたのを修正.

* Thu Sep 25 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.3.1リリース.

* Wed Sep 24 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/kawari.py: Python2.3の仕様変更(Boolean型の追加)で動作に問題が
    発生していたのを修正.
  - lib/ninix/sakura.py: ゴーストの再読み込みが機能しなくなっていたのを修正.
  - lib/ninix/sakura.py: Python2.3で警告が出ていたのを修正.

* Wed Sep 24 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.3リリース.

* Tue Sep 23 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - locale/ja.poを更新.
  - ポップアップメニューの内部構造の変更を終了.

* Mon Aug 18 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/bln.py: 本体と同じプロセスで動作するように戻した.
  - lib/ninix/dll/bln.py: actionにvibrateメソッドのサポートを追加.
  - lib/ninix/dll/bln.py: スクリプト・アップデートおよびスクリプト・アペンドを
    サポート.
  - lib/ninix/dll/bln.py: \c, \b?, \_q, \l タグのサポートを追加.
  - lib/ninix/dll/bln.py: font.boldをサポート.

* Sun Aug 17 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/bln.py: leftcenter, rightcenter, centertop, centerbottomの
    位置指定に対応.
  - lib/ninix/dll/bln.py: OnEBMouseMoveの通知周期を500msに変更.
  - lib/ninix/dll/bln.py: OnEBMouseClickの通知タイミングをプレス時から
    リリース時へ変更.
  - lib/ninix/dll/bln.py: action.referernce3のサポートを追加.

* Thu Aug 7 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/main.py, lib/ninix/sakura.py: ポップアップメニューの作成と管理を
    移動.

* Tue Jul 29 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/main.py: マルチスレッド化のための初期化処理を削除.

* Mon Jul 28 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.2リリース.

* Sat Jul 26 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/kawari.py: SAORIリクエストにCharsetエントリを追加.
  - lib/ninix/misaka.py: SAORIリクエストにCharsetエントリを追加.
  - lib/ninix/misaka.py: SHIORIリクエストの文字コード変換を修正.
  - lib/ninix/aya.py: SHIORIリクエストの文字コード変換を修正.

* Fri Jul 25 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.1.5リリース.
  - lib/ninix/sakura.py: 最小化/復帰した際のイベントが2重に送られていたの
    を修正.

* Thu Jul 24 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/sstplib.py, lib/ninix/sstp.yp: アイコン化されている状態の時はSSTP
    サーバがエラー512(Invisible)を返すように修正.
  - lib/ninix/communicate.py: 古いghost.dbが残っていた場合のエラー処理を追加.
  - lib/ninix/sakura.py: cantalkフラグが0の時はスクリプトを破棄するように変更.

* Wed Jul 23 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/main.py: マルチスレッド化のための初期化処理を追加.

* Mon Jul 21 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - SHIORIリクエストで文字コードを取得するよう変更. codeselect.pyは削除.
  - 放置状態だったPython栞のサポートを削除.
  - lib/ninix/sakura.py: oldtype指定の付いたSHIORIモジュールのサポートを削除.
  - lib/ninix/dll/kawari.py, lib/ninix/dll/niseshiori.py, 
    libninix/dll/satori.py:
    Shioriクラスにrequestメソッドを追加し, finalizeメソッドをunloadに改名.
    oldtype指定を削除.
  - lib/ninix/dll/niseshiori.py: リクエストの引数の数値を文字列に変換して
    しまっていたのを修正.
 
* Sun Jul 20 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - 本体のターミナル出力をUTF-8に変更.
  - SAORIモジュールがcodeselct.pyを使用しないよう変更.

* Sat Jul 19 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.1.4リリース.
 
* Fri Jul 18 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix-install.py, lib/ninix/config.py:
    インストールディレクトリの文字コードをUTF-8に変換するよう変更.
  - lib/ninix-install.py, lib/ninix/update.py, lib/ninix/config.py:
    ファイル名に関して文字コード変換を行なわないよう変更.
 
* Thu Jul 17 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - locale/zh_TW.poを追加. (Chieh-Nan Wang)
  - lib/ninix/sakura.py: 旧形式の互換SHIORIへのリクエストで文字コード変換
    ができていなかったのを修正.
  - lib/ninix/dll/niseshiori.py: 送られたSHIORIリクエストの文字コード変換
    を修正.
  - lib/ninix/dll/kawari.py: 送られたSHIORIリクエストの文字コード変換を修正.
 
* Wed Jul 16 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/kawari.py: find()の実行後に文字コードを初期化するよう修正.
 
* Wed Jul 16 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.1.3リリース.
 
* Tue Jul 15 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/kawari.py: 文字コードの初期化忘れを修正.
  - lib/ninix/sakura.py: バルーンに使用するウインドウの種類を変更.
  - lib/ninix/sakura.py: コミュニケートウインドウの移動に関する処理を変更.
  - lib/ninix/sakura.py: SHIORIリクエストの文字コード変換を修正.
  - lib/ninix/dll/hanayu.py: ウインドウの移動に関する処理を変更.
 
* Mon Jul 14 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: サーフェス・バルーン・コミュニケートウインドウに
    対してのサイズ変更を拒否するよう設定.
  - lib/ninix/dll/kawari.py: 文字コードの設定を修正.
 
* Sat Jul 12 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.1.2リリース.

* Fri Jul 11 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/satori.py: モジュール間のやりとりで使用する文字コードを
    codeselectを通して指定するように変更.(EUC-JPを使用.)
  - lib/ninix/dll/kawari.py: 内部文字コードをUnicodeに変更.
  - lib/ninix/dll/kawari.py: モジュール間のやりとりで使用する文字コードを
    codeselectを通して指定するように変更.(辞書に合わせて変化.)
  - lib/ninix/dll/niseshiori.py: 内部文字コードをUnicodeに変更.
  - lib/ninix/dll/niseshiori.py: モジュール間のやりとりで使用する文字コードを
    codeselectを通して指定するように変更.(UTF-8を使用.)
  - lib/ninix/sakura.py: 旧形式互換SHIORIインタフェースの文字コード設定を修正.

* Thu Jul 10 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - ウインドウが最小化された場合と復帰した場合のイベント(OnWindowStateMinimize,
    OnWindowStateRestore)を生成するようにした.
 
* Wed Jul 09 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix-install.py: pnaファイルもインストールするよう修正.

* Wed Jul 09 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.1.1リリース.
                                                                                
* Mon Jul 07 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - 互換SAORI内部で使用する文字コードをEUC-JPからUnicodeに変更.
  - SSTPサーバ内部で使用する文字コードをEUC-JPからUnicodeに変更.
  - ninix用プラグインの定義ファイルplugin.txtでEUC-JP以外の文字コードを
    使用可能にした.(デフォルトはEUC-JPなので既存のプラグインの変更は不要.)
                                                                                
* Thu Jul 03 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - 本体内部で使用する文字コードをEUC-JPからUnicodeに変更.
  - lib/ninix/dll/misaka.py: Lexerクラスで使用している正規表現を再度修正.
  - locale/ja.po: lib/ninix/main.pyのメッセージを追加.
  - lib/ninix/main.py: gettext化により埋め込まれた日本語メッセージを置き替え.
 
* Sun Jun 29 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: ゴースト起動時にOnDisplayChangeを送信するようにした.
 
* Fri Jun 27 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - locale/ja.po: lib/ninix/sakura.pyのメッセージを追加.
  - lib/ninix/sakura.py: gettext化により埋め込まれた日本語メッセージを置き替え.

* Thu Jun 26 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py, lib/ninix/main.py: gtk.Window.set_wmclass()を使用しない
    ようにした.

* Wed Jun 25 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.1リリース.

* Mon Jun 23 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/home.py: fontrc関連部分を削除.
  - lib/config/fontrc: 削除.
  - lib/config/gtkrc: doc/examplesに移動.
  - lib/ninix-install.py: gtkrc, fontrcファイルのインストールを削除.

* Sun Jun 22 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/main.py: ポップアップメニューのゴースト選択で現在起動中の
    ゴーストを選択できないようにした.
  - lib/ninix/sakura.py: ゴーストのアイコンをサーフェスウインドウのアイコン
    として使うようにした.
  - Makefile: ファイルのインストール先ディレクトリ名を変更.

* Fri Jun 20 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/misaka.py: Lexerクラスで使用している正規表現を再修正.
  - lib/ninix/main.py: ゴーストのアイコンをポップアップメニューで使うよう
    にした.
 
* Thu Jun 19 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/misaka.py: Lexerクラスを一部変更.
    (「フサギコ漫談」対応のため.)
  - gettext化を開始.

* Mon Jun 16 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: 暗号化PNGをサーフェスに使用できるようにした.
  - lib/ninix/pix.py: 暗号化PNGの解読機能を追加.

* Fri Jun 13 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/home.py: サーフェス画像として暗号化PNGを使えるようにした.
  - lib/ninix-install.py: サーフェス画像として暗号化PNGをインストールでき
    るようにした.
  - lib/ninix/main.py: ポップアップメニューでシェルの名前の文字コードが変
    換されていなかったのを修正.
  - lib/ninix/dll/aya.py: 辞書読み込みのバグ修正.

* Fri May 30 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン2.0リリース.
 
* Thu May 29 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py, lib/ninix/main.py, lib/ninix/pix.py:
    着せ替え機能SERIKO/1.3,1.7,1.8(MAYUNA/1.0,1.1,1.2)対応.
  - lib/ninix/mayuna.py 追加.
 
* Tue May 27 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - READMEを更新.
  - lib/ninix/main.py: バージョン情報を修正.
  - lib/ninix/sakura.py: \![*]タグによるSSTPマーカーの表示で位置がずれていたのを
    修正.
  - lib/ninix/dll/kawari8.py: SAORI互換モジュールのロード状態を管理するよ
    う修正.
 
* Thu May 22 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン1.9.11リリース.

* Wed May 21 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: overlayのオフセットが負の値の時に画像合成でエラーが出て
    いたのを修正.
 
* Tue May 20 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix-update.py, lib/ninix/update.py: 本体のネットワーク更新機能の変更で
    ninix-updateコマンドが動作しなくなっていたのを修正.
 
* Mon May 19 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/bln.py: 文字の表示がちらつかないよう表示速度を調整.
  - lib/ninix/dll/bln.py: bln.txtの読み込みでエラーが発生すると, bln.pyの
    unloadが正しく行なわれなくなるのを修正.
 
* Sun May 18 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン1.9.10リリース.
  - lib/ninix/sakura.py: 文字コード変換が1箇所抜けていたのを修正.
  - lib/ninix/dll/aya.py: 関数の検索方法の変更でシステム関数FUNCTIONEX, SAORIが
    動かなくなっていたのを修正.

* Fri May 16 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン1.9.9リリース.
  - lib/ninix/main.py, lib/ninix/sakura.py: 新しいバルーンフォント設定が機能
    するよう修正.

* Sun May 11 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン1.9.8リリース.
  - lib/ninix/main.py, lib/ninix/dll/bln.py, lib/ninix/dll/hanayu.py:
    pygtk-1.99.14以前のpango.Layout.set_text()の仕様に対応.

* Thu May 08 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン1.9.7リリース.
  - lib/ninix-install.py, lib/ninix/sakura.py, lib/ninix/home.py:
    残っていたxpm形式の画像ファイルサポートのコードを完全に削除.
  - lib/ninix/sakura.py: _image.soモジュールを使わずにサーフェス画像ファイルを
    読み込むように変更.(この変更でpygtk-1.99.14でも動作するようになった.)

* Wed May 07 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン1.9.6リリース.
  - README, doc/saori.txt, doc/kawari.txt を更新.
  - lib/ninix/sakura.py: 1.99.16より古いpygtkだとGdkWindow.set_back_pixmap()の
    バグで動作しない問題を修正.
  - lib/ninix-install.py: install.txtのnameエントリが一致しない場合に上書き
    しても良いかどうか確認するよう修正.
  - lib/ninix/main.py: ゴーストを消滅させる際にディレクトリとHISTORYファイルを
    残すよう変更.

* Mon May 05 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン1.9.5リリース.
 
* Sun May 04 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/aya.py:字句解析/構文解析関連メソッドをリクエスト処理際の負荷を
    できるだけ小さくする方向で再度大幅に変更.
 
* Sat May 03 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: バルーンの文字表示位置を調整.
 
* Thu May 01 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン1.9.4リリース.
  - lib/ninix/sakura.py: \![open,inputbox,,,<初期値>] で入力の初期値を
    指定できるように修正.
 
* Mon Apr 28 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/aya.py: システム関数の引数の型チェックを厳しくした.
  - lib/ninix-install.py: CROW同梱ゴーストのインストール機能を削除.
 
* Sun Apr 27 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/aya.py: DLLの名前が変更されている場合にaya_variable.cfg
    の名前もそれに合わせるようにした.
  - lib/ninix/dll/aya.py:字句解析/構文解析を強化.
  - lib/ninix/sakura.py:CommunicateWindow(およびサブクラス)のkey_pressメソッドで
    2重にイベントが発生していたのを修正.
 
* Fri Apr 25 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン1.9.3リリース.
  - lib/ninix/sakura.py:バルーンの再配置が正しく行われない場合があったのを修正.
  - lib/ninix-install.py: install.txtのrefresh, refreshundeletemaskエントリ対応.
  - lib/ninix/dll/aya.py: SakuraScriptのメタ文字列先頭の%%を誤って取ってしまう
    バグを修正.
  - lib/ninix/dll/aya.py: AyaFunctionクラスのevaluate_*メソッドを高速化.
  - lib/ninix/dll/aya.py: AyaFunctionクラスのparseメソッドを改良.
 
* Thu Apr 24 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン1.9.2リリース.
 
* Wed Apr 23 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/main.py: メニューが画面に入り切らない場合の処理はGTK+に任せる
    ことにしてメニューのリサイズ処理を削除.
                                                                                
* Tue Apr 22 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/dll/aya.py: 重複している処理を省くなどして高速化.
                                                                                
* Mon Apr 21 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: マウス移動検出の処理を変更. ボタンが押されていない
    状態でサーフェス上をマウスカーソルが移動するとOnMouseMoveイベントが発生する
    ようにした.
    イベント処理のタイマ割込みとGTK+のイベント生成を連動させることで無駄な
    イベントの発生を抑えている.
  - lib/ninix/sakura.py: サーフェスの当り判定領域でマウスカーソルが変わるように
    変更.
                                                                                
* Mon Apr 21 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン1.9.1リリース.
  - lib/ninix/dll/aya.py: 栞判定を強化. DLLの名前が変更されている場合に対応.
  - lib/ninix/home.py: 栞判定メソッドにDLLの名前を渡すようにした.
 
* Sun Apr 20 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/main.py: バルーンフォント設定以外の本体設定が機能するよう修正.
  - lib/ninix/sakura.py: バルーンの描画方法を一部変更.
  - lib/ninix/sakura.py: サーフェスオーバーレイの座標が負の場合にエラーが出る
    のを修正.
 
* Fri Apr 18 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: バルーンの位置計算のバグを修正.
 
* Thu Apr 17 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン1.9リリース.
  - lib/ninix/sakura.py: サーフェス・バルーンの位置計算を調整.
  - lib/ninix/sakura.py: 見切れ・重なり判定を調整.
  - lib/ninix/sakura.py: サーフェス配置パラメータを SurfaceWindow
    クラスに移した.
 
* Wed Apr 16 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: \_b[], \_v[]タグの処理でファイル名を小文字に
    変換するのを忘れていたのを修正.
  - ドキュメントの配置を変更.
 
* Sun Apr 13 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - lib/ninix/sakura.py: バルーンの位置計算を修正.
  - lib/ninix/sakura.py, lib/ninix/main.py: サーフェス縮小機能を追加.
  - lib/ninix/sakura.py: バルーンのスクロールボタンをマウスホイールで
    操作可能に.
  - lib/ninix/main.py, lib/ninix/sakura.py: -pオプションを廃止.
  - lib/utf8.py: 削除.
  - lib/ninix/dll/niseshiori.py: utf-8の処理にunicode()を使用するよう
    変更.
  - src/: 削除.
  - lib/ninix-install.py: pngからxpmへの変換(-xpmオプション)を削除.
  - gtkhack/: 削除.
  - GTK+2.0ベースに変更.
 
* Sat Apr 12 2003  Shyouzou Sugitani <shy@trifle.nips.ac.jp>
  - バージョン1.0リリース.
  - lib/ninix/dll/hanayu.py: 線の太さのデフォルト値を修正.
  - lib/ninix/sakura.py: \_b[] タグの処理を修正.

* Tue Apr 08 2003  period 30
  - ネットワーク更新を途中でキャンセル可能にした.(update.py, sakura.py)
  - ネットワーク更新でエラーが発生した場合や途中キャンセルされた場合にはファイル
    を更新前の状態に戻すようにした.(update.py)
  - AyaFunction.evaluate_statement() にエラー処理を追加.(aya.py)
  - 送信すべきイベントが無い場合にもイベントを本体に送信しようとしてエラーになっ
    ていたのを修正.(bln.py)
  - 文字の表示位置設定のバグを修正.(hanayu.py)
  - 描画のちらつきを抑えるためのモジュール _gtkhack を追加.
  - Shiori.reload() を追加.(satori.py)
  - 本体による AI トークの頻度調整を削除.(main.py, sakura.py)
 
* Mon Mar 03 2003  period 29
  - 再生するファイルのパス指定を修正.(mciaudio.py)
  - mciaudior.dll 互換モジュール追加.
  - おるすばんバルーンを出す前に通常バルーンを消去するようにした.(bln.py)
  - おるすばんバルーンが本体にイベント送信しないようにした.(bln.py)
 
* Sat Mar 01 2003  period 28
  - ゴーストの交代時に自由配置等の設定をリセットするようにした.(sakura.py)
  - SERIKO の interval エントリ yen-e と talk,n に対応.(sakura.py, seriko.py)
  - base メソッドのアニメーションが最後まで動作するようにした.
    (sakura.py, seriko.py)
  - res_reference* をリクエスト毎に削除するようにした.(aya.py)
  - AyaFunction.get_block() を修正.(aya.py)
  - ループ回数制限撤廃.(aya.py)
  - case 〜 when の候補値として文字列の範囲指定を使用可能にした.(aya.py)
  - セキュリティーログは既存のファイルがあればそれに追加するようにした.(aya.py)
  - セキュリティーログの書き込みの際にファイルロックするようにした.(aya.py)
  - システム関数 TOBINSTR, TOHEXSTR, BINSTRTONUM, HEXSTRTONUM を追加.(aya.py)
  - 数値の2進/16進表記に対応.(aya.py)
  - return ステートメントに対応.(aya.py)
  - while ループ内で break, continue を使用可能にした.(aya.py)
  - マルチステートメントの処理方法を変更.(aya.py)
  - for ループに対応.(aya.py)
  - SERIKO の "option,exclusive" に対応.(seriko.py, sakura.py)
  - 本体との間のタイミングを調整.(bln.py)
  - スクリプトの処理が終わるまではネットワーク更新後の再読み込みを実行しないよう
    に変更.(sakura.py)
* Mon Feb 10 2003  period 27
  - KIS コマンド saoriregist,saorierase,callsaori,callsaorix のサポートを追加.
    (kawari.py)
  - kawari.ini での SAORI 登録に対応.(kawari.py)
  - \![set,alignmenttodesktop,free] に対応.(sakura.py)
  - 見切れ・重なり判定でY軸方向も考慮するようにした.(sakura.py)
  - \![set,alignmenttodesktop,free], \![set,alignmentondesktop,*] がシンクロ
    ナイズドセッション中に実行された場合, 両方のサーフェスに作用するようにした.
    (sakura.py)
  - '\_v[filename]' のサポートを追加.(sakura.py)
  - 互換 SAORI 呼び出しのバグを修正.(kawari.py)
  - ゴーストが8体以上居る状態でゴーストリストの作成でエラーが発生するのを修正.
    (sakura.py)
  - 旧API 互換栞のためのゴースト間コミュニケーションのサポートを追加.(sakura.py)
  - ゴースト間コミュニケーション機能を一部実装.(kawari.py)
  - マッチエントリ検索以外のゴースト間コミュニケーション機能を実装.(kawari.py)
  - Saori.timeout_id の初期化処理を追加.(bln.py)
  - マッチエントリ検索の処理を追加.(kawari.py)
  - ゴースト間コミュニケーション機能を実装.(niseshiori.py)
  - case 〜 when 〜 others ステートメントの処理を追加.(aya.py)
  - 領域コメントに対応.(aya.py)
  - システム関数 GETLASTERROR を追加.(aya.py)
  - システム関数 ISINSIDE, IASC を追加.(aya.py)
  - case 〜 when の候補値として範囲指定を使用可能にした.(aya.py)
  - ファイル操作系システム関数で絶対パス指定を可能にした.(aya.py)
  - check_path 関数によるファイル操作のチェックを修正.(aya.py)
  - セキュリティ機能を実装.(aya.py)
  - システム関数 STRSTR を修正.(aya.py)
  - "OnTranslate" イベントを発生させるようにした.(sakura.py)
  - inputbox を再調整.(sakura.py)
  - 複雑な設定がされている場合のセキュリティチェックを高速化.(aya.py)
  - AyaFunction.parse() の処理結果に __TYPE_LITERAL を追加.(aya.py)
  - ローカル以外からの "\!" で始まるタグの実行を拒否するようにした.(sstp.py)
  - KIS コマンド split を修正.(kawari.py)
 
* Sun Jan 19 2003  period 26
  - ファイル操作システム関数でファイル名を小文字に変換するように修正.(aya.py)
  - システム関数 ROUND を修正.(aya.py)
  - 文字列の連結に string モジュールの join メソッドを使うようにした.(aya.py)
  - aya_variable.cfg の読み込みに成功したかどうかを AyaGlobalNamespace クラスの
    load_database メソッドの戻り値として返すようにした.(aya.py)
  - 高速化のために辞書の読み込み時点でできるだけ解析を済ませるようにした.
    (aya.py)
  - 変数・関数を探す際の名前空間のサーチ順序を変更.(aya.py)
  - 効率の悪いループやメソッド呼び出しを修正.(aya.py)
  - AyaFunction クラスの evaluate_string メソッドのヒストリ処理を修正.(aya.py)
  - AyaVariable クラスの put メソッドを修正.(aya.py)
  - play コマンドで再生/一時停止をトグルできるようにした.(mciaudio.py)
  - 出力確定子の処理を修正.(aya.py)
  - 画像にアルファチャンネルが設定されている場合の処理を追加.(_image.c)
  - KIS コマンド array のサポートを追加.(kawari.py)
  - モジュール名の取り出し部分のバグ修正.(dll.py)
  - nooverlap の処理の問題を修正.(bln.py)
  - ファイルチェックを強化.(hanayu.py)
  - 戻り値が無い場合のヘッダを修正.(bln.py, hanayu.py, mciaudio.py, textcopy.py)
  - KIS コマンド split のサポートを追加.(kawari.py)
 
* Mon Dec 30 2002  period 25
  - フォント関連パラメータの使い方を一部修正.(sakura.py, bln.py, hanayu.py)
  - Python 1.5 の環境でエラーが出ないように fcntl.lockf() の第一引数を修正.
    (communicate.py)(Thanks to あべさん)
  - 本体でヘルパーに設定されているコマンドをファイルの再生に使うように変更.
    (lettuce.py, mciaudio.py)
  - みんと(mint.dll)と名前が混ざっていたのを修正.(lettuce.py)
  - string.join() の引数が一箇所間違っていたのを修正.(aya.py)

* Tue Dec 24 2002  period 24
  - line_strip() の使用を控えるようにした.(aya.py)
  - 不要な 'otherghostname' イベントを発生させないようにした.(sakura.py)
  - 'otherghostname' イベントを 'NOTIFY' で送るように修正.(sakura.py)

* Mon Dec 16 2002  period 23
  - ninix-install に CROW 同梱ゴーストのインストール機能を追加.
    それに合わせてゴースト固有バルーンの検索の際にゴーストの descript.txt の
    内容もチェックするように変更(main.py)
  - ゴースト間コミュニケーションのための communicate.py を追加.
  - COMMUNICATE/1.1 のサポートを追加.(sstp.py)
  - 起動しているゴーストのデータベース更新機能を実装.(sakura.py)
  - 定期的に 'otherghostname' イベントを発生させるようにした.(sakura.py)
  - ゴースト間コミュニケーション用のメッセージ送信機能を実装.(sakura.py)
  - 'otherghostname' イベント用に Reference の処理を拡張.(sakura.py)
  - misaka.py をゴースト間コミュニケーションに対応させた.
  - リンク対象となるテキストが空の場合の処理を追加.(sakura.py)
  - inputbox を「仕様書通り」に使っているゴーストに対応.(sakura.py)
  - CROW 同梱ゴースト対応の際に入った, 固有バルーンを持たないゴーストへの切り
    換えの場合にゴースト名の入った変数を上書きしてしまうバグを修正.(main.py)
 
* Sat Dec 07 2002  period 22
  - 不要になったコードを削除.(ninix-install.py)
  - show_description() の表示内容に Copyright を追加.(aya.py, kawari8.py)
  - 旧 API の互換栞を ninix/dll に移動. API はそのままで Shiori クラスを追加.
    呼び出しは新 API 互換栞と同様に dll.py 経由で行なう.
    (niseshiori.py, kawari.py, satori.py, ninix-update.py, home.py, sakura.py)
  - 栞の終了処理を追加.(ninix-update.py)
  - ロードされていない状態で unload() が呼ばれても問題ないよう修正.(hanayu.py)
  - 選択肢がバルーンの表示領域内にあるかどうかの判定条件を修正.(sakura.py)
  - 文字列を囲むダブルクォートが片方抜けている場合の処理を追加.(aya.py)
  - DirectSSTP 機能として UNIX ドメインソケット版の SSTP サーバを追加.
    (sstplib.py, sstp.py, main.py, sakura.py)
  - bln.py をマルチプロセス化.
  - バルーンクリックイベントが2重に発生していたのを修正.(bln.py)
  - バルーンクリックイベントが発生しない場合があったのを修正.(bln.py)
  - マウス移動イベントが全く発生していなかったのを修正.(bln.py)
  - X 座標方向のバルーンの位置計算を修正.(bln.py)
  - DirectSSTP のレスポンスについては標準エラー出力にメッセージを出さないように
    した.(sstp.py)
  - ネットワーク更新のファイル数を0オリジンに変更.(update.py)
  - DirectSSTP 用のソケットディレクトリ名を socket に変更.(main.py)
  - SSTP の Sender フィールドに ninix が使われていた箇所を ninix-aya に変更.
    (ninix-install.py, ninix-update.py, sakura.py)
  - バージョン情報を ninix-aya のものに変更.(main.py)
  - pygtk で GTK+ のバージョンを指定するようにした.(main.py, bln.py)
    (Thanks to にっしーさん)
  - 以前の変更で Python SHIORI の判定が抜け落ちてしまっていたのを修正.(home.py)
  - サーフェスが充分離れている場合は '\4' が来ても移動しないよう修正.(sakura.py)

* Sat Nov 16 2002  period 21
  - バルーンの設定情報の優先順位を調整.(sakura.py)
  - ロードされていない SAORI へのリクエストに対する応答を修正.(kawari8.py)
  - InputBoxがESCキーでキャンセルされた場合にもイベントを発生させるように変更.
    (sakura.py)
  - CommunicateBox のモーダル設定を解除.(sakura.py)
  - \![set,alignmentondesktop,top], \![set,alignmentondesktop,bottom] に対応.
    (sakura.py)
  - 時々サーフェスが出てこないバグを修正.(sakura.py)
  - スクリプトの表示の際にバルーンも前面に出すようにした.(sakura.py)
  - OnKeyPress を新仕様と旧仕様の混成仕様に変更. ただし, キーマップは不完全.
    (keymap.py, sakura.py)
  - 一行に複数の選択肢とテキストを混在させられるように変更.(sakura.py)
  - サーフェスとバルーンが重なった場合にちらつくのを抑えるために前面に出す動作を
    調整. 変化があった時だけ前面に出てくるようにした.(sakura.py)
  - 選択肢が複数の行にまたがっても良いように変更.(sakura.py)
  - '\x' の位置に改行を入れるように変更.(sakura.py)
  - \![open,configurationdialog] に対応.(sakura.py)
  - サーフェスのドラッグの際にはサーフェスを前面に出すようにした.
  - バルーンの方向を決定する方法を変更.
  - '\4', '\5' に対応. ただし, alignmentondesktop は考慮していないので Y 座標の
    方向の移動は無し.(sakura.py)
  - '\![*]' に対応.(sakura.py)
  - バルーン切り換えの後は強制的にサーフェスを出すようにした.(main.py)
  - バルーンの位置を調整.(sakura.py)
  - '\4', '\5' がウインドウを10ピクセルずつ移動させるように変更.(sakura.py)
  - 栞判定を改良.(misaka.py)
  - バルーン内の表示領域に関する情報が更新されている間は選択肢がマウスの移動に
    反応しないように修正.(sakura.py)
  - '\_a[symbol]' に対応.(sakura.py)
  - '\4' の移動距離を調整.(sakura.py)
  - '\5' の移動先を調整.(sakura.py)
  - 全てのスクリプトがトランスレータを通るように修正.(sakura.py)
  - 選択肢の範囲チェックを修正.
    選択肢の先頭が表示領域内でも途中から外に出ている場合がある.(sakura.py)
         
*Sun Oct 27 2002  period 20
  - 花柚(hanayu.dll)互換 SAORI モジュール hanayu.py を追加.
  - れたす(lettuce.dll)互換 SAORI モジュール lettuce.py を追加.
  - タイムクリティカルセクション中もイベントを処理するよう変更.(sakura.py)
  - 多バイト文字列操作関数, 外部汎用DLL呼び出し関数, ファイル操作関数のテストを
    行ない, 見付かったバグを修正.(aya.py)
  - 辞書の暗号化機能を追加.(aya.py)
  - \![(un)lock,reapint] に対応.(sakura.py)
  - hanayu.txt の読み込みのバグを修正.(hanayu.py)
  - スクリプトの表示の際にサーフェスを前面に出すようにした.(sakura.py)
  - \![vanishbymyself] に対応.(sakura.py)
  - \![enter,passivemode], \![leave,passivemode] に対応.(sakura.py)
  - '\x' からの復帰の際に下向き矢印を消去するようにした.(sakura.py)
  - \_b[filename,x,y] に対応.(sakura.py)
  - メニューのネットワーク更新と消滅指示のボタンはメニュー表示の度に更新するよう
    にした. 消滅指示の表示/非表示の切り換えを反映させるため.(sakura.py)
  - \n[half] に対応.(sakura.py)
  - '_in_', '!_in_' の処理を修正.(aya.py)
  - passive mode でバルーンの消去が機能しないように修正.(sakura.py)
  - draw_last_line() の \n[half] の処理を修正.(sakura.py)
  - passive mode と \![lock,repaint] の動作を調整.(sakura.py)
  
* Fri Oct 04 2002  period 19
  - misaka.py を dll/ に移動. API を変更し互換 SAORI にも対応.
  - 梶山 API の互換栞の栞判定で互換栞が見つかっても100しか返さないようにした.
  - eval_globals() で sentences の中に関数が出てきた場合にその関数を実行するよう
    にした.(misaka.py)
  - 互換栞が無かった場合にシェルとして使用できるようにするコードを復活.(home.py)
  - 単体のバルーンの情報(1次情報)とゴースト同梱のバルーンまで含めたバルーン全て
    の情報(2次情報)を分離.(home.py, main.py)
  - 消滅指示後のゴースト切り換え時に全ファイルを再読み込みしていたのを必要最小限
    (次に起動するゴースト)の読み込みしか行なわないように変更.(main.py)
  - 消滅指示後に切り換わるゴーストがランダムに選択されなくなっていたのを修正.
    (main.py)
  - search_ghosts()を特定のゴーストのディレクトリを指定して呼び出せるようにした.
    (home.py)
  - ゴースト起動・変更時のイベントに反応が無い場合の動作を変更.(sakura.py)
  - タイマ割込みの制御を Sakura から Ghost に移動.(sakura.py)
  - ネットワーク更新の処理を Sakura から Ghost に移動.(sakura.py)
  - Sakura からの Application のメソッドの呼び出しは Ghost に任せるようにした.
    (sakura.py, main.py)
  - 現在のゴーストの情報を再読み込みするためのメソッドを追加.(main.py)
  - ネットワーク更新が完了したらゴーストの情報を再読み込みするようにした.
    (sakura.py)
 
*Sun Sep 22 2002  period 18
  - DLL 互換モジュールを管理するクラスは main.py でインスタンスを生成するように
    変更.(main.py, sakura.py, dll.py, aya.py)
  - 互換 SHIORI で互換 SAORI を使用する場合の処理の一部を dll.py に移して互換
    SHIORI 側の処理の負担を軽減.(main.py, dll.py, aya.py)
  - 互換 SAORI から Sakura のインスタンスへのアクセスを可能にした.(dll.py)
  - easyballoon(bln.dll) 互換 SAORI モジュール bln.py を追加.
  - unload() の戻り値を修正.(mciaudio.py, bln.py)
  - 互換 SAORI の状態の管理は SHIORI 毎に微妙に差があるため互換 SHIORI の責任で
    行なうようにした.(dll.py, main.py, aya.py, ninix-update.py)
  - kawari8.py を互換 SAORI に対応させた.
  - ウインドウを構成するウィジットを見直し.(bln.py)
  - ウインドウの初期座標が負の値の場合にも正しく表示されるよう修正.(bln.py)
  - タイムアウトの処理を修正.(bln.py)
  - スクリプトの表示が終わるまでは指定された寿命が来てもウィンドウを破棄しない
    ようにした.(bln.py)
  - ウィンドウの移動距離の計算を修正.(bln.py)
  - 変数名の誤りを修正.(bln.py)
  - textcopy.dll 互換 SAORI モジュール textcopy.py を追加.
  - gtk を import する DLL 互換モジュールは環境変数 DISPLAY をチェックするよう
    に修正.(bln.py, textcopy.py)
  - ninix-update.py と sakura.py で梶山 API の互換栞について栞判定を再度行なっ
    ていたのを修正. これで栞判定を行なう場所は home.py 内に限定された.
  - import したモジュールに目的のクラスが無い場合にはそのモジュールを削除する
    ようにした.(dll.py)
  - DLL 互換モジュールのサーチパスは __init__ の際に指定されたものに限定.
    (dll.py, sakura.py, aya.py, kawari8.py, ninix-update.py)
  - DLL 互換モジュールのサーチパスの指定を変更.(main.py)
  - 新しい栞判定を導入開始.(home.py)
  - 栞判定の変更により不要になった _kawari8.so の import 時のメッセージを削除.
    _kawari8.so が無ければ栞判定のスコアが 0 になる.(kawari8.py)
  - 新互換栞のロード後にモジュールの名前等を表示できるようにした.(sakura.py)
    Shiori クラスの show_description を呼び出すが, このメソッドは必須ではない.
  - Shiori クラスに show_description メソッドを実装.(aya.py, kawari8.py)
  - kawari8.py の栞判定の結果の1桁目を変更.(kawari8.py, sakura.py)
  - サーフェス・バルーンの位置の計算を修正.(sakura.py)
  - *Actor で無限ループに陥るのを修正.(seriko.py)
  - OnSurfaceRestore イベントは SHIORI にイベントを送るだけで, 本体側でサー
    フェスを戻さないよう変更.(sakura.py)
  - Sakura スクリプトで最初のサーフェス指定が来るまではサーフェスを表示しな
    いように変更. もし, メッセージ表示が先に来た場合はその時点でデフォルトが
    出る.(sakura.py)
  - 毎回ロード時に _kawari8.so をリロードするようにした.(kawari8.py)
  - ドラッグ中にサーフェスをデフォルトに戻さないようにした.(sakura.py)
  - 見切れ判定を調整.(sakura.py)
  - 再読み込みの後で OnGhostChanged を発生させるようにした.(sakura.py)
  - 再読み込み後に発生させるイベントを OnBoot に変更.(sakura.py)
  - OnGhostChanged に反応が無い場合には OnBoot を呼ぶようにした.(sakura.py)
  - '\x' による一時停止時にバルーンに下向き矢印を出させるようにした.(sakura.py)
         
* Mon Sep 02 2002  period 17
  - DLL 互換モジュールのデフォルトサーチパスの指定を必須にした.(dll.py)
  - DLL 互換モジュールを要求する際にサーチパスを追加出来るように変更.(dll.py)
  - DLL 互換モジュールインタフェースを使用した SHIORI 互換モジュールのサポートを
    追加.(sakura.py)
  - aya.py を lib/ninix/dll に移動. DLL 互換モジュールインタフェースに対応.
  - home.py における「文」ゴースト判定の方法を aya.txt の有無で判定するよう変更.
    ただし, 一時的な措置.
  - ninix-install, ninix-update から旧 aya.py 関連のコードを削除.
  - ninix-update を DLL 互換モジュールインタフェースに対応させた.
  - ninix-install でゴーストの全ファイルをインストールするように変更.
  - 新互換栞とのインタフェースを SHIORI/3.0 に変更.(sakura.py)
  - SHIORI API wrapper を削除し, SHIORI/3.0 のみのサポートに変更.(aya.py)
  - ninix-update を新互換栞でも利用できるよう SHIORI/3.0 に対応させた.
  - test() を修正.(aya.py)
  - SHIORI 判定を刷新. ただし, 各 SHIORI の判定ルーチンは従来のまま.
    (home.py, ninix-update.py, main.py, sakura.py, dll.py, aya.py)
  - shiori_name には DLL 名ではなく互換栞の名前を入れるように変更.(dll.py)
  - 華和梨8の判定を追加.(home.py)
  - 新形式互換栞 kawari8.py を dll/ に追加.
  - DLL互換モジュールのリクエストがディレクトリ名を含んでいる場合に対処.
    (dll.py)
  - SHIORI 判定関数のリストを作成.(home.py)
  - SAORI リクエストは Shift_JIS で送るように修正.(aya.py)
  - 代入の際に不要な整数から実数への変換をしないようにした.(aya.py)
  - load() に戻り値を設定するのを忘れていたので修正.(aya.py, kawari8.py)
  - 新互換栞の load() が失敗の場合には旧互換栞を探すように変更.
    (sakura.py, ninix-update.py)
  - システム関数 MSTRLEN, MSTRSTR, MSUBSTR, MERASE, MINSERT を実装.(aya.py)
  - saori.py から SAORI DLL 互換機能の実装を分離.
  - saori.py を dll.py に変更. SAORI だけでなく SHIORI も扱うようにした.
  - lib/ninix/dll/mciaudio.py に mciaudio.dll 互換機能を移した.
  - コミュニケートウインドウは ESC が押された場合のみ消えるよう変更.(sakura.py)
  - システム変数 systemuptickcount を実装.(aya.py)
  - システム関数 FWRITE2 を実装.(aya.py)
  - ファイル名を小文字に変換するよう修正.(mciaudio.py)
  - 不要な import を削除.(mciaudio.py)
  - get_actors()のsurface番号ゼロパディングバグ修正.(seriko.py) Thanks: あべさん
 
* Wed Aug 07 2002  period 15
  - 右辺の型によらず代入が実行されるように修正.
  - 変数比較の際の型チェックが実数と整数の比較にまで適用されていたのを修正.
 
* Tue Aug 06 2002  period 14
  - SAORI互換機能 (saory.py) 追加.
  - ユーザーからゴーストへのコミュニケート対応（aya のみ）.
  - 「和音」のメニューからの MIDI 演奏に対応.
  - 簡易配列を拡張する処理の条件判定が逆になっていたのを修正.
  - 変数への代入の際に既に変数が存在するかどうかの判定を忘れていたのを追加.
  - 変数を操作する場合, 事前に AyaVAriable.reset メソッドが実行されるようにした.
    これにより文字列の演算による簡易配列としての構造の変化に対応.
 
* Tue Jul 30 2002  period 13
  - クラス Aya に SHIORI API の request() を実装.
  - クラス Aya を Aya と AyaWrapper に分割. AyaWrapper で ninix 本体からの
    SHIORI/1.x, 2.x のリクエストを SHIORI/3.0 形式にして Aya に送るようにした.
  - Aya の応答から ninix 本体の要求する値を取り出すためのメソッド get_value を
    AyaWrapper に実装.
  - Aya のベースを Ver.4 仕様に変更.
  - リクエスト値の取得のためのシステム関数(REQ.*)を全て実装.
  - Ver.4 の OnRequest を使用するようになったので, 不要になったトークチェインを
    動作させるためのコードは削除.
  - Ver.3 互換のためのコードを追加.("# Ver.3" のコメントの個所.)
    ただし, 応答のヘッダ生成は省略. (AyaWrapper の get_value で区別している.)
  - システム関数 LETTONAME に引数のチェックを追加.
  - Aya.request() を修正. Ver.4 における応答の内容は栞機能辞書(aya_shiori3.dic)
    に完全に任せることにして, Aya.request() のリクエストヘッダー解析ではリターン
    しないようにした.
  - システム関数INSERTで挿入バイト位置が負数の場合には先頭に挿入するように修正.
  - AyaFunction.evaluate_string() が文字列を評価していく際に評価する文字の位置
    を正しく扱えていなかったのを修正.
  - 文字列結合出力を実装.
  - AyaFunction.evaluate() の辞書の評価方法を変更.
    基本的に AyaFunction.evaluate_statement() を使用して評価するようにした.
    この変更で四則演算, 文字列結合出力を完全にサポート.
  - AyaFunction.evaluate_statement() 内で型変換が正しく行なわれない場合が
    あったのを修正.
  - 比較演算で両辺の値の型をチェックするようにした.
  - obsolete なシステム変数 ghostexcount を削除.
  - コメントの追加など微調整.
  - AyaNamespace の変更で set_separator メソッドの追加を忘れていたのを修正.
  - random.randrange() の第2引数を修正.
    # Deprecatedになった random.randint() とは範囲が違っているのを見落としてた.
  - decrypt() の入力を1文字だけに変更し decrypt_char() にした.
    さらにこれと対を成す encrypt_char() を作成.
  - os.path.join() の2番目以降の引数に渡されるパス名が相対パスであることが保証
    されるように修正.
  - システム関数 FOPEN で作成されるファイル辞書のキーをノーマライズされた絶対
    パスに変更.
 
* Fri Jul 19 2002  period 12
  - 関数の内部ブロックの変数が外側のブロックの名前空間にまで伝わってしまって
    いたのを修正.
 
* Thu Jul 18 2002  period 11
  - 「文」Ver.4 対応開始.
  - ダブルクォーテーションのエスケープ処理を削除. (Ver.4)
  - マルチステートメントで出力確定子の後にも ';' が必要になった. (Ver.4)
  - システム関数 CUTSPACE を実装.
  - 「文」Ver.3 で削除された古いシステム変数についてサポートを終了.
    ただし ghostexcount はコミュニケートが実装されるまで残す.
  - システム関数 ISFUNCTION を実装.
  - ファイルを書き込み可能状態でオープンする際にはパスに親ディレクトリを指す
    '..' が含まれていないことを確認するようにした.
    読み取りのみの場合は3つまで許可.(~/.ninix の中に収まる範囲.)
    ファイル名が固定の場合にはチェックしていない.
  - システム変数 systemup* を実装.
    ただし, 中身はシステムではなくゴーストを起動してからの経過時間.
  - 未実装関数の戻り値も仕様書に記載されている型に合わせた.
  - 起動時に OnLoad を呼ぶようにした. (Ver.4)
  - 単項演算子 '+', '-' が正しく評価されない場合があったのを修正.
  - システム関数 FDELETE, FRENAME, FSIZE, MKDIR, RMDIR, FENUM を実装.
    これらの関数もパスのチェックをするようになっている.
  - 関係演算子 !_in_ を実装.
  - システム関数 FCOPY, FMOVE を実装.
  - 終了時に OnUnload を呼ぶようにした. (Ver.4)
  - AyaFunction の evaluate メソッドが常に結果を文字列に変換して返す動作を変更.
    連結が必要な場合にのみ文字列に変換するようにした.
  - システム関数リストの LOGGING の引数の数が間違っていたのを修正.
  - システム関数 LOGGING の出力形式を Ver.4 仕様に変更.
 
* Sun Jul 07 2002  period 10
  - AYA 内部イベント On_ID の処理を実装.
  - SHIORI/1.0 API の処理も AYA 内部イベント On_ID に変換するようにした.
 
* Mon Jul 01 2002  period 9
  - システム変数のリストに systemuptime を追加.
  - aya.txt の処理に logmode を(項目のみ)追加.
  - テスト用のメソッドを実装.
  - 文字列型のメソッド find() は python1.5 に無いので string module の find()
    を使用するようにした.
 
* Sun Jun 30 2002  period 8
  - 多項式演算を実装.
    代入演算子に含まれる演算を通常の演算とは別に処理していたのを一本化.
    この変更で '/=' で 0除算の場合のエラー処理を忘れていた問題は無くなった.
  - システム関数の引数の数をチェックしない場合の条件式が間違っていたのを修正.
  - AyaVariable クラスに合わせてシステム関数 ARRAYSIZE を修正.
  - こまごまとした見た目の修正を少々.
  - マルチステートメントの処理でデクリメントを出力確定子と間違えていたのを修正.
  - is_inc_or_dec() を修正してデクリメントが動作するようにした.
  - ブロックの評価結果が空の場合にも選択肢のリストに加えられていたのを修正.
  - if で条件文を羅列せずにリストを活用するように変更.
  - evaluate_statement() での演算子の検索方法を変更.
  - evaluate_statement() で型変換が正しく行なわれない場合があったのを修正.
  - プリプロセッサを強化. '#globaldefine' をサポート.
  - トークチェインのサポートを追加.
  - reference[n] に値が設定されない場合があったのを修正.
  - 'OnSecondChange' が正しく処理されていなかったのを修正.
  - aya.py を単独のスクリプトとしても呼び出せるようにした.
  - トークチェインの制御は aya_shiori3.dic に任せるようにした.
  - トークチェインに使用する変数の初期化とトークチェインの終了処理を追加して
    動作を本家に合わせた.
 
* Thu Jun 13 2002  period 7
  - システム関数 RAND, ASC とシステム変数 random, ascii を修正.
  - スクリプト中で random, ascii が使えなかったのを修正.
  - スクリプト中の簡易配列とヒストリーのインデックスに変数が使用できるように
    修正.
  - 暗号化辞書対応.
    暗号化辞書の解読は外部モジュールに頼らずに aya.py 内部で行なうことにした.
  - aitalkinterval が 0 の時には時間経過による OnAiTalk が発生しないように修正.
  - 型変換のエラーメッセージに変換結果を代入した変数を使用している個所があった
    のを修正.
  - TONUMBER2 の引数にイリーガルな文字列が渡された場合のエラー処理を追加.
  - エラー処理の分離のため辞書の読み込みは aya.txt の解析の後に行なうようにした
  - 文字列と簡易配列の2つの型の変数を統合.
    string = "a"     : string -> "a",     string[0] -> "a"
    array  = "a,b,c" : array  -> "a,b,c", array[0]  -> "a"
  - サイズを越えた要素への代入があると簡易配列が自動的に拡張されるようにした.
  - 文字列と簡易配列の統合に合わせ aya_variable.cfg のフォーマットを更新(v1.1).
    v1.0 フォーマットの読み込みも問題無く行なわれる.
  - システム関数 LOG, LOG10 の引数が 0 の場合には 0 を返すようにした.
  - nonoverlap / sequential が内側のブロックに間違って適用されていたのを修正.
  - ゴースト終了時のみ aya_variable.cfg のセーブを行なうようにした.
  - aya.py の内部で保持する変数を全て AyaVariable クラスにした.
    AyaStringArray はこのクラスに統合されたので削除.
  - 文字列終端の '"' の付け忘れの場合を考慮し, 確認してから削るよう変更.
 
* Sun Jun 09 2002  period 6
  - 数値を関数の戻り値にできるようにした.
  - 関数のオプション nonoverlap / sequential を実装.
  - マルチステートメントに対応.
  - システム関数 NAMETOVALUE 関連の if 節の位置を修正.
    システム関数をオーバーロード可能な状態に保つため.(仕様に規定は無い.)
  - 保存されている変数の値の読み込みを aya.txt を読む前に実行するように変更.
    これまでのコードだと aya.txt の設定が変更された場合でも保存されていた値で
    上書きしてしまって変更が反映されなくなっていた.
    ただし, ユーザーによるしゃべり頻度の設定は aitalkinterval を書換えることで
    行なわれるので, aitalkinterval のみ保存されている値の方を優先.
  - aya_variable.cfg が消失した場合に発生する問題の対処で OnGhostChanged の場合
    を忘れていたので追加.
  - 暗号化辞書対応. ただし, 外部モジュールは未実装なので実際には機能せず.
  - 0 除算の結果を強制的に 0 にするようにした.
  - 剰余演算子 %%, %%= を追加.
  - システム関数 RAND とシステム変数 rand の返す値の範囲を修正.
  - 整数だけでなく実数も使えるように拡張.
  - 変数の値を名前空間から拾ってくる部分で存在判定にバグがあったのを修正.
    # フォーラムで書いたバグ(#1)の修正です.
  - プリプロセスでの置換処理 #define を実装.
  - システム関数の呼出しで引数の数をチェックをするようにした.
  - コメント処理のコードが複数箇所に存在したのをメソッドとして実装.
    この変更で残っていた全角空白の処理忘れが修正された.
  - メソッド find_not_quoted を追加.
    マルチステートメントの処理やコメントの削除等の改良に使用.
  - 有効な要素が存在しない関数は空文字列を返すよう変更.(仕様に規定が追加された.)
  - 簡易配列の実装を変更. それに合わせてシステム関数 ARRAYSIZE も修正.
  - aya_variable.cfg のフォーマットを変更.
    古い形式(バージョン番号が無い)はデータ型の決定で問題があるので,
    読み込まずに破棄することにした.
  - 実数の出力フォーマットを調整.
  - システム関数をスクリプトの中から呼べるようにした.
  - 引数の無いシステム関数が処理されない問題を修正.
  - 以下のシステム関数を実装.
    CALLBYNAME, LOGGING, TOUPPER, TOLOWER, TONUMBER2, TOSTRING2,
    FLOOR, CEIL, ROUND, SIN, COS, TAN, LOG, LOG10, POW, SQRT,
    SETSEPARATOR, FOPEN, FCLOSE, FREAD, FWRITE, ISINTEGER, ISREAL

* Tue May 28 2002  period 5 (canceled)
  - 「文」Ver.3 文法に対応
  - SHIORI/1.0 APIに対応
 
* Wed May 22 2002  period 4
  - 配列以外で使われている '[]' で問題が起きないように修正.
 
* Tue May 21 2002  period 3
  - history, 簡易配列の序数が数値以外の場合のエラー処理を追加.
  - 辞書ファイル名を小文字に変換して読むようにした.
  - 簡易配列で範囲外の序数を指定した場合に仕様通り空文字列を返すよう
    にした.
  - 仕様に従って switch の条件文に文字列が来た場合の処理を switch 0
    と同じにした.
  - typo をいくつか修正.
  - 変数の保存先を aya_variable.cfg に変更.(ファイル形式は独自)
  - システム関数 RAND, ASC を実装.
  - ninix-install の再実行で aya_variable.cfg が消失した場合に発生す
    る問題に対処.
  - システム関数 ARRAYSIZE を実装.
  - 「和音」がエラーで固まるのを防ぐために ghostexcount は常に0を返
    すようにした. （COMMUNICATE実装までの暫定措置）
  
* Mon May 20 2002  period 2
  - 文 ver.3 一部対応
  - 全角スペースを空白と見なしていなかった問題の修正
  - 既定以外のキーの処理が抜けていたため追加
 
* Fri May 10 2002  period 1
  - first release
