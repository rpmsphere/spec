Summary: Popular cin tables of OXIM
Name: oxim-tables-popular
Version: 2.0.3
Release: 1
License: Public Domain
Group: System/Internationalization
Source0: oxim-tables-popular.zip
BuildRequires: oxim
BuildArch: noarch

%description
Including popular cin tables for Open X Input Method Server.

%package zh_TW
Summary: Popular cin tables of OXIM for Traditional Chinese
Requires: oxim

%description zh_TW
Including the following cin tables for Open X Input Method Server:
Array40, DaYi3, PinYin, UniLiu.

%package zh_CN
Summary: Popular cin tables of OXIM for Simplified Chinese
Requires: oxim         

%description zh_CN
Including the following cin tables for Open X Input Method Server:
PinYin0, WBX, ErBi.

%package zh_HK
Summary: Popular cin tables of OXIM for Hongkong Chinese
Requires: oxim

%description zh_HK
Including the following cin tables for Open X Input Method Server:
Changjei5, Simplex, CantonHK.

%package ja
Summary: Popular cin tables of OXIM for Japanese
Requires: oxim

%description ja
Including the following cin tables for Open X Input Method Server:
HalfKana, Katakana, Hiragana, Nippon.

%package ko
Summary: Popular cin tables of OXIM for Korean
Requires: oxim

%description ko
Including the following cin tables for Open X Input Method Server:
Hangul, HangulRomaja, Hanja.

%package vi
Summary: Popular cin tables of OXIM for vietnamese
Requires: oxim

%description vi
Including the following cin tables for Open X Input Method Server:
ViMS, ViQR, ViVNI, ViTelex.

%package th
Summary: Popular cin tables of OXIM for vietnamese
Requires: oxim         

%description th
Including the following cin tables for Open X Input Method Server:
Thai.

%prep
%setup -q -n %{name}

%build
for i in *.cin ; do oxim2tab $i ; done

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_libdir}/oxim/tables
%__install -m 644 *.tab %{buildroot}%{_libdir}/oxim/tables

%post
oxim-agent -r

%postun
oxim-agent -r

%files zh_TW
%{_libdir}/oxim/tables/array40.tab
%{_libdir}/oxim/tables/dayi3.tab
%{_libdir}/oxim/tables/pinyin.tab
%{_libdir}/oxim/tables/uniliu.tab

%files zh_CN
%{_libdir}/oxim/tables/pinyin0.tab
%{_libdir}/oxim/tables/wbx.tab
%{_libdir}/oxim/tables/fcitx-erbi.tab

%files zh_HK
%{_libdir}/oxim/tables/cj5.tab
%{_libdir}/oxim/tables/simplex.tab
%{_libdir}/oxim/tables/cantonhk.tab

%files ja
%{_libdir}/oxim/tables/halfwidth-kana.tab
%{_libdir}/oxim/tables/katakana.tab
%{_libdir}/oxim/tables/hiragana.tab
%{_libdir}/oxim/tables/nippon.tab

%files ko
%{_libdir}/oxim/tables/hangul.tab
%{_libdir}/oxim/tables/hangulromaja.tab
%{_libdir}/oxim/tables/hanja.tab

%files vi
%{_libdir}/oxim/tables/vims.tab
%{_libdir}/oxim/tables/viqr.tab
%{_libdir}/oxim/tables/vitelex.tab
%{_libdir}/oxim/tables/vivni.tab

%files th
%{_libdir}/oxim/tables/thai.tab

%changelog
* Sun Jul 18 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.3
- Package for Fedora
