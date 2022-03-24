%undefine _debugsource_packages

Name: aobook
Summary: 青空文庫テキストビューアです。
Version: 1.0.4
Release: 1
Group: text
License: Free Software
URL: http://azsky2.html.xdomain.jp/linux/aobook/
Source0: %{name}-%{version}.tar.xz
BuildRequires: desktop-file-utils
BuildRequires: libpng-devel
#Requires: libx11-6,
#Requires: libxext6,
#Requires: libfreetype6,
#Requires: libfontconfig1,
#Requires: zlib1g,
#Requires: libjpeg8,
#Requires: fonts-takao

%description
- freetype による縦書き表示＆アンチエイリアスで綺麗に表示できます。(フォントの描画品質は freetype に依存します)
- 一般的な青空文庫の注記に対応しています。(あまり使わないと思われるものには対応していません)
- UTF-8/Shift-JIS/EUC-JP/UTF16-LE/UTF16-BE に対応しています。
- 挿絵を表示することもできます。
- ZIP で圧縮されたテキストファイルも読み込めます。(先頭に格納されているファイルのみ)
- しおりを付けることができます。
- ツール実行機能や、テキスト行番号で指定してページが表示できるなど、テキスト編集時の確認用としても使えます。

%prep
%setup -q

%build
./configure --prefix=/usr
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.4
- Rebuilt for Fedora
