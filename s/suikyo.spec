%global        ruby_libdir /usr/share/ruby

Name:          suikyo
Version:       2.1.0
Release:       6.1
Summary:       A Romaji-Kana conversion Library
Group:         System/Internationalization
URL:           http://taiyaki.org/suikyo/
Source:        http://prime.sourceforge.jp/src/suikyo-%{version}.tar.gz
License:       GPL
Requires:      ruby
BuildRequires: ruby-devel
BuildArch:     noarch

%description
Suikyo is Romaji-Kana conversion Library.

%prep
%setup -q

%build
[[ ! -x configure ]] && ./autogen.sh
%configure --with-rubydir=%{ruby_libdir}
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -fr $RPM_BUILD_ROOT%{_datadir}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir %{ruby_libdir}/suikyo
%{ruby_libdir}/suikyo/suikyo*.rb
%{_datadir}/emacs/site-lisp/init-suikyo.el
%dir %{_datadir}/emacs/site-lisp/suikyo
%{_datadir}/emacs/site-lisp/suikyo/suikyo-config.el
%{_datadir}/emacs/site-lisp/suikyo/suikyo.el
%dir %{_datadir}/suikyo/conv-table
%{_datadir}/suikyo/conv-table/ascii-wideascii
%{_datadir}/suikyo/conv-table/azik
%{_datadir}/suikyo/conv-table/azik-all
%{_datadir}/suikyo/conv-table/azik-all_reverse
%{_datadir}/suikyo/conv-table/azik_reverse
%{_datadir}/suikyo/conv-table/egg-mark
%{_datadir}/suikyo/conv-table/egg-mark_reverse
%{_datadir}/suikyo/conv-table/halfkatakana-hiragana
%{_datadir}/suikyo/conv-table/halfkatakana-katakana
%{_datadir}/suikyo/conv-table/hiragana-halfkatakana
%{_datadir}/suikyo/conv-table/hiragana-katakana
%{_datadir}/suikyo/conv-table/kana
%{_datadir}/suikyo/conv-table/kana-romaji
%{_datadir}/suikyo/conv-table/kana_reverse
%{_datadir}/suikyo/conv-table/katakana-halfkatakana
%{_datadir}/suikyo/conv-table/katakana-hiragana
%{_datadir}/suikyo/conv-table/kuten
%{_datadir}/suikyo/conv-table/kuten_reverse
%{_datadir}/suikyo/conv-table/romaji
%{_datadir}/suikyo/conv-table/romaji-hepburn_reverse
%{_datadir}/suikyo/conv-table/romaji-kana
%{_datadir}/suikyo/conv-table/romaji_reverse
%{_datadir}/suikyo/conv-table/skk-mark
%{_datadir}/suikyo/conv-table/skk-mark_reverse
%{_datadir}/suikyo/conv-table/tcode
%{_datadir}/suikyo/conv-table/tcode-dvorak
%{_datadir}/suikyo/conv-table/tcode-dvorak_reverse
%{_datadir}/suikyo/conv-table/tcode_reverse
%{_datadir}/suikyo/conv-table/tutcode
%{_datadir}/suikyo/conv-table/tutcode_reverse
%{_datadir}/suikyo/conv-table/wideascii-ascii
%{_libdir}/pkgconfig/*.pc
%doc AUTHORS COPYING ChangeLog README

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0
- Rebuilt for Fedora
* Fri Jul 25 2008 gil <puntogil@libero.it> 2.1.0-1mamba
- package created by autospec
