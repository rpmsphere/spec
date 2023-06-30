Summary: Macopix Mascots
Name: macopix-mascots
Version: 20160804
Release: 3.1
License: free
URL: https://rosegray.sakura.ne.jp/macopix/
Group: Amusements/Games
Source0: macopix-mascot-comic_party-euc-ja-1.02.tar.gz
Source1: macopix-mascot-cosmos-euc-ja-1.02.tar.gz
Source2: macopix-mascot-HxB-euc-ja-0.30.tar.gz
Source3: macopix-mascot-kanon-euc-ja-1.02.tar.gz
Source4: macopix-mascot-marimite-euc-ja-2.20.tar.gz
Source5: macopix-mascot-mizuiro-euc-ja-1.02.tar.gz
Source6: macopix-mascot-one-euc-ja-1.02.tar.gz
Source7: macopix-mascot-pia2-euc-ja-1.02.tar.gz
Source8: macopix-mascot-triangle_heart-euc-ja-1.02.tar.gz
Source9: macopix-mascot-tsukihime-euc-ja-1.02.tar.gz
Source10: https://dl.opendesktop.org/api/files/download/id/1465383051/107477-soldier.tar.bz2
Requires:  macopix
BuildArch: noarch

%description
Mascot packages for macopix:
comic_party-1.02
cosmos-1.02
HxB-0.30
kanon-1.02
marimite-2.20
mizuiro-1.02
one-1.02
pia2-1.02
triangle_heart-1.02
tsukihime-1.02
soldier-1.0 https://www.kde-look.org/p/1112248/

%prep
%setup -q -c -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10
for files in macopix-mascot-*
do 
    iconv -f=EUCJP -t=UTF-8 -o $files-README.jp $files/README.jp
done

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/macopix/pixmap

for files in */*.menu */*.mcpx
do 
    iconv -f=EUCJP -t=UTF-8 -o ./code_tmp $files
    sed 's/EUC-JP/UTF-8/' ./code_tmp > $files
done
install -m 444 */*.menu */*.mcpx $RPM_BUILD_ROOT%{_datadir}/macopix
install -m 444 */*.png $RPM_BUILD_ROOT%{_datadir}/macopix/pixmap
cat > $RPM_BUILD_ROOT%{_datadir}/macopix/soldier.menu <<EOF
[General]
code=UTF-8

[Menu00]
Name=Soldier
file00=soldier.mcpx
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc *-README.jp
%{_datadir}/macopix/*

%changelog
* Thu Aug 04 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20160804
- Rebuilt for Fedora
* Wed May 02 2007 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- new upstream release 0.30
* Thu Sep 15 2005 Satoshi IWAMOTO <satoshi.iwamoto@nifty.ne.jp>
- 1st release 0.10
